---
name: incremental-upgrade
description: Guides staged, incremental modernization of .NET Framework applications to modern .NET, EF6 to EF Core, and MVC 5 to ASP.NET Core while preventing monolithic rewrite failures.
---

# Incremental Upgrade & Modernization Skill

## 1. When to Use
- When executing planned modernization of legacy .NET Framework projects (e.g. .NET 4.8 to .NET 8/10).
- When migrating EF6 to EF Core or ASP.NET MVC 5 to ASP.NET Core.
- When multi-targeting libraries during a multi-phase migration.

## 2. When NOT to Use
- During routine maintenance of legacy applications where migration has NOT been explicitly requested.
- When building new greenfield applications.

## 3. The 7-Step Incremental Modernization Workflow
$$\text{Inventory} \longrightarrow \text{Compatibility Audit} \longrightarrow \text{Migration Plan} \longrightarrow \text{Shared Lib Migration} \longrightarrow \text{App Migration} \longrightarrow \text{Verification} \longrightarrow \text{Cutover}$$

1. **Step 1: Inventory & Dependency Analysis**:
   - Audit all NuGet packages and third-party binaries in `packages.config` or `.csproj`.
   - Identify obsolete or discontinued packages; find modern replacements before editing code.
2. **Step 2: Compatibility Audit**:
   - Check usage of non-portable .NET Framework APIs: `System.Web`, `AppDomain`, `Remoting`, `WCF`, `ConfigurationManager`.
3. **Step 3: Author Formal Migration Plan**:
   - Write plan in `docs/migration/` using `templates/migration-plan.md`.
4. **Step 4: Migrate Foundation & Shared Libraries**:
   - Convert shared domain and utility `.csproj` files to SDK style.
   - Target `.NET Standard 2.0` or multi-target: `<TargetFrameworks>net48;net8.0</TargetFrameworks>`.
5. **Step 5: Migrate Application Layer Incrementally**:
   - Use the Strangler Fig pattern or YARP (Yet Another Reverse Proxy) to route endpoints incrementally from legacy IIS to the modern ASP.NET Core host.
6. **Step 6: Build & Test Verification**:
   - Verify that all existing unit and integration tests compile and pass.
7. **Step 7: Cutover & Cleanup**:
   - Decommission legacy IIS dependencies only after full parity is proven in production.

## 4. Anti-Patterns
- **The "Big Bang" Rewrite**: Trying to rewrite an entire 500,000-line solution in a single branch without intermediate releases.
- **Architectural Hijacking**: Introducing Clean Architecture, CQRS, or DDD during a framework upgrade when the original code was simple 3-tier.

## 5. Verification Checklist
- [ ] Dependencies audited for .NET Standard/Core compatibility.
- [ ] Shared libraries converted to SDK-style multi-targeting first.
- [ ] API contracts and serialization formats preserved identically.
- [ ] Automated regression tests confirm functional parity.
