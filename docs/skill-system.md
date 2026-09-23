# Skill System & Progressive Disclosure

The Universal .NET AI Core Team implements the **Agent Skills open standard** (compatible with Antigravity, Anthropic, and Microsoft ecosystems). Skills serve as modular runbooks and domain-specific knowledge packages that extend agent capabilities on demand.

---

## 1. Directory Structure

Every skill is a self-contained directory under `.agents/skills/<category>/<skill-name>/`:

```text
skills/<category>/<skill-name>/
├── SKILL.md          # Required: Frontmatter + core workflow + checklist
├── references/       # Optional: Bulky technical manuals, API specs
└── scripts/          # Optional: Executable verification or scaffolding scripts
```

---

## 2. Progressive Disclosure Mechanics

To ensure context windows remain uncluttered and token-efficient:

1. **Discovery (Metadata Only)**:
   - At startup, the agent context is injected ONLY with the skill's YAML frontmatter:
     ```yaml
     ---
     name: ef-diagnostics
     description: Diagnoses and resolves Entity Framework Core and EF6 query performance issues...
     ---
     ```
   - No body text, checklists, or scripts are loaded into initial context.
2. **Decision & Activation**:
   - When the agent (or Tech Lead) determines that a subtask requires the skill based on its description, the agent executes `view_file` on `SKILL.md`.
3. **Reference Fetching**:
   - If the task requires deep domain specs, the agent follows relative markdown links to `references/*.md` on demand.

---

## 3. Core Skill Taxonomy (15 Skills)

| Domain | Skill Name | Scope |
| :--- | :--- | :--- |
| **Project Analysis** | `project-profiler` | Metadata scanning & `.project-context.json` generation |
| | `legacy-discovery` | Reverse-engineering entry points, static state, risk maps |
| **Engineering** | `evidence-first` | Empirical verification before code modification |
| | `minimal-change` | Surgical diffs, formatting preservation, reversibility |
| | `dependency-hygiene`| NuGet version alignment, CPM, binding redirect safety |
| **Architecture** | `clean-boundaries` | Inward dependency direction, domain isolation |
| | `adr-management` | Architecture Decision Record authoring |
| **Coding** | `csharp-idioms` | Version-aware C# syntax (C# 7.3 through C# 13) |
| | `error-handling-result`| Result pattern for expected domain failures |
| **Database** | `ef-diagnostics` | AsNoTracking, AsSplitQuery, N+1 query elimination |
| | `sql-safety` | Absolute SQL parameterization, transaction isolation |
| **Testing** | `test-pyramid` | Task-driven test selection (unit, integration, API) |
| | `regression-testing` | Reproduce bug before fix, verify fix after |
| **Security** | `secure-by-default` | Authorization boundaries, CSRF, path traversal |
| | `secrets-audit` | Hardcoded credential detection, sensitive logging guards |
| **Performance** | `allocation-profiling`| Heap allocations, boxing, string manipulation, LOH |
| | `async-hygiene` | Sync-over-async deadlock prevention, thread pool hygiene |
| **Migration** | `incremental-upgrade`| Staged modernization (Migration != Rewrite) |
| **Legacy** | `legacy-safety-guard`| Maintenance != Migration, web.config & WCF protection |
