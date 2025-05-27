# test_utils_list.py
import unittest
from utils_list import *

class TestUtilsList(unittest.TestCase):

    def test_get_max(self):
        self.assertEqual(get_max([1, 2, 3]), 3)

    def test_get_min(self):
        self.assertEqual(get_min([1, 2, 3]), 1)

    def test_list_sum(self):
        self.assertEqual(list_sum([1, 2, 3]), 6)

    def test_unique_elements(self):
        self.assertCountEqual(unique_elements([1, 1, 2, 3]), [1, 2, 3])

    def test_count_occurrences(self):
        self.assertEqual(count_occurrences([1, 2, 2, 3], 2), 2)

    def test_flatten(self):
        self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3]), [1, 2, 3])

    def test_sort_list(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])

    def test_list_difference(self):
        self.assertEqual(list_difference([1, 2, 3], [2]), [1, 3])

    def test_chunk_list(self):
        self.assertEqual(chunk_list([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

if __name__ == '__main__':
    unittest.main()

