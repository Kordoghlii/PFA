# test_utils_string.py
import unittest
from utils_string import *

class TestUtilsString(unittest.TestCase):

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")

    def test_count_words(self):
        self.assertEqual(count_words("Hello world!"), 2)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("abc"), "cba")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("Hello"))

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_contains_number(self):
        self.assertTrue(contains_number("abc123"))
        self.assertFalse(contains_number("abc"))

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("a b c"), "abc")

if __name__ == '__main__':
    unittest.main()
