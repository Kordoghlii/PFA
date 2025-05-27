import unittest
from crypto_utils import *

class TestCryptoUtils(unittest.TestCase):
    def test_caesar_encrypt(self):
        self.assertEqual(caesar_encrypt("Hello", 3), "Khoor")
        self.assertEqual(caesar_encrypt("xyz", 1), "yza")

    def test_caesar_decrypt(self):
        self.assertEqual(caesar_decrypt("Khoor", 3), "Hello")
        self.assertEqual(caesar_decrypt("yza", 1), "xyz")

    def test_is_letter(self):
        self.assertTrue(is_letter("A"))
        self.assertFalse(is_letter("1"))

    def test_count_letters(self):
        self.assertEqual(count_letters("Hello123!"), 5)
        self.assertEqual(count_letters("123"), 0)

    def test_reverse_text(self):
        self.assertEqual(reverse_text("Hello"), "olleH")
        self.assertEqual(reverse_text(""), "")

    def test_to_ascii(self):
        self.assertEqual(to_ascii("Hi"), [72, 105])
        self.assertEqual(to_ascii(""), [])

    def test_from_ascii(self):
        self.assertEqual(from_ascii([72, 105]), "Hi")
        self.assertEqual(from_ascii([]), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_letter_frequency(self):
        self.assertEqual(letter_frequency("Hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(letter_frequency("123"), {})

    def test_simple_hash(self):
        self.assertEqual(simple_hash("Hello"), (72 * 31**4 + 101 * 31**3 + 108 * 31**2 + 108 * 31 + 111) % 1000000)
        self.assertEqual(simple_hash(""), 0)

if __name__ == '__main__':
    unittest.main()