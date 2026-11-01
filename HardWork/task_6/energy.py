from dataclasses import dataclass
from datetime import datetime
from typing import Iterable


@dataclass(frozen=True)
class HalfHourReading:
    start: datetime
    average_kw: float


@dataclass(frozen=True)
class EnergyResult:
    energy_kwh: float
    is_reliable: bool
    reasons: tuple[str, ...] = ()


def calculate_energy(readings: Iterable[HalfHourReading]) -> EnergyResult:
    variants_by_start: dict[datetime, set[float]] = {}
    for reading in readings:
        variants_by_start.setdefault(reading.start, set()).add(
            reading.average_kw
        )

    conflicts_found = False
    accepted_powers: list[float] = []
    for variants in variants_by_start.values():
        if len(variants) == 1:
            accepted_powers.append(next(iter(variants)))
        else:
            conflicts_found = True

    energy_kwh = sum(power_kw * 0.5 for power_kw in accepted_powers)
    reasons = ("conflicting_intervals",) if conflicts_found else ()
    return EnergyResult(
        energy_kwh=energy_kwh,
        is_reliable=not conflicts_found,
        reasons=reasons,
    )
