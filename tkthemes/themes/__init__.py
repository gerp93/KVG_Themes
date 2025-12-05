"""
Built-in Themes
Automatically registers all built-in themes
"""

from ..registry import register_theme

# Import all theme modules
from . import light
from . import dark
from . import neon
from . import retrowave
from . import hacker
from . import lava
from . import electric_lime
from . import bubblegum
from . import commander_keen

# List of all theme modules
_THEME_MODULES = [
    light,
    dark,
    neon,
    retrowave,
    hacker,
    lava,
    electric_lime,
    bubblegum,
    commander_keen,
]


def _register_builtin_themes():
    """Register all built-in themes."""
    for module in _THEME_MODULES:
        info = module.THEME_INFO
        register_theme(
            theme_id=info["id"],
            name=info["name"],
            apply_fn=module.apply,
            icon=info.get("icon", ""),
            description=info.get("description", "")
        )


# Auto-register built-in themes on import
_register_builtin_themes()

# Export theme modules for direct access if needed
__all__ = [
    "light",
    "dark",
    "neon",
    "retrowave",
    "hacker",
    "lava",
    "electric_lime",
    "bubblegum",
    "commander_keen",
]
