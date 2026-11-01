import unittest

from voltage import VoltageSagResult, detect_voltage_sags


class DetectVoltageSagsTests(unittest.TestCase):
    def test_normal_voltage_has_no_sag(self):
        self.assertEqual(
            detect_voltage_sags({"A": 230.0}, nominal_voltage=230.0),
            VoltageSagResult(dropped_phases=()),
        )

    def test_phase_below_seventy_percent_is_a_sag(self):
        self.assertEqual(
            detect_voltage_sags({"B": 160.0}, nominal_voltage=230.0),
            VoltageSagResult(dropped_phases=("B",)),
        )

    def test_exactly_seventy_percent_is_not_more_than_thirty_percent_drop(self):
        self.assertEqual(
            detect_voltage_sags({"A": 70.0}, nominal_voltage=100.0),
            VoltageSagResult(dropped_phases=()),
        )

    def test_each_phase_is_checked_independently(self):
        self.assertEqual(
            detect_voltage_sags(
                {"A": 230.0, "B": 150.0, "C": 140.0},
                nominal_voltage=230.0,
            ),
            VoltageSagResult(dropped_phases=("B", "C")),
        )

    def test_missing_measurement_marks_result_unreliable(self):
        self.assertEqual(
            detect_voltage_sags(
                {"A": 230.0, "B": None}, nominal_voltage=230.0
            ),
            VoltageSagResult(dropped_phases=(), invalid_phases=("B",)),
        )

    def test_non_finite_measurement_is_invalid(self):
        self.assertEqual(
            detect_voltage_sags({"C": float("nan")}, nominal_voltage=230.0),
            VoltageSagResult(dropped_phases=(), invalid_phases=("C",)),
        )


if __name__ == "__main__":
    unittest.main()
