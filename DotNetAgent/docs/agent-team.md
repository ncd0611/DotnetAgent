# Core Agent Team Specification

The Universal .NET AI Core Team consists of **11 specialized agents**, organized into three functional tiers:

```mermaid
graph TD
    subgraph Tier 1: Leadership & Discovery
        TL[tech-lead]
        PP[project-profiler]
        LA[legacy-analyst]
    end

    subgraph Tier 2: Architecture & Implementation
        SA[architect]
        DNE[dotnet-engineer]
        DBE[database-engineer]
        ME[migration-engineer]
    end

    subgraph Tier 3: Quality, Security & Performance
        TE[test-engineer]
        SE[security-engineer]
        PE[performance-engineer]
        CR[code-reviewer]
    end

    TL --> PP
    TL --> LA
    TL --> SA
    TL --> DNE
    TL --> DBE
    TL --> ME
    TL --> TE
    TL --> SE
    TL --> PE
    TL --> CR
```

---

## Agent Deep Dives

### 1. `tech-lead` (Tech Lead / Orchestrator)
- **Mandate**: Workflow orchestration, dependency graph planning, delegation, quality gates.
- **Invariants**: Evidence First, Minimal Change, Zero Unsolicited Rewrites.
- **Tools**: `view_file`, `list_dir`, `grep_search`, `search_web`, `run_command`, `schedule`.

### 2. `project-profiler` (Project Profiler)
- **Mandate**: Authoritative repository stack and version detection from metadata files.
- **Invariants**: Strictly read-only, never guesses from folder names.
- **Tools**: `view_file`, `list_dir`, `grep_search`.

### 3. `architect` (Software Architect)
- **Mandate**: Inward dependency direction, domain isolation, ADR authoring.
- **Invariants**: Avoid Unnecessary Abstraction, Respect Existing Architecture.
- **Tools**: `view_file`, `list_dir`, `grep_search`, `search_web`, `write_to_file`, `replace_file_content` (docs only).

### 4. `dotnet-engineer` (.NET Engineer)
- **Mandate**: Idiomatic C# implementation tailored to detected runtime and language version.
- **Invariants**: Minimal Change, Preserve Existing Behavior, Detect Version Before Coding.
- **Tools**: All file editing tools, compilation commands.

### 5. `database-engineer` (Database Engineer)
- **Mandate**: Data persistence, EF Core/EF6/Dapper queries, migrations, SQL injection prevention.
- **Invariants**: No Performance Claim Without Evidence, Parameterized SQL Always.
- **Tools**: File editing tools (scoped to data access), database CLI tooling.

### 6. `test-engineer` (Test Engineer)
- **Mandate**: Task-driven test suite formulation and execution.
- **Invariants**: Test Important Behavior, Verify With Real Tooling.
- **Tools**: File editing tools (scoped to test projects), `dotnet test`.

### 7. `security-engineer` (Security Engineer)
- **Mandate**: Vulnerability auditing (OWASP Top 10), AuthN/AuthZ, secrets protection.
- **Invariants**: Secure by Default, Zero Speculation.
- **Tools**: Exploration tools, documentation authoring (docs only).

### 8. `performance-engineer` (Performance Engineer)
- **Mandate**: Empirical bottleneck diagnosis (memory, allocations, N+1 queries, async deadlocks).
- **Invariants**: No Performance Claim Without Evidence.
- **Tools**: Exploration tools, benchmarking / diagnostic commands.

### 9. `migration-engineer` (Migration Engineer)
- **Mandate**: Staged incremental modernization from legacy .NET Framework to modern .NET.
- **Invariants**: Migration != Rewrite, Strangler Fig increments.
- **Tools**: File editing tools, build and migration tooling.

### 10. `legacy-analyst` (Legacy Analyst)
- **Mandate**: Reverse-engineering legacy, complex, or undocumented systems.
- **Invariants**: Strictly read-only during discovery, Preserve Existing Behavior.
- **Tools**: `view_file`, `list_dir`, `grep_search`.

### 11. `code-reviewer` (Code Reviewer)
- **Mandate**: Independent severity-based review (P0-P3, BUG/RISK/IMPROVEMENT/STYLE).
- **Invariants**: Zero Subjective Preference Nitpicking, Non-Mutating.
- **Tools**: Exploration and diff tools, test runner, review report authoring.
