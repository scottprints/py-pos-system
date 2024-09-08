class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, amount):
        self.stock += amount

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"


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

    def __repr__(self):
        return f"Cart(items={self.items})"
