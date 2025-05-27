import unittest
from list_utils_script3 import *

class TestListUtils(unittest.TestCase):

    def test_list_sum(self):
        self.assertEqual(list_sum([1, 2, 3]), 6)
        self.assertEqual(list_sum([]), 0)  # Test avec liste vide
        self.assertEqual(list_sum([-1, 0, 1]), 0)  # Test avec nombres négatifs
        self.assertEqual(list_sum([10]), 10)  # Test avec un seul élément

    def test_list_max(self):
        self.assertEqual(list_max([1, 5, 3]), 5)
        self.assertEqual(list_max([-5, -1, -10]), -1)  # Test avec nombres négatifs
        self.assertEqual(list_max([7]), 7)  # Test avec un seul élément
        with self.assertRaises(ValueError):  # Test avec liste vide
            list_max([])

    def test_list_min(self):
        self.assertEqual(list_min([1, 5, 3]), 1)
        self.assertEqual(list_min([-5, -1, -10]), -10)  # Test avec nombres négatifs
        self.assertEqual(list_min([9]), 9)  # Test avec un seul élément
        with self.assertRaises(ValueError):  # Test avec liste vide
            list_min([])

    def test_average(self):
        self.assertAlmostEqual(average([1, 2, 3]), 2.0)
        self.assertAlmostEqual(average([10, 20, 30, 40]), 25.0)
        self.assertAlmostEqual(average([-1, 0, 1]), 0.0)  # Test avec nombres négatifs
        self.assertEqual(average([5]), 5.0)  # Test avec un seul élément
        with self.assertRaises(ZeroDivisionError):  # Test avec liste vide
            average([])

    def test_list_length(self):
        self.assertEqual(list_length([1, 2, 3]), 3)
        self.assertEqual(list_length([]), 0)  # Test avec liste vide
        self.assertEqual(list_length(['a', 'b', 'c', 'd']), 4)  # Test avec strings

    def test_contains_element(self):
        self.assertTrue(contains_element([1, 2, 3], 2))
        self.assertFalse(contains_element([1, 2, 3], 4))
        self.assertFalse(contains_element([], 1))  # Test avec liste vide
        self.assertTrue(contains_element(['a', 'b'], 'a'))  # Test avec strings

    def test_remove_element(self):
        self.assertEqual(remove_element([1, 2, 3], 2), [1, 3])
        self.assertEqual(remove_element([1, 2, 3], 4), [1, 2, 3])  # Élément non présent
        self.assertEqual(remove_element([], 1), [])  # Test avec liste vide
        self.assertEqual(remove_element([1, 2, 2, 3], 2), [1, 2, 3])  # Supprime une seule occurrence

    def test_duplicate_elements(self):
        self.assertEqual(duplicate_elements([1, 2]), [1, 2, 1, 2])
        self.assertEqual(duplicate_elements([]), [])  # Test avec liste vide
        self.assertEqual(duplicate_elements(['a']), ['a', 'a'])  # Test avec strings

    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_list([]), [])  # Test avec liste vide
        self.assertEqual(reverse_list([1]), [1])  # Test avec un seul élément

    def test_unique_elements(self):
        self.assertEqual(sorted(unique_elements([1, 2, 2, 3])), [1, 2, 3])
        self.assertEqual(unique_elements([]), [])  # Test avec liste vide
        self.assertEqual(unique_elements(['a', 'b', 'a']), ['a', 'b'] or ['b', 'a'])  # Test avec strings (ordre non garanti)

if __name__ == '__main__':
    unittest.main()