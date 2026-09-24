# Implementation Plan: {{TASK_TITLE}}

**Author**: Tech Lead / Orchestrator
**Context**: [`.project-context.json`](file:///.project-context.json)
**Date**: `{{DATE}}`

---

## 1. Problem Statement & Objective
{{OBJECTIVE_SUMMARY}}

## 2. Evidence & Discovery Findings
- **Stack Verified**: `{{DETECTED_STACK}}`
- **Root Cause / Code Locations**:
  - `{{FILE_LOCATION_1}}`

## 3. Phased Execution Plan

### Phase 1: Architecture & Structural Blueprint
- **Assigned Agent**: `architect`
- **Scope**: Define interfaces, contracts, or boundary rules.
- **Output Artifact**: Architecture proposal or ADR.

### Phase 2: Implementation
- **Assigned Agent**: `dotnet-engineer` (and/or `database-engineer`)
- **Scope**: Surgical code changes adhering to `minimal-change` and detected C# version.
- **Expected Diffs**:
  - `[MODIFY]` `{{TARGET_FILE_1}}`

### Phase 3: Testing & Behavioral Verification
- **Assigned Agent**: `test-engineer`
- **Strategy**: Unit / Integration / API tests validating observable outcomes.
- **Verification Command**: `dotnet test --filter {{FILTER}}`

### Phase 4: Independent Code Review
- **Assigned Agent**: `code-reviewer`
- **Gate**: Zero P0/P1 defects permitted before completion.

## 4. Risks & Mitigations
- **Risk 1**: `{{RISK_DESCRIPTION}}` $\rightarrow$ **Mitigation**: `{{MITIGATION_STRATEGY}}`
