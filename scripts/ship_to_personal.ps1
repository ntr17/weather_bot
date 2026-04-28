<#
.SYNOPSIS
    Bundle latest code commits and email them to the personal machine via Outlook.
    Run this on the WORK machine when you want to ship code changes.

.DESCRIPTION
    1. Commits any pending changes with a timestamp message.
    2. Creates a git bundle (incremental since last ship, or full if first time).
    3. Tags the commit as shipped_YYYYMMDD_HHMM.
    4. Sends the bundle as an email attachment via Outlook to PERSONAL_EMAIL.
    5. Cleans up the temp bundle file.

.PARAMETER Full
    Force a full bundle even if an incremental one could be made.
    Use this if the personal machine has diverged or on first use.

.NOTES
    - Requires Outlook desktop app to be open and logged in.
    - Reads PERSONAL_EMAIL from .env in the project root.

.EXAMPLE
    scripts\ship_to_personal.ps1
    scripts\ship_to_personal.ps1 -Full
#>

param(
    [switch]$Full
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# --- Resolve paths ---
$repoRoot  = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$envFile   = Join-Path $repoRoot ".env"

# --- Load .env ---
$personalEmail = $null
if (Test-Path $envFile) {
    Get-Content $envFile | ForEach-Object {
        if ($_ -match "^\s*PERSONAL_EMAIL\s*=\s*(.+?)\s*$") {
            $personalEmail = $Matches[1]
        }
    }
}
if (-not $personalEmail) {
    Write-Error "PERSONAL_EMAIL not set in .env`nAdd: PERSONAL_EMAIL=your.gmail@gmail.com"
    exit 1
}

# --- Navigate to repo ---
Push-Location $repoRoot

try {
    # --- Commit any pending changes ---
    $pending = git status --porcelain 2>&1
    if ($pending) {
        $ts = Get-Date -Format "yyyy-MM-dd HH:mm"
        git add -A
        git commit -m "ship: $ts"
        Write-Host "Committed pending changes."
    } else {
        Write-Host "Working tree clean -- bundling current HEAD."
    }

    # --- Determine bundle range ---
    $date = Get-Date -Format "yyyyMMdd_HHmm"
    $bundleFile = Join-Path $env:TEMP "WeatherBot_CODE_$date.bundle"

    $lastTag = git tag --list "shipped_*" 2>$null | Sort-Object -Descending | Select-Object -First 1

    if ($Full -or -not $lastTag) {
        Write-Host "Creating full bundle..."
        git bundle create $bundleFile master
    } else {
        Write-Host "Creating incremental bundle since $lastTag ..."
        git bundle create $bundleFile "${lastTag}..master" 2>&1
        # Fall back to full if incremental is empty (no new commits)
        $verify = git bundle verify $bundleFile 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "Incremental bundle empty or invalid -- falling back to full bundle."
            git bundle create $bundleFile master
        }
    }

    if (-not (Test-Path $bundleFile)) {
        Write-Error "Bundle file was not created."
        exit 1
    }

    $bundleSizeKB = [math]::Round((Get-Item $bundleFile).Length / 1KB, 1)
    Write-Host "Bundle: $(Split-Path $bundleFile -Leaf) ($bundleSizeKB KB)"

    # --- Tag this shipment ---
    git tag "shipped_$date"
    Write-Host "Tagged: shipped_$date"

    # --- Send via Outlook ---
    Write-Host "Sending via Outlook to $personalEmail ..."
    try {
        $Outlook = New-Object -ComObject Outlook.Application
    } catch {
        Write-Error "Could not launch Outlook COM. Ensure Outlook is installed and running."
        exit 1
    }

    $Mail = $Outlook.CreateItem(0)
    $Mail.To = $personalEmail
    $Mail.Subject = "[WeatherBot Code] $date"
    $Mail.HTMLBody = @"
<p><b>WeatherBot code bundle — $date</b></p>
<p>Apply on personal machine:</p>
<pre>scripts\receive_bundle.ps1</pre>
<p>Bundle: $(Split-Path $bundleFile -Leaf) ($bundleSizeKB KB)</p>
<p><i>This is an automated transfer email. Do not reply.</i></p>
"@
    $Mail.Attachments.Add($bundleFile) | Out-Null
    $Mail.Send()
    Write-Host "Email sent to $personalEmail"

} finally {
    Pop-Location
    # Clean up temp bundle
    if (Test-Path $bundleFile) { Remove-Item $bundleFile }
}

Write-Host ""
Write-Host "Done. Bundle shipped to personal machine."
