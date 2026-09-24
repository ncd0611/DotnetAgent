# Rule 05: Detect Version Before Coding

## Rule Statement
Before authoring or editing any C#, Razor, or project file, the agent must verify the project's target framework (`net48`, `net8.0`, `net10.0`), C# language version (`LangVersion`), and nullable configuration.

## Why It Exists
C# features evolve rapidly. Authoring modern syntax (e.g. primary constructors, collection expressions, file-scoped namespaces) in a project targeting .NET Framework 4.8 or older Roslyn compilers causes compilation failures (`CS8370: Feature is not available in C# 7.3`).

## Good Example
```text
Inspected csproj: TargetFramework is net472, LangVersion is default (C# 7.3).
Authored: Classic class with explicit constructor and standard namespace block.
```

## Bad Example
```csharp
// In a .NET Framework 4.7.2 project:
namespace MyCompany.LegacyApp; // CS8400: Feature 'file-scoped namespace' is not available in C# 7.3
public class CustomerService(ICustomerRepo repo) // CS8840: Feature 'primary constructor' is not available
```

## Exception Cases
None. Version awareness is mandatory for all code generation.

## Enforcement Guidance
The `.NET Engineer` must read `.project-context.json` prior to drafting code. Diffs introducing unsupported syntax will be flagged P0 by `Code Reviewer`.
