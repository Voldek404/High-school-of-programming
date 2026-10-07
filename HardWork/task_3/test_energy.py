"""Примеры контрактов для TDD. Запуск: python -m pytest -q"""
import sqlite3
from datetime import datetime, timedelta, timezone
import pytest
from energy import HalfHour, EnergyCalculator, EnergyMonitor, MeterRepository

START = datetime(2026, 10, 6, 12, 0, tzinfo=timezone.utc)


def sample(power=5.0, minutes=0, meter='001', channel='P_IMPORT', reasons=()):
    return HalfHour(meter, START + timedelta(minutes=minutes), channel, power, reasons)


def test_energy_from_half_hour_powers():
    result = EnergyCalculator.energy_kwh([sample(4), sample(6, minutes=30)])
    assert result.energy_kwh == pytest.approx(5)
    assert result.is_complete


def test_equal_powers_at_different_times_are_valid():
    result = EnergyCalculator.energy_kwh([sample(), sample(minutes=30)])
    assert result.energy_kwh == pytest.approx(5)
    assert result.is_complete


@pytest.mark.parametrize('value', [None, float('nan'), float('inf'), 'bad'])
def test_bad_power_is_marked_without_exception(value):
    row = sample(value)
    assert not row.is_reliable
    assert row.average_kw is None
    assert row.reasons


def test_quality_flag_from_source_is_preserved():
    row = sample(5, reasons=('Недостоверно по данным комплекса',))
    assert row.average_kw == 5
    assert not row.is_reliable


def test_shifted_timestamp_is_marked():
    assert not sample(minutes=15).is_reliable


def test_bad_interval_does_not_stop_energy_calculation():
    result = EnergyCalculator.energy_kwh([
        sample(4), sample(None, minutes=30), sample(6, minutes=60)])
    assert result.energy_kwh == pytest.approx(5)
    assert not result.is_complete
    assert result.reasons


def test_missing_interval_marks_partial_total():
    result = EnergyCalculator.energy_kwh([sample(), sample(minutes=60)])
    assert result.energy_kwh == pytest.approx(5)
    assert not result.is_complete


def test_duplicate_is_not_counted_twice():
    result = EnergyCalculator.energy_kwh([sample(), sample()])
    assert result.energy_kwh == pytest.approx(2.5)
    assert not result.is_complete


def test_meters_cannot_be_mixed_in_calculation():
    with pytest.raises(ValueError):
        EnergyCalculator.energy_kwh([sample(), sample(meter='002')])


def test_empty_report_is_incomplete():
    result = EnergyCalculator.energy_kwh([])
    assert result.energy_kwh == 0
    assert not result.is_complete


@pytest.mark.parametrize('active, expected', [(8, .8), (-8, -.8), (0, 0)])
def test_signed_power_factor(active, expected):
    assert EnergyCalculator.signed_power_factor(active, 10) == pytest.approx(expected)


@pytest.mark.parametrize('active, apparent', [(0, 0), (11, 10), (None, 10)])
def test_undefined_power_factor(active, apparent):
    assert EnergyCalculator.signed_power_factor(active, apparent) is None


@pytest.mark.parametrize('power, expected', [(4.9, False), (5, False), (5.1, True)])
def test_power_limit(power, expected):
    row = sample(power)
    assert EnergyMonitor.power_exceeded(row, 5).triggered is expected
    assert row.is_reliable  # Превышение не означает недостоверность.


def test_unreliable_power_cannot_produce_reliable_alarm_decision():
    result = EnergyMonitor.power_exceeded(sample(None), 5)
    assert result.triggered is None
    assert result.reasons


@pytest.mark.parametrize('voltage, expected', [(230, ()), (161, ()), (160, ('A',))])
def test_voltage_drop_threshold(voltage, expected):
    result = EnergyMonitor.low_voltage_phases({'A': voltage, 'B': 230, 'C': 230})
    assert result.low_phases == expected
    assert result.unknown_phases == ()


def test_missing_phase_does_not_hide_known_voltage_drop():
    result = EnergyMonitor.low_voltage_phases({'A': 160, 'B': None, 'C': 230})
    assert result.low_phases == ('A',)
    assert result.unknown_phases == ('B',)


@pytest.fixture
def repository():
    connection = sqlite3.connect(':memory:')
    repo = MeterRepository(connection)
    repo.create_schema()
    repo.add_meter('001')
    repo.add_meter('002')
    yield repo
    connection.close()


def test_same_power_different_times_is_saved(repository):
    repository.save(sample())
    repository.save(sample(minutes=30))
    assert [r.average_kw for r in repository.list_for_meter('001')] == [5, 5]


def test_unreliable_interval_and_next_good_interval_are_saved(repository):
    repository.save(sample(float('nan')))
    repository.save(sample(6, minutes=30))
    rows = repository.list_for_meter('001')
    assert len(rows) == 2
    assert not rows[0].is_reliable
    assert rows[0].average_kw is None
    assert rows[1].is_reliable
    assert rows[1].average_kw == 6


def test_quality_reason_survives_database_roundtrip(repository):
    row = sample(reasons=('Ошибка связи',))
    repository.save(row)
    assert repository.list_for_meter('001') == [row]


def test_same_time_different_meters_does_not_conflict(repository):
    repository.save(sample())
    repository.save(sample(meter='002', power=7))
    assert repository.list_for_meter('001')[0].average_kw == 5
    assert repository.list_for_meter('002')[0].average_kw == 7


def test_same_time_different_channels_is_allowed(repository):
    repository.save(sample())
    repository.save(sample(channel='P_EXPORT'))
    assert len(repository.list_for_meter('001')) == 2


def test_duplicate_key_is_rejected(repository):
    repository.save(sample())
    with pytest.raises(sqlite3.IntegrityError):
        repository.save(sample())
    assert len(repository.list_for_meter('001')) == 1


def test_unknown_meter_is_rejected(repository):
    with pytest.raises(sqlite3.IntegrityError):
        repository.save(sample(meter='UNKNOWN'))
    assert repository.list_for_meter('UNKNOWN') == []
