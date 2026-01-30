# Deploy Florisoft (Streamlit only) – access from any computer without your PC on

You only deploy **one** Streamlit app. No FastAPI, no second service, no API URL to set.

---

## Option A – Streamlit Community Cloud (easiest, free)

1. **Push your code to GitHub** (repo: florisoft3.0).
2. Go to **https://share.streamlit.io** and sign in with GitHub.
3. Click **New app**.
4. **Repository:** `vankwiaty/florisoft3.0` (or your fork).
5. **Branch:** `main`.
6. **Main file path:** `web/app.py`.
7. **App URL:** leave default (e.g. `https://your-app-name.streamlit.app`).
8. Click **Deploy**. Wait a few minutes.
9. Open the given URL from any computer or phone; your PC can be off.

**Note:** Streamlit Cloud runs from the repo root, so `web/app.py` can import `config` from the project root. No extra settings needed.

---

## Option B – Render (one Web Service)

1. **Push your code to GitHub**.
2. Go to **https://dashboard.render.com** → **New +** → **Web Service**.
3. Connect the **florisoft3.0** repo.
4. **Build command:** `pip install -r requirements.txt`
5. **Start command:** `streamlit run web/app.py --server.port $PORT --server.address 0.0.0.0`
6. **Plan:** Free. Create the service and wait for deploy.
7. Open the service URL from any device.

---

## Run locally (no deploy)

From project root:

```powershell
pip install -r requirements.txt
streamlit run web/app.py
```

Then open http://localhost:8501. No FastAPI to start.

---

## Summary

| What        | Command / URL |
|------------|----------------|
| Run locally | `streamlit run web/app.py` (from project root) |
| Deploy (easiest) | Streamlit Community Cloud → connect repo, main file `web/app.py` |
| Deploy (Render) | One Web Service, start: `streamlit run web/app.py --server.port $PORT --server.address 0.0.0.0` |

One app, one service – simpler.
