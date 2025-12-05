"""
Lava Theme
Fiery red hot theme
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the lava theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#cc0000"
    
    molten_orange = "#ff6600"
    fire_yellow = "#ffcc00"
    white_hot = "#ffffff"
    dark_ember = "#330000"
    charcoal = "#1a0000"
    bright_flame = "#ff3300"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=white_hot,
                  font=('Impact', 10))
    style.configure('Header.TLabel', background=bg_color, foreground=fire_yellow,
                  font=('Impact', 12))
    
    style.configure('TButton', background=dark_ember, foreground=fire_yellow,
                  font=('Arial Black', 9))
    style.map('TButton', 
             background=[('active', '#4d0000'), ('pressed', '#660000')],
             foreground=[('active', white_hot)])
    
    style.configure('Control.TButton', background=charcoal, foreground=molten_orange,
                  font=('Impact', 14), padding=10)
    style.map('Control.TButton',
             background=[('active', dark_ember), ('pressed', '#4d0000')],
             foreground=[('active', fire_yellow)])
    
    style.configure('TMenubutton', background=dark_ember, foreground=bright_flame)
    style.configure('TCheckbutton', background=bg_color, foreground=white_hot)
    style.configure('TRadiobutton', background=bg_color, foreground=fire_yellow)
    style.configure('TEntry', fieldbackground=charcoal, foreground=fire_yellow,
                  insertcolor=fire_yellow)
    
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background=dark_ember, foreground=molten_orange,
                  font=('Impact', 10), padding=[15, 5])
    style.map('TNotebook.Tab', 
             background=[('selected', '#660000')],
             foreground=[('selected', fire_yellow)])
    
    style.configure('Treeview', background=charcoal, foreground=fire_yellow,
                  fieldbackground=charcoal, font=('Arial', 9),
                  rowheight=24)
    style.map('Treeview', 
             background=[('selected', '#800000')],
             foreground=[('selected', white_hot)])
    style.configure('Treeview.Heading', background=dark_ember, foreground=molten_orange,
                  font=('Impact', 10))
    
    style.configure('TScale', background=bg_color, troughcolor=dark_ember)
    style.configure('TScrollbar', background=dark_ember, troughcolor=bg_color,
                  arrowcolor=fire_yellow)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "lava",
    "name": "🌋 LAVA",
    "icon": "🌋",
    "description": "Fiery red hot theme"
}
