# Start FastAPI + Streamlit with one command.
# Double-click this file, or in PowerShell: .\run_web.ps1
# Close both terminal windows when you're done (or Ctrl+C in each).

$projectRoot = $PSScriptRoot
$venvActivate = Join-Path $projectRoot "venv\Scripts\Activate.ps1"

if (-not (Test-Path $venvActivate)) {
    Write-Host "Creating virtual environment first..."
    python -m venv venv
}

# Start FastAPI in a new window (leave it open)
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$projectRoot'; & '$venvActivate'; uvicorn backend.main:app --reload"

# Wait a moment so the API is up before Streamlit tries to connect
Start-Sleep -Seconds 2

# Start Streamlit in this window
Set-Location $projectRoot
& $venvActivate
Write-Host "Streamlit starting. When done, close this window and the other (FastAPI) window." -ForegroundColor Green
streamlit run web/app.py
