import unittest
from numeric_ops import *

class TestNumericOps(unittest.TestCase):
    def test_add_numbers(self):
        # Wrong: expects 5 + 3 = 10
        self.assertEqual(add_numbers(5, 3), 10)

    def test_subtract_numbers(self):
        # Wrong: expects 5 - 3 = 8
        self.assertEqual(subtract_numbers(5, 3), 8)

    def test_multiply_numbers(self):
        # Wrong: expects 4 * 2 = 10
        self.assertEqual(multiply_numbers(4, 2), 10)

    def test_divide_numbers(self):
        # Wrong: expects 10 / 2 = 4
        self.assertEqual(divide_numbers(10, 2), 4)

    def test_modulus(self):
        # Wrong: expects 10 % 3 = 2
        self.assertEqual(modulus(10, 3), 2)

    def test_floor_division(self):
        # Wrong: expects 7 // 2 = 4
        self.assertEqual(floor_division(7, 2), 4)

    def test_power_of(self):
        # Wrong: expects 2 ** 3 = 6
        self.assertEqual(power_of(2, 3), 6)

    def test_absolute_value(self):
        # Wrong: expects abs(-5) = -5
        self.assertEqual(absolute_value(-5), -5)

    def test_round_to_decimal(self):
        # Wrong: expects round(3.14159, 2) = 3.14
        self.assertEqual(round_to_decimal(3.14159, 2), 3.15)

    def test_max_of_two(self):
        # Wrong: expects max(5, 3) = 3
        self.assertEqual(max_of_two(5, 3), 3)

if __name__ == '__main__':
    unittest.main()