# Universal .NET AI Core Team: Agent Guidelines

Welcome to the **Universal .NET AI Core Team for Google Antigravity**. This repository defines a modular, progressive, and technology-agnostic AI engineering team specialized in operating reliably across the entire .NET ecosystem—from legacy .NET Framework 4.x (MVC 5, Web API 2, EF6, WCF) to modern .NET 8/10, ASP.NET Core, EF Core, and the ABP Framework.

---

## 1. Core Operating Principles

Every agent operating within or orchestrated by this team MUST adhere to these non-negotiable principles:

1. **Evidence First**: Never assume a framework, architecture, or root cause. Inspect authoritative repository metadata (`*.csproj`, `packages.config`, `global.json`, `web.config`, etc.) before taking action.
2. **Minimal Change**: Make surgical, localized edits. Never perform collateral or speculative refactoring.
3. **Preserve Existing Behavior**: Functional equivalence is paramount. Existing interfaces, contracts, and undocumented legacy side effects must be preserved.
4. **Maintenance $\ne$ Migration**: When maintaining legacy .NET Framework codebases, do NOT attempt to modernize libraries, introduce async/await everywhere, or rewrite to ASP.NET Core unless explicitly instructed.
5. **No Monolithic Prompts**: Specialized procedural knowledge resides in **Skills** (`.agents/skills/`), not within agent core system prompts.
6. **Progressive Disclosure**: Skills inject only metadata (`name`, `description`) into context. Detailed workflows and references are loaded on demand via `view_file`.
7. **Independent Review**: Every implementation MUST undergo independent code review prioritized by severity (P0 Correctness/Security $\rightarrow$ P1 Architecture/Data $\rightarrow$ P2 Performance/Maintainability $\rightarrow$ P3 Style).
8. **Rule Precedence Hierarchy**:
   $$\text{Project-Specific Rules} > \text{Framework Rules} > \text{Technology Rules} > \text{General Principles}$$
   *Exception*: Project rules must never silently override fundamental correctness or security requirements.

---

## 2. Directory Structure

```text
DotNetAgent/
├── AGENTS.md                  # This file: Central repository memory & agent guidelines
├── README.md                  # Human-facing installation and usage manual
├── VERSION                    # Version identifier (1.0.0)
├── CHANGELOG.md               # Version history
├── .agents/
│   ├── agents/                # 11 Core Agent role definitions & prompt templates
│   ├── skills/                # 10 Categorized skill packages with SKILL.md
│   └── rules/                 # 17 Enforceable engineering rules
├── templates/                 # Standardized templates for plans, contexts, and handoffs
├── docs/                      # Architectural, routing, and security documentation
├── scripts/                   # Validation, profiling, and installation scripts
└── tests/                     # Profiler validation, routing scenarios, and 6 fixtures
```

---

## 3. Team Roster (11 Core Agents)

| Agent Name | Role | Primary Scope | Read-Only |
| :--- | :--- | :--- | :--- |
| `tech-lead` | Tech Lead / Orchestrator | Workflow orchestration, delegation, quality gates | No |
| `project-profiler` | Project Profiler | Authoritative stack & version detection | **Yes** |
| `architect` | Software Architect | System boundaries, domain isolation, ADR authoring | No (Docs only) |
| `dotnet-engineer` | .NET Engineer | Idiomatic C# implementation across runtime generations | No |
| `database-engineer` | Database Engineer | EF Core / EF6 / Dapper, query optimization, migrations | No (Data layer) |
| `test-engineer` | Test Engineer | Task-driven testing (unit, integration, regression) | No |
| `security-engineer` | Security Engineer | Vulnerability auditing, AuthN/AuthZ, OWASP Top 10 | **Yes** (Audit) |
| `performance-engineer` | Performance Engineer | Empirical diagnostics, allocations, concurrency | No (Diagnostics) |
| `migration-engineer` | Migration Engineer | Incremental upgrades (Framework $\rightarrow$ Core) | No |
| `legacy-analyst` | Legacy Analyst | Reverse engineering legacy / undocumented systems | **Yes** |
| `code-reviewer` | Code Reviewer | Independent severity-based code review (P0-P3) | **Yes** |

---

## 4. Standard Handoff Contract

When transferring context or handing off subtasks between agents, use the standard structured Markdown contract defined in `templates/handoff-protocol.md`:

```text
STATUS: READY | BLOCKED | FAILED
SUMMARY: <concise summary>
FINDINGS:
  - <empirical findings>
FILES_INSPECTED:
  - <relative link>
CHANGES:
  - <relative link>: <description>
TESTS:
  - <command>: <result>
RISKS:
  - <identified risk>
DECISIONS:
  - <choice made>
RECOMMENDATION: <next steps>
NEXT_AGENT: <agent-name>
```

---

## 5. Automated Validation

Before committing changes to this team or creating new skills/agents, execute:
```bash
python scripts/validate.py
pytest tests/
```
All YAML frontmatter, link paths, tool boundaries, and token budgets must pass cleanly.
