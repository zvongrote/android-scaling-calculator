from scaling_calculator import Dimension
import unittest
from random import randrange, random

class DimensionTest(unittest.TestCase):

    def test_width_and_height(self):
        width = randrange(1) * random()
        height = randrange(1) * random()

        dimension = Dimension(width, height)

        self.assertAlmostEqual(width, dimension.width)
        self.assertAlmostEqual(height, dimension.height)

if __name__ == "__main__":
    unittest.main()