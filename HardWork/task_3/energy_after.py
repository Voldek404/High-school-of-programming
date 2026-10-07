"""Учёт получасовых средних мощностей. Python 3.10+.

Спецификация и обоснование дизайна: energy_design_review.md.
Входная величина — средняя МОЩНОСТЬ за 30 минут, не энергия и не
накопительный регистр. Отрицательная мощность сохраняет свой знак.
Недостоверность измерения, срабатывание сигнала и ошибка использования
API — три разных результата. Цвет выбирает UI по is_reliable/reasons.
"""
from abc import ABC, abstractmethod
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import json
from math import fsum, isfinite
from numbers import Real
import sqlite3
from typing import Iterable, Mapping

HALF_HOUR = timedelta(minutes=30)
HALF_HOUR_HOURS = 0.5
VOLTAGE_DROP_FRACTION = 0.30
PHASES = ('A', 'B', 'C')
MISSING_POWER = 'Нет данных от прибора'
INVALID_POWER = 'Мощность не является конечным числом'
SHIFTED_TIME = 'Время не на границе получаса UTC'
MISSING_INTERVALS = 'Не все получасовки отчётного периода учтены'
CONFLICTING_INTERVALS = 'Конфликт значений или качества одной получасовки'
NUMERIC_OVERFLOW = 'Сумма не представима конечным числом'


def finite_number(value: object) -> bool:
    """Числовой контракт: Real, кроме bool, представимый конечным float."""
    if not isinstance(value, Real) or isinstance(value, bool):
        return False
    try:
        return isfinite(float(value))
    except (OverflowError, ValueError):
        return False


