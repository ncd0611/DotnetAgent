---
name: csharp-idioms
description: Provides version-aware C# patterns, syntax rules, and language idioms covering C# 7.3 (legacy .NET Framework) up through modern C# 10, 11, 12, and 13 (.NET 8/10).
---

# C# Idioms Skill

## 1. When to Use
- When writing, refactoring, or reviewing any C# source code.
- When determining whether a language feature is compatible with the project's detected `LangVersion`.

## 2. When NOT to Use
- When editing non-C# files (e.g. SQL, XML, JSON, YAML).

## 3. Version Matrix & Idiom Selection

| Runtime | Default C# | Supported Language Features | FORBIDDEN Syntax |
| :--- | :--- | :--- | :--- |
| **.NET Framework 4.5–4.8** | C# 5.0–7.3 | Explicit constructors, `var`, expression bodies, tuple returns, classic namespaces, `using` statements | Primary constructors, file-scoped namespaces, collection expressions, records, init-only setters, null-coalescing assignment (`??=`), nullable reference annotations |
| **.NET Core 3.1** | C# 8.0 | Nullable reference types, default interface methods, pattern matching, async streams | Records, init-only setters, top-level statements |
| **.NET 6** | C# 10.0 | File-scoped namespaces, records, global usings, interpolated string improvements | Collection expressions, primary constructors for classes |
| **.NET 8** | C# 12.0 | Primary constructors for classes/structs, collection expressions (`[1, 2, 3]`), ref readonly, default lambda params | C# 13 features |
| **.NET 10** | C# 13.0 | `params` collections, `lock` object improvements, ref struct in generics | N/A |

## 4. Universal C# Best Practices
1. **Nullability Hygiene**:
   - In modern .NET (`<Nullable>enable</Nullable>`), never ignore compiler warnings (`CS8600`, `CS8602`, `CS8603`).
   - Use null-forgiving operator (`!`) only when guaranteed safe by unexpressible runtime invariants, with an accompanying explanatory comment.
2. **Dispose Pattern & Asynchrony**:
   - Always dispose unmanaged resources or use `await using` for `IAsyncDisposable`.
   - Propagate `CancellationToken` through all asynchronous method signatures down to I/O operations.
3. **Immutability & Value Objects**:
   - Prefer `record` or `record struct` for DTOs and immutable domain events in modern .NET.
   - Use `readonly` fields and properties where mutations are not intended.

## 5. Anti-Patterns
- **Syntax Anachronisms**: Using C# 12 collection expressions (`int[] x = [1, 2];`) in a .NET Framework 4.7.2 project that compiles with C# 7.3.
- **Async Overuse in Legacy**: Converting classic synchronous ASP.NET MVC 5 controllers to async without handling `SynchronizationContext`, introducing deadlocks.

## 6. Verification Checklist
- [ ] Code syntax compiles against detected `LangVersion` without syntax errors.
- [ ] Nullable warnings addressed without blind `!` suppression.
- [ ] Cancellation tokens propagated where supported.
