from tkinter import messagebox, simpledialog
from models import Product, Cart, User
from db import save_products, load_products
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize products
products = load_products()
if not products:
    products = [
        Product("Gizmo", 19.99, 100, category="Electronics"),
        Product("Widget", 29.99, 50, category="Electronics"),
        Product("Doodad", 9.99, 200, category="Accessories")
    ]

# Initialize cart
cart = Cart()

# Initialize transactions
transactions = []

# Initialize users
users = []
current_user = None

def display_products():
    logging.info("Displaying products")
    print("\nAvailable Products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} - ${product.price:.2f} (Stock: {product.stock})")

def add_to_cart():
    display_products()
    try:
        choice = int(input("\nEnter the product number to add to cart: ")) - 1
        quantity = int(input("Enter the quantity: "))
        if 0 <= choice < len(products):
            product = products[choice]
            if product.age_restricted:
                logging.warning(f"Attempt to add age-restricted product {product.name} without admin approval")
                print(f"{product.name} is age-restricted. Admin approval is required.")
                if current_user is None:
                    print("No admin is currently logged in. Please call an admin for approval.")
                    return
            if product.stock >= quantity:
                cart.add_product(product, quantity)
                product.update_stock(-quantity)
                logging.info(f"Added {quantity} x {product.name} to the cart")
                print(f"Added {quantity} x {product.name} to the cart.")
            else:
                logging.warning(f"Not enough stock for product {product.name}")
                print("Not enough stock available.")
        else:
            logging.error("Invalid product number entered")
            print("Invalid product number.")
    except ValueError:
        logging.error("Invalid input for product number or quantity")
        print("Invalid input. Please enter a number.")

def view_cart():
    logging.info("Viewing cart")
    print("\nCurrent Cart:")
    for item in cart.items.values():
        product = item['product']
        quantity = item['quantity']
        print(f"{product.name} - {quantity} x ${product.price:.2f}")
    print(f"Total: ${cart.calculate_total():.2f}")

def checkout():
    if cart.items:
        transactions.append(cart.items.copy())
        cart.checkout()
        save_products(products)
        logging.info("Checkout completed")
    else:
        logging.warning("Checkout attempted with an empty cart")
        print("Your cart is empty.")

def remove_from_cart():
    view_cart()
    product_name = input("\nEnter the product name to remove from cart: ")
    if product_name in cart.items:
        cart.remove_product(product_name)
        logging.info(f"Removed {product_name} from the cart")
        print(f"Removed {product_name} from the cart.")
    else:
        logging.error(f"Product {product_name} not found in cart")
        print("Product not found in cart.")

def cancel_transaction():
    cart.clear_cart()
    logging.info("Transaction cancelled")
    print("Transaction cancelled. Cart is now empty.")

def add_new_product():
    if current_user is None or current_user.role != 'admin':
        logging.warning("Attempt to add new product without admin login")
        messagebox.showwarning("Warning", "You must be logged in as an admin to perform this action.")
        return
    name = simpledialog.askstring("Input", "Enter the product name:")
    price = float(simpledialog.askstring("Input", "Enter the product price:"))
    stock = int(simpledialog.askstring("Input", "Enter the product stock:"))
    age_restricted = simpledialog.askstring("Input", "Age-restricted? (yes/no):").strip().lower() == 'yes'
    category = simpledialog.askstring("Input", "Enter the product category:")
    new_product = Product(name, price, stock, age_restricted, category=category)
    products.append(new_product)
    save_products(products)
    logging.info(f"Product {name} added successfully")
    messagebox.showinfo("Info", f"Product {name} added successfully.")