def _identifier(value: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Нужен непустой строковый идентификатор')


def _utc(value: datetime) -> datetime:
    if not isinstance(value, datetime) or value.utcoffset() is None:
        raise ValueError('Нужно время с часовым поясом')
    return value.astimezone(timezone.utc)


def _aligned(value: datetime) -> bool:
    return value.minute in (0, 30) and value.second == 0 and value.microsecond == 0


@dataclass(frozen=True)
class ReportPeriod:
    """Отчётный период [start, end). Обе границы на сетке получасов UTC.

    Предусловие: aware datetime, start < end, границы кратны 30 минутам.
    Постусловие: неизменяемый период в UTC; end в отчёт не входит.
    """
    start: datetime
    end: datetime

    def __post_init__(self):
        start, end = _utc(self.start), _utc(self.end)
        if start >= end or not _aligned(start) or not _aligned(end):
            raise ValueError('Нужен непустой период на границах получасов UTC')
        object.__setattr__(self, 'start', start)
        object.__setattr__(self, 'end', end)

    @property
    def interval_count(self) -> int:
        return (self.end - self.start) // HALF_HOUR


@dataclass(frozen=True)
class HalfHour:
    """Одно измерение; ключ (номер прибора, начало UTC, канал).

    Предусловие: непустые идентификаторы, aware datetime; reasons — tuple
    непустых строк. Ошибки этих метаданных дают ValueError.
    Постусловие: время нормализовано в UTC без потери точности; плохое
    значение/смещённое время маркируется; объект неизменяем.
    Инвариант: is_reliable <=> нет reasons. Достоверная мощность конечна.
    """
    meter_number: str
    start: datetime
    channel: str
    average_kw: float | None
    reasons: tuple[str, ...] = ()

    def __post_init__(self):
        _identifier(self.meter_number)
        _identifier(self.channel)
        start = _utc(self.start)
        if not isinstance(self.reasons, tuple) or any(
            not isinstance(r, str) or not r.strip() for r in self.reasons
        ):
            raise ValueError('Причины должны быть кортежем непустых строк')
        reasons = set(self.reasons)
        value = self.average_kw
        if value is None:
            # Сохраняем нормализованную запись при чтении из хранилища:
            # invalid -> None не должен превратиться в другую причину.
            if INVALID_POWER not in reasons:
                reasons.add(MISSING_POWER)
        elif not finite_number(value):
            reasons.add(INVALID_POWER)
            value = None
        else:
            value = float(value)
        if not _aligned(start):
            reasons.add(SHIFTED_TIME)
        object.__setattr__(self, 'start', start)
        object.__setattr__(self, 'average_kw', value)
        object.__setattr__(self, 'reasons', tuple(sorted(reasons)))

    @property
    def key(self) -> tuple[str, datetime, str]:
        return self.meter_number, self.start, self.channel

    @property
    def is_reliable(self) -> bool:
        return not self.reasons


@dataclass(frozen=True)
class EnergyResult:
    energy_kwh: float | None  # Частичная сумма; None при переполнении.
    is_complete: bool
    reasons: tuple[str, ...]
    expected_intervals: int
    counted_intervals: int


@dataclass(frozen=True)
class CheckResult:
    triggered: bool | None  # None — нельзя принять достоверное решение.
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class VoltageResult:
    low_phases: tuple[str, ...]
    unknown_phases: tuple[str, ...]


class EnergyCalculator:
    @staticmethod
    def energy_kwh(intervals: Iterable[HalfHour], period: ReportPeriod) -> EnergyResult:
        """Сумма Pср * 0.5 ч по одному прибору и каналу в period.

        Предусловие: все записи относятся к одному прибору/каналу.
        Постусловия: вне периода записи не учитываются; точные повторы
        схлопываются; конфликтующие записи одного ключа ВСЕ исключаются.
        Недостоверные записи исключаются, причины возвращаются.
        Полнота истинна только если каждый ожидаемый интервал учтён
        и сумма конечна. Вход и порядок записей на результат не влияют.
        """
        rows = list(intervals)
        if len({(r.meter_number, r.channel) for r in rows}) > 1:
            raise ValueError('Нельзя смешивать приборы и каналы')
        groups = defaultdict(list)
        for row in rows:
            if period.start <= row.start < period.end:
                groups[row.start].append(row)
        reasons, powers = set(), []
        for start in sorted(groups):
            variants = set(groups[start])
            reasons.update(reason for row in variants for reason in row.reasons)
            if len(variants) > 1:
                reasons.add(CONFLICTING_INTERVALS)
                continue
            row = next(iter(variants))
            if row.is_reliable:
                powers.append(row.average_kw)
        expected, counted = period.interval_count, len(powers)
        if counted != expected:
            reasons.add(MISSING_INTERVALS)
        try:
            total = fsum(p * HALF_HOUR_HOURS for p in powers)
            if not isfinite(total):
                raise OverflowError
        except OverflowError:
            total = None
            reasons.add(NUMERIC_OVERFLOW)
        return EnergyResult(total, not reasons, tuple(sorted(reasons)), expected, counted)

    @staticmethod
    def signed_power_factor(active_kw, apparent_kva) -> float | None:
        """Знаковый коэффициент P/S, НЕ универсальный алгоритм cos(phi).

        При конечных P, S > 0 и |P| <= S: результат P/S в [-1, 1].
        Иначе None. Знак задаётся P; знак Q этим методом не определяется.
        """
        if not finite_number(active_kw) or not finite_number(apparent_kva):
            return None
        p, s = float(active_kw), float(apparent_kva)
        if s <= 0 or abs(p) > s:
            return None
        return p / s


class EnergyMonitor:
    @staticmethod
    def power_exceeded(interval: HalfHour, allowed_kw: float) -> CheckResult:
        """Лимит > 0. Сигнал: достоверное Pср > лимита; равенство допустимо.

        Недостоверные данные дают None с причинами. Проверяется положительное
        направление, не |P|. Сигнал не меняет качество исходного измерения.
        """
        if not finite_number(allowed_kw) or allowed_kw <= 0:
            raise ValueError('Лимит должен быть положительным конечным числом')
        if not interval.is_reliable:
            return CheckResult(None, interval.reasons)
        return CheckResult(interval.average_kw > float(allowed_kw))

    @staticmethod
    def low_voltage_phases(voltages: Mapping[str, object], nominal_v=230.0) -> VoltageResult:
        """Номинал > 0. Для A/B/C сигнал при U < 0.70 * Uном.

        Это проверка переданных величин, без оценки длительности провала.
        Недостающая/нечисловая/отрицательная фаза — unknown. Другие фазы
        продолжают проверяться. Порядок фаз в результате всегда A, B, C.
        """
        if not finite_number(nominal_v) or nominal_v <= 0:
            raise ValueError('Номинальное напряжение должно быть положительным')
        low, unknown = [], []
        threshold = float(nominal_v) * (1 - VOLTAGE_DROP_FRACTION)
        for phase in PHASES:
            value = voltages.get(phase)
            if not finite_number(value) or value < 0:
                unknown.append(phase)
            elif float(value) < threshold:
                low.append(phase)
        return VoltageResult(tuple(low), tuple(unknown))


class RepositoryError(Exception):
    """Базовая ошибка контракта хранилища."""


class UnknownMeterError(RepositoryError):
    pass


class ConflictingIntervalError(RepositoryError):
    pass


class StorageError(RepositoryError):
    """Сбой хранилища; причина доступна через __cause__."""


class UnsupportedSchemaError(StorageError):
    pass


class MeterRepository(ABC):
    """Контракт хранилища для последовательных вызовов.

    Идентификаторы непустые; прибор регистрируется до записи измерения.
    add_meter повторно безопасен. save хранит ВСЕ качества измерений:
    новый ключ -> запись; точный повтор -> без изменений; иной объект с тем
    же ключом -> ConflictingIntervalError без перезаписи. Неизвестный прибор
    -> UnknownMeterError без записи. Сбой backend -> StorageError.
    list_for_meter возвращает новый список неизменяемых объектов,
    упорядоченный по (start, channel); неизвестный прибор -> [].
    Один прибор имеет много измерений. Доступа к SQL клиенту не требуется.
    """
    @abstractmethod
    def add_meter(self, number: str) -> None:
        pass

    @abstractmethod
    def save(self, interval: HalfHour) -> None:
        pass

    @abstractmethod
    def list_for_meter(self, number: str) -> list[HalfHour]:
        pass


class InMemoryMeterRepository(MeterRepository):
    """Альтернативная реализация того же контракта, без SQL."""
    def __init__(self):
        self._meters = set()
        self._intervals = {}

    def add_meter(self, number):
        _identifier(number)
        self._meters.add(number)

    def save(self, interval):
        if interval.meter_number not in self._meters:
            raise UnknownMeterError(interval.meter_number)
        old = self._intervals.get(interval.key)
        if old is not None and old != interval:
            raise ConflictingIntervalError(str(interval.key))
        self._intervals[interval.key] = interval

    def list_for_meter(self, number):
        _identifier(number)
        return sorted((r for r in self._intervals.values() if r.meter_number == number),
                      key=lambda r: (r.start, r.channel))


class SQLiteMeterRepository(MeterRepository):
    """SQLite adapter. Соединением владеет вызывающий код.

    До использования вызвать create_schema(). Каждая запись — отдельная
    транзакция; внешняя активная транзакция запрещена (ValueError), чтобы
    метод не мог неожиданно закоммитить её. Соединение не закрывается здесь.
    Старая схема с start_epoch требует явной миграции, а не автозамены.
    """
    def __init__(self, connection: sqlite3.Connection):
        self._connection = connection
        with self._operation():
            connection.execute('PRAGMA foreign_keys = ON')

    @contextmanager
    def _operation(self):
        try:
            if self._connection.in_transaction:
                raise ValueError('Репозиторий нельзя вызывать внутри внешней транзакции')
            yield
        except sqlite3.Error as exc:
            raise StorageError('Ошибка SQLite') from exc

    def create_schema(self):
        with self._operation():
            columns = self._connection.execute('PRAGMA table_info(half_hours)').fetchall()
            if columns and [c[1] for c in columns] != [
                'meter_number', 'start_utc', 'channel', 'average_kw', 'reasons_json'
            ]:
                raise UnsupportedSchemaError('Нужна явная миграция прежней схемы')
            self._connection.executescript('''
                CREATE TABLE IF NOT EXISTS meters (number TEXT PRIMARY KEY);
                CREATE TABLE IF NOT EXISTS half_hours (
                    meter_number TEXT NOT NULL REFERENCES meters(number),
                    start_utc TEXT NOT NULL,
                    channel TEXT NOT NULL,
                    average_kw REAL,
                    reasons_json TEXT NOT NULL,
                    PRIMARY KEY (meter_number, start_utc, channel)
                );
            ''')

    def add_meter(self, number):
        _identifier(number)
        with self._operation(), self._connection:
            self._connection.execute('INSERT OR IGNORE INTO meters VALUES (?)', (number,))

    @staticmethod
    def _decode(number, row):
        start, channel, power, reasons = row
        return HalfHour(number, datetime.fromisoformat(start), channel,
                        power, tuple(json.loads(reasons)))

    def save(self, interval):
        start = interval.start.isoformat(timespec='microseconds')
        with self._operation(), self._connection:
            # BEGIN IMMEDIATE: проверка и запись используют один снимок БД.
            self._connection.execute('BEGIN IMMEDIATE')
            if self._connection.execute('SELECT 1 FROM meters WHERE number = ?',
                                        (interval.meter_number,)).fetchone() is None:
                raise UnknownMeterError(interval.meter_number)
            old = self._connection.execute('''
                SELECT start_utc, channel, average_kw, reasons_json FROM half_hours
                WHERE meter_number = ? AND start_utc = ? AND channel = ?
            ''', (interval.meter_number, start, interval.channel)).fetchone()
            if old is not None:
                if self._decode(interval.meter_number, old) != interval:
                    raise ConflictingIntervalError(str(interval.key))
                return
            self._connection.execute('INSERT INTO half_hours VALUES (?, ?, ?, ?, ?)',
                                     (interval.meter_number, start, interval.channel,
                                      interval.average_kw,
                                      json.dumps(interval.reasons, ensure_ascii=False)))

    def list_for_meter(self, number):
        _identifier(number)
        with self._operation():
            rows = self._connection.execute('''
                SELECT start_utc, channel, average_kw, reasons_json
                FROM half_hours WHERE meter_number = ? ORDER BY start_utc, channel
            ''', (number,)).fetchall()
        return [self._decode(number, row) for row in rows]
