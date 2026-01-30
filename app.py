"""Main Florisoft application."""
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Header, Footer, Button
from textual.reactive import reactive
from config import Config
from widgets.margin_widget import MarginWidget
from widgets.checklist_widget import ChecklistWidget
from widgets.proforma_widget import ProformaWidget
from widgets.fetch_email_widget import FetchAndEmailWidget


class FlorisoftApp(App):
    """Main application class for Florisoft."""
    
    CSS = """
    Screen {
        align: center top;
        padding: 0 1;
    }
    #menu {
        layout: horizontal;
        padding: 0;
        margin: 0;
    }
    #menu Button {
        margin: 0;
        padding: 0 2 0 2;
    }
    #content {
        padding-top: 0;
        margin-top: 0;
    }
    .title {
        text-style: bold;
        padding-bottom: 0;
    }
    .subtitle {
        text-style: bold;
        padding-top: 0;
        padding-bottom: 0;
    }
    """
    
    active = reactive("margin")  # default
    
    def __init__(self):
        """Initialize application with configuration."""
        super().__init__()
        self.config = Config()
    
    def compose(self) -> ComposeResult:
        """Compose application UI."""
        yield Header(show_clock=True)
        with Horizontal(id="menu"):
            yield Button("Marże", id="nav_margin")
            yield Button("Checklist (PDF)", id="nav_pdf")
            yield Button("Proformy", id="nav_proforma")
            yield Button("Fetch & Email", id="nav_fetch_email")
        yield Container(id="content")
        yield Footer()
    
    def on_mount(self):
        """Called when application is mounted."""
        self.load_widget()
    
    def load_widget(self):
        """Load the appropriate widget based on active tab."""
        content = self.query_one("#content", Container)
        content.remove_children()
        
        if self.active == "margin":
            content.mount(MarginWidget(self.config))
        elif self.active == "pdf":
            content.mount(ChecklistWidget(self.config))
        elif self.active == "proforma":
            content.mount(ProformaWidget(self.config))
        elif self.active == "fetch_email":
            content.mount(FetchAndEmailWidget(self.config))
    
    def on_button_pressed(self, event):
        """Handle navigation button presses."""
        btn_id = event.button.id or ""
        
        if btn_id == "nav_margin":
            self.active = "margin"
            self.load_widget()
        elif btn_id == "nav_pdf":
            self.active = "pdf"
            self.load_widget()
        elif btn_id == "nav_proforma":
            self.active = "proforma"
            self.load_widget()
        elif btn_id == "nav_fetch_email":
            self.active = "fetch_email"
            self.load_widget()
