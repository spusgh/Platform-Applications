# Run Thoughtful AI Support Agent

Write-Host "Starting Thoughtful AI Support Agent..." -ForegroundColor Cyan

if (!(Test-Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv .venv
}

Write-Host "Activating virtual environment..." -ForegroundColor Yellow
. .\.venv\Scripts\Activate.ps1
Write-Host "Installing dependencies into the virtual environment..." -ForegroundColor Yellow
# Use the venv's python executable explicitly to ensure packages are installed into the venv
$python = Join-Path (Get-Location) ".venv\Scripts\python.exe"
if (-Not (Test-Path $python)) {
    Write-Host "ERROR: Virtual environment python not found at $python" -ForegroundColor Red
    exit 1
}

& $python -m pip install --upgrade pip
& $python -m pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to install dependencies into virtual environment." -ForegroundColor Red
    exit 1
}

Write-Host "Launching Streamlit using virtual environment python..." -ForegroundColor Yellow
& $python -m streamlit run app.py
