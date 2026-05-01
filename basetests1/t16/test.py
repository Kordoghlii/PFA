import unittest
from library import *

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = {}

    def test_add_book(self):
        result = add_book(self.library, "123", "Python", "John Doe", 2020)
        self.assertEqual(result["123"], {"title": "Python", "author": "John Doe", "year": 2020, "available": True})

    def test_remove_book(self):
        add_book(self.library, "123", "Python", "John Doe", 2020)
        result = remove_book(self.library, "123")
        self.assertNotIn("123", result)

    def test_borrow_book(self):
        add_book(self.library, "123", "Python", "John Doe", 2020)
        result = borrow_book(self.library, "123")
        self.assertFalse(result["123"]["available"])

    def test_count_books_by_author(self):
        add_book(self.library, "123", "Python", "John Doe", 2020)
        add_book(self.library, "456", "Java", "John Doe", 2021)
        self.assertEqual(count_books_by_author(self.library, "John Doe"), 2)

    def test_is_book_available(self):
        add_book(self.library, "123", "Python", "John Doe", 2020)
        borrow_book(self.library, "123")
        self.assertFalse(is_book_available(self.library, "123"))
if __name__ == '__main__':
    unittest.main()