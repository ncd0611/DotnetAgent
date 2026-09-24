---
name: async-hygiene
description: Enforces asynchronous programming correctness, eliminating sync-over-async deadlocks (.Result, .Wait()), thread pool starvation, and synchronization context hazards across modern and legacy .NET.
---

# Async Hygiene & Threading Skill

## 1. When to Use
- When writing or reviewing asynchronous methods (`async Task`, `ValueTask`).
- When diagnosing thread pool starvation, unexplained application hangs, or 504 gateway timeouts.
- When dealing with `SynchronizationContext` differences between legacy ASP.NET (.NET Framework) and modern ASP.NET Core.

## 2. When NOT to Use
- For purely synchronous in-memory transformations where no I/O is involved.

## 3. Core Async Rules

### A. Forbid Sync-Over-Async
- **NEVER** call `.Result`, `.Wait()`, or `GetAwaiter().GetResult()` on asynchronous tasks.
- **Consequence**: In legacy ASP.NET with a single-threaded `SynchronizationContext`, this causes an immediate permanent deadlock. In ASP.NET Core, it ties up thread pool threads, leading to thread pool starvation under moderate load.
```csharp
// BAD (Deadlock & thread pool starvation):
var customer = customerService.GetCustomerAsync(id).Result;

// GOOD:
var customer = await customerService.GetCustomerAsync(id, cancellationToken);
```

### B. ConfigureAwait in Libraries vs Applications
- In non-UI reusable class libraries, use `.ConfigureAwait(false)` to prevent resuming on captured synchronization contexts.
- In modern ASP.NET Core, `SynchronizationContext` does not exist, so `ConfigureAwait(false)` is generally unnecessary in controller/endpoint application code, but remains good practice in general-purpose libraries.

### C. Async All the Way Down
- Do not wrap synchronous blocking I/O calls (e.g. `File.ReadAllText`) inside `Task.Run()` merely to satisfy an async interface. Use true asynchronous I/O (`File.ReadAllTextAsync`).

### D. Avoid Async Void
- `async void` must only ever be used for UI event handlers. For all other methods, use `async Task` or `async ValueTask`. Exceptions in `async void` methods crash the entire process.

## 4. Anti-Patterns
- **Fire-and-Forget Without Exception Handling**: Calling `_ = DoWorkAsync()` without a try/catch or logging handler.
- **Async Overuse on Synchronous Operations**: Putting `async Task<int>` on `return Task.FromResult(42)`. Use simple synchronous returns or `ValueTask<int>`.

## 5. Verification Checklist
- [ ] Zero `.Result` or `.Wait()` calls on Tasks.
- [ ] No `async void` methods outside UI events.
- [ ] `CancellationToken` propagated to I/O endpoints.