def update_product():
    if current_user is None:
        logging.warning("Attempt to update product without admin login")
        print("You must be logged in as an admin to perform this action.")
        return
    display_products()
    choice = int(input("\nEnter the product number to update: ")) - 1
    if 0 <= choice < len(products):
        product = products[choice]
        print(f"Updating {product.name}")
        product.price = float(input(f"Enter new price (current: {product.price}): "))
        product.stock = int(input(f"Enter new stock (current: {product.stock}): "))
        product.category = input(f"Enter new category (current: {product.category}): ")
        save_products(products)
        logging.info(f"Product {product.name} updated successfully")
        print(f"Product {product.name} updated successfully.")
    else:
        logging.error("Invalid product number entered for update")
        print("Invalid product number.")

def view_transactions():
    if current_user is None:
        logging.warning("Attempt to view transactions without admin login")
        print("You must be logged in as an admin to perform this action.")
        return
    logging.info("Viewing transactions")
    print("\nTransaction Summary:")
    for idx, transaction in enumerate(transactions, start=1):
        print(f"Transaction {idx}:")
        for item in transaction.values():
            product = item['product']
            quantity = item['quantity']
            print(f"  {product.name} - {quantity} x ${product.price:.2f}")
        print()

def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    new_user = User(username, password)
    users.append(new_user)
    logging.info(f"User {username} registered successfully")
    print(f"User {username} registered successfully.")

def login_user():
    global current_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users:
        if user.username == username and user.password == password:
            current_user = user
            logging.info(f"User {username} logged in successfully")
            print(f"User {username} logged in successfully.")
            return
    logging.warning("Invalid username or password entered")
    print("Invalid username or password.")

def apply_discount():
    if current_user is None or current_user.role != 'admin':
        logging.warning("Attempt to apply discount without admin login")
        print("You must be logged in as an admin to perform this action.")
        return
    display_products()
    choice = int(input("\nEnter the product number to apply discount: ")) - 1
    if 0 <= choice < len(products):
        product = products[choice]
        discount = float(input(f"Enter discount percentage for {product.name} (e.g., 0.10 for 10%): "))
        product.apply_discount(discount)
        save_products(products)
        logging.info(f"Discount of {discount*100}% applied to {product.name}")
        print(f"Discount of {discount*100}% applied to {product.name}.")
    else:
        logging.error("Invalid product number entered for discount")
        print("Invalid product number.")

def remove_discount():
    if current_user is None:
        logging.warning("Attempt to remove discount without admin login")
        print("You must be logged in as an admin to perform this action.")
        return
    display_products()
    choice = int(input("\nEnter the product number to remove discount: ")) - 1
    if 0 <= choice < len(products):
        product = products[choice]
        product.remove_discount()
        save_products(products)
        logging.info(f"Discount removed from {product.name}")
        print(f"Discount removed from {product.name}.")
    else:
        logging.error("Invalid product number entered for removing discount")
        print("Invalid product number.")

from recommendation import get_recommendations

def recommend_products():
    if not products:
        print("No products available for recommendation.")
        return
    product_name = input("Enter the product name for recommendations: ")
    if product_name not in [product.name for product in products]:
        print("Product not found.")
        return
    recommendations = get_recommendations(products, product_name)
    print(f"Recommendations for {product_name}:")
    for product in recommendations:
        print(f"- {product.name} ({product.category})")

def main():
    actions = {
        '1': register_user,
        '2': login_user,
        '3': display_products,
        '4': add_to_cart,
        '5': view_cart,
        '6': remove_from_cart,
        '7': cancel_transaction,
        '8': checkout,
        '9': add_new_product,
        '10': update_product,
        '11': view_transactions,
        '12': apply_discount,
        '13': remove_discount,
        '14': recommend_products,
        '15': exit
    }

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. View Products")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Remove from Cart")
        print("7. Cancel Transaction")
        print("8. Checkout")
        print("9. Add New Product")
        print("10. Update Product")
        print("11. View Transactions")
        print("12. Apply Discount")
        print("13. Remove Discount")
        print("14. Recommend Products")
        print("15. Exit")
        choice = input("Choose an option: ")

        action = actions.get(choice)
        if action:
            action()
        else:
            logging.error("Invalid menu choice entered")
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
