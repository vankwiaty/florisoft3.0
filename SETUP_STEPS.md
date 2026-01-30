# Step-by-step: Run Florisoft (Streamlit), GitHub, deploy

**Do I have to keep it always on?** No. Run it when you want to use the app, then stop (Ctrl+C). Next time you want it, start again. To start the app, run: `streamlit run web/app.py` (from project root).

**Want to access it from another computer (or phone) without your PC on?** Deploy the Streamlit app to the cloud (Streamlit Community Cloud or Render). See **DEPLOY.md**.

**Start the app (Streamlit only – no FastAPI):**  
From project folder:
```powershell
.\venv\Scripts\Activate.ps1
streamlit run web/app.py
```
Then open http://localhost:8501.

---

## Part 1 – Run the app for the first time (Streamlit only)

1. **Open a terminal in your project**
   - In Cursor: **Terminal → New Terminal** (or `` Ctrl+` ``).
   - Make sure you're in: `C:\Users\Tom\Documents\GitHub\florisoft3.0`

2. **Create a virtual environment (recommended)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
   (You should see `(venv)` in the prompt.)

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Start the app**
   ```powershell
   streamlit run web/app.py
   ```
   Open **http://localhost:8501** in your browser.

5. **Stop when done**
   - In the terminal press **Ctrl+C**.

---

## Part 2 – Connect with GitHub (save your code)

1. **Make sure Git is installed**
   - If `git` is not in your PATH, install [Git for Windows](https://git-scm.com/download/win) and restart Cursor.

2. **Check your current Git state**
   - In Cursor: open **Source Control** (Ctrl+Shift+G) or the branch icon in the left sidebar.
   - You should see changed/untracked files (e.g. `backend/`, `web/`, `requirements.txt`, `README_WEB.md`, `SETUP_STEPS.md`).

3. **Stage all changes**
   - In Source Control, click **+** next to "Changes" to stage all,  
     or in a terminal (new terminal, not the one running uvicorn):
   ```powershell
   git add .
   ```

4. **Commit**
   ```powershell
   git commit -m "Add FastAPI backend, Streamlit web app, and web setup docs"
   ```

5. **Push to GitHub**
   - If you're already signed in to GitHub in Cursor (Accounts), push from Source Control (↑ Push),  
     or in terminal:
   ```powershell
   git push origin main
   ```
   - If Git asks for credentials, use your GitHub username and a **Personal Access Token** (not your GitHub password). Create one: GitHub → Settings → Developer settings → Personal access tokens.

6. **Confirm**
   - Open **https://github.com/vankwiaty/florisoft3.0** and check that the new files (backend, web, README_WEB.md, etc.) are there.

---

## Part 3 – Use the app next time

1. **Start the app** (if it’s not running)
   ```powershell
   cd C:\Users\Tom\Documents\GitHub\florisoft3.0
   .\venv\Scripts\Activate.ps1
   streamlit run web/app.py
   ```
2. Open **http://localhost:8501** and use the sidebar: **Marże**, **Checklist (PDF)**, **Proformy**, **Fetch & Email**.
3. **Stop:** **Ctrl+C** in the terminal.

---

## Quick reference

| What              | Command / URL |
|-------------------|----------------|
| Activate venv     | `.\venv\Scripts\Activate.ps1` |
| Run app           | `streamlit run web/app.py` |
| Web UI            | http://localhost:8501 |
| Push to GitHub    | `git add .` → `git commit -m "..."` → `git push origin main` |
| Deploy (any device) | See **DEPLOY.md** (Streamlit Community Cloud or Render) |
