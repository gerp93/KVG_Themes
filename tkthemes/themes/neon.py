"""
Neon Theme
Visually wild but readable
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the neon theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#0a0a0a"
    
    neon_pink = "#ff00ff"
    neon_cyan = "#00ffff"
    neon_green = "#39ff14"
    neon_yellow = "#ffff00"
    neon_orange = "#ff6600"
    hot_pink = "#ff1493"
    electric_blue = "#7df9ff"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=neon_cyan,
                  font=('Consolas', 10, 'bold'))
    style.configure('Header.TLabel', background=bg_color, foreground=neon_pink,
                  font=('Consolas', 12, 'bold'))
    
    style.configure('TButton', background='#330033', foreground=neon_green,
                  font=('Consolas', 9, 'bold'))
    style.map('TButton', 
             background=[('active', '#660066'), ('pressed', '#990099')],
             foreground=[('active', neon_yellow)])
    
    style.configure('Control.TButton', background='#003333', foreground=neon_cyan,
                  font=('Consolas', 14, 'bold'), padding=10)
    style.map('Control.TButton',
             background=[('active', '#006666'), ('pressed', '#009999')],
             foreground=[('active', neon_yellow)])
    
    style.configure('TMenubutton', background='#330033', foreground=neon_pink)
    style.configure('TCheckbutton', background=bg_color, foreground=neon_orange)
    style.configure('TRadiobutton', background=bg_color, foreground=hot_pink)
    style.configure('TEntry', fieldbackground='#1a1a2e', foreground=neon_green,
                  insertcolor=neon_green)
    
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background='#1a0033', foreground=neon_pink,
                  font=('Consolas', 10, 'bold'), padding=[15, 5])
    style.map('TNotebook.Tab', 
             background=[('selected', '#330066')],
             foreground=[('selected', neon_cyan)])
    
    style.configure('Treeview', background='#0d0d1a', foreground=electric_blue,
                  fieldbackground='#0d0d1a', font=('Consolas', 9),
                  rowheight=25)
    style.map('Treeview', 
             background=[('selected', '#660066')],
             foreground=[('selected', neon_yellow)])
    style.configure('Treeview.Heading', background='#1a0033', foreground=neon_pink,
                  font=('Consolas', 10, 'bold'))
    
    style.configure('TScale', background=bg_color, troughcolor='#330033')
    style.configure('TScrollbar', background='#330033', troughcolor=bg_color,
                  arrowcolor=neon_pink)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "neon",
    "name": "🌈 NEON Theme",
    "icon": "🌈",
    "description": "Visually wild but readable"
}
