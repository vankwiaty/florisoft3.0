"""Configuration settings for Florisoft application."""
from dataclasses import dataclass


@dataclass
class Config:
    """Application configuration."""
    excel_path: str = "dane_do_faktury.xlsx"
    pdf_output: str = "lista_kontrolna.pdf"
    font_name: str = "DejaVuSans"
    ifirma_user: str = "MIKOLAJ.MARCINKOWSKI@INTERIA.PL"
    ifirma_key: str = "35CB43FAE2F0242E"
    klucz_nazwa: str = "faktura"
    url: str = "https://www.ifirma.pl/iapi/fakturaproformakraj.json"
    margin_threshold: float = 10.0
    deviant_threshold: float = 5.0
    
    # Client mappings
    client_map: dict = None
    series_map: dict = None
    
    def __post_init__(self):
        if self.client_map is None:
            self.client_map = {
                "58A": "ID_KLIENTA_58A",
                "58B": "FLO",
                "58C": "ZKT",
                "58D": "ALE",
                "58E": "ARC",
                "58F": "JEA",
                "58G": "INS",
                "58H": "ONI",
                "58J": "LAW",
                "58K": "SAL",
                "58L": "MDL",
                "58M": "FLD",
                "58N": "MON",
                "58P": "REN",
                "58Q": "ZYL",
                "58Z": "ZYL"
            }
        
        if self.series_map is None:
            self.series_map = {
                "58A": "PF-58A",
                "58B": "Flori Studio ProForma",
                "58C": "Zakątek ProForma",
                "58D": "Ale Ładnie ProForma",
                "58E": "Architektura kwiatów ProForma",
                "58F": "Jeanette ProForma",
                "58G": "Kwiatowe Inspiracje ProForma",
                "58H": "OniŚlub ProForma",
                "58J": "Lawendowy Ogród ProForma",
                "58K": "Salonik ProForma",
                "58L": "MDL Expo ProForma",
                "58M": "Flora Deco ProForma",
                "58N": "MONICA.FLOWERSSS",
                "58P": "Renee ProForma",
                "58Q": "Zylinscy kwietnik",
                "58Z": "Zylinscy kwietnik"
            }
