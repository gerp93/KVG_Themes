"""
Dark Theme
Easy on the eyes
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the dark theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#2b2b2b"
    fg_color = "#ffffff"
    btn_bg = "#505050"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=fg_color)
    style.configure('TButton', background=btn_bg, foreground=fg_color)
    style.map('TButton', 
             background=[('active', '#606060'), ('pressed', '#707070')],
             foreground=[('active', fg_color)])
    style.configure('TMenubutton', background=btn_bg, foreground=fg_color)
    style.configure('TCheckbutton', background=bg_color, foreground=fg_color)
    style.configure('TRadiobutton', background=bg_color, foreground=fg_color)
    style.configure('TEntry', fieldbackground='#404040', foreground=fg_color)
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background='#404040', foreground=fg_color)
    style.map('TNotebook.Tab', background=[('selected', '#505050')])
    style.configure('Treeview', background='#353535', foreground=fg_color, 
                  fieldbackground='#353535')
    style.map('Treeview', background=[('selected', '#505050')])
    style.configure('Treeview.Heading', background='#404040', foreground=fg_color)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "dark",
    "name": "Dark Theme",
    "icon": "",
    "description": "Easy on the eyes"
}
