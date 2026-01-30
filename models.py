"""Data models for Florisoft application."""
from dataclasses import dataclass
from typing import Optional
import pandas as pd


@dataclass
class MarginResult:
    """Result of margin calculation."""
    avg_margin_by_client: pd.DataFrame
    all_margins: pd.DataFrame
    deviant_items: pd.DataFrame
    eur_rate: float


@dataclass
class ChecklistItem:
    """Single item for checklist PDF."""
    subclient: str
    article: str
    quantity: int
    size: str


@dataclass
class ProformaItem:
    """Single item for proforma invoice."""
    subclient: str
    article: str
    quantity: float
    client_price: float


@dataclass
class ProformaRequest:
    """Complete proforma invoice request."""
    buyer_id: str
    series_name: str
    date: str
    items: list[ProformaItem]
    
    def to_dict(self) -> dict:
        """Convert to API request format."""
        return {
            "IdentyfikatorKontrahenta": self.buyer_id,
            "NazwaSeriiNumeracji": self.series_name,
            "LiczOd": "BRT",
            "TypFakturyKrajowej": "SPRZ",
            "DataWystawienia": self.date,
            "SposobZaplaty": "PRZ",
            "RodzajPodpisuOdbiorcy": "BPO",
            "Pozycje": [
                {
                    "StawkaVat": 0.08,
                    "TypStawkiVat": "PRC",
                    "Ilosc": float(item.quantity),
                    "CenaJednostkowa": float(item.client_price),
                    "NazwaPelna": item.article,
                    "Jednostka": "szt."
                }
                for item in self.items
            ]
        }
