<#
.SYNOPSIS
    Search Outlook inbox for the latest WeatherBot data email from personal machine,
    download the zip attachment, and extract it into the local data/ folder.

.DESCRIPTION
    Run this on the WORK machine after the personal machine has sent data back.
    Looks for the most recent email with "[WeatherBot Data]" in the subject.
    Extracts the zip contents into data/, overwriting existing files.

.NOTES
    - Requires Outlook desktop app to be open and logged in.
    - Marks the email as read after processing.

.EXAMPLE
    scripts\receive_from_personal.ps1
#>

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.IO.Compression.FileSystem

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$dataDir  = Join-Path $repoRoot "data"

# --- Connect to Outlook ---
Write-Host "Connecting to Outlook..."
try {
    $Outlook   = New-Object -ComObject Outlook.Application
    $Namespace = $Outlook.GetNamespace("MAPI")
    $Inbox     = $Namespace.GetDefaultFolder(6)   # 6 = olFolderInbox
} catch {
    Write-Error "Could not connect to Outlook. Ensure Outlook is open and logged in."
    exit 1
}

# --- Find latest [WeatherBot Data] email ---
$matches = @()
foreach ($item in $Inbox.Items) {
    if ($item.Subject -like "*WeatherBot Data*") {
        $matches += $item
    }
}

if ($matches.Count -eq 0) {
    Write-Warning "No emails found with '[WeatherBot Data]' in the subject."
    Write-Warning "Make sure the personal machine sent data and Outlook is synced."
    exit 1
}

$latest = $matches | Sort-Object ReceivedTime -Descending | Select-Object -First 1
Write-Host "Found: '$($latest.Subject)' received $($latest.ReceivedTime)"

# --- Get the zip attachment ---
$zipAtt = $null
foreach ($att in $latest.Attachments) {
    if ($att.FileName -like "*.zip") {
        $zipAtt = $att
        break
    }
}

if (-not $zipAtt) {
    Write-Error "No .zip attachment found in email '$($latest.Subject)'."
    exit 1
}

# --- Save attachment to temp ---
$tempZip = Join-Path $env:TEMP "WeatherBot_Data_incoming.zip"
$zipAtt.SaveAsFile($tempZip)
$zipSizeKB = [math]::Round((Get-Item $tempZip).Length / 1KB, 1)
Write-Host "Saved attachment: $($zipAtt.FileName) ($zipSizeKB KB)"

# --- Extract to data/ (overwrite) ---
if (-not (Test-Path $dataDir)) {
    New-Item -ItemType Directory -Path $dataDir | Out-Null
}

Write-Host "Extracting to $dataDir ..."
$zip = [System.IO.Compression.ZipFile]::OpenRead($tempZip)
try {
    foreach ($entry in $zip.Entries) {
        $destPath = Join-Path $dataDir $entry.FullName
        $destDir  = Split-Path $destPath -Parent
        if (-not (Test-Path $destDir)) {
            New-Item -ItemType Directory -Path $destDir | Out-Null
        }
        if ($entry.Name -ne "") {
            [System.IO.Compression.ZipFileExtensions]::ExtractToFile($entry, $destPath, $true)
        }
    }
} finally {
    $zip.Dispose()
}

Remove-Item $tempZip
Write-Host "Extracted successfully."

# --- Mark email as read ---
$latest.UnRead = $false
Write-Host ""
Write-Host "Done. Latest trade data is now in data/"
