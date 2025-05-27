import unittest
from string_utils import *

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates("hello"), "helo")

    def test_longest_word_empty(self):  # Test incorrect
        self.assertEqual(longest_word(""), "hello")  # Devrait échouer
if __name__ == '__main__':
    unittest.main()