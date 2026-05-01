import unittest
from text_utils import *

class TestTextUtils(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 2)
        self.assertEqual(count_words(""), 0)

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase(""), "")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase(""), "")

    def test_count_chars(self):
        self.assertEqual(count_chars("hello world"), 10)
        self.assertEqual(count_chars(""), 0)

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("hello, world!"), "hello world")
        self.assertEqual(remove_punctuation(""), "")

    def test_split_sentences(self):
        self.assertEqual(split_sentences("Hello. World!"), ["Hello", " World", ""])
        self.assertEqual(split_sentences(""), [""])

    def test_word_frequency(self):
        self.assertEqual(word_frequency("hello hello world"), {"hello": 2, "world": 1})
        self.assertEqual(word_frequency(""), {})

    def test_trim_whitespace(self):
        self.assertEqual(trim_whitespace("  hello  "), "hello")
        self.assertEqual(trim_whitespace(""), "")

    def test_is_all_digits(self):
        self.assertTrue(is_all_digits("123"))
        self.assertFalse(is_all_digits("12a3"))

    def test_replace_word(self):
        self.assertEqual(replace_word("hello world", "world", "earth"), "hello earth")
        self.assertEqual(replace_word("", "a", "b"), "")

if __name__ == '__main__':
    unittest.main()