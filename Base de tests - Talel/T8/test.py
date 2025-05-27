import unittest
from string_utils import *

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words(""), "")

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates("hello"), "helo")
        self.assertEqual(remove_duplicates(""), "")

    def test_longest_word(self):
        self.assertEqual(longest_word("the quick brown fox"), "quick")
        self.assertEqual(longest_word(""), "")

    def test_char_frequency(self):
        self.assertEqual(char_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(char_frequency(""), {})

    def test_is_substring(self):
        self.assertTrue(is_substring("hell", "hello"))
        self.assertFalse(is_substring("xyz", "hello"))

    def test_replace_spaces(self):
        self.assertEqual(replace_spaces("hello world"), "hello_world")
        self.assertEqual(replace_spaces(""), "")

    def test_truncate_failing(self):
        # This test is intentionally wrong to produce a false result
        self.assertEqual(truncate("hello", 3), "hel...")  # Should be "hel", not "hel..."

if __name__ == '__main__':
    unittest.main()