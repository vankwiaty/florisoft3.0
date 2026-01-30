"""Fetch and email widget."""
from textual.containers import Vertical
from textual.widgets import Static
from config import Config


class FetchAndEmailWidget(Vertical):
    """Widget for fetch and email actions."""

    def __init__(self, config: Config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = config

    def compose(self):
        yield Static("[bold]Fetch & Email[/bold]", classes="title")
        yield Static("Placeholder: fetch and email view", classes="subtitle")
