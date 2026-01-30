"""
Florisoft web app (Streamlit) – talks to FastAPI backend.
Run backend first: uvicorn backend.main:app --reload
Then: streamlit run web/app.py

When deployed: set env FLORISOFT_API_URL to your API URL (e.g. https://florisoft-api.onrender.com).
"""
import os
import streamlit as st
import httpx

API_BASE = os.environ.get("FLORISOFT_API_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Florisoft", layout="wide")
st.title("Florisoft")

sidebar = st.sidebar
sidebar.title("Menu")
page = sidebar.radio(
    "Sekcja",
    ["Marże", "Checklist (PDF)", "Proformy", "Fetch & Email"],
    label_visibility="collapsed",
)


def call_api(path: str, method: str = "GET", json: dict = None):
    try:
        with httpx.Client(timeout=10.0) as client:
            if method == "GET":
                r = client.get(f"{API_BASE}{path}")
            else:
                r = client.post(f"{API_BASE}{path}", json=json)
        return r.json()
    except httpx.ConnectError:
        return {"error": "Backend nie działa. Uruchom: uvicorn backend.main:app --reload"}
    except Exception as e:
        return {"error": str(e)}


if page == "Marże":
    st.header("Marże")
    data = call_api("/api/margins")
    if "error" in data:
        st.error(data["error"])
    else:
        st.json(data)
    with st.expander("Wgraj plik Excel"):
        f = st.file_uploader("Excel", type=["xlsx", "xls"])
        if f and st.button("Oblicz marże"):
            with httpx.Client(timeout=30.0) as client:
                try:
                    r = client.post(f"{API_BASE}/api/margins/upload", files={"file": (f.name, f.getvalue())})
                    st.json(r.json())
                except httpx.ConnectError:
                    st.error("Backend nie działa.")

elif page == "Checklist (PDF)":
    st.header("Checklist (PDF)")
    data = call_api("/api/checklist")
    if "error" in data:
        st.error(data["error"])
    else:
        st.json(data)
    st.info("Generowanie PDF – do implementacji w backendzie.")

elif page == "Proformy":
    st.header("Proformy")
    data = call_api("/api/config")
    if "error" in data:
        st.error(data["error"])
    else:
        st.json(data.get("series_map", {}))
    with st.form("proforma"):
        buyer_id = st.text_input("Identyfikator kontrahenta")
        series_name = st.text_input("Nazwa serii")
        date = st.text_input("Data (YYYY-MM-DD)")
        if st.form_submit_button("Wyślij proformę"):
            out = call_api("/api/proforma", method="POST", json={
                "buyer_id": buyer_id,
                "series_name": series_name,
                "date": date,
                "items": [],
            })
            st.json(out)

elif page == "Fetch & Email":
    st.header("Fetch & Email")
    data = call_api("/api/fetch-email")
    if "error" in data:
        st.error(data["error"])
    else:
        st.json(data)
