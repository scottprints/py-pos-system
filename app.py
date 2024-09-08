from models import Product, Cart

# Initialize products
products = [
    Product("Gizmo", 19.99, 100),
    Product("Widget", 29.99, 50),
    Product("Doodad", 9.99, 200)
]

# Initialize cart
cart = Cart()

def display_products():
    print("\nAvailable Products:")
    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name} - ${product.price:.2f} (Stock: {product.stock})")

def add_to_cart():
    display_products()
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

def view_cart():
    print("\nCurrent Cart:")
    for item in cart.items.values():
        product = item['product']
        quantity = item['quantity']
        print(f"{product.name} - {quantity} x ${product.price:.2f}")
    print(f"Total: ${cart.calculate_total():.2f}")

def main():
    while True:
        print("\n1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_cart()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
