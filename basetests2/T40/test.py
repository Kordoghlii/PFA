import unittest
import script1

class TestScript1(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(script1.add_numbers(2, 3), 5)

    def test_subtract_numbers(self):
        self.assertEqual(script1.subtract_numbers(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(script1.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(script1.divide(10, 2), 5)

    def test_is_even(self):
        self.assertTrue(script1.is_even(4))
        self.assertFalse(script1.is_even(5))

    def test_reverse_string(self):
        self.assertEqual(script1.reverse_string("hello"), "olleh")

    def test_factorial(self):
        self.assertEqual(script1.factorial(5), 120)

    def test_to_upper(self):
        self.assertEqual(script1.to_upper("abc"), "ABC")

    def test_count_words(self):
        self.assertEqual(script1.count_words("hello world"), 2)

    def test_square(self):
        self.assertEqual(script1.square(5), 25)

if __name__ == '__main__':
    unittest.main()


