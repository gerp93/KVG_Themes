"""
Theme Registry
Manages theme registration and lookup
"""

from typing import Dict, Any, List, Tuple, Callable, Optional

# Type alias for theme apply function
ThemeApplyFn = Callable[['ttk.Style', Any], str]

# Global theme registry
_THEMES: Dict[str, Dict[str, Any]] = {}


def register_theme(
    theme_id: str,
    name: str,
    apply_fn: ThemeApplyFn,
    icon: str = "",
    description: str = ""
) -> None:
    """
    Register a theme in the registry.
    
    Args:
        theme_id: Unique identifier for the theme (e.g., "dark", "neon")
        name: Display name for the theme (e.g., "Dark Theme")
        apply_fn: Function that applies the theme, signature: (style, root) -> bg_color
        icon: Optional emoji icon for the theme
        description: Optional description of the theme
    """
    _THEMES[theme_id] = {
        "name": name,
        "icon": icon,
        "description": description,
        "apply_fn": apply_fn
    }


def unregister_theme(theme_id: str) -> bool:
    """
    Remove a theme from the registry.
    
    Args:
        theme_id: Unique identifier for the theme to remove
        
    Returns:
        True if theme was removed, False if theme was not found
    """
    if theme_id in _THEMES:
        del _THEMES[theme_id]
        return True
    return False


def get_theme(theme_id: str) -> Optional[Dict[str, Any]]:
    """
    Get theme info by ID.
    
    Args:
        theme_id: Unique identifier for the theme
        
    Returns:
        Theme info dict or None if not found
    """
    return _THEMES.get(theme_id)


def get_theme_list() -> List[Tuple[str, str]]:
    """
    Get list of (theme_id, display_name) tuples.
    
    Returns:
        List of tuples containing theme IDs and their display names
    """
    return [(tid, info["name"]) for tid, info in _THEMES.items()]


def get_all_themes() -> Dict[str, Dict[str, Any]]:
    """
    Get a copy of all registered themes.
    
    Returns:
        Dictionary of all themes
    """
    return dict(_THEMES)


def theme_exists(theme_id: str) -> bool:
    """
    Check if a theme exists in the registry.
    
    Args:
        theme_id: Unique identifier for the theme
        
    Returns:
        True if theme exists, False otherwise
    """
    return theme_id in _THEMES
