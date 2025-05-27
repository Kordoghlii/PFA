import unittest
import script2

class TestScript2(unittest.TestCase):

    def test_get_length(self):
        self.assertEqual(script2.get_length([1, 2, 3]), 3)

    def test_max_of_two(self):
        self.assertEqual(script2.max_of_two(10, 20), 20)

    def test_min_of_two(self):
        self.assertEqual(script2.min_of_two(10, 5), 5)

    def test_is_palindrome(self):
        self.assertTrue(script2.is_palindrome("radar"))
        self.assertFalse(script2.is_palindrome("hello"))

    def test_capitalize_words(self):
        self.assertEqual(script2.capitalize_words("hello world"), "Hello World")

    def test_sum_list(self):
        self.assertEqual(script2.sum_list([1, 2, 3]), 6)

    def test_is_positive(self):
        self.assertTrue(script2.is_positive(3))
        self.assertFalse(script2.is_positive(-2))

    def test_char_frequency(self):
        self.assertEqual(script2.char_frequency("banana", "a"), 3)

    def test_unique_elements(self):
        self.assertEqual(set(script2.unique_elements([1, 2, 2, 3])), {1, 2, 3})

    def test_average(self):
        self.assertAlmostEqual(script2.average([2, 4, 6]), 4)

if __name__ == '__main__':
    unittest.main()



