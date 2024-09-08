from models import Product, Cart, User
from db import save_products, load_products

# Initialize products
products = load_products()
if not products:
    products = [
        Product("Gizmo", 19.99, 100),
        Product("Widget", 29.99, 50),
        Product("Doodad", 9.99, 200)
    ]

# Initialize cart
cart = Cart()

# Initialize transactions
transactions = []

# Initialize users
users = []
current_user = None

def display_products():
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
            if product.stock >= quantity:
                cart.add_product(product, quantity)
                product.update_stock(-quantity)
                print(f"Added {quantity} x {product.name} to the cart.")
            else:
                print("Not enough stock available.")
        else:
            print("Invalid product number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_cart():
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
    else:
        print("Your cart is empty.")

def remove_from_cart():
    view_cart()
    product_name = input("\nEnter the product name to remove from cart: ")
    if product_name in cart.items:
        cart.remove_product(product_name)
        print(f"Removed {product_name} from the cart.")
    else:
        print("Product not found in cart.")

def cancel_transaction():
    cart.clear_cart()
    print("Transaction cancelled. Cart is now empty.")

def add_new_product():
    if current_user is None:
        print("You must be logged in as an admin to perform this action.")
        return
    name = input("Enter the product name: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the product stock: "))
    new_product = Product(name, price, stock)
    products.append(new_product)
    save_products(products)
    print(f"Product {name} added successfully.")

def update_product():
    if current_user is None:
        print("You must be logged in as an admin to perform this action.")
        return
    display_products()
    choice = int(input("\nEnter the product number to update: ")) - 1
    if 0 <= choice < len(products):
        product = products[choice]
        print(f"Updating {product.name}")
        product.price = float(input(f"Enter new price (current: {product.price}): "))
        product.stock = int(input(f"Enter new stock (current: {product.stock}): "))
        save_products(products)
        print(f"Product {product.name} updated successfully.")
    else:
        print("Invalid product number.")

def view_transactions():
    if current_user is None:
        print("You must be logged in as an admin to perform this action.")
        return
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
    print(f"User {username} registered successfully.")

def login_user():
    global current_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users:
        if user.username == username and user.password == password:
            current_user = user
            print(f"User {username} logged in successfully.")
            return
    print("Invalid username or password.")

def main():
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
        print("12. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            display_products()
        elif choice == '4':
            add_to_cart()
        elif choice == '5':
            view_cart()
        elif choice == '6':
            remove_from_cart()
        elif choice == '7':
            cancel_transaction()
        elif choice == '8':
            checkout()
        elif choice == '9':
            add_new_product()
        elif choice == '10':
            update_product()
        elif choice == '11':
            view_transactions()
        elif choice == '12':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
