import unittest
from string_utils import *

class TestStringUtils(unittest.TestCase):
    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO!")  # Faux : pas de !

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello!")  # Faux : pas de !

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olle")  # Faux : olleh

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 3)  # Faux : 2 voyelles

    def test_is_palindrome(self):
        self.assertFalse(is_palindrome("racecar"))  # Faux : racecar est palindrome

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("hello world"), "helloworld ")  # Faux : pas d'espace

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello world")  # Faux : Hello World

    def test_count_words(self):
        self.assertEqual(count_words("hello world"), 3)  # Faux : 2 mots

    def test_replace_char(self):
        self.assertEqual(replace_char("hello", "l", "x"), "hexxo")  # Faux : hexlo

    def test_is_alpha(self):
        self.assertFalse(is_alpha("hello"))  # Faux : hello est alpha

if __name__ == '__main__':
    unittest.main()