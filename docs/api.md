# API Reference

## Core Functions

### `apply_theme(theme_id, style, root) -> str`

Apply a theme to the application.

**Parameters:**
- `theme_id` (str): The unique identifier for the theme (e.g., "dark", "neon")
- `style` (ttk.Style): The ttk.Style object to configure
- `root`: The root Tk window

**Returns:**
- `str`: The background color for the root window (e.g., "#2b2b2b")

**Raises:**
- `ValueError`: If the theme_id is not found and no default theme is available

**Example:**
```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme

root = tk.Tk()
style = ttk.Style()
bg_color = apply_theme("neon", style, root)
print(f"Background color: {bg_color}")
```

---

### `get_theme_list() -> List[Tuple[str, str]]`

Get a list of all available themes.

**Returns:**
- `List[Tuple[str, str]]`: List of (theme_id, display_name) tuples

**Example:**
```python
from tkthemes import get_theme_list

themes = get_theme_list()
for theme_id, display_name in themes:
    print(f"{theme_id}: {display_name}")
```

---

### `register_custom_theme(theme_id, config)`

Register a custom theme.

**Parameters:**
- `theme_id` (str): Unique identifier for the theme
- `config` (dict): Theme configuration containing:
  - `name` (str, required): Display name for the theme
  - `apply_fn` (callable, required): Function to apply the theme
  - `icon` (str, optional): Emoji icon for the theme
  - `description` (str, optional): Description of the theme

**Raises:**
- `ValueError`: If required fields (`name` or `apply_fn`) are missing

**Example:**
```python
from tkthemes import register_custom_theme

def my_apply_fn(style, root):
    style.configure('TFrame', background='#1a1a2e')
    root.configure(bg='#1a1a2e')
    return '#1a1a2e'

register_custom_theme("midnight", {
    "name": "🌙 Midnight",
    "icon": "🌙",
    "description": "A dark midnight theme",
    "apply_fn": my_apply_fn
})
```

---

## Registry Functions

### `register_theme(theme_id, name, apply_fn, icon="", description="")`

Register a theme directly with all parameters.

**Parameters:**
- `theme_id` (str): Unique identifier for the theme
- `name` (str): Display name for the theme
- `apply_fn` (callable): Function that applies the theme
- `icon` (str, optional): Emoji icon for the theme
- `description` (str, optional): Description of the theme

**Example:**
```python
from tkthemes import register_theme

register_theme(
    theme_id="ocean",
    name="🌊 Ocean",
    apply_fn=ocean_apply,
    icon="🌊",
    description="Deep blue ocean vibes"
)
```

---

### `unregister_theme(theme_id) -> bool`

Remove a theme from the registry.

**Parameters:**
- `theme_id` (str): Unique identifier for the theme to remove

**Returns:**
- `bool`: True if theme was removed, False if not found

**Example:**
```python
from tkthemes import unregister_theme

success = unregister_theme("my_custom_theme")
```

---

### `get_theme(theme_id) -> Optional[Dict[str, Any]]`

Get theme information by ID.

**Parameters:**
- `theme_id` (str): Unique identifier for the theme

**Returns:**
- `Dict[str, Any]` or `None`: Theme info dictionary or None if not found

**Example:**
```python
from tkthemes import get_theme

theme_info = get_theme("neon")
if theme_info:
    print(f"Name: {theme_info['name']}")
    print(f"Icon: {theme_info['icon']}")
```

---

### `theme_exists(theme_id) -> bool`

Check if a theme exists in the registry.

**Parameters:**
- `theme_id` (str): Unique identifier for the theme

**Returns:**
- `bool`: True if theme exists, False otherwise

**Example:**
```python
from tkthemes import theme_exists

if theme_exists("dark"):
    apply_theme("dark", style, root)
```

---

### `get_all_themes() -> Dict[str, Dict[str, Any]]`

Get all registered themes.

**Returns:**
- `Dict[str, Dict[str, Any]]`: Dictionary mapping theme IDs to theme info

**Example:**
```python
from tkthemes import get_all_themes

all_themes = get_all_themes()
for theme_id, info in all_themes.items():
    print(f"{theme_id}: {info['name']}")
```

---

## Constants

### `THEMES`

Dictionary of all registered themes. Equivalent to calling `get_all_themes()`.

```python
from tkthemes import THEMES

print(THEMES.keys())  # dict_keys(['light', 'dark', 'neon', ...])
```

---

### `AVAILABLE_THEMES`

Alias for `get_all_themes` function.

```python
from tkthemes import AVAILABLE_THEMES

themes = AVAILABLE_THEMES()
```

---

## Theme Apply Function Signature

When creating a custom theme, your apply function must have the following signature:

```python
def my_apply_fn(style: ttk.Style, root: tk.Tk) -> str:
    """
    Apply the theme to the application.
    
    Args:
        style: The ttk.Style object to configure
        root: The root Tk window
        
    Returns:
        The background color string (e.g., "#2b2b2b")
    """
    bg_color = "#2b2b2b"
    
    # Configure ttk styles
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground='#ffffff')
    style.configure('TButton', background='#505050', foreground='#ffffff')
    # ... configure more widget styles
    
    # Configure root window
    root.configure(bg=bg_color)
    
    return bg_color
```

### Available Widget Styles to Configure

- `TFrame` - Frame widgets
- `TLabel` - Label widgets
- `TButton` - Button widgets
- `TMenubutton` - Menu button widgets
- `TCheckbutton` - Checkbox widgets
- `TRadiobutton` - Radio button widgets
- `TEntry` - Entry (text input) widgets
- `TNotebook` - Notebook (tab container) widgets
- `TNotebook.Tab` - Notebook tabs
- `Treeview` - Treeview widgets
- `Treeview.Heading` - Treeview column headings
- `TScale` - Scale (slider) widgets
- `TScrollbar` - Scrollbar widgets
- `Header.TLabel` - Custom header label style
- `Control.TButton` - Custom control button style
