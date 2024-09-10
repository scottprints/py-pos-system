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
- **Logging**: Record events, errors, and runtime information for debugging and monitoring.
- **AI-Based Recommendations**: Provide product recommendations based on user purchase history.

## Setup

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/scottprints/py-pos-system.git
    cd py-pos-system
    ```

2. Install required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the original GUI application:
    ```sh
    python gui_original.py
    ```

2. Run the touchscreen-optimized GUI application:
    ```sh
    python gui_touchscreen.py
    ```

3. Follow the on-screen prompts to interact with the POS system.

## Functionalities

The POS system provides a range of functionalities including:

- **User Registration and Login**: Register new users and login existing users.
- **Product Management**: View, add, and update products (admin only).
- **Cart Management**: Add products to the cart, view the cart, and remove products from the cart.
- **Checkout**: Complete transactions and save the state of products.
- **Transaction History**: View a summary of all transactions (admin only).
- **Discount Management**: Apply and remove discounts on products (admin only).
- **Product Recommendations**: Get product recommendations based on a selected product.

## Code Structure

- `app.py`: Main application file containing the CLI and core functions.
- `gui_original.py`: Original GUI application file using `tkinter`.
- `gui_touchscreen.py`: Touchscreen-optimized GUI application file using `tkinter`.
- `models.py`: Contains the necessary classes (`Product`, `Cart`, `User`).
- `db.py`: Handles saving and loading product data to/from `products.json`.
- `recommendation.py`: Contains the recommendation logic using `scikit-learn`.
- `virtual_keyboard.py`: Virtual keyboard implementation for touchscreen input.
- `products.json`: JSON file storing product data.
- `requirements.txt`: File listing the required Python packages.

## License

This project is licensed under the MIT License.

![Early snapshot](https://i.imgur.com/pWHKJMY.png)