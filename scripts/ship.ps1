<#
.SYNOPSIS
    Commit pending changes and push to GitHub.
    Run this on the work machine when you want to ship code to personal.

.EXAMPLE
    scripts\ship.ps1
#>

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Push-Location $repoRoot

$pending = git status --porcelain 2>&1
if ($pending) {
    $date = Get-Date -Format "yyyy-MM-dd HH:mm"
    git add -A
    git commit -m "wip: $date"
}

git push github master
if ($LASTEXITCODE -ne 0) {
    Write-Error "Push failed. Check your PAT in the github remote URL (git remote -v)."
    exit 1
}

Write-Host "Pushed to GitHub. On personal machine run: git pull origin master"
Pop-Location
