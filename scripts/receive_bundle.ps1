<#
.SYNOPSIS
    Apply a WeatherBot code bundle received from the work machine.
    Run this on the PERSONAL machine after downloading the bundle from Gmail.

.DESCRIPTION
    1. Auto-detects the latest WeatherBot_CODE_*.bundle in your Downloads folder,
       or use -BundlePath to specify one explicitly.
    2. Verifies bundle integrity.
    3. Pulls the new commits into the local repo (master branch).
    4. Pushes updated code to GitHub.
    5. Reinstalls Python requirements if requirements.txt changed.

.PARAMETER BundlePath
    Full path to the .bundle file. Optional -- auto-detects from Downloads if omitted.

.EXAMPLE
    scripts\receive_bundle.ps1
    scripts\receive_bundle.ps1 -BundlePath "C:\Users\you\Downloads\WeatherBot_CODE_20260428_1430.bundle"
#>

param(
    [string]$BundlePath = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

# --- Auto-detect bundle from Downloads ---
if (-not $BundlePath) {
    $downloads = Join-Path $env:USERPROFILE "Downloads"
    $bundles = Get-ChildItem $downloads -Filter "WeatherBot_CODE_*.bundle" -ErrorAction SilentlyContinue |
               Sort-Object LastWriteTime -Descending
    if (-not $bundles) {
        Write-Error "No WeatherBot_CODE_*.bundle found in $downloads`nSpecify path: scripts\receive_bundle.ps1 -BundlePath C:\path\to\file.bundle"
        exit 1
    }
    $BundlePath = $bundles[0].FullName
    Write-Host "Auto-detected bundle: $(Split-Path $BundlePath -Leaf)"
}

if (-not (Test-Path $BundlePath)) {
    Write-Error "Bundle file not found: $BundlePath"
    exit 1
}

# --- Verify bundle integrity ---
Write-Host "Verifying bundle..."
$verify = git -C $repoRoot bundle verify $BundlePath 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "Bundle verification failed:`n$verify"
    exit 1
}
Write-Host "Bundle OK."

# --- Get current HEAD to detect what changed ---
$headBefore = git -C $repoRoot rev-parse HEAD 2>$null

# --- Pull from bundle ---
Write-Host "Applying bundle to master..."
git -C $repoRoot pull $BundlePath master
if ($LASTEXITCODE -ne 0) {
    Write-Error "git pull failed. If there are conflicts, resolve them and try again."
    exit 1
}

# --- Push to GitHub ---
Write-Host "Pushing to GitHub..."
git -C $repoRoot push origin master
if ($LASTEXITCODE -ne 0) {
    Write-Warning "GitHub push failed (network issue? check git push manually)."
}

# --- Reinstall requirements if changed ---
$reqChanged = git -C $repoRoot diff "${headBefore}..HEAD" --name-only 2>$null |
              Where-Object { $_ -eq "requirements.txt" }
if ($reqChanged) {
    Write-Host "requirements.txt changed -- updating venv..."
    $pip = Join-Path $repoRoot ".venv\Scripts\pip.exe"
    if (Test-Path $pip) {
        & $pip install -r (Join-Path $repoRoot "requirements.txt")
    } else {
        Write-Warning "No .venv found. Run: scripts\setup_venv.ps1"
    }
}

# --- Untrack config.json if the new .gitignore excludes it ---
$configTracked = git -C $repoRoot ls-files "config.json" 2>$null
if ($configTracked) {
    Write-Host "Untracking config.json (now gitignored)..."
    git -C $repoRoot rm --cached config.json 2>$null
    git -C $repoRoot commit -m "chore: untrack config.json (now gitignored)" 2>$null
}

Write-Host ""
Write-Host "Done. Code is up to date."
Write-Host "Start the bot: python main.py"
