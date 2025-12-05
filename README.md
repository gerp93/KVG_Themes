# tkthemes

A standalone theming library for tkinter applications. Drop-in themes for any tkinter/ttk application with zero dependencies beyond Python's standard library.

## Features

- **9 Pre-built Themes**: Light, Dark, Neon, Retrowave, Hacker, Lava, Electric Lime, Bubblegum, Commander Keen
- **Zero Dependencies**: Works on any system with Python 3.7+ and tkinter
- **Plug & Play**: Minimal setup required
- **Extensible**: Easy API for creating and registering custom themes
- **Type Hints**: Full type annotation support

## Installation

```bash
pip install tkthemes
```

Or install from source:

```bash
git clone https://github.com/gerp93/KVG_Themes.git
cd KVG_Themes
pip install -e .
```

## Quick Start

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme, get_theme_list

# Create your application
root = tk.Tk()
root.title("Themed App")
root.geometry("400x300")

# Get ttk style
style = ttk.Style()

# Apply a theme (returns background color)
bg_color = apply_theme("neon", style, root)

# Create some widgets
ttk.Label(root, text="Hello, themed world!").pack(padx=20, pady=10)
ttk.Button(root, text="Click me").pack(pady=5)
ttk.Entry(root).pack(pady=5)

root.mainloop()
```

## Available Themes

| Theme ID | Name | Description |
|----------|------|-------------|
| `light` | Light Theme | Default clean look |
| `dark` | Dark Theme | Easy on the eyes |
| `neon` | 🌈 NEON Theme | Visually wild but readable |
| `retrowave` | 🌅 Retrowave | 80s synthwave sunset vibes |
| `hacker` | 💻 Hacker | Matrix-style green on black |
| `lava` | 🌋 LAVA | Fiery red hot theme |
| `electric_lime` | ⚡ Electric Lime | Blindingly bright green-yellow |
| `bubblegum` | 🍬 Bubblegum | Hot pink explosion |
| `commander_keen` | 🚀 Commander Keen | Classic DOS EGA/VGA palette |

## API Reference

### Core Functions

#### `apply_theme(theme_id, style, root) -> str`

Apply a theme to your application.

```python
from tkthemes import apply_theme

bg_color = apply_theme("dark", style, root)
```

**Parameters:**
- `theme_id` (str): The ID of the theme to apply
- `style` (ttk.Style): The ttk Style object to configure
- `root`: The root Tk window

**Returns:** The background color string (e.g., "#2b2b2b")

#### `get_theme_list() -> List[Tuple[str, str]]`

Get a list of all available themes.

```python
from tkthemes import get_theme_list

themes = get_theme_list()
# Returns: [("light", "Light Theme"), ("dark", "Dark Theme"), ...]
```

### Custom Themes

#### `register_custom_theme(theme_id, config)`

Register your own custom theme.

```python
from tkthemes import register_custom_theme

def my_theme_apply(style, root):
    bg_color = "#1a1a2e"
    style.configure('TFrame', background=bg_color)
    style.configure('TLabel', background=bg_color, foreground='#ffffff')
    style.configure('TButton', background='#4a4a6a', foreground='#ffffff')
    root.configure(bg=bg_color)
    return bg_color

register_custom_theme("my_theme", {
    "name": "My Custom Theme",
    "description": "A cool custom theme",
    "icon": "🎨",
    "apply_fn": my_theme_apply
})

# Now you can use it
apply_theme("my_theme", style, root)
```

#### `register_theme(theme_id, name, apply_fn, icon="", description="")`

Lower-level function for registering themes.

```python
from tkthemes import register_theme

register_theme(
    theme_id="ocean",
    name="Ocean Theme",
    apply_fn=ocean_apply_function,
    icon="🌊",
    description="Deep blue ocean vibes"
)
```

### Registry Functions

#### `get_theme(theme_id) -> Optional[Dict]`

Get theme information by ID.

```python
from tkthemes import get_theme

theme_info = get_theme("neon")
# Returns: {"name": "🌈 NEON Theme", "icon": "🌈", ...}
```

#### `theme_exists(theme_id) -> bool`

Check if a theme exists.

```python
from tkthemes import theme_exists

if theme_exists("custom_theme"):
    apply_theme("custom_theme", style, root)
```

#### `unregister_theme(theme_id) -> bool`

Remove a theme from the registry.

```python
from tkthemes import unregister_theme

success = unregister_theme("my_theme")
```

#### `get_all_themes() -> Dict[str, Dict]`

Get all registered themes.

```python
from tkthemes import get_all_themes

all_themes = get_all_themes()
```

## Building a Theme Selector

Here's a complete example with a theme selector dropdown:

```python
import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme, get_theme_list

class ThemedApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Theme Demo")
        self.root.geometry("500x400")
        
        self.style = ttk.Style()
        
        # Theme selector
        selector_frame = ttk.Frame(self.root)
        selector_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(selector_frame, text="Select Theme:").pack(side='left')
        
        self.theme_var = tk.StringVar(value="light")
        themes = get_theme_list()
        theme_names = [name for _, name in themes]
        theme_ids = [tid for tid, _ in themes]
        
        combo = ttk.Combobox(
            selector_frame, 
            textvariable=self.theme_var,
            values=theme_names,
            state='readonly'
        )
        combo.pack(side='left', padx=10)
        combo.bind('<<ComboboxSelected>>', lambda e: self.change_theme(theme_ids[combo.current()]))
        
        # Demo widgets
        ttk.Label(self.root, text="Sample Label").pack(pady=5)
        ttk.Button(self.root, text="Sample Button").pack(pady=5)
        ttk.Entry(self.root).pack(pady=5)
        ttk.Checkbutton(self.root, text="Checkbox").pack(pady=5)
        
        # Apply initial theme
        apply_theme("light", self.style, self.root)
        
    def change_theme(self, theme_id):
        apply_theme(theme_id, self.style, self.root)
        
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ThemedApp()
    app.run()
```

## Development

### Running Tests

```bash
pip install -e .[dev]
pytest
```

### Project Structure

```
tkthemes/
├── __init__.py          # Package exports
├── core.py              # Core theme engine
├── registry.py          # Theme registry
└── themes/              # Built-in themes
    ├── __init__.py
    ├── light.py
    ├── dark.py
    ├── neon.py
    ├── retrowave.py
    ├── hacker.py
    ├── lava.py
    ├── electric_lime.py
    ├── bubblegum.py
    └── commander_keen.py
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Add your theme to `tkthemes/themes/`
4. Submit a pull request

## Credits

Originally extracted from [KVGroove](https://github.com/gerp93/KVGroove) music player