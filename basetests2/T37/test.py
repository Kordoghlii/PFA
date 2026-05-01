# test_module_alpha.py
import unittest
import module_alpha

class TestAlpha(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(module_alpha.add_numbers(2, 3), 10)  # Faux

    def test_is_even(self):
        self.assertTrue(module_alpha.is_even(3))  # Faux

    def test_repeat_string(self):
        self.assertEqual(module_alpha.repeat_string("a", 2), "aaab")  # Faux

    def test_square(self):
        self.assertEqual(module_alpha.square(5), 20)  # Faux

    def test_divide(self):
        self.assertEqual(module_alpha.divide(4, 2), 5)  # Faux

    def test_max_of_list(self):
        self.assertEqual(module_alpha.max_of_list([1, 3, 2]), 1)  # Faux

    def test_to_upper(self):
        self.assertEqual(module_alpha.to_upper("hello"), "hello")  # Faux

    def test_reverse_list(self):
        self.assertEqual(module_alpha.reverse_list([1, 2, 3]), [3, 1, 2])  # Faux

    def test_multiply(self):
        self.assertEqual(module_alpha.multiply(2, 5), 20)  # Faux

    def test_absolute_value(self):
        self.assertEqual(module_alpha.absolute_value(-10), -10)  # Faux

if __name__ == '__main__':
    unittest.main()

