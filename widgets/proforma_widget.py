"""Proforma invoice widget."""
from textual.containers import Vertical
from textual.widgets import Static
from config import Config


class ProformaWidget(Vertical):
    """Widget for proforma invoices."""

    def __init__(self, config: Config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config

    def compose(self):
        yield Static("[bold]Proformy[/bold]", classes="title")
        yield Static("Placeholder: proforma view (iFirma)", classes="subtitle")
