"""
Commander Keen Theme
Classic DOS EGA/VGA palette!
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the Commander Keen theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#0000aa"
    
    ega_black = "#000000"
    ega_magenta = "#aa00aa"
    ega_dark_gray = "#555555"
    ega_bright_blue = "#5555ff"
    ega_bright_green = "#55ff55"
    ega_bright_cyan = "#55ffff"
    ega_yellow = "#ffff55"
    ega_white = "#ffffff"
    ega_brown = "#aa5500"
    ega_cyan = "#00aaaa"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=ega_yellow,
                  font=('Fixedsys', 10, 'bold'))
    style.configure('Header.TLabel', background=bg_color, foreground=ega_bright_green,
                  font=('Fixedsys', 12, 'bold'))
    
    style.configure('TButton', background=ega_bright_blue, foreground=ega_yellow,
                  font=('Fixedsys', 9, 'bold'))
    style.map('TButton', 
             background=[('active', ega_bright_cyan), ('pressed', ega_cyan)],
             foreground=[('active', ega_black)])
    
    style.configure('Control.TButton', background=ega_bright_green, foreground=ega_black,
                  font=('Fixedsys', 14, 'bold'), padding=10)
    style.map('Control.TButton',
             background=[('active', ega_yellow), ('pressed', ega_brown)],
             foreground=[('active', ega_black)])
    
    style.configure('TMenubutton', background=ega_bright_blue, foreground=ega_yellow)
    style.configure('TCheckbutton', background=bg_color, foreground=ega_bright_cyan)
    style.configure('TRadiobutton', background=bg_color, foreground=ega_bright_green)
    style.configure('TEntry', fieldbackground=ega_black, foreground=ega_bright_green,
                  insertcolor=ega_bright_green)
    
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background=ega_dark_gray, foreground=ega_yellow,
                  font=('Fixedsys', 10, 'bold'), padding=[15, 5])
    style.map('TNotebook.Tab', 
             background=[('selected', ega_bright_blue)],
             foreground=[('selected', ega_white)])
    
    style.configure('Treeview', background=ega_black, foreground=ega_bright_cyan,
                  fieldbackground=ega_black, font=('Fixedsys', 9),
                  rowheight=22)
    style.map('Treeview', 
             background=[('selected', ega_bright_blue)],
             foreground=[('selected', ega_yellow)])
    style.configure('Treeview.Heading', background=ega_magenta, foreground=ega_yellow,
                  font=('Fixedsys', 10, 'bold'))
    
    style.configure('TScale', background=bg_color, troughcolor=ega_dark_gray)
    style.configure('TScrollbar', background=ega_dark_gray, troughcolor=ega_black,
                  arrowcolor=ega_bright_green)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "commander_keen",
    "name": "🚀 Commander Keen",
    "icon": "🚀",
    "description": "Classic DOS EGA/VGA palette!"
}
