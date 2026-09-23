# Agent Routing & Dynamic Skill Resolution

This document details the dynamic routing pipeline used by the Tech Lead to decompose user tasks, resolve relevant skills, and delegate subtasks to specialized agents.

---

## 1. Dynamic Resolution Pipeline

```text
[Repository Metadata: *.csproj, packages.config, global.json]
                         ↓
             [Project Profiler Agent]
                         ↓
               .project-context.json
                         ↓
               [Skill Resolver Engine]
                         ↓
[Matched Skills] (e.g. legacy-safety-guard + csharp-idioms [C# 7.3])
                         ↓
              [Tech Lead / Orchestrator]
                         ↓
     [Task Dependency Graph & Specialist Delegation]
```

---

## 2. Technology Pack Resolution Table

The table below defines how detected repository characteristics map to active skills and future Technology Packs:

| Detected Repository Features | Active Core Skills | Future Technology Pack Target |
| :--- | :--- | :--- |
| **.NET Framework 4.x + MVC 5 + EF6** | `legacy-safety-guard`, `csharp-idioms`, `sql-safety`, `ef-diagnostics` | `legacy-dotnet-framework`, `mvc5`, `ef6` |
| **.NET 8/10 + ASP.NET Core + EF Core** | `csharp-idioms`, `ef-diagnostics`, `error-handling-result`, `test-pyramid` | `modern-dotnet`, `aspnet-core`, `ef-core` |
| **ABP Framework + ASP.NET Core** | `clean-boundaries`, `ef-diagnostics`, `secure-by-default` | `modern-dotnet`, `abp-framework`, `ef-core` |
| **ASP.NET Core + Dapper** | `sql-safety`, `csharp-idioms`, `test-pyramid` | `modern-dotnet`, `dapper`, `sql-server` |
| **Mixed Legacy (.NET 4.7.2 WCF + .NET 8)** | `legacy-safety-guard`, `incremental-upgrade`, `csharp-idioms` | `legacy-dotnet-framework`, `modern-dotnet` |

---

## 3. Subagent Execution Rules

### A. Independent Tasks (Parallelizable)
When subtasks have no data dependencies or ordering constraints, the Tech Lead can spawn them in parallel:
- **Investigation & Discovery**: Architecture analysis (`architect`) + Database audit (`database-engineer`) + Security audit (`security-engineer`).

### B. Dependent Tasks (Sequential Pipeline)
When subtasks rely on upstream outputs, execution must strictly follow dependency order:
$$\text{Architect (Plan)} \longrightarrow \text{.NET Engineer (Code)} \longrightarrow \text{Test Engineer (Test)} \longrightarrow \text{Code Reviewer (Review)}$$

---

## 4. Real-World Task Routing Scenarios (Scenarios A through H)

| Scenario | Objective | Detected Stack | Primary Agents | Active Skills | Execution Mode |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A. Add CRUD Endpoint** | Add REST endpoint | .NET 8 / ASP.NET Core | `dotnet-engineer` $\rightarrow$ `test-engineer` $\rightarrow$ `code-reviewer` | `csharp-idioms`, `test-pyramid` | Sequential |
| **B. Fix EF Tracking Issue** | Eliminate tracking bug | .NET 8 / EF Core | `database-engineer` $\rightarrow$ `test-engineer` $\rightarrow$ `code-reviewer` | `ef-diagnostics`, `evidence-first` | Sequential |
| **C. Fix Authentication Bug** | Resolve token validation flaw | Modern ASP.NET Core | `security-engineer` $\parallel$ `dotnet-engineer` $\rightarrow$ `test-engineer` $\rightarrow$ `code-reviewer` | `secure-by-default`, `secrets-audit` | Hybrid |
| **D. Optimize Slow SQL Query** | Eliminate slow query | SQL Server / Dapper | `database-engineer` $\parallel$ `performance-engineer` $\rightarrow$ `test-engineer` $\rightarrow$ `code-reviewer` | `sql-safety`, `allocation-profiling` | Hybrid |
| **E. Modernize MVC 5 App** | Staged .NET 8 upgrade | .NET 4.8 / MVC 5 | `legacy-analyst` $\rightarrow$ `migration-engineer` $\rightarrow$ `test-engineer` $\rightarrow$ `code-reviewer` | `legacy-safety-guard`, `incremental-upgrade` | Sequential |
| **F. Add ABP Permission** | Implement permission policy | ABP v9 / EF Core | `dotnet-engineer` $\rightarrow$ `test-engineer` $\rightarrow$ `code-reviewer` | `clean-boundaries`, `secure-by-default` | Sequential |
| **G. Investigate Legacy Repo** | Reverse-engineer system | .NET 4.7.2 / WCF | `legacy-analyst` $\parallel$ `project-profiler` $\rightarrow$ `tech-lead` | `legacy-discovery`, `evidence-first` | Parallel |
| **H. Perform Code Review** | Review pull request | Any .NET codebase | `code-reviewer` | `evidence-first`, `minimal-change` | Single Specialist |
