<#
.SYNOPSIS
    Create or update the Python virtual environment for WeatherBot.
    Run this once on any machine after cloning or receiving a bundle.
.EXAMPLE
    scripts\setup_venv.ps1
#>

$repoRoot = Join-Path $PSScriptRoot ".."
$venvPath = Join-Path $repoRoot ".venv"
$requirements = Join-Path $repoRoot "requirements.txt"

# Create venv if it doesn't exist
if (-not (Test-Path $venvPath)) {
    Write-Host "Creating virtual environment at .venv ..."
    python -m venv $venvPath
    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to create venv. Is Python installed and on PATH?"
        exit 1
    }
    Write-Host "Virtual environment created."
} else {
    Write-Host "Virtual environment already exists."
}

# Install / upgrade requirements
$pip = Join-Path $venvPath "Scripts\pip.exe"
Write-Host "Installing requirements..."
& $pip install --upgrade pip --quiet
& $pip install -r $requirements

if ($LASTEXITCODE -ne 0) {
    Write-Error "pip install failed."
    exit 1
}

Write-Host ""
Write-Host "Done. To activate the venv in this terminal:"
Write-Host "  .venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "To run the bot:  python main.py"
Write-Host "To dry-run:      python main.py probe"
