"""
Theme Demo Application
Full demo showing all available themes with a theme selector
"""

import tkinter as tk
from tkinter import ttk
from tkthemes import apply_theme, get_theme_list


class ThemeDemoApp:
    """Demo application showcasing all tkthemes."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("tkthemes Demo")
        self.root.geometry("600x500")
        
        self.style = ttk.Style()
        self.current_theme = "light"
        
        self._create_widgets()
        self._apply_current_theme()
    
    def _create_widgets(self):
        """Create all demo widgets."""
        # Theme selector at top
        self.selector_frame = ttk.Frame(self.root, padding="10")
        self.selector_frame.pack(fill="x")
        
        ttk.Label(self.selector_frame, text="🎨 Select Theme:").pack(side="left")
        
        self.themes = get_theme_list()
        self.theme_var = tk.StringVar(value=self.themes[0][1])
        
        self.theme_combo = ttk.Combobox(
            self.selector_frame,
            textvariable=self.theme_var,
            values=[name for _, name in self.themes],
            state="readonly",
            width=30
        )
        self.theme_combo.pack(side="left", padx=10)
        self.theme_combo.bind("<<ComboboxSelected>>", self._on_theme_change)
        
        # Main content area
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill="both", expand=True)
        
        # Header
        ttk.Label(
            self.main_frame, 
            text="tkthemes Demo Application",
            style="Header.TLabel"
        ).pack(pady=(0, 20))
        
        # Notebook with tabs
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill="both", expand=True)
        
        # Tab 1: Basic widgets
        self._create_basic_tab()
        
        # Tab 2: Buttons
        self._create_buttons_tab()
        
        # Tab 3: Data display
        self._create_data_tab()
    
    def _create_basic_tab(self):
        """Create tab with basic input widgets."""
        tab = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(tab, text="Basic Widgets")
        
        # Labels
        ttk.Label(tab, text="Standard Label").pack(pady=5, anchor="w")
        ttk.Label(tab, text="Header Label", style="Header.TLabel").pack(pady=5, anchor="w")
        
        # Entry
        ttk.Label(tab, text="Text Entry:").pack(pady=(15, 0), anchor="w")
        entry = ttk.Entry(tab, width=40)
        entry.insert(0, "Sample text input")
        entry.pack(pady=5, anchor="w")
        
        # Checkbuttons
        ttk.Label(tab, text="Checkbuttons:").pack(pady=(15, 0), anchor="w")
        check_frame = ttk.Frame(tab)
        check_frame.pack(anchor="w")
        for i in range(3):
            ttk.Checkbutton(check_frame, text=f"Option {i+1}").pack(side="left", padx=5)
        
        # Radiobuttons
        ttk.Label(tab, text="Radiobuttons:").pack(pady=(15, 0), anchor="w")
        radio_frame = ttk.Frame(tab)
        radio_frame.pack(anchor="w")
        radio_var = tk.StringVar(value="1")
        for i in range(3):
            ttk.Radiobutton(
                radio_frame, 
                text=f"Choice {i+1}", 
                variable=radio_var, 
                value=str(i+1)
            ).pack(side="left", padx=5)
    
    def _create_buttons_tab(self):
        """Create tab with button styles."""
        tab = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(tab, text="Buttons")
        
        ttk.Label(tab, text="Standard Buttons:").pack(pady=5, anchor="w")
        btn_frame1 = ttk.Frame(tab)
        btn_frame1.pack(anchor="w", pady=5)
        for i in range(3):
            ttk.Button(btn_frame1, text=f"Button {i+1}").pack(side="left", padx=5)
        
        ttk.Label(tab, text="Control Buttons (larger):").pack(pady=(20, 5), anchor="w")
        btn_frame2 = ttk.Frame(tab)
        btn_frame2.pack(anchor="w", pady=5)
        ttk.Button(btn_frame2, text="⏮ Prev", style="Control.TButton").pack(side="left", padx=5)
        ttk.Button(btn_frame2, text="▶ Play", style="Control.TButton").pack(side="left", padx=5)
        ttk.Button(btn_frame2, text="⏭ Next", style="Control.TButton").pack(side="left", padx=5)
        
        ttk.Label(tab, text="Menu Button:").pack(pady=(20, 5), anchor="w")
        menu_btn = ttk.Menubutton(tab, text="Options ▼")
        menu = tk.Menu(menu_btn, tearoff=0)
        menu.add_command(label="Option 1")
        menu.add_command(label="Option 2")
        menu.add_separator()
        menu.add_command(label="Exit")
        menu_btn["menu"] = menu
        menu_btn.pack(anchor="w", pady=5)
    
    def _create_data_tab(self):
        """Create tab with data display widgets."""
        tab = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(tab, text="Data Display")
        
        ttk.Label(tab, text="Treeview:").pack(anchor="w")
        
        # Create treeview with scrollbar
        tree_frame = ttk.Frame(tab)
        tree_frame.pack(fill="both", expand=True, pady=5)
        
        tree = ttk.Treeview(tree_frame, columns=("col1", "col2", "col3"), show="headings", height=8)
        tree.heading("col1", text="Name")
        tree.heading("col2", text="Type")
        tree.heading("col3", text="Status")
        
        # Sample data
        data = [
            ("Light Theme", "Default", "Active"),
            ("Dark Theme", "Dark Mode", "Available"),
            ("Neon Theme", "Colorful", "Available"),
            ("Retrowave", "80s Style", "Available"),
            ("Hacker", "Matrix", "Available"),
            ("Lava", "Hot", "Available"),
            ("Electric Lime", "Bright", "Available"),
            ("Bubblegum", "Pink", "Available"),
            ("Commander Keen", "Retro DOS", "Available"),
        ]
        
        for item in data:
            tree.insert("", "end", values=item)
        
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def _on_theme_change(self, event=None):
        """Handle theme selection change."""
        selected_name = self.theme_var.get()
        for tid, name in self.themes:
            if name == selected_name:
                self.current_theme = tid
                self._apply_current_theme()
                break
    
    def _apply_current_theme(self):
        """Apply the current theme."""
        apply_theme(self.current_theme, self.style, self.root)
    
    def run(self):
        """Run the application."""
        self.root.mainloop()


if __name__ == "__main__":
    app = ThemeDemoApp()
    app.run()
