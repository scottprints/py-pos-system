import unittest
from unittest.mock import patch
from app import add_to_cart, products, cart, current_user, login_user

class TestApp(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2'])
    def test_add_to_cart(self, mock_input):
        product = products[0]
        initial_stock = product.stock
        add_to_cart()
        self.assertEqual(cart.items[product.name]['quantity'], 2)
        self.assertEqual(product.stock, initial_stock - 2)

    @patch('builtins.input', side_effect=['4', '1', '2'])
    def test_add_age_restricted_to_cart_no_admin(self, mock_input):
        product = products[3]  # Assuming this is the age-restricted product
        initial_stock = product.stock
        add_to_cart()
        self.assertNotIn(product.name, cart.items)
        self.assertEqual(product.stock, initial_stock)

    @patch('builtins.input', side_effect=['admin', 'password', '4', '1', '2'])
    def test_add_age_restricted_to_cart_with_admin(self, mock_input):
        login_user()
        product = products[3]  # Assuming this is the age-restricted product
        initial_stock = product.stock
        add_to_cart()
        self.assertEqual(cart.items[product.name]['quantity'], 2)
        self.assertEqual(product.stock, initial_stock - 2)

if __name__ == '__main__':
    unittest.main()
