import unittest
import script3

class TestScript3(unittest.TestCase):

    def test_remove_spaces(self):
        self.assertEqual(script3.remove_spaces("a b c"), "abc")

    def test_count_characters(self):
        self.assertEqual(script3.count_characters("hello"), 5)

    def test_is_uppercase(self):
        self.assertTrue(script3.is_uppercase("HELLO"))
        self.assertFalse(script3.is_uppercase("Hello"))

    def test_sort_list(self):
        self.assertEqual(script3.sort_list([3, 1, 2]), [1, 2, 3])

    def test_starts_with(self):
        self.assertTrue(script3.starts_with("hello", "he"))

    def test_ends_with(self):
        self.assertTrue(script3.ends_with("hello", "lo"))

    def test_repeat_string(self):
        self.assertEqual(script3.repeat_string("hi", 3), "hihihi")

    def test_contains_substring(self):
        self.assertTrue(script3.contains_substring("hello world", "world"))

    def test_abs_diff(self):
        self.assertEqual(script3.abs_diff(10, 4), 6)

    def test_string_to_list(self):
        self.assertEqual(script3.string_to_list("hello world"), ["hello", "world"])

if __name__ == '__main__':
    unittest.main()



