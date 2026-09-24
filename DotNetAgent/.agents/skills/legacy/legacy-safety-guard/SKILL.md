---
name: legacy-safety-guard
description: Protects legacy .NET Framework repositories from accidental or unsolicited modernization, enforcing the core rule that Maintenance does not equal Migration.
---

# Legacy Safety Guard Skill

## 1. When to Use
- When operating in any .NET Framework (2.0–4.8.1), ASP.NET MVC 5, Web API 2, WCF, or EF6 codebase.
- Whenever tempted to introduce modern C# syntax, async/await everywhere, or dependency injection into legacy systems.

## 2. When NOT to Use
- When the user explicitly commands a migration project (in which case, activate `migration/incremental-upgrade`).
- In modern .NET 8/10 projects.

## 3. The Prime Invariant: Maintenance $\ne$ Migration
When performing maintenance, bug fixes, or minor feature enhancements on legacy .NET Framework systems, **NEVER** perform accidental modernization:

| Legacy Component | FORBIDDEN Unsolicited Action | REQUIRED Maintenance Action |
| :--- | :--- | :--- |
| **.NET Framework 4.x** | Bumping target to .NET 8 or modern .NET | Maintain existing `TargetFrameworkVersion` (e.g. `v4.8`) |
| **`web.config`** | Deleting or replacing with `appsettings.json` | Keep `web.config` as the source of configuration |
| **`packages.config`** | Converting all packages to `<PackageReference>` | Preserve `packages.config` and binding redirects |
| **ASP.NET MVC 5 / Web API 2** | Migrating to ASP.NET Core Controllers | Write standard MVC 5 `ActionResult` or Web API 2 `IHttpActionResult` |
| **Synchronous Actions** | Converting everything to `async/await` | Keep existing synchronous methods unless I/O performance requires it |
| **Entity Framework 6** | Replacing with EF Core | Use standard EF6 patterns (`DbContext`, `DbSet<T>`) |
| **WCF / ASMX** | Replacing with gRPC or Minimal APIs | Maintain existing `[ServiceContract]` and SOAP/WSDL endpoints |
| **Static State** | Rewriting entire architecture to remove static state | Respect static state and ensure thread safety via synchronization |

## 4. Why This Invariant Exists
Legacy systems are production-critical applications with years of accumulated, often undocumented, edge cases, timing assumptions, and IIS pipeline behaviors. 
Converting synchronous MVC 5 actions to `async` can lead to deadlocks due to ASP.NET's `SynchronizationContext`, while removing `web.config` breaks IIS handlers, modules, and security filters.

## 5. Anti-Patterns
- **The Modernizer's Crusade**: Refactoring a 15-year-old working enterprise app into Clean Architecture because "it's old".
- **Blind Async Conversions**: Adding `async Task<ActionResult>` and calling `.Result` inside a helper, creating deadlock traps.

## 6. Verification Checklist
- [ ] No unrequested target framework upgrades.
- [ ] `web.config` and `packages.config` preserved.
- [ ] Code compiles with legacy compiler without requiring modern C# runtime features.
- [ ] Existing architecture and conventions respected.
