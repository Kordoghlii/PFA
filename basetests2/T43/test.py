# test_utils_script1.py
import unittest
from utils_script1 import *

class TestUtils(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 10)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 1)

    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 3)

    def test_power(self):
        self.assertEqual(power(2, 3), 5)

    def test_mod(self):
        self.assertEqual(mod(10, 3), 1.5)

    def test_is_even(self):
        self.assertTrue(is_even(3))

    def test_is_odd(self):
        self.assertFalse(is_odd(7))

    def test_max_of_two(self):
        self.assertEqual(max_of_two(3, 9), 3)

    def test_min_of_two(self):
        self.assertEqual(min_of_two(1, -1), 1)

if __name__ == '__main__':
    unittest.main()


