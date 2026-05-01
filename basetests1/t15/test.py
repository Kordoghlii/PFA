import unittest
from stats import *

class TestStats(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_median_odd(self):
        self.assertEqual(median([1, 3, 2]), 2)

    def test_variance(self):
        self.assertAlmostEqual(variance([1, 2, 3]), 0.6666666666666666)

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3]), 0.816496580927726)

    def test_frequency(self):
        self.assertEqual(frequency([1, 1, 2]), {1: 2, 2: 1})
if __name__ == '__main__':
    unittest.main()