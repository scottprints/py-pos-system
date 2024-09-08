class Product:
    def __init__(self, name, price, stock, age_restricted=False, discount=0.0, category=""):
        self.name = name
        self.price = price
        self.stock = stock
        self.age_restricted = age_restricted
        self.discount = discount
        self.category = category

    def update_stock(self, amount):
        self.stock += amount

    def apply_discount(self, discount):
        self.discount = discount

    def remove_discount(self):
        self.discount = 0.0

    def get_final_price(self):
        return self.price * (1 - self.discount)

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock}, age_restricted={self.age_restricted}, discount={self.discount}, category={self.category})"


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.name in self.items:
            self.items[product.name]['quantity'] += quantity
        else:
            self.items[product.name] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_name):
        if product_name in self.items:
            del self.items[product_name]

    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def checkout(self):
        for item in self.items.values():
            product = item['product']
            quantity = item['quantity']
            product.update_stock(-quantity)
        self.items.clear()
        print("Checkout successful. Thank you for your purchase!")

    def clear_cart(self):
        self.items.clear()

    def __repr__(self):
        return f"Cart(items={self.items})"


class User:
    def __init__(self, username, password, role='customer'):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"User(username={self.username}, role={self.role})"
