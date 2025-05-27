# test_string_utils_script2.py
import unittest
from string_utils_script2 import *

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "abc")

    def test_is_palindrome(self):
        self.assertFalse(is_palindrome("radar"))

    def test_to_upper(self):
        self.assertEqual(to_upper("abc"), "abc")

    def test_to_lower(self):
        self.assertEqual(to_lower("ABC"), "ABC")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 10)

    def test_count_consonants(self):
        self.assertEqual(count_consonants("bcdfg"), 10)

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("a b c"), "a b c")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "hello world")

    def test_string_length(self):
        self.assertEqual(string_length("abc"), 10)

    def test_contains_digit(self):
        self.assertFalse(contains_digit("abc123"))

if __name__ == '__main__':
    unittest.main()



