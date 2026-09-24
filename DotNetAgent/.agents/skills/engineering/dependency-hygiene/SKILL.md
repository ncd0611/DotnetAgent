---
name: dependency-hygiene
description: Manages NuGet dependencies, transitive package conflicts, Central Package Management (CPM), and binding redirects without causing breaking version mismatches.
---

# Dependency Hygiene Skill

## 1. When to Use
- When adding, updating, or removing NuGet packages or project references.
- When resolving package downgrade warnings (`NU1605`), binding redirect issues, or duplicate assembly references.
- When configuring `Directory.Packages.props` (Central Package Management).

## 2. When NOT to Use
- When performing localized logic changes that require no dependency alterations.

## 3. Workflow & Procedure
1. **Detect Dependency Management Scheme**:
   - Check if the repository uses Central Package Management (`<ManagePackageVersionsCentrally>true</ManagePackageVersionsCentrally>` in `Directory.Packages.props`).
   - If legacy, check `packages.config` and `web.config` `<runtime><assemblyBinding>` sections.
2. **Minimize Added Dependencies**:
   - Prefer standard library / BCL APIs before introducing a third-party NuGet package.
   - Never add heavy multi-megabyte dependencies for trivial utility functions.
3. **Audit Version Compatibility**:
   - Ensure the package version supports the detected `<TargetFramework>`.
   - In legacy .NET Framework, verify that required assembly binding redirects are generated or present.
4. **Clean Restoration & Build**:
   - Run `dotnet restore` or verify compilation to catch transitive conflicts early.

## 4. Decision Guidance
- Do not bump major dependency versions arbitrarily during a feature task.
- If a package dependency conflict arises, trace the dependency tree using `dotnet list package --include-transitive`.

## 5. Anti-Patterns
- **Uncontrolled Package Upgrades**: Running `dotnet upgrade` or bumping all NuGet packages indiscriminately.
- **Bypassing CPM**: Adding hardcoded `<PackageReference Version="..." />` inside individual `.csproj` files when CPM is active.

## 6. Verification Checklist
- [ ] Added package is strictly necessary and vetted.
- [ ] Package version is compatible with runtime target.
- [ ] Restoration succeeds with zero `NU*` warnings.
