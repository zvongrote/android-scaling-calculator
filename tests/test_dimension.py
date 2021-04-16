from scaling_calculator import Dimension
import unittest
from random import randrange, random
from sys import maxsize


class DimensionTest(unittest.TestCase):

    def test_width_and_height(self):
        width = randrange(1, maxsize) * random()
        height = randrange(1, maxsize) * random()

        dimension = Dimension(width, height)

        self.assertAlmostEqual(width, dimension.width)
        self.assertAlmostEqual(height, dimension.height)

    def test_scale(self):
        width = randrange(1, maxsize) * random()
        height = randrange(1, maxsize) * random()
        dimension = Dimension(width, height)

        scaling_factor = randrange(1, maxsize) / randrange(1, maxsize)

        new_dimension = dimension.scale(scaling_factor)

        self.assertAlmostEqual(new_dimension.width, width * scaling_factor)
        self.assertAlmostEqual(new_dimension.height, height * scaling_factor)


if __name__ == "__main__":
    unittest.main()
