import unittest
from inventory import *

class TestInventory(unittest.TestCase):
    def setUp(self):
        self.inventory = {}

    def test_add_product(self):
        result = add_product(self.inventory, "apple", 0.5, 100)
        self.assertEqual(result["apple"], {"price": 0.5, "quantity": 100})

    def test_remove_product(self):
        add_product(self.inventory, "apple", 0.5, 100)
        result = remove_product(self.inventory, "apple")
        self.assertNotIn("apple", result)

    def test_update_price(self):
        add_product(self.inventory, "apple", 0.5, 100)
        result = update_price(self.inventory, "apple", 0.6)
        self.assertEqual(result["apple"]["price"], 0.6)

    def test_total_value(self):
        add_product(self.inventory, "apple", 0.5, 100)
        add_product(self.inventory, "banana", 0.3, 50)
        self.assertEqual(get_total_value(self.inventory), 65.0)

    def test_is_available_false(self):  # Test incorrect
        add_product(self.inventory, "apple", 0.5, 10)
        self.assertTrue(is_product_available(self.inventory, "apple", 20))  # Devrait échouer
if __name__ == '__main__':
    unittest.main()