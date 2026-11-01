import unittest
from datetime import datetime, timezone
from itertools import permutations

from energy import EnergyResult, HalfHourReading, calculate_energy


class CalculateEnergyTests(unittest.TestCase):
    def test_empty_collection_has_zero_energy(self):
        self.assertEqual(
            calculate_energy([]),
            EnergyResult(energy_kwh=0.0, is_reliable=True),
        )

    def test_one_half_hour_contributes_half_of_average_power(self):
        reading = HalfHourReading(
            start=datetime(2026, 11, 1, 12, 0, tzinfo=timezone.utc),
            average_kw=4.0,
        )

        self.assertEqual(
            calculate_energy([reading]),
            EnergyResult(energy_kwh=2.0, is_reliable=True),
        )

    def test_equal_values_at_different_times_are_both_counted(self):
        readings = [
            HalfHourReading(
                datetime(2026, 11, 1, 12, 0, tzinfo=timezone.utc), 4.0
            ),
            HalfHourReading(
                datetime(2026, 11, 1, 12, 30, tzinfo=timezone.utc), 4.0
            ),
        ]

        self.assertEqual(
            calculate_energy(readings),
            EnergyResult(energy_kwh=4.0, is_reliable=True),
        )

    def test_exact_repeat_is_idempotent(self):
        reading = HalfHourReading(
            datetime(2026, 11, 1, 12, 0, tzinfo=timezone.utc), 4.0
        )

        self.assertEqual(
            calculate_energy([reading, reading]),
            EnergyResult(energy_kwh=2.0, is_reliable=True),
        )

    def test_conflict_is_excluded_independently_of_input_order(self):
        first_start = datetime(2026, 11, 1, 12, 0, tzinfo=timezone.utc)
        readings = [
            HalfHourReading(first_start, 4.0),
            HalfHourReading(first_start, 9.0),
            HalfHourReading(
                datetime(2026, 11, 1, 12, 30, tzinfo=timezone.utc), 6.0
            ),
        ]
        expected = EnergyResult(
            energy_kwh=3.0,
            is_reliable=False,
            reasons=("conflicting_intervals",),
        )

        for variant in permutations(readings):
            with self.subTest(variant=variant):
                self.assertEqual(calculate_energy(variant), expected)


if __name__ == "__main__":
    unittest.main()
