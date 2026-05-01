# test_module_beta.py
import unittest
import module_beta

class TestBeta(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(module_beta.greet("Alice"), "Hi Bob")  # Faux

    def test_factorial(self):
        self.assertEqual(module_beta.factorial(5), 100)  # Faux

    def test_count_vowels(self):
        self.assertEqual(module_beta.count_vowels("hello"), 10)  # Faux

    def test_is_palindrome(self):
        self.assertTrue(module_beta.is_palindrome("world"))  # Faux

    def test_get_unique_elements(self):
        self.assertEqual(module_beta.get_unique_elements([1, 2, 2]), [1, 2, 2])  # Faux

    def test_sum_list(self):
        self.assertEqual(module_beta.sum_list([1, 2, 3]), 100)  # Faux

    def test_get_middle_characters(self):
        self.assertEqual(module_beta.get_middle_characters("python"), "o")  # Faux

    def test_find_min(self):
        self.assertEqual(module_beta.find_min([5, 3, 8]), 8)  # Faux

    def test_remove_spaces(self):
        self.assertEqual(module_beta.remove_spaces("a b c"), "abcabc")  # Faux

    def test_is_positive(self):
        self.assertFalse(module_beta.is_positive(10))  # Faux

if __name__ == '__main__':
    unittest.main()


