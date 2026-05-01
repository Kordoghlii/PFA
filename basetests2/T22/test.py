import unittest
from stats_utils import *

class TestStatsUtils(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)
        self.assertEqual(mean([]), 0)

    def test_median(self):
        self.assertEqual(median([1, 3, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([]), 0)

    def test_variance(self):
        self.assertAlmostEqual(variance([1, 2, 3, 4]), 1.25)
        self.assertEqual(variance([]), 0)

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4]), 1.118033988749895)
        self.assertEqual(standard_deviation([]), 0)

    def test_min_value(self):
        self.assertEqual(min_value([3, 1, 4, 2]), 1)
        self.assertIsNone(min_value([]))

    def test_max_value(self):
        self.assertEqual(max_value([3, 1, 4, 2]), 4)
        self.assertIsNone(max_value([]))

    def test_range_values(self):
        self.assertEqual(range_values([3, 1, 4, 2]), 3)
        self.assertEqual(range_values([]), 0)

    def test_count_values(self):
        self.assertEqual(count_values([1, 2, 2, 3], 2), 2)
        self.assertEqual(count_values([], 1), 0)

    def test_sum_values(self):
        self.assertEqual(sum_values([1, 2, 3]), 6)
        self.assertEqual(sum_values([]), 0)

    def test_is_sorted_ascending(self):
        self.assertTrue(is_sorted_ascending([1, 2, 3]))
        self.assertFalse(is_sorted_ascending([3, 1, 2]))

if __name__ == '__main__':
    unittest.main()