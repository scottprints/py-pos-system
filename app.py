from models import Product, Cart

# Create some products
product1 = Product("Gizmo", 19.99, 100)
product2 = Product("Widget", 29.99, 50)

# Create a cart and add products
cart = Cart()
cart.add_product(product1, 2)
cart.add_product(product2, 1)

# Print cart details and total
print(cart)
print(f"Total: ${cart.calculate_total():.2f}")

# Update stock and print product details
product1.update_stock(-2)
print(product1)
