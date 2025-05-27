import unittest
from math_utils import *

class TestMathUtils(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 6)  # Faux : 2 + 3 = 5

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 1)  # Faux : 5 - 3 = 2

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 3), 10)  # Faux : 4 * 3 = 12

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 4)  # Faux : 10 / 2 = 5

    def test_power_number(self):
        self.assertEqual(power_number(2, 3), 9)  # Faux : 2^3 = 8

    def test_square_root(self):
        self.assertEqual(square_root(16), 5)  # Faux : sqrt(16) = 4

    def test_absolute_value(self):
        self.assertEqual(absolute_value(-5), -5)  # Faux : |-5| = 5

    def test_is_even(self):
        self.assertFalse(is_even(4))  # Faux : 4 est pair

    def test_factorial(self):
        self.assertEqual(factorial(5), 100)  # Faux : 5! = 120

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 7)  # Faux : F(6) = 8

if __name__ == '__main__':
    unittest.main()