import tkinter as tk

class VirtualKeyboard(tk.Toplevel):
    def __init__(self, entry_widget, prompt="Enter the quantity of items:"):
        super().__init__()
        self.entry_widget = entry_widget
        self.title("Virtual Keyboard")
        self.geometry("800x600")
        self.create_widgets(prompt)

    def create_widgets(self, prompt):
        self.display_label = tk.Label(self, text=prompt, font=("Helvetica", 24))
        self.display_label.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.05)

        keys = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', 'Backspace', 'Enter'
        ]

        for i, key in enumerate(keys):
            button = tk.Button(self, text=key, font=("Helvetica", 18), command=lambda k=key: self.on_key_press(k))
            button.place(relwidth=0.25, relheight=0.15, relx=(i % 3) * 0.3 + 0.05, rely=(i // 3) * 0.15 + 0.2)

    def on_key_press(self, key):
        if key == 'Enter':
            self.destroy()
        elif key == 'Backspace':
            current_text = self.entry_widget.get()
            self.entry_widget.delete(0, tk.END)
            self.entry_widget.insert(tk.END, current_text[:-1])
        else:
            self.entry_widget.insert(tk.END, key)
        
        if self.display_label.winfo_exists():
            self.display_label.config(text=self.entry_widget.get())
