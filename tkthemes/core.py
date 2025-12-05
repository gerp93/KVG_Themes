"""
Core Theme Engine
Main functions for applying themes
"""

from __future__ import annotations

from typing import Any, List, Tuple, Dict, Callable, Optional

from .registry import (
    register_theme,
    get_theme,
    get_theme_list as _get_theme_list,
    get_all_themes,
    theme_exists
)


def apply_theme(theme_id: str, style: Any, root: Any) -> str:
    """
    Apply the specified theme to the application.
    
    Args:
        theme_id: The ID of the theme to apply (e.g., "dark", "neon")
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color for the root window
        
    Raises:
        ValueError: If the theme_id is not found in the registry
    """
    theme = get_theme(theme_id)
    
    if theme is None:
        # Fall back to light theme if available, otherwise raise error
        if theme_exists("light"):
            theme = get_theme("light")
        else:
            raise ValueError(f"Theme '{theme_id}' not found and no default theme available")
    
    apply_fn = theme["apply_fn"]
    return apply_fn(style, root)


def get_theme_list() -> List[Tuple[str, str]]:
    """
    Get list of available themes.
    
    Returns:
        List of (theme_id, display_name) tuples
    """
    return _get_theme_list()


def register_custom_theme(
    theme_id: str,
    config: Dict[str, Any]
) -> None:
    """
    Register a custom theme.
    
    Args:
        theme_id: Unique identifier for the theme
        config: Dictionary containing:
            - name: Display name (required)
            - apply_fn: Function to apply theme (required)
            - icon: Optional emoji icon
            - description: Optional description
            
    Raises:
        ValueError: If required fields are missing
    """
    if "name" not in config:
        raise ValueError("Theme config must include 'name'")
    if "apply_fn" not in config:
        raise ValueError("Theme config must include 'apply_fn'")
    
    register_theme(
        theme_id=theme_id,
        name=config["name"],
        apply_fn=config["apply_fn"],
        icon=config.get("icon", ""),
        description=config.get("description", "")
    )


# Alias for backwards compatibility
AVAILABLE_THEMES = get_all_themes
