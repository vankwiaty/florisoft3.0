# Deploy Florisoft so you can access it from any computer (without your PC on)

Deploy the app to **Render.com** (free tier). You get two URLs: one for the API, one for the web UI. Use the web UI URL on any computer or phone.

---

## What you need

- A **GitHub** account (you already have the repo).
- A **Render** account (free): https://render.com → Sign up (e.g. with GitHub).

---

## Step 1 – Push your code to GitHub

Make sure the latest code (including `render.yaml`, `web/app.py` with `FLORISOFT_API_URL`, and this file) is on GitHub:

```powershell
git add .
git commit -m "Add deployment for Render"
git push origin main
```

---

## Step 2 – Create the API service on Render

1. Go to **https://dashboard.render.com** and log in.
2. Click **New +** → **Web Service**.
3. Connect your GitHub account if needed, then select the **florisoft3.0** repository.
4. Configure the **first** service (this will be the **API**):
   - **Name:** `florisoft-api` (or any name you like).
   - **Region:** choose one close to you.
   - **Branch:** `main`.
   - **Runtime:** `Python 3`.
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Leave **Plan** as **Free**.
6. Click **Create Web Service**. Wait until the first deploy finishes (a few minutes).
7. Copy the service URL (e.g. `https://florisoft-api.onrender.com`). You need it for the next step.

---

## Step 3 – Create the Streamlit (web) service on Render

1. In Render dashboard, click **New +** → **Web Service** again.
2. Select the same repo **florisoft3.0**.
3. Configure the **second** service (this will be the **web UI**):
   - **Name:** `florisoft-web`.
   - **Branch:** `main`.
   - **Runtime:** `Python 3`.
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run web/app.py --server.port $PORT --server.address 0.0.0.0`
4. Open **Environment** (or **Environment Variables**).
   - Add:
     - **Key:** `FLORISOFT_API_URL`
     - **Value:** your API URL from Step 2, e.g. `https://florisoft-api.onrender.com`  
     (No slash at the end.)
5. Plan: **Free**. Click **Create Web Service** and wait for the deploy to finish.
6. Copy the **web** service URL (e.g. `https://florisoft-web.onrender.com`). This is the link you use from any computer or phone.

---

## Step 4 – Use the app from anywhere

- Open the **web** URL (e.g. `https://florisoft-web.onrender.com`) in a browser on any device.
- Your PC can be off; the app runs on Render’s servers.

**Note (free tier):** On Render’s free plan, a service may “spin down” after some idle time. The first request after that can take 30–60 seconds to wake up. After that it’s fast until it goes idle again.

---

## Optional: Deploy with one click (Blueprint)

If Render supports **Blueprint** for your account:

1. In Render dashboard: **New +** → **Blueprint**.
2. Connect the repo and select **florisoft3.0**.
3. Render will read `render.yaml` and create both services. After the first deploy:
   - Open the **florisoft-web** service → **Environment**.
   - Set `FLORISOFT_API_URL` to your **florisoft-api** URL (e.g. `https://florisoft-api.onrender.com`).
   - Redeploy the web service so it uses the API.

---

## Summary

| What        | URL / Command |
|------------|----------------|
| API (backend) | `https://florisoft-api.onrender.com` (or the URL Render gives you) |
| Web UI (Streamlit) | `https://florisoft-web.onrender.com` (or the URL Render gives you) – **use this from other computers** |
| Local run  | `.\run_web.ps1` (only when your PC is on) |

Your app is then available from any computer or phone, without your local machine turned on.
