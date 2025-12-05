"""
Electric Lime Theme
Blindingly bright green-yellow
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the electric lime theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#ccff00"
    
    hot_black = "#0a0a0a"
    deep_purple = "#4a0080"
    electric_blue = "#0066ff"
    magenta_pop = "#ff00aa"
    dark_lime = "#88aa00"
    ultra_violet = "#7700ff"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=hot_black,
                  font=('Trebuchet MS', 10, 'bold'))
    style.configure('Header.TLabel', background=bg_color, foreground=deep_purple,
                  font=('Trebuchet MS', 12, 'bold'))
    
    style.configure('TButton', background=deep_purple, foreground=bg_color,
                  font=('Trebuchet MS', 9, 'bold'))
    style.map('TButton', 
             background=[('active', ultra_violet), ('pressed', '#5c00a3')],
             foreground=[('active', '#ffffff')])
    
    style.configure('Control.TButton', background=electric_blue, foreground='#ffffff',
                  font=('Trebuchet MS', 14, 'bold'), padding=10)
    style.map('Control.TButton',
             background=[('active', '#0080ff'), ('pressed', '#0099ff')],
             foreground=[('active', bg_color)])
    
    style.configure('TMenubutton', background=deep_purple, foreground=bg_color)
    style.configure('TCheckbutton', background=bg_color, foreground=magenta_pop)
    style.configure('TRadiobutton', background=bg_color, foreground=deep_purple)
    style.configure('TEntry', fieldbackground='#ffffff', foreground=hot_black,
                  insertcolor=deep_purple)
    
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background=dark_lime, foreground=hot_black,
                  font=('Trebuchet MS', 10, 'bold'), padding=[15, 5])
    style.map('TNotebook.Tab', 
             background=[('selected', deep_purple)],
             foreground=[('selected', '#ffffff')])
    
    style.configure('Treeview', background='#eeffaa', foreground=hot_black,
                  fieldbackground='#eeffaa', font=('Trebuchet MS', 9),
                  rowheight=24)
    style.map('Treeview', 
             background=[('selected', deep_purple)],
             foreground=[('selected', '#ffffff')])
    style.configure('Treeview.Heading', background=dark_lime, foreground=hot_black,
                  font=('Trebuchet MS', 10, 'bold'))
    
    style.configure('TScale', background=bg_color, troughcolor=dark_lime)
    style.configure('TScrollbar', background=dark_lime, troughcolor=bg_color,
                  arrowcolor=hot_black)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "electric_lime",
    "name": "⚡ Electric Lime",
    "icon": "⚡",
    "description": "Blindingly bright green-yellow"
}
