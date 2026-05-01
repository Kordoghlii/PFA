import unittest
from number_utils import *

class TestNumberUtils(unittest.TestCase):
    def test_is_multiple(self):
        self.assertTrue(is_multiple(10, 2))
        self.assertFalse(is_multiple(7, 3))

    def test_round_number(self):
        self.assertEqual(round_number(3.14159, 2), 3.14)
        self.assertEqual(round_number(5.0, 0), 5.0)

    def test_absolute_difference(self):
        self.assertEqual(absolute_difference(5, 2), 3)
        self.assertEqual(absolute_difference(2, 5), 3)

    def test_to_binary(self):
        self.assertEqual(to_binary(10), "1010")
        self.assertEqual(to_binary(0), "0")

    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(16))
        self.assertFalse(is_perfect_square(15))

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(3), 14)  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
        self.assertEqual(sum_of_squares(0), 0)

    def test_is_power_of_two(self):
        self.assertTrue(is_power_of_two(8))
        self.assertFalse(is_power_of_two(6))

    def test_next_prime(self):
        self.assertEqual(next_prime(7), 11)
        self.assertEqual(next_prime(13), 17)

    def test_digit_count(self):
        self.assertEqual(digit_count(123), 3)
        self.assertEqual(digit_count(-45), 2)

    def test_clamp(self):
        self.assertEqual(clamp(10, 0, 5), 5)
        self.assertEqual(clamp(-1, 0, 5), 0)
        self.assertEqual(clamp(3, 0, 5), 3)

if __name__ == '__main__':
    unittest.main()