import tkinter as tk

class VirtualKeyboard(tk.Toplevel):
    def __init__(self, entry_widget):
        super().__init__()
        self.entry_widget = entry_widget
        self.title("Virtual Keyboard")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.display_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.display_label.grid(row=0, column=0, columnspan=3, pady=10)

        keys = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', 'Backspace', 'Enter'
        ]

        for i, key in enumerate(keys):
            button = tk.Button(self, text=key, width=5, height=2, command=lambda k=key: self.on_key_press(k))
            button.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)

    def on_key_press(self, key):
        if key == 'Enter':
            self.destroy()
        elif key == 'Backspace':
            current_text = self.entry_widget.get()
            self.entry_widget.delete(0, tk.END)
            self.entry_widget.insert(tk.END, current_text[:-1])
        else:
            self.entry_widget.insert(tk.END, key)
        self.display_label.config(text=self.entry_widget.get())
