---
name: project-profiler
description: Discovers and inspects authoritative .NET repository metadata (*.sln, *.csproj, packages.config, web.config, global.json) to generate .project-context.json and .project-context.md without modifying any files.
---

# Project Profiler Skill

## 1. When to Use
- When initiating work on any unfamiliar or unprofiled .NET repository.
- When `.project-context.json` is missing, incomplete, or out of date.
- When verifying the exact target framework version, C# language version, or package dependencies before planning changes.

## 2. When NOT to Use
- When `.project-context.json` is already present, verified, and reflects the current state of the repository.
- During implementation phases where code editing or test execution is underway.

## 3. Workflow & Procedure
1. **Locate Solution & Project Files**:
   - Run `list_dir` on root to find `*.sln`, `*.slnx`, `global.json`, `Directory.Build.props`, `Directory.Packages.props`.
   - Run `grep_search` across `*.csproj` files to extract `<TargetFramework>`, `<TargetFrameworks>`, and `<LangVersion>`.
2. **Inspect Dependencies & Manifests**:
   - Check for legacy manifests: `packages.config`, `web.config`, `App.config`.
   - Check for modern SDK-style `<PackageReference>` entries.
   - Look for hallmark enterprise packages:
     - ABP Framework: `Volo.Abp.*`
     - ORMs: `Microsoft.EntityFrameworkCore.*`, `EntityFramework` (EF6), `Dapper`
     - Testing: `xunit`, `nunit`, `MSTest.TestFramework`
3. **Analyze Frontend & Infrastructure**:
   - Check for `package.json` (Angular, React, Vue, AngularJS).
   - Check for `Dockerfile`, `docker-compose.yml`, CI/CD workflows in `.github/` or `.azure/`.
4. **Generate Context Artifacts**:
   - Write `.project-context.json` formatted per `templates/project-context.json`.
   - Write `.project-context.md` formatted per `templates/project-context.md`.

## 4. Decision Guidance
- **Multi-Targeting**: If `<TargetFrameworks>` contains multiple entries (e.g. `net48;net8.0`), classify as multi-targeted library and ensure both targets are considered.
- **Ambiguity Rule**: If project files specify `LangVersion=latest`, check the SDK version in `global.json` or target framework default to determine the effective C# version.

## 5. Anti-Patterns
- **Guessing by Folders**: Inferring ASP.NET Core because a `/Controllers/` folder exists (ASP.NET MVC 5 also uses `/Controllers/`).
- **Touching Code**: Editing any project or source file during profiling. The profiler is strictly read-only.

## 6. Verification Checklist
- [ ] Solutions and project files identified.
- [ ] Target framework and runtime generation confirmed with file line references.
- [ ] ORM and database dependencies identified.
- [ ] `.project-context.json` validated against JSON schema.
- [ ] `.project-context.md` written to repository root.
