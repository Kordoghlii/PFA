import unittest
from list_ops import *

class TestListOps(unittest.TestCase):
    def test_append_item(self):
        # Wrong: expects [1, 2] + [3] = [1, 2, 3, 3]
        self.assertEqual(append_item([1, 2], 3), [1, 2, 3, 3])

    def test_pop_last(self):
        # Wrong: expects pop from [1, 2, 3] = 2
        self.assertEqual(pop_last([1, 2, 3]), 2)

    def test_list_length(self):
        # Wrong: expects len([1, 2, 3]) = 4
        self.assertEqual(list_length([1, 2, 3]), 4)

    def test_get_first(self):
        # Wrong: expects first of [1, 2, 3] = 2
        self.assertEqual(get_first([1, 2, 3]), 2)

    def test_get_last(self):
        # Wrong: expects last of [1, 2, 3] = 1
        self.assertEqual(get_last([1, 2, 3]), 1)

    def test_contains_item(self):
        # Wrong: expects 2 in [1, 3, 4] = False
        self.assertFalse(contains_item([1, 3, 4], 2))

    def test_remove_first(self):
        # Wrong: expects remove first from [1, 2, 3] = [2, 3, 4]
        self.assertEqual(remove_first([1, 2, 3]), [2, 3, 4])

    def test_sort_ascending(self):
        # Wrong: expects sorted([3, 1, 2]) = [3, 2, 1]
        self.assertEqual(sort_ascending([3, 1, 2]), [3, 2, 1])

    def test_reverse_list(self):
        # Wrong: expects reverse([1, 2, 3]) = [1, 2, 3]
        self.assertEqual(reverse_list([1, 2, 3]), [1, 2, 3])

    def test_sum_list(self):
        # Wrong: expects sum([1, 2, 3]) = 7
        self.assertEqual(sum_list([1, 2, 3]), 7)

if __name__ == '__main__':
    unittest.main()