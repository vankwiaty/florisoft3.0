# Florisoft – Web (FastAPI + Streamlit)

## Database

**There is no database.** Data comes from:

- **Excel:** `dane_do_faktury.xlsx` (config)
- **iFirma API:** proformy
- **Files:** PDF checklist output

To add a DB later (e.g. SQLite for users/sessions), see `backend/database.py`.

---

## Run the web stack

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the FastAPI backend** (from project root)
   ```bash
   uvicorn backend.main:app --reload
   ```
   API: http://127.0.0.1:8000  
   Docs: http://127.0.0.1:8000/docs

3. **Start Streamlit** (new terminal, from project root)
   ```bash
   streamlit run web/app.py
   ```
   Web UI: http://localhost:8501

Use the sidebar in Streamlit to switch: Marże, Checklist (PDF), Proformy, Fetch & Email.
