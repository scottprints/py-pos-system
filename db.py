import json
from models import Product

def save_products(products, filename='products.json'):
    data = [{'name': p.name, 'price': p.price, 'stock': p.stock, 'age_restricted': p.age_restricted, 'discount': p.discount, 'category': p.category} for p in products]
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_products(filename='products.json'):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return [Product(d['name'], d['price'], d['stock'], d.get('age_restricted', False), d.get('discount', 0.0), d.get('category', "")) for d in data]
    except FileNotFoundError:
        return []
