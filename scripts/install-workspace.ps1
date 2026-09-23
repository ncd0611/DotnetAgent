<#
.SYNOPSIS
    Installs the Universal .NET AI Core Team locally into a target workspace repository.
.DESCRIPTION
    Installs .agents/ and AGENTS.md directly into the specified workspace root.
.PARAMETER TargetPath
    The absolute path to the target repository.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$TargetPath
)

$ErrorActionPreference = "Stop"

Write-Host "=== Universal .NET AI Core Team: Workspace Installer ===" -ForegroundColor Cyan
Write-Host "Target Workspace: $TargetPath" -ForegroundColor Gray

if (-not (Test-Path $TargetPath)) {
    throw "Target path '$TargetPath' does not exist."
}

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$SourceAgents = Join-Path $RepoRoot ".agents"
$SourceAgentsMd = Join-Path $RepoRoot "AGENTS.md"

$DestAgents = Join-Path $TargetPath ".agents"
$DestAgentsMd = Join-Path $TargetPath "AGENTS.md"

if (-not (Test-Path $DestAgents)) {
    New-Item -ItemType Directory -Path $DestAgents -Force | Out-Null
}

Write-Host "Installing .agents/ into target workspace..." -ForegroundColor Yellow
Copy-Item -Path (Join-Path $SourceAgents "*") -Destination $DestAgents -Recurse -Force

if (-not (Test-Path $DestAgentsMd)) {
    Write-Host "Installing AGENTS.md into workspace root..." -ForegroundColor Yellow
    Copy-Item -Path $SourceAgentsMd -Destination $DestAgentsMd -Force
} else {
    Write-Host "Workspace AGENTS.md already exists; preserving existing file." -ForegroundColor Gray
}

Write-Host "Successfully installed Universal .NET AI Core Team into $TargetPath" -ForegroundColor Green
