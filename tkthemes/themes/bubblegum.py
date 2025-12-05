"""
Bubblegum Theme
Hot pink explosion
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the bubblegum theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#ff69b4"
    
    white = "#ffffff"
    deep_magenta = "#cc0066"
    baby_blue = "#87ceeb"
    candy_purple = "#9932cc"
    sunshine = "#ffff00"
    cotton_candy = "#ffb6c1"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=white,
                  font=('Comic Sans MS', 10, 'bold'))
    style.configure('Header.TLabel', background=bg_color, foreground=sunshine,
                  font=('Comic Sans MS', 12, 'bold'))
    
    style.configure('TButton', background=candy_purple, foreground=white,
                  font=('Comic Sans MS', 9, 'bold'))
    style.map('TButton', 
             background=[('active', '#aa28aa'), ('pressed', '#bb33bb')],
             foreground=[('active', sunshine)])
    
    style.configure('Control.TButton', background=baby_blue, foreground=deep_magenta,
                  font=('Comic Sans MS', 14, 'bold'), padding=10)
    style.map('Control.TButton',
             background=[('active', '#a0d8ef'), ('pressed', '#b8e2f2')],
             foreground=[('active', candy_purple)])
    
    style.configure('TMenubutton', background=candy_purple, foreground=white)
    style.configure('TCheckbutton', background=bg_color, foreground=white)
    style.configure('TRadiobutton', background=bg_color, foreground=sunshine)
    style.configure('TEntry', fieldbackground=cotton_candy, foreground=deep_magenta,
                  insertcolor=deep_magenta)
    
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background=deep_magenta, foreground=white,
                  font=('Comic Sans MS', 10, 'bold'), padding=[15, 5])
    style.map('TNotebook.Tab', 
             background=[('selected', candy_purple)],
             foreground=[('selected', sunshine)])
    
    style.configure('Treeview', background=cotton_candy, foreground=deep_magenta,
                  fieldbackground=cotton_candy, font=('Comic Sans MS', 9),
                  rowheight=24)
    style.map('Treeview', 
             background=[('selected', candy_purple)],
             foreground=[('selected', white)])
    style.configure('Treeview.Heading', background=deep_magenta, foreground=white,
                  font=('Comic Sans MS', 10, 'bold'))
    
    style.configure('TScale', background=bg_color, troughcolor=deep_magenta)
    style.configure('TScrollbar', background=deep_magenta, troughcolor=bg_color,
                  arrowcolor=white)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "bubblegum",
    "name": "🍬 Bubblegum",
    "icon": "🍬",
    "description": "Hot pink explosion"
}
