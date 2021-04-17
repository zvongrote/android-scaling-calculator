import unittest
from scaling_calculator import Dimension, default_round, scale_dimension


class ScaleTest(unittest.TestCase):

    def test_scale_up_default_round_no_rounding(self):
        base_dimension = Dimension(20, 30)
        densities = {"m": 4, "h": 6}
        base_density = "m"
        target_density = "h"
        round_function = default_round

        scaled_dimension = scale_dimension(
            base_dimension, base_density, target_density, densities, round_function)

        self.assertEqual(scaled_dimension.width, 30)
        self.assertEqual(scaled_dimension.height, 45)

    def test_scale_down_default_round_no_rounding(self):
        base_dimension = Dimension(30, 45)
        densities = {"m": 4, "h": 6}
        base_density = "h"
        target_density = "m"
        round_function = default_round

        scaled_dimension = scale_dimension(
            base_dimension, base_density, target_density, densities, round_function)

        self.assertEqual(scaled_dimension.width, 20)
        self.assertEqual(scaled_dimension.height, 30)

    def test_scale_up_default_round(self):
        base_dimension = Dimension(93.738, 123.976)
        densities = {"m": 4, "h": 6}
        base_density = "m"
        target_density = "h"
        round_function = default_round

        scaled_dimension = scale_dimension(
            base_dimension, base_density, target_density, densities, round_function)

        self.assertEqual(scaled_dimension.width, 141)
        self.assertEqual(scaled_dimension.height, 186)

    def test_scale_down_default_round(self):
        base_dimension = Dimension(46.113, 164.798)
        densities = {"m": 4, "h": 6}
        base_density = "h"
        target_density = "m"
        round_function = default_round

        scaled_dimension = scale_dimension(
            base_dimension, base_density, target_density, densities, round_function)

        self.assertEqual(scaled_dimension.width, 31)
        self.assertEqual(scaled_dimension.height, 111)


if __name__ == "__main__":
    unittest.main()
