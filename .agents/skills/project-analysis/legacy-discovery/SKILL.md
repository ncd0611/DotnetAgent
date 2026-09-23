---
name: legacy-discovery
description: Reverse-engineers legacy or undocumented .NET solutions, mapping application entry points, static state, hidden couplings, database access, and architectural risks.
---

# Legacy Discovery Skill

## 1. When to Use
- When assigned to an unfamiliar legacy .NET Framework repository (e.g., .NET 4.5–4.8, MVC 5, WCF, Web Forms).
- When investigating undocumented business logic, hidden static state, or fragile dependencies prior to planning changes.
- When generating system maps for architecture or risk evaluation.

## 2. When NOT to Use
- In clean, well-documented modern .NET solutions where architecture and contracts are explicit.
- When performing routine localized bug fixes that do not touch legacy core subsystems.

## 3. Workflow & Procedure
1. **Entry Point Tracing**:
   - Inspect `Global.asax.cs` (`Application_Start`, `Application_BeginRequest`).
   - Check `Startup.cs` for OWIN middleware pipelines (`IAppBuilder`).
   - Identify HTTP Modules (`IHttpModule`) and HTTP Handlers (`IHttpHandler`) in `web.config`.
2. **Static State & Global Coupling Audit**:
   - Run `grep_search` for `HttpContext.Current`, `ThreadStatic`, `CallContext`, static collections (`static Dictionary`, `static List`).
   - Identify singleton service instances or ambient transaction scopes.
3. **Data Access & Schema Reverse-Engineering**:
   - Locate connection strings in `web.config` (`<connectionStrings>`).
   - Trace EF6 `DbContext` or `ObjectContext` definitions.
   - Search for inline ADO.NET (`SqlCommand`, `SqlDataReader`, `ExecuteReader`) or stored procedure references.
4. **Integration & Protocol Mapping**:
   - Identify WCF service contracts (`[ServiceContract]`, `.svc` files) and ASMX web services.
   - Trace external HTTP clients or remoting endpoints.
5. **Artifact Generation**:
   - Write architectural, database, dependency, and risk maps into `docs/maps/`.

## 4. Decision Guidance
- If `HttpContext.Current` is pervasive: Warn the team that refactoring to `async/await` will cause `NullReferenceException` when execution resumes on a different thread without `SynchronizationContext`.
- If static state is mutable without locks: Flag as high concurrency risk in `docs/maps/risk-map.md`.

## 5. Anti-Patterns
- **Modernization Lecturing**: Documenting how bad legacy patterns are instead of objectively explaining what they do.
- **Speculative Rewriting**: Modifying legacy code during discovery.

## 6. Verification Checklist
- [ ] Application entry points traced and documented.
- [ ] Mutable static state locations cataloged.
- [ ] Database access technologies and connection strings mapped.
- [ ] `docs/maps/architecture-map.md` and `docs/maps/risk-map.md` created.
