import unittest
from models import Product, Cart

class TestProduct(unittest.TestCase):
    def test_update_stock(self):
        product = Product("Test", 10.0, 100)
        product.update_stock(-10)
        self.assertEqual(product.stock, 90)

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.product = Product("Test", 10.0, 100)

    def test_add_product(self):
        self.cart.add_product(self.product, 2)
        self.assertIn("Test", self.cart.items)
        self.assertEqual(self.cart.items["Test"]["quantity"], 2)

    def test_calculate_total(self):
        self.cart.add_product(self.product, 2)
        self.assertEqual(self.cart.calculate_total(), 20.0)

    def test_checkout(self):
        self.cart.add_product(self.product, 2)
        self.cart.checkout()
        self.assertEqual(self.product.stock, 98)
        self.assertEqual(len(self.cart.items), 0)

if __name__ == '__main__':
    unittest.main()
