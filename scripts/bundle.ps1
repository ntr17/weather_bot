<#
.SYNOPSIS
    Create a git bundle and open the folder so you can email it manually.

.EXAMPLE
    scripts\bundle.ps1
    Then attach the .bundle file to an email to your personal Gmail.
#>

$repoRoot  = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$date      = Get-Date -Format "yyyyMMdd_HHmm"
$bundleOut = Join-Path $env:USERPROFILE "Desktop\WeatherBot_$date.bundle"

Push-Location $repoRoot

# Commit anything pending
$pending = git status --porcelain 2>&1
if ($pending) {
    git add -A
    git commit -m "wip: $date"
}

git bundle create $bundleOut master
git tag "shipped_$date"

Pop-Location

$sizeKB = [math]::Round((Get-Item $bundleOut).Length / 1KB, 1)
Write-Host "Bundle ready on Desktop: WeatherBot_$date.bundle ($sizeKB KB)"
Write-Host "Attach it to an email to your personal Gmail."
Invoke-Item (Split-Path $bundleOut)
