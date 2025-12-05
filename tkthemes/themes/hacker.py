"""
Hacker Theme
Matrix-style green on black
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the hacker theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#0d0d0d"
    
    matrix_green = "#00ff00"
    lime = "#32cd32"
    phosphor = "#00ff41"
    amber = "#ffbf00"
    terminal_green = "#20c20e"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=matrix_green,
                  font=('Courier New', 10, 'bold'))
    style.configure('Header.TLabel', background=bg_color, foreground=phosphor,
                  font=('Courier New', 12, 'bold'))
    
    style.configure('TButton', background='#001a00', foreground=matrix_green,
                  font=('Courier New', 9, 'bold'))
    style.map('TButton', 
             background=[('active', '#003300'), ('pressed', '#004d00')],
             foreground=[('active', amber)])
    
    style.configure('Control.TButton', background='#001a00', foreground=phosphor,
                  font=('Courier New', 14, 'bold'), padding=10)
    style.map('Control.TButton',
             background=[('active', '#003300'), ('pressed', '#004d00')],
             foreground=[('active', amber)])
    
    style.configure('TMenubutton', background='#001a00', foreground=lime)
    style.configure('TCheckbutton', background=bg_color, foreground=terminal_green)
    style.configure('TRadiobutton', background=bg_color, foreground=matrix_green)
    style.configure('TEntry', fieldbackground='#001100', foreground=matrix_green,
                  insertcolor=matrix_green)
    
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background='#001a00', foreground=matrix_green,
                  font=('Courier New', 10, 'bold'), padding=[15, 5])
    style.map('TNotebook.Tab', 
             background=[('selected', '#003300')],
             foreground=[('selected', amber)])
    
    style.configure('Treeview', background='#0a0a0a', foreground=terminal_green,
                  fieldbackground='#0a0a0a', font=('Courier New', 9),
                  rowheight=22)
    style.map('Treeview', 
             background=[('selected', '#003300')],
             foreground=[('selected', amber)])
    style.configure('Treeview.Heading', background='#001a00', foreground=phosphor,
                  font=('Courier New', 10, 'bold'))
    
    style.configure('TScale', background=bg_color, troughcolor='#001a00')
    style.configure('TScrollbar', background='#001a00', troughcolor=bg_color,
                  arrowcolor=matrix_green)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "hacker",
    "name": "💻 Hacker",
    "icon": "💻",
    "description": "Matrix-style green on black"
}
