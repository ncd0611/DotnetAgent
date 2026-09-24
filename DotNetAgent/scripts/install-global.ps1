<#
.SYNOPSIS
    Installs the Universal .NET AI Core Team globally into ~/.gemini/config/.agents/
.DESCRIPTION
    Copies agents, skills, and rules from the core repository into the global
    Google Antigravity configuration directory, making them available to all projects.
#>
[CmdletBinding()]
param(
    [string]$GlobalConfigDir = [System.IO.Path]::Combine($env:USERPROFILE, ".gemini", "config")
)

$ErrorActionPreference = "Stop"

Write-Host "=== Universal .NET AI Core Team: Global Installer ===" -ForegroundColor Cyan
Write-Host "Target Directory: $GlobalConfigDir" -ForegroundColor Gray

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$SourceAgents = Join-Path $RepoRoot ".agents"

if (-not (Test-Path $SourceAgents)) {
    throw "Source .agents directory not found at $SourceAgents"
}

$DestAgents = Join-Path $GlobalConfigDir ".agents"
if (-not (Test-Path $GlobalConfigDir)) {
    New-Item -ItemType Directory -Path $GlobalConfigDir -Force | Out-Null
}
if (-not (Test-Path $DestAgents)) {
    New-Item -ItemType Directory -Path $DestAgents -Force | Out-Null
}

Write-Host "Copying core agents, skills, and rules to global roots..." -ForegroundColor Yellow
# 1. Copy directly into ~/.gemini/config/ (standard global discovery root)
Copy-Item -Path (Join-Path $SourceAgents "*") -Destination $GlobalConfigDir -Recurse -Force
# 2. Also preserve inside ~/.gemini/config/.agents/ for namespaced tools
Copy-Item -Path (Join-Path $SourceAgents "*") -Destination $DestAgents -Recurse -Force

Write-Host "Successfully installed Universal .NET AI Core Team to $GlobalConfigDir" -ForegroundColor Green
Write-Host "Run 'scripts/doctor.ps1' to verify installation health." -ForegroundColor Cyan
