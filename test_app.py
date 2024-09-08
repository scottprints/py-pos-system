import unittest
from unittest.mock import patch
from app import add_to_cart, products, cart

class TestApp(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2'])
    def test_add_to_cart(self, mock_input):
        product = products[0]
        initial_stock = product.stock
        add_to_cart()
        self.assertEqual(cart.items[product.name]['quantity'], 2)
        self.assertEqual(product.stock, initial_stock - 2)

if __name__ == '__main__':
    unittest.main()
