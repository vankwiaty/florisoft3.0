"""Margin calculation widget."""
from textual.containers import Vertical
from textual.widgets import Static
from config import Config


class MarginWidget(Vertical):
    """Widget for margin calculations."""

    def __init__(self, config: Config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config

    def compose(self):
        yield Static("[bold]Marże[/bold]", classes="title")
        yield Static("Placeholder: margin view (Excel: " + self.config.excel_path + ")", classes="subtitle")
