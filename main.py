"""Streamlit entrypoint for Florisoft.

This main.py replaces the Textual TUI entrypoint so hosting platforms that expect a Streamlit "main.py" will open the web UI.
Run locally from project root: streamlit run main.py
"""

import sys
from pathlib import Path

# Ensure project root is on sys.path so `config` and package modules are importable
_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from config import Config
import streamlit as st

cfg = Config()

st.set_page_config(page_title="Florisoft", layout="wide")
st.title("Florisoft")

sidebar = st.sidebar
sidebar.title("Menu")
page = sidebar.radio(
    "Sekcja",
    ["Marże", "Checklist (PDF)", "Proformy", "Fetch & Email"],
    label_visibility="collapsed",
)

if page == "Marże":
    st.header("Marże")
    st.write("Ścieżka Excel:", cfg.excel_path)
    st.write("Próg marży:", cfg.margin_threshold, "| Odchylenia:", cfg.deviant_threshold)
    with st.expander("Wgraj plik Excel"):
        f = st.file_uploader("Excel", type=["xlsx", "xls"])
        if f and st.button("Oblicz marże"):
            st.info("Logika marży – do implementacji (wczytaj Excel i policz).")

elif page == "Checklist (PDF)":
    st.header("Checklist (PDF)")
    st.write("Plik PDF:", cfg.pdf_output)
    st.info("Generowanie PDF – do implementacji.")

elif page == "Proformy":
    st.header("Proformy")
    st.json(cfg.series_map)
    with st.form("proforma"):
        buyer_id = st.text_input("Identyfikator kontrahenta")
        series_name = st.text_input("Nazwa serii")
        date = st.text_input("Data (YYYY-MM-DD)")
        if st.form_submit_button("Wyślij proformę"):
            st.info("Wysyłka do iFirma – do implementacji (użyj cfg.url, cfg.ifirma_user, cfg.ifirma_key).")

elif page == "Fetch & Email":
    st.header("Fetch & Email")
    st.info("Fetch & Email – do implementacji.")
