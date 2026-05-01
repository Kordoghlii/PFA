# test_utils_math.py
import unittest
from utils_math import *

class TestUtilsMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self):
        self.assertAlmostEqual(divide(8, 2), 4)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_mod(self):
        self.assertEqual(mod(10, 3), 1)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(3))

    def test_is_odd(self):
        self.assertTrue(is_odd(5))
        self.assertFalse(is_odd(8))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_average(self):
        self.assertAlmostEqual(average([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            average([])

if __name__ == '__main__':
    unittest.main()
