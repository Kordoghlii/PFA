# test_chaine.py

import unittest
import chaine as ch

class TestChaine(unittest.TestCase):

    def test_str1(self):
        self.assertEqual(ch.str1("hello"), "HELLO")

    def test_str2(self):
        self.assertEqual(ch.str2("bonjour"), 7)

    def test_str3(self):
        self.assertEqual(ch.str3("hello"), "olleh")

    def test_str4(self):
        self.assertTrue(ch.str4("find something"))
        self.assertFalse(ch.str4("nothing here"))

    def test_str5(self):
        self.assertTrue(ch.str5("c'est un mot"))
        self.assertFalse(ch.str5("pas de mot ici"))

    def test_str6(self):
        self.assertTrue(ch.str6("search something"))
        self.assertFalse(ch.str6("nothing to search"))

    def test_str7(self):
        self.assertEqual(ch.str7("HELLO"), "hello")

    def test_str8(self):
        self.assertEqual(ch.str8("hello world"), "hello world")

    def test_str9(self):
        self.assertEqual(ch.str9("banana"), "bn")

    def test_str10(self):
        self.assertTrue(ch.str10("madam"))
        self.assertFalse(ch.str10("hello"))

if __name__ == '__main__':
    unittest.main()
