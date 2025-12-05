"""
Basic Example
Demonstrates basic theme usage with tkthemes
"""

import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme

# Create the main window
root = tk.Tk()
root.title("tkthemes Basic Example")
root.geometry("400x300")

# Get the ttk style
style = ttk.Style()

# Apply the neon theme
bg_color = apply_theme("neon", style, root)

# Create some widgets to demonstrate the theme
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Hello, themed world!", style="Header.TLabel").pack(pady=10)
ttk.Label(main_frame, text="This is a standard label").pack(pady=5)

button_frame = ttk.Frame(main_frame)
button_frame.pack(pady=10)
ttk.Button(button_frame, text="Normal Button").pack(side="left", padx=5)
ttk.Button(button_frame, text="Control Button", style="Control.TButton").pack(side="left", padx=5)

ttk.Entry(main_frame).pack(pady=5, fill="x")

check_frame = ttk.Frame(main_frame)
check_frame.pack(pady=5)
ttk.Checkbutton(check_frame, text="Checkbox option").pack(side="left", padx=10)
ttk.Radiobutton(check_frame, text="Radio option").pack(side="left", padx=10)

# Run the application
if __name__ == "__main__":
    root.mainloop()
