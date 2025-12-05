"""
tkthemes - A standalone theming library for tkinter applications

This package provides a collection of pre-built themes and an extensible
framework for creating custom themes for tkinter/ttk applications.

Usage:
    from tkthemes import apply_theme, get_theme_list, THEMES
    
    import tkinter as tk
    from tkinter import ttk
    
    root = tk.Tk()
    style = ttk.Style()
    
    # Apply a theme
    apply_theme("neon", style, root)
    
    # List available themes
    themes = get_theme_list()  # Returns: [("light", "Light Theme"), ...]
    
    # Register a custom theme
    from tkthemes import register_custom_theme
    
    def my_custom_apply(style, root):
        style.configure('TButton', background='#ff00ff')
        root.configure(bg='#1a1a1a')
        return '#1a1a1a'
    
    register_custom_theme("my_theme", {
        "name": "My Custom Theme",
        "apply_fn": my_custom_apply
    })
"""

__version__ = "1.0.0"
__author__ = "KVGroove"

# Import and register built-in themes first
from . import themes  # noqa: F401 - This registers all built-in themes

# Import core functionality for public API
from .core import (
    apply_theme,
    get_theme_list,
    register_custom_theme,
    AVAILABLE_THEMES,
)

from .registry import (
    register_theme,
    unregister_theme,
    get_theme,
    get_all_themes,
    theme_exists,
)

# For backwards compatibility with original KVGroove usage
THEMES = get_all_themes()

__all__ = [
    # Core functions
    "apply_theme",
    "get_theme_list",
    "register_custom_theme",
    "AVAILABLE_THEMES",
    # Registry functions
    "register_theme",
    "unregister_theme",
    "get_theme",
    "get_all_themes",
    "theme_exists",
    # Compatibility
    "THEMES",
    # Metadata
    "__version__",
    "__author__",
]
