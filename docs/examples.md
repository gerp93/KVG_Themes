# Examples

## Basic Usage

Apply a built-in theme to your application:

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme

root = tk.Tk()
root.title("My App")
root.geometry("400x300")

style = ttk.Style()
apply_theme("neon", style, root)

ttk.Label(root, text="Hello World!").pack(pady=20)
ttk.Button(root, text="Click Me").pack()

root.mainloop()
```

## Theme Selector Dropdown

Create a dropdown to switch themes at runtime:

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme, get_theme_list

root = tk.Tk()
root.geometry("400x300")
style = ttk.Style()

# Get available themes
themes = get_theme_list()
theme_var = tk.StringVar(value=themes[0][1])

# Create dropdown
ttk.Label(root, text="Theme:").pack(pady=5)
combo = ttk.Combobox(
    root,
    textvariable=theme_var,
    values=[name for _, name in themes],
    state="readonly"
)
combo.pack(pady=5)

def change_theme(event):
    for tid, name in themes:
        if name == theme_var.get():
            apply_theme(tid, style, root)
            break

combo.bind("<<ComboboxSelected>>", change_theme)

# Demo widgets
ttk.Label(root, text="Sample Label").pack(pady=10)
ttk.Button(root, text="Sample Button").pack()

apply_theme("light", style, root)
root.mainloop()
```

## Custom Theme

Create and register your own theme:

```python
from tkinter import ttk
from tkthemes import register_custom_theme, apply_theme

def ocean_theme(style, root):
    bg = "#0a3d62"
    fg = "#dfe6e9"
    accent = "#00cec9"
    
    style.configure('TFrame', background=bg)
    style.configure('TLabel', background=bg, foreground=fg)
    style.configure('TButton', background=accent, foreground=bg)
    style.map('TButton', background=[('active', '#55efc4')])
    style.configure('TEntry', fieldbackground='#2d3436', foreground=fg)
    
    root.configure(bg=bg)
    return bg

register_custom_theme("ocean", {
    "name": "🌊 Ocean",
    "icon": "🌊",
    "description": "Deep sea blue theme",
    "apply_fn": ocean_theme
})

# Use it
import tkinter as tk
root = tk.Tk()
style = ttk.Style()
apply_theme("ocean", style, root)
# ...
```

## Form Application

A complete form with various widgets:

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme

root = tk.Tk()
root.title("User Registration")
root.geometry("500x400")

style = ttk.Style()
apply_theme("retrowave", style, root)

# Main frame
main = ttk.Frame(root, padding="20")
main.pack(fill="both", expand=True)

# Title
ttk.Label(main, text="User Registration", style="Header.TLabel").pack(pady=(0, 20))

# Form fields
fields = ttk.Frame(main)
fields.pack(fill="x")

ttk.Label(fields, text="Name:").grid(row=0, column=0, sticky="e", pady=5)
ttk.Entry(fields, width=30).grid(row=0, column=1, pady=5, padx=10)

ttk.Label(fields, text="Email:").grid(row=1, column=0, sticky="e", pady=5)
ttk.Entry(fields, width=30).grid(row=1, column=1, pady=5, padx=10)

ttk.Label(fields, text="Password:").grid(row=2, column=0, sticky="e", pady=5)
ttk.Entry(fields, width=30, show="*").grid(row=2, column=1, pady=5, padx=10)

# Options
options = ttk.Frame(main)
options.pack(pady=20)

ttk.Checkbutton(options, text="Subscribe to newsletter").pack(anchor="w")
ttk.Checkbutton(options, text="Accept terms and conditions").pack(anchor="w")

# Buttons
buttons = ttk.Frame(main)
buttons.pack(pady=20)

ttk.Button(buttons, text="Register", style="Control.TButton").pack(side="left", padx=5)
ttk.Button(buttons, text="Cancel").pack(side="left", padx=5)

root.mainloop()
```

## Notebook with Tabs

Application with tabbed interface:

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme

root = tk.Tk()
root.title("Tabbed App")
root.geometry("600x400")

style = ttk.Style()
apply_theme("hacker", style, root)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Tab 1
tab1 = ttk.Frame(notebook, padding="20")
notebook.add(tab1, text="Home")
ttk.Label(tab1, text="Welcome to the home tab!").pack(pady=20)

# Tab 2
tab2 = ttk.Frame(notebook, padding="20")
notebook.add(tab2, text="Settings")
ttk.Label(tab2, text="Settings go here").pack(pady=10)
ttk.Checkbutton(tab2, text="Enable feature 1").pack(anchor="w")
ttk.Checkbutton(tab2, text="Enable feature 2").pack(anchor="w")

# Tab 3
tab3 = ttk.Frame(notebook, padding="20")
notebook.add(tab3, text="About")
ttk.Label(tab3, text="Version 1.0.0").pack(pady=10)
ttk.Label(tab3, text="Built with tkthemes").pack()

root.mainloop()
```

## Treeview (Data Table)

Display tabular data:

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme

root = tk.Tk()
root.title("Data Table")
root.geometry("600x400")

style = ttk.Style()
apply_theme("commander_keen", style, root)

frame = ttk.Frame(root, padding="10")
frame.pack(fill="both", expand=True)

# Treeview with columns
tree = ttk.Treeview(frame, columns=("name", "status", "score"), show="headings")
tree.heading("name", text="Player Name")
tree.heading("status", text="Status")
tree.heading("score", text="Score")

# Sample data
data = [
    ("Player 1", "Online", "2500"),
    ("Player 2", "Away", "1800"),
    ("Player 3", "Online", "3200"),
    ("Player 4", "Offline", "950"),
    ("Player 5", "Online", "4100"),
]

for row in data:
    tree.insert("", "end", values=row)

# Scrollbar
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
```

## Check Theme Existence

Handle missing themes gracefully:

```python
from tkthemes import apply_theme, theme_exists

def safe_apply_theme(theme_id, style, root):
    if theme_exists(theme_id):
        return apply_theme(theme_id, style, root)
    else:
        print(f"Theme '{theme_id}' not found, using light theme")
        return apply_theme("light", style, root)

# Usage
bg = safe_apply_theme("custom_theme", style, root)
```
