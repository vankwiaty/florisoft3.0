# Start Florisoft (Streamlit only). Double-click or: .\run_web.ps1
$projectRoot = $PSScriptRoot
$venvActivate = Join-Path $projectRoot "venv\Scripts\Activate.ps1"

if (-not (Test-Path $venvActivate)) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}
Set-Location $projectRoot
& $venvActivate
streamlit run web/app.py
