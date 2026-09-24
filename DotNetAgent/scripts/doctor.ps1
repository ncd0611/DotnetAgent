<#
.SYNOPSIS
    Health and configuration doctor for Universal .NET AI Core Team in Antigravity.
.DESCRIPTION
    Validates that agents, skills, and rules are intact, and checks runtime dependencies.
#>
[CmdletBinding()]
param()

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$AgentsDir = Join-Path $RepoRoot ".agents"

Write-Host "=== Antigravity Core Team Doctor ===" -ForegroundColor Cyan
Write-Host "Checking repository root: $RepoRoot" -ForegroundColor Gray

$allGood = $true

# 1. Check .agents directory
if (Test-Path $AgentsDir) {
    Write-Host "[OK] .agents directory exists" -ForegroundColor Green
} else {
    Write-Host "[FAIL] Missing .agents directory" -ForegroundColor Red
    $allGood = $false
}

# 2. Check Agents count (Must have 11)
$agents = Get-ChildItem -Path (Join-Path $AgentsDir "agents") -Directory -ErrorAction SilentlyContinue
$expectedAgents = @("tech-lead", "project-profiler", "architect", "dotnet-engineer", "database-engineer", "test-engineer", "security-engineer", "performance-engineer", "migration-engineer", "legacy-analyst", "code-reviewer")
$foundCount = 0
foreach ($agentName in $expectedAgents) {
    $agentPath = Join-Path $AgentsDir "agents\$agentName\agent.md"
    if (Test-Path $agentPath) {
        $foundCount++
    } else {
        Write-Host "[FAIL] Missing agent definition: $agentName" -ForegroundColor Red
        $allGood = $false
    }
}
Write-Host "[OK] Core Agents: $foundCount / 11 discovered" -ForegroundColor Green

# 3. Check Skills count
$skills = Get-ChildItem -Path (Join-Path $AgentsDir "skills") -Recurse -Filter "SKILL.md" -ErrorAction SilentlyContinue
Write-Host "[OK] Discovered $($skills.Count) Core Skills" -ForegroundColor Green

# 4. Check Rules count
$rules = Get-ChildItem -Path (Join-Path $AgentsDir "rules") -Filter "*.md" -ErrorAction SilentlyContinue
Write-Host "[OK] Discovered $($rules.Count) Engineering Rules" -ForegroundColor Green

# 5. Check Python for validation
try {
    $pyVer = python --version 2>&1
    Write-Host "[OK] Python installed: $pyVer" -ForegroundColor Green
} catch {
    Write-Host "[WARN] Python not found in PATH (needed for automated validation)" -ForegroundColor Yellow
}

# 6. Check .NET SDK
try {
    $dotnetVer = dotnet --version 2>&1
    Write-Host "[OK] .NET SDK installed: $dotnetVer" -ForegroundColor Green
} catch {
    Write-Host "[WARN] .NET SDK not detected in PATH" -ForegroundColor Yellow
}

Write-Host "--------------------------------------------------" -ForegroundColor Gray
if ($allGood) {
    Write-Host "All Core Team components are healthy and operational!" -ForegroundColor Green
} else {
    Write-Host "Doctor detected issues. Please review failures above." -ForegroundColor Red
}
