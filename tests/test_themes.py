"""
Tests for tkthemes core functionality
"""

import unittest
from unittest.mock import MagicMock, patch


class TestCore(unittest.TestCase):
    """Test core theme functionality."""

    def setUp(self):
        """Set up test fixtures."""
        # Import here to get fresh registry state
        import tkthemes
        self.tkthemes = tkthemes

    def test_apply_theme_valid(self):
        """Test applying a valid theme."""
        mock_style = MagicMock()
        mock_root = MagicMock()
        
        # Apply light theme
        bg_color = self.tkthemes.apply_theme("light", mock_style, mock_root)
        
        # Check that a background color was returned
        self.assertIsInstance(bg_color, str)
        self.assertTrue(bg_color.startswith("#"))
        
        # Check that root was configured
        mock_root.configure.assert_called()

    def test_apply_theme_dark(self):
        """Test applying dark theme."""
        mock_style = MagicMock()
        mock_root = MagicMock()
        
        bg_color = self.tkthemes.apply_theme("dark", mock_style, mock_root)
        
        self.assertEqual(bg_color, "#2b2b2b")

    def test_apply_theme_neon(self):
        """Test applying neon theme."""
        mock_style = MagicMock()
        mock_root = MagicMock()
        
        bg_color = self.tkthemes.apply_theme("neon", mock_style, mock_root)
        
        self.assertEqual(bg_color, "#0a0a0a")

    def test_apply_theme_fallback(self):
        """Test that invalid theme falls back to light."""
        mock_style = MagicMock()
        mock_root = MagicMock()
        
        # Apply non-existent theme - should fallback to light
        bg_color = self.tkthemes.apply_theme("nonexistent_theme", mock_style, mock_root)
        
        self.assertEqual(bg_color, "#f5f5f5")  # Light theme bg

    def test_get_theme_list(self):
        """Test getting theme list."""
        themes = self.tkthemes.get_theme_list()
        
        self.assertIsInstance(themes, list)
        self.assertGreater(len(themes), 0)
        
        # Check structure
        for theme_id, theme_name in themes:
            self.assertIsInstance(theme_id, str)
            self.assertIsInstance(theme_name, str)
        
        # Check expected themes exist
        theme_ids = [tid for tid, _ in themes]
        self.assertIn("light", theme_ids)
        self.assertIn("dark", theme_ids)
        self.assertIn("neon", theme_ids)


class TestRegistry(unittest.TestCase):
    """Test theme registry functionality."""

    def setUp(self):
        """Set up test fixtures."""
        from tkthemes import registry
        self.registry = registry

    def test_theme_exists(self):
        """Test checking if theme exists."""
        self.assertTrue(self.registry.theme_exists("light"))
        self.assertTrue(self.registry.theme_exists("dark"))
        self.assertFalse(self.registry.theme_exists("nonexistent"))

    def test_get_theme(self):
        """Test getting theme info."""
        theme = self.registry.get_theme("light")
        
        self.assertIsNotNone(theme)
        self.assertIn("name", theme)
        self.assertIn("apply_fn", theme)
        self.assertEqual(theme["name"], "Light Theme")

    def test_get_theme_nonexistent(self):
        """Test getting nonexistent theme."""
        theme = self.registry.get_theme("nonexistent")
        self.assertIsNone(theme)

    def test_get_all_themes(self):
        """Test getting all themes."""
        all_themes = self.registry.get_all_themes()
        
        self.assertIsInstance(all_themes, dict)
        self.assertGreater(len(all_themes), 0)
        self.assertIn("light", all_themes)
        self.assertIn("dark", all_themes)


class TestCustomThemes(unittest.TestCase):
    """Test custom theme registration."""

    def setUp(self):
        """Set up test fixtures."""
        import tkthemes
        self.tkthemes = tkthemes

    def tearDown(self):
        """Clean up after tests."""
        # Remove test themes if they exist
        try:
            self.tkthemes.unregister_theme("test_custom_theme")
        except Exception:
            pass

    def test_register_custom_theme(self):
        """Test registering a custom theme."""
        def custom_apply(style, root):
            root.configure(bg="#123456")
            return "#123456"
        
        self.tkthemes.register_custom_theme("test_custom_theme", {
            "name": "Test Custom Theme",
            "apply_fn": custom_apply,
            "icon": "🧪",
            "description": "A test theme"
        })
        
        # Check it exists
        self.assertTrue(self.tkthemes.theme_exists("test_custom_theme"))
        
        # Check we can apply it
        mock_style = MagicMock()
        mock_root = MagicMock()
        bg_color = self.tkthemes.apply_theme("test_custom_theme", mock_style, mock_root)
        
        self.assertEqual(bg_color, "#123456")

    def test_register_custom_theme_missing_name(self):
        """Test that missing name raises error."""
        with self.assertRaises(ValueError):
            self.tkthemes.register_custom_theme("bad_theme", {
                "apply_fn": lambda s, r: "#000000"
            })

    def test_register_custom_theme_missing_apply_fn(self):
        """Test that missing apply_fn raises error."""
        with self.assertRaises(ValueError):
            self.tkthemes.register_custom_theme("bad_theme", {
                "name": "Bad Theme"
            })

    def test_unregister_theme(self):
        """Test unregistering a theme."""
        def custom_apply(style, root):
            return "#ffffff"
        
        self.tkthemes.register_custom_theme("test_custom_theme", {
            "name": "Test Theme",
            "apply_fn": custom_apply
        })
        
        self.assertTrue(self.tkthemes.theme_exists("test_custom_theme"))
        
        result = self.tkthemes.unregister_theme("test_custom_theme")
        
        self.assertTrue(result)
        self.assertFalse(self.tkthemes.theme_exists("test_custom_theme"))

    def test_unregister_nonexistent_theme(self):
        """Test unregistering a theme that doesn't exist."""
        result = self.tkthemes.unregister_theme("definitely_not_a_theme")
        self.assertFalse(result)


class TestAllThemes(unittest.TestCase):
    """Test that all built-in themes work correctly."""

    def setUp(self):
        """Set up test fixtures."""
        import tkthemes
        self.tkthemes = tkthemes

    def test_all_themes_apply(self):
        """Test that all themes can be applied without error."""
        themes = self.tkthemes.get_theme_list()
        
        for theme_id, theme_name in themes:
            with self.subTest(theme=theme_id):
                mock_style = MagicMock()
                mock_root = MagicMock()
                
                bg_color = self.tkthemes.apply_theme(theme_id, mock_style, mock_root)
                
                # Should return a color string
                self.assertIsInstance(bg_color, str)
                self.assertTrue(bg_color.startswith("#"), 
                    f"Theme {theme_id} returned invalid bg_color: {bg_color}")
                
                # Should have called style.configure at least once
                self.assertTrue(mock_style.configure.called,
                    f"Theme {theme_id} did not configure any styles")
                
                # Should have configured root background
                mock_root.configure.assert_called()

    def test_expected_themes_exist(self):
        """Test that all expected themes are registered."""
        expected_themes = [
            "light",
            "dark", 
            "neon",
            "retrowave",
            "hacker",
            "lava",
            "electric_lime",
            "bubblegum",
            "commander_keen"
        ]
        
        for theme_id in expected_themes:
            with self.subTest(theme=theme_id):
                self.assertTrue(self.tkthemes.theme_exists(theme_id),
                    f"Expected theme '{theme_id}' not found")


if __name__ == "__main__":
    unittest.main()
