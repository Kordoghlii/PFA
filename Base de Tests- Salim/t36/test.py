# test_liste.py

import unittest
import liste as lst

class TestListe(unittest.TestCase):

    def test_lst1(self):
        self.assertEqual(lst.lst1([1, 2, 3]), 6)

    def test_lst2(self):
        self.assertEqual(lst.lst2([4, 2, 8]), 8)

    def test_lst3(self):
        self.assertEqual(lst.lst3([4, 2, 8]), 2)

    def test_lst4(self):
        self.assertEqual(lst.lst4([3, 1, 2]), [1, 2, 3])

    def test_lst5(self):
        self.assertTrue(lst.lst5([1, 2, 3]))
        self.assertFalse(lst.lst5([4, 5, 6]))

    def test_lst6(self):
        self.assertEqual(lst.lst6([1, 2, 3, 3]), 2)

    def test_lst7(self):
        self.assertEqual(lst.lst7([1, 2, 3]), [1, 2, 3, 10])

    def test_lst8(self):
        self.assertEqual(lst.lst8([1, 2, 3]), [1, 2])

    def test_lst9(self):
        self.assertEqual(lst.lst9([1, 2, 3]), [3, 2, 1])

    def test_lst10(self):
        self.assertEqual(lst.lst10([1, 2, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
