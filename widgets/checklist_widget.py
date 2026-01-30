"""Checklist PDF widget."""
from textual.containers import Vertical
from textual.widgets import Static
from config import Config


class ChecklistWidget(Vertical):
    """Widget for checklist PDF generation."""

    def __init__(self, config: Config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config

    def compose(self):
        yield Static("[bold]Checklist (PDF)[/bold]", classes="title")
        yield Static("Placeholder: PDF output → " + self.config.pdf_output, classes="subtitle")
