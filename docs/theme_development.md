# Theme Development Guide

This guide explains how to create custom themes for tkthemes.

## Quick Start

```python
from tkthemes import register_custom_theme, apply_theme
from tkinter import ttk

def my_theme(style: ttk.Style, root) -> str:
    bg = "#1a1a2e"
    style.configure('TFrame', background=bg)
    style.configure('TLabel', background=bg, foreground='#ffffff')
    root.configure(bg=bg)
    return bg

register_custom_theme("my_theme", {
    "name": "My Theme",
    "apply_fn": my_theme
})
```

## Theme Structure

A theme consists of:

1. **Apply Function**: A callable that configures ttk styles and the root window
2. **Metadata**: Name, icon, and description

### Apply Function Requirements

```python
def apply_fn(style: ttk.Style, root: tk.Tk) -> str:
    """
    Args:
        style: ttk.Style object for configuring widget styles
        root: The root Tk window
        
    Returns:
        Background color string (e.g., "#2b2b2b")
    """
```

## Complete Theme Example

```python
from tkinter import ttk
from typing import Any

def apply_sunset_theme(style: ttk.Style, root: Any) -> str:
    """Sunset Theme - Warm orange and purple tones."""
    
    # Define color palette
    bg_color = "#1a0533"
    
    orange = "#ff6b35"
    purple = "#7b2cbf"
    pink = "#e0479e"
    gold = "#ffd166"
    white = "#ffffff"
    dark = "#0d0221"
    
    # Configure base widgets
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=gold,
                    font=('Segoe UI', 10))
    
    # Header style (optional custom style)
    style.configure('Header.TLabel', background=bg_color, foreground=orange,
                    font=('Segoe UI', 12, 'bold'))
    
    # Buttons
    style.configure('TButton', background=purple, foreground=white,
                    font=('Segoe UI', 9))
    style.map('TButton',
              background=[('active', pink), ('pressed', orange)],
              foreground=[('active', white)])
    
    # Control buttons (optional larger style)
    style.configure('Control.TButton', background=orange, foreground=dark,
                    font=('Segoe UI', 14, 'bold'), padding=10)
    style.map('Control.TButton',
              background=[('active', gold), ('pressed', pink)])
    
    # Menu buttons
    style.configure('TMenubutton', background=purple, foreground=gold)
    
    # Checkbuttons and Radiobuttons
    style.configure('TCheckbutton', background=bg_color, foreground=pink)
    style.configure('TRadiobutton', background=bg_color, foreground=orange)
    
    # Entry fields
    style.configure('TEntry', fieldbackground=dark, foreground=gold,
                    insertcolor=gold)
    
    # Notebook (tabs)
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background=purple, foreground=gold,
                    font=('Segoe UI', 10), padding=[15, 5])
    style.map('TNotebook.Tab',
              background=[('selected', pink)],
              foreground=[('selected', white)])
    
    # Treeview (lists/tables)
    style.configure('Treeview', background=dark, foreground=gold,
                    fieldbackground=dark, font=('Segoe UI', 9),
                    rowheight=24)
    style.map('Treeview',
              background=[('selected', purple)],
              foreground=[('selected', white)])
    style.configure('Treeview.Heading', background=purple, foreground=orange,
                    font=('Segoe UI', 10, 'bold'))
    
    # Scales (sliders)
    style.configure('TScale', background=bg_color, troughcolor=purple)
    
    # Scrollbars
    style.configure('TScrollbar', background=purple, troughcolor=dark,
                    arrowcolor=gold)
    
    # Configure root window
    root.configure(bg=bg_color)
    
    return bg_color


# Register the theme
from tkthemes import register_custom_theme

register_custom_theme("sunset", {
    "name": "🌅 Sunset",
    "icon": "🌅",
    "description": "Warm orange and purple sunset tones",
    "apply_fn": apply_sunset_theme
})
```

## Widget Style Reference

### Standard TTK Widget Styles

| Style Name | Widget | Key Options |
|------------|--------|-------------|
| `TFrame` | Frame | `background` |
| `TLabel` | Label | `background`, `foreground`, `font` |
| `TButton` | Button | `background`, `foreground`, `font`, `padding` |
| `TMenubutton` | Menubutton | `background`, `foreground` |
| `TCheckbutton` | Checkbutton | `background`, `foreground` |
| `TRadiobutton` | Radiobutton | `background`, `foreground` |
| `TEntry` | Entry | `fieldbackground`, `foreground`, `insertcolor` |
| `TNotebook` | Notebook | `background` |
| `TNotebook.Tab` | Tab | `background`, `foreground`, `font`, `padding` |
| `Treeview` | Treeview | `background`, `foreground`, `fieldbackground`, `font`, `rowheight` |
| `Treeview.Heading` | Header | `background`, `foreground`, `font` |
| `TScale` | Scale | `background`, `troughcolor` |
| `TScrollbar` | Scrollbar | `background`, `troughcolor`, `arrowcolor` |

### Custom Styles

You can create custom style variants:

```python
# Header label with different styling
style.configure('Header.TLabel', 
                background=bg_color, 
                foreground='#ff0000',
                font=('Arial', 14, 'bold'))

# Control buttons (larger, for media controls etc.)
style.configure('Control.TButton',
                background='#00ff00',
                foreground='#000000',
                font=('Arial', 12, 'bold'),
                padding=10)
```

### State Mapping

Use `style.map()` to define colors for different states:

```python
style.map('TButton',
          background=[
              ('active', '#aaaaaa'),    # Mouse hover
              ('pressed', '#888888'),   # Being clicked
              ('disabled', '#cccccc')   # Disabled state
          ],
          foreground=[
              ('active', '#000000'),
              ('disabled', '#666666')
          ])
```

## Color Palette Tips

### Accessibility
- Ensure sufficient contrast between text and background
- Test with colorblind simulation tools
- Consider providing high-contrast variants

### Consistency
- Define a base color palette at the top of your function
- Use named variables for colors to make adjustments easy
- Keep related colors together (e.g., all button colors)

### Common Patterns

**Dark Theme Base:**
```python
bg_color = "#2b2b2b"      # Main background
fg_color = "#ffffff"       # Main text
accent = "#0078d4"         # Highlights/selections
secondary = "#404040"      # Secondary backgrounds
```

**Light Theme Base:**
```python
bg_color = "#f5f5f5"      # Main background
fg_color = "#000000"       # Main text
accent = "#0078d4"         # Highlights/selections
secondary = "#e0e0e0"      # Secondary backgrounds
```

## Testing Your Theme

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme, register_custom_theme

# Register your theme
register_custom_theme("test", {...})

# Create test window
root = tk.Tk()
style = ttk.Style()

# Apply theme
apply_theme("test", style, root)

# Add test widgets
ttk.Label(root, text="Test Label").pack()
ttk.Button(root, text="Test Button").pack()
ttk.Entry(root).pack()
# ... add more widgets to test

root.mainloop()
```

## Sharing Your Theme

To contribute a theme to the built-in collection:

1. Create a new file in `tkthemes/themes/`
2. Follow the structure of existing theme files
3. Add the theme to `tkthemes/themes/__init__.py`
4. Submit a pull request
