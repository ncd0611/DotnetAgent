# Rule 07: Avoid Unnecessary Abstraction

## Rule Statement
Do not add interfaces, wrappers, adapters, or indirection layers unless there is an immediate, concrete requirement (e.g. multiple implementations, unit testing isolation, or clean architecture boundary requirements).

## Why It Exists
Over-abstraction creates "indirection lasagna," where navigating code requires jumping through 6 single-implementation interfaces to find a 2-line database query. In .NET, `DbContext` and `HttpClientFactory` already provide powerful abstraction.

## Good Example
```csharp
// Simple, direct service with an interface only because unit testing mock is required:
public interface ICustomerNotifier { Task NotifyAsync(Guid id, CancellationToken ct); }
public class EmailCustomerNotifier : ICustomerNotifier { ... }
```

## Bad Example
```csharp
// Creating IGenericRepository<T>, IGenericUnitOfWork, IQuerySpecification<T>,
// and IEntityMapper<TSource, TDest> for a single internal microservice.
```

## Exception Cases
When implementing formal Clean Architecture or Domain-Driven Design where infrastructure dependencies must be decoupled from the core domain.

## Enforcement Guidance
The Architect will review all new interfaces and reject those that wrap existing standard .NET abstractions without adding value.
