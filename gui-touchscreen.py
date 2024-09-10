import tkinter as tk
from tkinter import messagebox, simpledialog
from app import (
    register_user, login_user, display_products, add_to_cart, view_cart,
    remove_from_cart, cancel_transaction, checkout, add_new_product,
    update_product, view_transactions, apply_discount, remove_discount,
    recommend_products, products, cart, save_products, transactions
)
from recommendation import get_recommendations
from virtual_keyboard import VirtualKeyboard

class POSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("POS System")
        self.root.attributes('-fullscreen', True)

        self.create_widgets()

    def create_widgets(self):
        # Create frames
        self.left_frame = tk.Frame(self.root, bg="lightgrey")
        self.left_frame.place(relwidth=0.5, relheight=1.0)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.place(relx=0.5, relwidth=0.5, relheight=1.0)

        # Left frame (Product display)
        self.product_listbox = tk.Listbox(self.left_frame, font=("Helvetica", 14))
        self.product_listbox.place(relwidth=0.9, relheight=0.7, rely=0.05, relx=0.05)

        self.refresh_products_button = tk.Button(self.left_frame, text="Refresh Products", command=self.refresh_products, font=("Helvetica", 14))
        self.refresh_products_button.place(relwidth=0.9, relheight=0.1, rely=0.8, relx=0.05)

        # Right frame (Cart and actions)
        self.cart_listbox = tk.Listbox(self.right_frame, font=("Helvetica", 14))
        self.cart_listbox.place(relwidth=0.9, relheight=0.4, rely=0.05, relx=0.05)

        self.total_label = tk.Label(self.right_frame, text="Total: $0.00", font=("Helvetica", 14))
        self.total_label.place(relwidth=0.9, relheight=0.1, rely=0.5, relx=0.05)

        self.add_to_cart_button = tk.Button(self.right_frame, text="Add to Cart", command=self.add_to_cart, font=("Helvetica", 14))
        self.add_to_cart_button.place(relwidth=0.9, relheight=0.08, rely=0.6, relx=0.05)

        self.remove_from_cart_button = tk.Button(self.right_frame, text="Remove from Cart", command=self.remove_from_cart, font=("Helvetica", 14))
        self.remove_from_cart_button.place(relwidth=0.9, relheight=0.08, rely=0.68, relx=0.05)

        self.checkout_button = tk.Button(self.right_frame, text="Checkout", command=self.checkout, font=("Helvetica", 14))
        self.checkout_button.place(relwidth=0.9, relheight=0.08, rely=0.76, relx=0.05)

        self.cancel_transaction_button = tk.Button(self.right_frame, text="Cancel Transaction", command=self.cancel_transaction, font=("Helvetica", 14))
        self.cancel_transaction_button.place(relwidth=0.9, relheight=0.08, rely=0.84, relx=0.05)

        self.exit_button = tk.Button(self.right_frame, text="Exit", command=self.root.quit, font=("Helvetica", 14))
        self.exit_button.place(relwidth=0.9, relheight=0.08, rely=0.92, relx=0.05)

        self.refresh_products()

    def refresh_products(self):
        self.product_listbox.delete(0, tk.END)
        for product in products:
            self.product_listbox.insert(tk.END, f"{product.name} - ${product.price:.2f} (Stock: {product.stock})")

    def add_to_cart(self):
        selected_product = self.product_listbox.curselection()
        if not selected_product:
            messagebox.showwarning("Warning", "Please select a product to add to the cart.")
            return
        product_idx = selected_product[0]
        quantity_entry = tk.Entry(self.root, font=("Helvetica", 14))
        quantity_entry.place_forget()
        virtual_keyboard = VirtualKeyboard(quantity_entry, prompt="Enter the quantity of items:")
        self.root.wait_window(virtual_keyboard)
        try:
            quantity = int(quantity_entry.get())
            if quantity <= 0:
                messagebox.showwarning("Warning", "Invalid quantity.")
                return
        except ValueError:
            messagebox.showwarning("Warning", "Invalid quantity.")
            return

        product = products[product_idx]
        if product.stock < quantity:
            messagebox.showwarning("Warning", "Not enough stock available.")
            return
        cart.add_product(product, quantity)
        product.update_stock(-quantity)
        self.update_cart()
        self.refresh_products()

    def remove_from_cart(self):
        selected_item = self.cart_listbox.curselection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an item to remove from the cart.")
            return
        item_idx = selected_item[0]
        product_name = list(cart.items.keys())[item_idx]
        cart.remove_product(product_name)
        self.update_cart()

    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        for item in cart.items.values():
            product = item['product']
            quantity = item['quantity']
            self.cart_listbox.insert(tk.END, f"{product.name} - {quantity} x ${product.price:.2f}")
        self.total_label.config(text=f"Total: ${cart.calculate_total():.2f}")

    def checkout(self):
        if not cart.items:
            messagebox.showwarning("Warning", "Your cart is empty.")
            return
        transactions.append(cart.items.copy())
        cart.checkout()
        save_products(products)
        self.update_cart()
        self.refresh_products()
        messagebox.showinfo("Info", "Checkout successful. Thank you for your purchase!")

    def cancel_transaction(self):
        cart.clear_cart()
        self.update_cart()
        messagebox.showinfo("Info", "Transaction cancelled. Cart is now empty.")

    def recommend_products(self):
        selected_product = self.product_listbox.curselection()
        if not selected_product:
            messagebox.showwarning("Warning", "Please select a product for recommendations.")
            return
        product_idx = selected_product[0]
        product_name = products[product_idx].name
        recommendations = get_recommendations(products, product_name)
        recommendation_text = f"Recommendations for {product_name}:\n"
        for idx, product in enumerate(recommendations, start=1):
            recommendation_text += f"{idx}. {product.name} ({product.category})\n"
        recommendation_text += "\nSelect a product number to add to cart."
        selected_recommendation_entry = tk.Entry(self.root, font=("Helvetica", 14))
        selected_recommendation_entry.place_forget()
        virtual_keyboard = VirtualKeyboard(selected_recommendation_entry)
        self.root.wait_window(virtual_keyboard)
        try:
            selected_recommendation = int(selected_recommendation_entry.get())
            if selected_recommendation is not None and 1 <= selected_recommendation <= len(recommendations):
                recommended_product = recommendations[selected_recommendation - 1]
                quantity_entry = tk.Entry(self.root, font=("Helvetica", 14))
                quantity_entry.place_forget()
                virtual_keyboard = VirtualKeyboard(quantity_entry)
                self.root.wait_window(virtual_keyboard)
                quantity = int(quantity_entry.get())
                if quantity <= 0:
                    messagebox.showwarning("Warning", "Invalid quantity.")
                    return
                if recommended_product.stock < quantity:
                    messagebox.showwarning("Warning", "Not enough stock available.")
                    return
                cart.add_product(recommended_product, quantity)
                recommended_product.update_stock(-quantity)
                self.update_cart()
                self.refresh_products()
        except ValueError:
            messagebox.showwarning("Warning", "Invalid selection.")
            return

if __name__ == "__main__":
    root = tk.Tk()
    app = POSApp(root)
    root.mainloop()