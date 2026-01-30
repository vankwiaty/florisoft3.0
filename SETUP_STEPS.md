# Step-by-step: Run FastAPI, GitHub, then Streamlit

**Do I have to keep it always on?** No. Run it when you want to use the app, then stop (Ctrl+C). Next time you want it, start again. To start both FastAPI and Streamlit in one go, use the script below.

**Want to access it from another computer (or phone) without your PC on?** Deploy the app to the cloud (e.g. Render.com, free tier). See **DEPLOY.md** for step-by-step instructions.

**One-click start (after first-time setup):**  
In PowerShell, from the project folder, run:
```powershell
.\run_web.ps1
```
That opens FastAPI in one window and Streamlit in another. When you're done, close both windows (or Ctrl+C in each).

---

## Part 1 – Run FastAPI for the first time

1. **Open a terminal in your project**
   - In Cursor: **Terminal → New Terminal** (or `` Ctrl+` ``).
   - Make sure you're in the project folder: `C:\Users\Tom\Documents\GitHub\florisoft3.0`

2. **Create a virtual environment (recommended)**
   ```powershell
   python -m venv venv
   ```
   Then activate it:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   (You should see `(venv)` in the prompt.)

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Start the FastAPI backend**
   ```powershell
   uvicorn backend.main:app --reload
   ```
   Leave this terminal open. You should see something like:
   `Uvicorn running on http://127.0.0.1:8000`

5. **Check that it works**
   - In a browser open: **http://127.0.0.1:8000**  
     You should see: `{"app":"Florisoft API","docs":"/docs"}`
   - Open: **http://127.0.0.1:8000/docs**  
     You should see the interactive API docs (Swagger).

6. **Stop the server when you're done**
   - In the terminal where uvicorn is running, press **Ctrl+C**.

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

## Part 3 – What to do next with Streamlit

1. **Start the FastAPI backend again** (if it’s not running)
   - Terminal 1:
   ```powershell
   cd C:\Users\Tom\Documents\GitHub\florisoft3.0
   .\venv\Scripts\Activate.ps1
   uvicorn backend.main:app --reload
   ```

2. **Open a second terminal** (Terminal → New Terminal).

3. **Activate venv and run Streamlit**
   ```powershell
   cd C:\Users\Tom\Documents\GitHub\florisoft3.0
   .\venv\Scripts\Activate.ps1
   streamlit run web/app.py
   ```

4. **Use the web app**
   - Browser should open to **http://localhost:8501** (or open that URL manually).
   - Use the **sidebar** to switch: **Marże**, **Checklist (PDF)**, **Proformy**, **Fetch & Email**.
   - The app calls your FastAPI backend; if you see "Backend nie działa", make sure uvicorn is running in the first terminal.

5. **Stop when finished**
   - Streamlit: **Ctrl+C** in the Streamlit terminal.
   - FastAPI: **Ctrl+C** in the uvicorn terminal.

---

## Quick reference

| What              | Command / URL |
|-------------------|----------------|
| **Start both (API + Streamlit)** | `.\run_web.ps1` |
| Activate venv     | `.\venv\Scripts\Activate.ps1` |
| Run FastAPI       | `uvicorn backend.main:app --reload` |
| API base          | http://127.0.0.1:8000 |
| API docs          | http://127.0.0.1:8000/docs |
| Run Streamlit     | `streamlit run web/app.py` |
| Web UI            | http://localhost:8501 |
| Push to GitHub    | `git add .` → `git commit -m "..."` → `git push origin main` |
