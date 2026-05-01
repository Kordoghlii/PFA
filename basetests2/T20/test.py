import unittest
from text_analysis import *

class TestTextAnalysis(unittest.TestCase):
    def test_count_letters(self):
        # Wrong: expects "Hello123!" = 8 letters (should be 5)
        self.assertEqual(count_letters("Hello123!"), 8)

    def test_count_digits(self):
        # Wrong: expects "Hello123!" = 0 digits (should be 3)
        self.assertEqual(count_digits("Hello123!"), 0)

    def test_count_spaces(self):
        # Wrong: expects "Hello world" = 0 spaces (should be 1)
        self.assertEqual(count_spaces("Hello world"), 0)

    def test_count_punctuation(self):
        # Wrong: expects "Hello!!" = 0 punctuation (should be 2)
        self.assertEqual(count_punctuation("Hello!!"), 0)

    def test_average_word_length(self):
        # Wrong: expects "Hello world" = 6 (should be 5)
        self.assertEqual(average_word_length("Hello world"), 6)

    def test_longest_word_length(self):
        # Wrong: expects "Hello world" = 4 (should be 5)
        self.assertEqual(longest_word_length("Hello world"), 4)

    def test_shortest_word_length(self):
        # Wrong: expects "Hello hi" = 5 (should be 2)
        self.assertEqual(shortest_word_length("Hello hi"), 5)

    def test_count_unique_words(self):
        # Wrong: expects "hello Hello world" = 1 unique word (should be 2)
        self.assertEqual(count_unique_words("hello Hello world"), 1)

    def test_most_common_char(self):
        # Wrong: expects "hello" = "h" (should be "l")
        self.assertEqual(most_common_char("hello"), "h")

    def test_has_special_chars(self):
        # Wrong: expects "Hello!!" = False (should be True)
        self.assertFalse(has_special_chars("Hello!!"))

if __name__ == '__main__':
    unittest.main()