# Changelog

All notable changes to the **Universal .NET AI Core Team for Google Antigravity** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-09-24

### Added
- **Core Agent Team (11 Specialized Roles)**:
  - `tech-lead`: Primary orchestrator, dependency planner, specialist delegator, quality gate keeper.
  - `project-profiler`: Authoritative technology stack detection from project metadata (`*.csproj`, `packages.config`, `global.json`, etc.). Read-only.
  - `architect`: System boundaries, inward dependency rules, architectural decision records (ADRs).
  - `dotnet-engineer`: Idiomatic C# implementation across runtime generations (C# 7.3 through C# 13).
  - `database-engineer`: EF Core, EF6, Dapper, SQL optimization, migrations, transaction boundaries.
  - `test-engineer`: Task-driven test pyramids (unit, integration, API, regression).
  - `security-engineer`: OWASP Top 10, AuthN/AuthZ, claims, CSRF, secrets, multi-tenant isolation.
  - `performance-engineer`: Empirical diagnostics (N+1 queries, allocations, async deadlocks, thread pool starvation).
  - `migration-engineer`: Incremental modernization (Maintenance != Migration, Migration != Rewrite).
  - `legacy-analyst`: Read-only reverse engineering for legacy/undocumented systems.
  - `code-reviewer`: Independent severity-tiered reviewer (P0-P3, BUG/RISK/IMPROVEMENT/STYLE).
- **Core Skill Architecture (10 Domains, 15 Skills)**:
  - `project-analysis`: `project-profiler`, `legacy-discovery`
  - `engineering`: `evidence-first`, `minimal-change`, `dependency-hygiene`
  - `architecture`: `clean-boundaries`, `adr-management`
  - `coding`: `csharp-idioms`, `error-handling-result`
  - `database`: `ef-diagnostics`, `sql-safety`
  - `testing`: `test-pyramid`, `regression-testing`
  - `security`: `secure-by-default`, `secrets-audit`
  - `performance`: `allocation-profiling`, `async-hygiene`
  - `migration`: `incremental-upgrade`
  - `legacy`: `legacy-safety-guard`
- **Core Engineering Rules (17 Rules)**:
  - Enforcing Evidence First, Minimal Change, Legacy Safety, Version Awareness, Reversibility, and Review Standards.
  - Conflict precedence: Project > Framework > Technology > General.
- **Dynamic Technology Resolution Pipeline**:
  - Project Profiler $\rightarrow$ Technology Detection $\rightarrow$ Version Detection $\rightarrow$ Skill Resolution $\rightarrow$ Core Agent $\rightarrow$ Task Execution.
  - Extensible interface design for future Technology Packs (`modern-dotnet`, `aspnet-core`, `ef-core`, `sql-server`, `legacy-dotnet-framework`, `mvc5`, `ef6`, `abp`).
- **Tool Permission Matrix**:
  - Strict least privilege per role (read-only discovery, bounded write implementation, diff-only review).
- **Standard Agent Handoff Protocol**:
  - Machine-readable structured Markdown contract (`STATUS`, `SUMMARY`, `FINDINGS`, `FILES_INSPECTED`, `CHANGES`, `TESTS`, `RISKS`, `DECISIONS`, `RECOMMENDATION`, `NEXT_AGENT`).
- **Automated Validation Suite**:
  - `scripts/validate.py`: Automated syntax, YAML frontmatter, reference, permission boundary, and prompt size validation.
  - `scripts/profile-project.py`: Standalone CLI profiling engine.
  - `scripts/doctor.ps1`: Environment and installation health checker.
- **6 Representative Test Fixtures**:
  - Fixture 1: .NET Framework 4.8 + ASP.NET MVC 5 + EF6 (`web.config`, `packages.config`).
  - Fixture 2: .NET 8 + ASP.NET Core Web API + EF Core.
  - Fixture 3: .NET 10 + Modern C# 13 + Native AOT.
  - Fixture 4: ABP Framework v9.x + ASP.NET Core + EF Core.
  - Fixture 5: ASP.NET Core + Dapper + SQL Server.
  - Fixture 6: Mixed Legacy Solution (.NET 4.7.2 WCF + .NET Standard 2.0 + .NET 8).
- **Task Routing Test Suite**:
  - Scenarios A through H validated against expected profiling results, specialist selection, and execution orders.
