import unittest
from math_utils import *

class TestMathUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(7))

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_lcm(self):
        self.assertEqual(lcm(6, 8), 24)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 8)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_is_armstrong_false(self):  # Test incorrect
        self.assertTrue(is_armstrong(100))  # Devrait échouer
if __name__ == '__main__':
    unittest.main()