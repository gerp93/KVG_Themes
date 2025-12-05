"""
Custom Theme Example
Demonstrates how to create and register custom themes
"""

import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme, register_custom_theme, get_theme_list


def apply_ocean_theme(style: ttk.Style, root) -> str:
    """
    Custom ocean theme - Deep blue sea vibes
    """
    bg_color = "#0a2342"
    
    # Ocean colors
    deep_blue = "#0a2342"
    wave_blue = "#2e5077"
    foam_white = "#e0f7fa"
    sand = "#d4a574"
    coral = "#ff6b6b"
    sea_green = "#4dd0e1"
    
    style.configure('TFrame', background=deep_blue)
    style.configure('TLabel', background=deep_blue, foreground=foam_white,
                  font=('Helvetica', 10))
    style.configure('Header.TLabel', background=deep_blue, foreground=sea_green,
                  font=('Helvetica', 12, 'bold'))
    
    style.configure('TButton', background=wave_blue, foreground=foam_white,
                  font=('Helvetica', 9))
    style.map('TButton',
             background=[('active', coral), ('pressed', sand)],
             foreground=[('active', deep_blue)])
    
    style.configure('TEntry', fieldbackground=wave_blue, foreground=foam_white)
    style.configure('TCheckbutton', background=deep_blue, foreground=sea_green)
    style.configure('TRadiobutton', background=deep_blue, foreground=coral)
    
    root.configure(bg=bg_color)
    return bg_color


# Register the custom theme
register_custom_theme("ocean", {
    "name": "🌊 Ocean Theme",
    "icon": "🌊",
    "description": "Deep blue sea vibes",
    "apply_fn": apply_ocean_theme
})

# Create the main window
root = tk.Tk()
root.title("Custom Theme Example")
root.geometry("500x400")

style = ttk.Style()

# Create theme selector
selector_frame = ttk.Frame(root, padding="10")
selector_frame.pack(fill="x")

ttk.Label(selector_frame, text="Select Theme:").pack(side="left")

theme_var = tk.StringVar(value="ocean")
themes = get_theme_list()
theme_combo = ttk.Combobox(
    selector_frame,
    textvariable=theme_var,
    values=[name for _, name in themes],
    state="readonly",
    width=25
)
theme_combo.pack(side="left", padx=10)

# Theme ID mapping
theme_ids = {name: tid for tid, name in themes}


def on_theme_change(event):
    selected_name = theme_var.get()
    for tid, name in themes:
        if name == selected_name:
            apply_theme(tid, style, root)
            break


theme_combo.bind("<<ComboboxSelected>>", on_theme_change)

# Demo widgets
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Custom Theme Demo", style="Header.TLabel").pack(pady=10)
ttk.Label(main_frame, text="Try selecting different themes above!").pack(pady=5)

ttk.Button(main_frame, text="Sample Button").pack(pady=5)
ttk.Entry(main_frame).pack(pady=5, fill="x")
ttk.Checkbutton(main_frame, text="Checkbox").pack(pady=5)
ttk.Radiobutton(main_frame, text="Radio button").pack(pady=5)

# Apply initial theme
apply_theme("ocean", style, root)

# Set the combobox to show the custom theme
for i, (tid, name) in enumerate(themes):
    if tid == "ocean":
        theme_combo.current(i)
        break

if __name__ == "__main__":
    root.mainloop()
