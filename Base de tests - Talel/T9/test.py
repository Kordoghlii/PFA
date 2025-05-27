import unittest
from list_utils import *

class TestListUtils(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 5, 3]), 5)
        self.assertIsNone(find_max([]))

    def test_find_min(self):
        self.assertEqual(find_min([1, 5, 3]), 1)
        self.assertIsNone(find_min([]))

    def test_list_sum(self):
        self.assertEqual(list_sum([1, 2, 3]), 6)
        self.assertEqual(list_sum([]), 0)

    def test_list_average(self):
        self.assertEqual(list_average([1, 2, 3]), 2.0)
        self.assertEqual(list_average([]), 0)

    def test_remove_duplicates_list(self):
        self.assertEqual(remove_duplicates_list([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_duplicates_list([]), [])

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list([]), [])

    def test_sort_list(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])
        self.assertEqual(sort_list([]), [])

    def test_is_sorted(self):
        self.assertTrue(is_sorted([1, 2, 3]))
        self.assertFalse(is_sorted([3, 1, 2]))

    def test_merge_lists(self):
        self.assertEqual(merge_lists([1, 3], [2, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_lists([], []), [])

    def test_chunk_list_failing(self):
        # This test is intentionally wrong to produce a false result
        self.assertEqual(chunk_list([1, 2, 3, 4], 2), [[1, 2], [3]])  # Should be [[1, 2], [3, 4]]

if __name__ == '__main__':
    unittest.main()