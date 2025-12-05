# Installation

## Requirements

- Python 3.7 or higher
- tkinter (usually included with Python)

## Install from PyPI

```bash
pip install tkthemes
```

## Install from Source

Clone the repository and install in development mode:

```bash
git clone https://github.com/gerp93/KVG_Themes.git
cd KVG_Themes
pip install -e .
```

## Install with Development Dependencies

To run tests and contribute to development:

```bash
pip install -e .[dev]
```

## Verify Installation

```python
import tkthemes
print(tkthemes.__version__)
print(tkthemes.get_theme_list())
```

## Troubleshooting

### tkinter not found

If you get an error about tkinter not being found, you may need to install it separately:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**macOS (with Homebrew Python):**
```bash
brew install python-tk
```

**Windows:**
tkinter is included with the standard Python installer. Make sure to check the "tcl/tk and IDLE" option during installation.
