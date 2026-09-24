---
name: allocation-profiling
description: Analyzes memory allocation patterns in .NET, minimizing heap allocations, boxing, Large Object Heap (LOH) pressure, and inefficient string operations.
---

# Allocation Profiling & Memory Hygiene Skill

## 1. When to Use
- When diagnosing high GC (Garbage Collection) pauses or excessive Gen0/Gen1/Gen2 collections.
- When optimizing high-throughput loops, hot paths, or message processing pipelines.
- When reviewing data serialization or string parsing code.

## 2. When NOT to Use
- On cold paths executed once at startup (e.g. DI service configuration, routing setup).
- For premature optimization where code readability would be sacrificed without measurable benefit.

## 3. High-Impact Memory Patterns

### A. String Concatenation & Parsing
- In loops or large iterations, avoid string concatenation (`+` or `$""`), which allocates a new string object on every iteration. Use `StringBuilder` or modern interpolated string handlers.
- Use `ReadOnlySpan<char>` for parsing substrings without allocating heap strings:
```csharp
// Allocates substring:
string prefix = text.Substring(0, 5);

// Zero allocations:
ReadOnlySpan<char> prefixSpan = text.AsSpan(0, 5);
```

### B. Boxing & Unboxing Prevention
- Ensure generic collections (`List<int>`, `Dictionary<Guid, T>`) are used instead of non-generic `ArrayList` or `Hashtable`.
- Implement `IEquatable<T>` on `struct` types to avoid boxing during equality checks in dictionary lookups.

### C. Large Object Heap (LOH) Awareness
- Any single allocation $\ge$ 85,000 bytes goes directly to the Large Object Heap (LOH), which is only collected during Gen2 full GC cycles.
- For large byte buffers, utilize `ArrayPool<byte>.Shared` instead of allocating `new byte[100_000]`.

## 4. Anti-Patterns
- **Micro-Optimizing Cold Paths**: Using `unsafe` pointers or `Span` in a background batch job running once a month.
- **Ignoring GC Traces**: Guessing what allocates without inspecting memory profile dumps or BenchmarkDotNet memory diagnosers (`[MemoryDiagnoser]`).

## 5. Verification Checklist
- [ ] Hot path allocations minimized.
- [ ] Boxing eliminated in high-frequency collections.
- [ ] Large buffers pooled via `ArrayPool<T>` where appropriate.
