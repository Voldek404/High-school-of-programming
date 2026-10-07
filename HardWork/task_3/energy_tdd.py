"""Получасовые мощности, качество данных и хранение в SQLite.

Python 3.10+. Недостоверные измерения маркируются, а не прерывают пакет.
Номер прибора и время — обязательные идентификаторы: их ошибки остаются
исключениями, как и ошибки конфигурации/БД. Цвет выбирает интерфейс по
is_reliable; он не хранится в измерении. Превышения — отдельно от качества.
Знаковый P/S не заменяет согласованный с прибором алгоритм cos phi.
"""
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from math import isfinite
from numbers import Real


def finite_number(value):
    return isinstance(value, Real) and not isinstance(value, bool) and isfinite(value)


@dataclass(frozen=True)
class HalfHour:
    meter_number: str
    start: datetime  # Начало интервала с часовым поясом.
    channel: str
    average_kw: float | None
    reasons: tuple[str, ...] = ()  # Включая флаги недостоверности из комплекса.

    def __post_init__(self):
        if not isinstance(self.meter_number, str) or not self.meter_number.strip():
            raise ValueError('Не указан номер прибора')
        if not isinstance(self.channel, str) or not self.channel.strip():
            raise ValueError('Не указан канал')
        if not isinstance(self.start, datetime) or self.start.utcoffset() is None:
            raise ValueError('Нужно время с часовым поясом')
        reasons = list(self.reasons)
        value = self.average_kw
        if value is None:
            reasons.append('Нет данных от прибора')
        elif not finite_number(value):
            reasons.append('Мощность не является конечным числом')
            value = None  # NaN/inf не записываем в числовую колонку.
        else:
            value = float(value)
        if self.start.minute not in (0, 30) or self.start.second or self.start.microsecond:
            reasons.append('Время не на границе получаса')
        object.__setattr__(self, 'average_kw', value)
        object.__setattr__(self, 'reasons', tuple(dict.fromkeys(reasons)))

    @property
    def is_reliable(self):
        return not self.reasons


@dataclass(frozen=True)
class EnergyResult:
    energy_kwh: float  # Сумма только достоверных интервалов.
    is_complete: bool
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class CheckResult:
    triggered: bool | None  # None: данных недостаточно для решения.
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class VoltageResult:
    low_phases: tuple[str, ...]
    unknown_phases: tuple[str, ...]


class EnergyCalculator:
    @staticmethod
    def energy_kwh(intervals: list[HalfHour]) -> EnergyResult:
        if not intervals:
            return EnergyResult(0.0, False, ('Нет получасовок',))
        rows = sorted(intervals, key=lambda r: r.start.timestamp())
        identity = (rows[0].meter_number, rows[0].channel)
        if any((r.meter_number, r.channel) != identity for r in rows):
            raise ValueError('Нельзя смешивать приборы и каналы')
        reasons = []
        total = 0.0
        seen = set()
        for row in rows:
            timestamp = row.start.timestamp()
            if timestamp in seen:
                reasons.append('Повтор получасовки: требуется разрешение конфликта')
                continue  # Первый экземпляр учитывается, повтор — нет.
            seen.add(timestamp)
            if row.is_reliable:
                total += row.average_kw * 0.5
            else:
                reasons.extend(row.reasons)
        unique_times = sorted(seen)
        if any(b - a != 1800 for a, b in zip(unique_times, unique_times[1:])):
            reasons.append('Есть пропуск или смещение интервалов')
        reasons = tuple(dict.fromkeys(reasons))
        # Полнота относится к диапазону от первой до последней записи.
        # Для проверки краёв отчётного периода нужен отдельно заданный диапазон.
        return EnergyResult(total, not reasons, reasons)

    @staticmethod
    def signed_power_factor(active_kw, apparent_kva) -> float | None:
        if not finite_number(active_kw) or not finite_number(apparent_kva):
            return None
        if apparent_kva <= 0 or abs(active_kw) > apparent_kva:
            return None
        return active_kw / apparent_kva


class EnergyMonitor:
    @staticmethod
    def power_exceeded(interval: HalfHour, allowed_kw: float) -> CheckResult:
        if not finite_number(allowed_kw) or allowed_kw <= 0:
            raise ValueError('Лимит должен быть положительным')
        if not interval.is_reliable:
            return CheckResult(None, interval.reasons)
        return CheckResult(interval.average_kw > allowed_kw)

    @staticmethod
    def low_voltage_phases(voltages: dict, nominal_v: float = 230.0) -> VoltageResult:
        if not finite_number(nominal_v) or nominal_v <= 0:
            raise ValueError('Номинальное напряжение должно быть положительным')
        low, unknown = [], []
        for phase in ('A', 'B', 'C'):
            value = voltages.get(phase)
            if not finite_number(value) or value < 0:
                unknown.append(phase)
            elif value < nominal_v * 0.7:
                low.append(phase)
        return VoltageResult(tuple(low), tuple(unknown))


class MeterRepository:
    def __init__(self, connection: sqlite3.Connection):
        self.connection = connection
        if connection.in_transaction:
            raise ValueError('Создайте репозиторий вне активной транзакции')
        connection.execute('PRAGMA foreign_keys = ON')

    def create_schema(self):
        self.connection.executescript('''
            CREATE TABLE IF NOT EXISTS meters (number TEXT PRIMARY KEY);
            CREATE TABLE IF NOT EXISTS half_hours (
                meter_number TEXT NOT NULL REFERENCES meters(number),
                start_epoch INTEGER NOT NULL,
                channel TEXT NOT NULL,
                average_kw REAL,
                is_reliable INTEGER NOT NULL CHECK(is_reliable IN (0, 1)),
                reasons_json TEXT NOT NULL,
                UNIQUE(meter_number, start_epoch, channel)
            );
        ''')

    def add_meter(self, number: str):
        if not isinstance(number, str) or not number.strip():
            raise ValueError('Не указан номер прибора')
        with self.connection:
            self.connection.execute('INSERT INTO meters VALUES (?)', (number,))

    def save(self, interval: HalfHour):
        with self.connection:
            self.connection.execute('''
                INSERT INTO half_hours VALUES (?, ?, ?, ?, ?, ?)
            ''', (interval.meter_number, int(interval.start.timestamp()),
                  interval.channel, interval.average_kw, int(interval.is_reliable),
                  json.dumps(interval.reasons, ensure_ascii=False)))

    def list_for_meter(self, number: str) -> list[HalfHour]:
        from datetime import timezone
        rows = self.connection.execute('''
            SELECT start_epoch, channel, average_kw, reasons_json
            FROM half_hours WHERE meter_number = ? ORDER BY start_epoch, channel
        ''', (number,)).fetchall()
        return [HalfHour(number, datetime.fromtimestamp(t, timezone.utc),
                         channel, power, tuple(json.loads(reasons)))
                for t, channel, power, reasons in rows]
