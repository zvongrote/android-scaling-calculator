import unittest
import sys
from tests.test_dimension import DimensionTest
from tests.test_scale import ScaleTest


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner().run(suite)