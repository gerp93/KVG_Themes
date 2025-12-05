# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-05

### Added
- Initial release of tkthemes as a standalone package
- 9 built-in themes:
  - Light - Default clean look
  - Dark - Easy on the eyes
  - Neon - Visually wild but readable
  - Retrowave - 80s synthwave sunset vibes
  - Hacker - Matrix-style green on black
  - Lava - Fiery red hot theme
  - Electric Lime - Blindingly bright green-yellow
  - Bubblegum - Hot pink explosion
  - Commander Keen - Classic DOS EGA/VGA palette
- Core API:
  - `apply_theme()` - Apply themes to applications
  - `get_theme_list()` - List available themes
  - `register_custom_theme()` - Register custom themes
  - `register_theme()` - Low-level theme registration
  - `unregister_theme()` - Remove themes from registry
  - `get_theme()` - Get theme info by ID
  - `theme_exists()` - Check if theme exists
  - `get_all_themes()` - Get all registered themes
- Full documentation
- Example applications
- Test suite
- Zero dependencies (only Python stdlib)
- Python 3.7+ support
