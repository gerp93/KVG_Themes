"""
Light Theme
Default clean look
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the light theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#f5f5f5"
    fg_color = "#000000"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=fg_color)
    style.configure('TButton', background='#e0e0e0', foreground=fg_color)
    style.map('TButton',
             background=[('active', '#d0d0d0'), ('pressed', '#c0c0c0')],
             foreground=[('active', fg_color)])
    style.configure('TMenubutton', background='#e0e0e0', foreground=fg_color)
    style.configure('TCheckbutton', background=bg_color, foreground=fg_color)
    style.configure('TRadiobutton', background=bg_color, foreground=fg_color)
    style.configure('TEntry', fieldbackground='white', foreground=fg_color)
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background='#e0e0e0', foreground=fg_color)
    style.configure('Treeview', background='white', foreground=fg_color,
                  fieldbackground='white')
    style.map('Treeview', background=[('selected', '#0078d4')])
    style.configure('Treeview.Heading', background='#e0e0e0', foreground=fg_color)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "light",
    "name": "☀️ Light Theme",
    "icon": "☀️",
    "description": "Default clean look"
}
