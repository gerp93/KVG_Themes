"""
Retrowave Theme
80s synthwave sunset vibes
"""

from __future__ import annotations

from typing import Any


def apply(style: Any, root: Any) -> str:
    """
    Apply the retrowave theme.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color
    """
    bg_color = "#1a0a2e"
    
    sunset_pink = "#ff6b9d"
    sunset_orange = "#ff9a56"
    sunset_yellow = "#ffd93d"
    synth_purple = "#c77dff"
    hot_magenta = "#e040fb"
    chrome = "#e0e0e0"
    
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground=sunset_pink,
                  font=('Arial Black', 10))
    style.configure('Header.TLabel', background=bg_color, foreground=sunset_orange,
                  font=('Arial Black', 12))
    
    style.configure('TButton', background='#2d1b4e', foreground=sunset_yellow,
                  font=('Arial', 9, 'bold'))
    style.map('TButton', 
             background=[('active', '#4a2c7a'), ('pressed', '#6b3fa0')],
             foreground=[('active', chrome)])
    
    style.configure('Control.TButton', background='#3d1f5c', foreground=sunset_orange,
                  font=('Arial Black', 14), padding=10)
    style.map('Control.TButton',
             background=[('active', '#5c2d8a'), ('pressed', '#7a3db8')],
             foreground=[('active', sunset_yellow)])
    
    style.configure('TMenubutton', background='#2d1b4e', foreground=hot_magenta)
    style.configure('TCheckbutton', background=bg_color, foreground=synth_purple)
    style.configure('TRadiobutton', background=bg_color, foreground=sunset_pink)
    style.configure('TEntry', fieldbackground='#2d1b4e', foreground=chrome,
                  insertcolor=sunset_pink)
    
    style.configure('TNotebook', background=bg_color)
    style.configure('TNotebook.Tab', background='#3d1f5c', foreground=sunset_pink,
                  font=('Arial', 10, 'bold'), padding=[15, 5])
    style.map('TNotebook.Tab', 
             background=[('selected', '#5c2d8a')],
             foreground=[('selected', sunset_yellow)])
    
    style.configure('Treeview', background='#1f0f3d', foreground=chrome,
                  fieldbackground='#1f0f3d', font=('Arial', 9),
                  rowheight=25)
    style.map('Treeview', 
             background=[('selected', '#5c2d8a')],
             foreground=[('selected', sunset_yellow)])
    style.configure('Treeview.Heading', background='#3d1f5c', foreground=sunset_orange,
                  font=('Arial Black', 10))
    
    style.configure('TScale', background=bg_color, troughcolor='#3d1f5c')
    style.configure('TScrollbar', background='#3d1f5c', troughcolor=bg_color,
                  arrowcolor=sunset_pink)
    
    root.configure(bg=bg_color)
    return bg_color


# Theme metadata
THEME_INFO = {
    "id": "retrowave",
    "name": "🌅 Retrowave",
    "icon": "🌅",
    "description": "80s synthwave sunset vibes"
}
