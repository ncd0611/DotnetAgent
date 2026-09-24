---
name: ef-diagnostics
description: Diagnoses and resolves Entity Framework Core and EF6 query performance issues, including N+1 queries, AsNoTracking usage, AsSplitQuery, and change tracking overhead.
---

# Entity Framework Diagnostics Skill

## 1. When to Use
- When debugging slow database queries or high database latency in EF Core or EF6.
- When reviewing data access code for N+1 query patterns or memory bloat.
- When configuring projections, split queries, or tracking behaviors on `DbContext`.

## 2. When NOT to Use
- In codebases utilizing Dapper or raw ADO.NET without Entity Framework.
- When querying small in-memory collections.

## 3. Core Diagnostic Areas & Rules

### A. Read-Only Queries (`AsNoTracking`)
- **Rule**: Whenever querying entities solely for display, reporting, or serialization, always attach `.AsNoTracking()`.
- **Impact**: Eliminates change-tracking snapshot allocations and reduces memory consumption by up to 60%.
```csharp
// EF Core / EF6:
var products = await context.Products
    .AsNoTracking()
    .Where(p => p.IsActive)
    .ToListAsync(cancellationToken);
```

### B. Cartesian Product Explosion (`AsSplitQuery`)
- **Rule**: When loading multiple child collections using `.Include()`, apply `.AsSplitQuery()` in EF Core to avoid exponential row multiplication in SQL joins.
```csharp
var customer = await context.Customers
    .AsNoTracking()
    .Include(c => c.Orders)
    .Include(c => c.Invoices)
    .AsSplitQuery()
    .FirstOrDefaultAsync(c => c.Id == id, cancellationToken);
```

### C. N+1 Query Prevention
- **Symptom**: Iterating over a collection and accessing navigation properties that trigger lazy loading queries in a loop.
- **Remedy**: Use eager loading (`.Include()`), explicit projection (`.Select(x => new { ... })`), or batch querying.

### D. Targeted Projections
- Instead of loading full entity graphs with 50 columns, project only required fields using `.Select()`:
```csharp
var dtoList = await context.Users
    .Where(u => u.TenantId == tenantId)
    .Select(u => new UserSummaryDto(u.Id, u.Email, u.FullName))
    .ToListAsync(cancellationToken);
```

## 4. Anti-Patterns
- **Unbounded Queries**: Calling `.ToListAsync()` without a `.Take()` or pagination filter.
- **Client-Side Evaluation**: Writing C# methods inside EF LINQ expressions that cannot translate to SQL, forcing client-side data streaming.

## 5. Verification Checklist
- [ ] Read queries use `.AsNoTracking()`.
- [ ] Multi-collection includes evaluated for `.AsSplitQuery()`.
- [ ] No queries executed inside `foreach` loops.
- [ ] Queries project only required columns.
