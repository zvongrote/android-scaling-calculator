import unittest
from scaling_calculator import Dimension, scale_dimension


class ScaleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.densities = {"l": 3, "m": 4, "h": 6}

        cls.dimension_whole_width_whole_height = Dimension(56, 70)

        cls.dimension_lower_width_whole_height = Dimension(88.229, 127)
        cls.dimension_higher_width_whole_height = Dimension(124.715, 19)

        cls.dimension_whole_width_lower_height = Dimension(104, 102.115)
        cls.dimension_whole_width_higher_height = Dimension(103, 198.917)

        cls.dimension_lower_width_lower_height = Dimension(118.119, 113.494)
        cls.dimension_lower_width_higher_height = Dimension(75.030, 40.923)
        cls.dimension_higher_width_lower_height = Dimension(135.506, 225.375)
        cls.dimension_higher_width_higher_height = Dimension(106.780, 100.643)

    # dimension_whole_width_whole_height

    def test_scale_dimension_whole_width_whole_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 42)
        self.assertEqual(scaled_dimension.height, 53)

    def test_scale_dimension_whole_width_whole_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 56)
        self.assertEqual(scaled_dimension.height, 70)

    def test_scale_dimension_whole_width_whole_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 84)
        self.assertEqual(scaled_dimension.height, 105)

    # dimension_lower_width_whole_height

    def test_scale_dimension_lower_width_whole_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 66)
        self.assertEqual(scaled_dimension.height, 95)

    def test_scale_dimension_lower_width_whole_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 88)
        self.assertEqual(scaled_dimension.height, 127)

    def test_scale_dimension_lower_width_whole_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 132)
        self.assertEqual(scaled_dimension.height, 190)

    # dimension_higher_width_whole_height

    def test_scale_dimension_higher_width_whole_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 94)
        self.assertEqual(scaled_dimension.height, 14)

    def test_scale_dimension_higher_width_whole_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 125)
        self.assertEqual(scaled_dimension.height, 19)

    def test_scale_dimension_higher_width_whole_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_whole_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 187)
        self.assertEqual(scaled_dimension.height, 28)

    # dimension_whole_width_lower_height = Dimension(104, 102.115)

    def test_scale_dimension_whole_width_lower_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 78)
        self.assertEqual(scaled_dimension.height, 77)

    def test_scale_dimension_whole_width_lower_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 104)
        self.assertEqual(scaled_dimension.height, 102)

    def test_scale_dimension_whole_width_lower_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 156)
        self.assertEqual(scaled_dimension.height, 153)

    # dimension_whole_width_higher_height = Dimension(103, 198.917)

    def test_scale_dimension_whole_width_higher_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 77)
        self.assertEqual(scaled_dimension.height, 149)  

    def test_scale_dimension_whole_width_higher_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 103)
        self.assertEqual(scaled_dimension.height, 199)

    def test_scale_dimension_whole_width_higher_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_whole_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 155)
        self.assertEqual(scaled_dimension.height, 299)  

    # dimension_lower_width_lower_height = Dimension(118.119, 113.494)

    def test_scale_dimension_lower_width_lower_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 89)
        self.assertEqual(scaled_dimension.height, 86)

    def test_scale_dimension_lower_width_lower_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 118)
        self.assertEqual(scaled_dimension.height, 113)

    def test_scale_dimension_lower_width_lower_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 177)
        self.assertEqual(scaled_dimension.height, 170)

    # dimension_lower_width_higher_height = Dimension(75.030, 40.923)

    def test_scale_dimension_lower_width_higher_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 56)
        self.assertEqual(scaled_dimension.height, 31)

    def test_scale_dimension_lower_width_higher_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 75)
        self.assertEqual(scaled_dimension.height, 41)

    def test_scale_dimension_lower_width_higher_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_lower_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 113)
        self.assertEqual(scaled_dimension.height, 62)

    # dimension_higher_width_lower_height = Dimension(135.506, 225.375)

    def test_scale_dimension_higher_width_lower_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 102)
        self.assertEqual(scaled_dimension.height, 170)

    def test_scale_dimension_higher_width_lower_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 136)
        self.assertEqual(scaled_dimension.height, 226)

    def test_scale_dimension_higher_width_lower_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_lower_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 203)
        self.assertEqual(scaled_dimension.height, 338)

    # cls.dimension_higher_width_higher_height = Dimension(106.780, 100.643)

    def test_scale_dimension_higher_width_higher_height_from_medium_to_low(self):
        base_density = "m"
        target_density = "l"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 80)
        self.assertEqual(scaled_dimension.height, 75)

    def test_scale_dimension_higher_width_higher_height_from_medium_to_medium(self):
        base_density = "m"
        target_density = "m"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 107)
        self.assertEqual(scaled_dimension.height, 101)

    def test_scale_dimension_higher_width_higher_height_from_medium_to_high(self):
        base_density = "m"
        target_density = "h"

        scaled_dimension = scale_dimension(
            self.dimension_higher_width_higher_height, base_density, target_density, self.densities)

        self.assertEqual(scaled_dimension.width, 160)
        self.assertEqual(scaled_dimension.height, 151)


if __name__ == "__main__":
    unittest.main()
