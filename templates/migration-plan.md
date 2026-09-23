# Migration Plan: {{PROJECT_NAME}}

- **Source Target**: `{{SOURCE_TARGET}}` (e.g. .NET Framework 4.8 / MVC 5 / EF6)
- **Destination Target**: `{{DESTINATION_TARGET}}` (e.g. .NET 8 / ASP.NET Core / EF Core)
- **Lead Specialist**: `migration-engineer`
- **Date**: `{{DATE}}`

---

## 1. Migration Philosophy
**Migration $\ne$ Rewrite**: Modernize infrastructure and runtime platforms incrementally while preserving functional business logic and external API contracts.

## 2. Inventory & Compatibility Assessment
### A. Incompatible Dependencies
- `{{DEPENDENCY_1}}` $\rightarrow$ Replacement: `{{REPLACEMENT_1}}`

### B. Incompatible APIs Detected
- `System.Web.HttpContext` $\rightarrow$ Replace with `Microsoft.AspNetCore.Http.IHttpContextAccessor`
- `ConfigurationManager.AppSettings` $\rightarrow$ Replace with `IConfiguration`

## 3. Staged Execution Milestones

### Milestone 1: Shared Library Dual-Targeting
- Target shared class libraries with `<TargetFrameworks>netstandard2.0;net48;net8.0</TargetFrameworks>`.
- Convert project files to modern SDK style.

### Milestone 2: Data Access Modernization
- Transition EF6 contexts to EF Core or dual-target data mappings.
- Validate database schema parity between EF6 and EF Core models.

### Milestone 3: Web Host Modernization (Strangler Fig)
- Deploy modern ASP.NET Core web host in parallel.
- Route endpoints incrementally via YARP reverse proxy.

### Milestone 4: Verification & Cutover
- Execute complete regression test suite.
- Validate telemetry and decommission legacy IIS instance.
