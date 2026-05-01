import unittest
from string_manip import *

class TestStringManip(unittest.TestCase):
    def test_concatenate_strings(self):
        # Wrong: expects "hello" + "world" = "helloworld "
        self.assertEqual(concatenate_strings("hello", "world"), "helloworld ")

    def test_first_char(self):
        # Wrong: expects first char of "hello" = "e"
        self.assertEqual(first_char("hello"), "e")

    def test_last_char(self):
        # Wrong: expects last char of "hello" = "h"
        self.assertEqual(last_char("hello"), "h")

    def test_string_length(self):
        # Wrong: expects len("hello") = 6
        self.assertEqual(string_length("hello"), 6)

    def test_to_title_case(self):
        # Wrong: expects "hello world" = "HELLO WORLD"
        self.assertEqual(to_title_case("hello world"), "HELLO WORLD")

    def test_count_char(self):
        # Wrong: expects count of "l" in "hello" = 3
        self.assertEqual(count_char("hello", "l"), 3)

    def test_starts_with(self):
        # Wrong: expects "hello".startswith("he") = False
        self.assertFalse(starts_with("hello", "he"))

    def test_ends_with(self):
        # Wrong: expects "hello".endswith("lo") = False
        self.assertFalse(ends_with("hello", "lo"))

    def test_strip_string(self):
        # Wrong: expects "  hello  ".strip() = "hello  "
        self.assertEqual(strip_string("  hello  "), "hello  ")

    def test_split_string(self):
        # Wrong: expects "a,b,c".split(",") = ["a", "b"]
        self.assertEqual(split_string("a,b,c", ","), ["a", "b"])

if __name__ == '__main__':
    unittest.main()