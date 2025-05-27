import unittest
from math_utils import *

class TestMathUtils(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(4), 16)
        self.assertEqual(square(-3), 9)

    def test_cube(self):
        self.assertEqual(cube(3), 27)
        self.assertEqual(cube(0), 0)

    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertIsNone(factorial(-1))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(0), [])

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(7, 13), 1)

    def test_lcm(self):
        self.assertEqual(lcm(6, 8), 24)
        self.assertEqual(lcm(3, 5), 15)

    def test_is_prime(self):
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))

    def test_sum_digits(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(-456), 15)

    def test_power_failing(self):
        # This test is intentionally wrong to produce a false result
        self.assertEqual(power(2, 3), 9)  # Should be 8, not 9

if __name__ == '__main__':
    unittest.main()