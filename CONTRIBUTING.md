# Contributing to tkthemes

Thank you for your interest in contributing to tkthemes! This document provides guidelines for contributing.

## Ways to Contribute

1. **Report Bugs**: Open an issue describing the bug
2. **Suggest Features**: Open an issue describing the feature
3. **Submit Themes**: Add new themes to the collection
4. **Improve Documentation**: Help make the docs better
5. **Fix Bugs**: Submit pull requests for bug fixes

## Development Setup

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/KVG_Themes.git
   cd KVG_Themes
   ```

2. Install in development mode:
   ```bash
   pip install -e .[dev]
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Adding a New Theme

1. Create a new file in `tkthemes/themes/` (e.g., `my_theme.py`)

2. Follow this template:
   ```python
   """
   My Theme
   Brief description
   """
   
   from tkinter import ttk
   from typing import Any
   
   
   def apply(style: ttk.Style, root: Any) -> str:
       """Apply the theme."""
       bg_color = "#your_color"
       
       # Configure styles...
       style.configure('TFrame', background=bg_color)
       # ... more configurations
       
       root.configure(bg=bg_color)
       return bg_color
   
   
   THEME_INFO = {
       "id": "my_theme",
       "name": "🎨 My Theme",
       "icon": "🎨",
       "description": "Brief description"
   }
   ```

3. Register in `tkthemes/themes/__init__.py`:
   ```python
   from . import my_theme
   
   _THEME_MODULES = [
       # ... existing themes
       my_theme,
   ]
   ```

4. Add tests for your theme

5. Submit a pull request

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Include docstrings for functions
- Keep theme code consistent with existing themes

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/my-theme`
2. Make your changes
3. Run tests: `pytest`
4. Commit with clear message: `git commit -m "Add my_theme"`
5. Push to your fork: `git push origin feature/my-theme`
6. Open a pull request

## Theme Guidelines

When creating themes:

- Ensure text is readable against backgrounds
- Test all widget types (buttons, entries, treeviews, etc.)
- Use a consistent color palette
- Consider accessibility (color contrast)
- Include an appropriate emoji icon
- Provide a clear name and description

## Questions?

Open an issue for any questions about contributing!
