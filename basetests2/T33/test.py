import unittest
from list_utils import *

class TestListUtils(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 7)  # Faux : 1+2+3 = 6

    def test_average_list(self):
        self.assertEqual(average_list([1, 2, 3]), 3)  # Faux : (1+2+3)/3 = 2

    def test_max_list(self):
        self.assertEqual(max_list([1, 5, 3]), 6)  # Faux : max = 5

    def test_min_list(self):
        self.assertEqual(min_list([1, 5, 3]), 0)  # Faux : min = 1

    def test_sort_list(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3, 4])  # Faux : [1, 2, 3]

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2])  # Faux : [3, 2, 1]

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2]), [1, 2, 2])  # Faux : [1, 2]

    def test_is_sorted(self):
        self.assertFalse(is_sorted([1, 2, 3]))  # Faux : [1, 2, 3] est triée

    def test_list_length(self):
        self.assertEqual(list_length([1, 2, 3]), 4)  # Faux : longueur = 3

    def test_append_element(self):
        self.assertEqual(append_element([1, 2], 3), [1, 2])  # Faux : [1, 2, 3]

if __name__ == '__main__':
    unittest.main()