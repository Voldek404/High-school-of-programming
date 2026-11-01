from dataclasses import dataclass
from math import isfinite
from typing import Mapping


@dataclass(frozen=True)
class VoltageSagResult:
    dropped_phases: tuple[str, ...]
    invalid_phases: tuple[str, ...] = ()

    @property
    def is_reliable(self) -> bool:
        return not self.invalid_phases


def detect_voltage_sags(
    phase_voltages: Mapping[str, float | None],
    nominal_voltage: float,
) -> VoltageSagResult:
    threshold = nominal_voltage * 0.70
    dropped: list[str] = []
    invalid: list[str] = []

    for phase, voltage in phase_voltages.items():
        if voltage is None or not isfinite(voltage):
            invalid.append(phase)
        elif voltage < threshold:
            dropped.append(phase)

    return VoltageSagResult(
        dropped_phases=tuple(dropped),
        invalid_phases=tuple(invalid),
    )
