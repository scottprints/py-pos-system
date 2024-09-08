# Python Point of Sale (POS) System

## Overview

This is a modular Point of Sale (POS) system implemented in Python. It is designed to be used at a self-checkout machine in a grocery store, with additional administrative controls for managing products, approving age-restricted items, and applying discounts.

## Features

- **Product Management**: Add, update, and view products.
- **Cart Management**: Add products to the cart, view the cart, and remove products from the cart.
- **Checkout**: Complete transactions and save the state of products.
- **User Authentication**: Register and login users, with administrative controls for managing products and transactions.
- **Age-Restricted Items**: Require approval for purchasing age-restricted items.
- **Discounts**: Apply and remove discounts on products.
- **Transaction History**: View a summary of all transactions.

## Setup

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/scottprints/py-pos-system.git
    cd py-pos-system
    ```

2. Install required packages (if any):
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure the `products.json` file is in the root directory with the following initial content:
    ```json
    [
        {"name": "Gizmo", "price": 19.99, "stock": 100, "age_restricted": false},
        {"name": "Widget", "price": 29.99, "stock": 50, "age_restricted": false},
        {"name": "Doodad", "price": 9.99, "stock": 200, "age_restricted": false},
        {"name": "Alcohol", "price": 15.99, "stock": 30, "age_restricted": true}
    ]
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```

2. Follow the on-screen prompts to interact with the POS system.

### Main Menu Options

1. **Register**: Register a new user.
2. **Login**: Login as an existing user.
3. **View Products**: Display all available products.
4. **Add to Cart**: Add products to the cart.
5. **View Cart**: View the current cart.
6. **Remove from Cart**: Remove products from the cart.
7. **Cancel Transaction**: Clear the current cart.
8. **Checkout**: Complete the transaction and save the state of products.
9. **Add New Product**: Add a new product (admin only).
10. **Update Product**: Update an existing product (admin only).
11. **View Transactions**: View a summary of all transactions (admin only).
12. **Apply Discount**: Apply a discount to a product (admin only).
13. **Remove Discount**: Remove a discount from a product (admin only).
14. **Exit**: Exit the application.

## Code Structure

- `app.py`: Main application file containing the CLI and core functions.
- `models.py`: Contains the `Product`, `Cart`, and `User` classes.
- `db.py`: Handles saving and loading product data to/from `products.json`.
- `products.json`: JSON file storing product data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---