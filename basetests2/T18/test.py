import unittest
from set_utils import *

class TestSetUtils(unittest.TestCase):
    def test_union_sets(self):
        self.assertEqual(union_sets({1, 2}, {2, 3}), {1, 2, 3})
        self.assertEqual(union_sets(set(), {1}), {1})

    def test_intersection_sets(self):
        self.assertEqual(intersection_sets({1, 2, 3}, {2, 3, 4}), {2, 3})
        self.assertEqual(intersection_sets({1}, {2}), set())

    def test_difference_sets(self):
        self.assertEqual(difference_sets({1, 2, 3}, {2, 4}), {1, 3})
        self.assertEqual(difference_sets({1}, {1}), set())

    def test_symmetric_difference_sets(self):
        self.assertEqual(symmetric_difference_sets({1, 2}, {2, 3}), {1, 3})
        self.assertEqual(symmetric_difference_sets(set(), set()), set())

    def test_is_subset(self):
        self.assertTrue(is_subset({1, 2}, {1, 2, 3}))
        self.assertFalse(is_subset({1, 4}, {1, 2, 3}))

    def test_is_superset(self):
        self.assertTrue(is_superset({1, 2, 3}, {1, 2}))
        self.assertFalse(is_superset({1, 2}, {1, 2, 3}))

    def test_add_element(self):
        self.assertEqual(add_element({1, 2}, 3), {1, 2, 3})
        self.assertEqual(add_element(set(), 1), {1})

    def test_remove_element(self):
        self.assertEqual(remove_element({1, 2, 3}, 2), {1, 3})
        self.assertEqual(remove_element({1}, 2), {1})

    def test_set_size(self):
        self.assertEqual(set_size({1, 2, 3}), 3)
        self.assertEqual(set_size(set()), 0)

    def test_is_disjoint(self):
        self.assertTrue(is_disjoint({1, 2}, {3, 4}))
        self.assertFalse(is_disjoint({1, 2}, {2, 3}))

if __name__ == '__main__':
    unittest.main()