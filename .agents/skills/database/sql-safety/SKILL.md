---
name: sql-safety
description: Enforces SQL parameterization, injection prevention, safe transaction boundaries, indexing analysis, and connection leak avoidance in Dapper, EF, and ADO.NET.
---

# SQL Safety & Optimization Skill

## 1. When to Use
- When writing or reviewing raw SQL queries in Dapper, ADO.NET, or Entity Framework (`FromSqlRaw`, `SqlQuery`).
- When defining database transactions, migration scripts, or indexing strategies.
- When auditing database access code for SQL injection vulnerabilities.

## 2. When NOT to Use
- When using high-level LINQ queries that generate parameterized SQL automatically, unless inspecting raw SQL translation.

## 3. Core Safety Rules

### A. Absolute Parameterization (Zero Concatenation)
- **CRITICAL INVARIANT**: Never concatenate or interpolate user-supplied strings into SQL commands.
```csharp
// BAD (SQL Injection vulnerability):
string sql = $"SELECT * FROM Users WHERE UserName = '{username}'";
var user = connection.QueryFirstOrDefault<User>(sql);

// GOOD (Dapper Parameterization):
string sql = "SELECT * FROM Users WHERE UserName = @UserName";
var user = await connection.QueryFirstOrDefaultAsync<User>(sql, new { UserName = username });

// GOOD (EF Core Parameterization):
var user = await context.Users
    .FromSqlInterpolated($"SELECT * FROM Users WHERE UserName = {username}")
    .FirstOrDefaultAsync();
```

### B. Transaction Boundaries & Isolation
- Keep transactions as short as possible to minimize lock contention.
- Never perform long-running external HTTP or file I/O operations inside an open database transaction.
- Explicitly commit or rollback transactions within a `using` block:
```csharp
await using var transaction = await context.Database.BeginTransactionAsync(cancellationToken);
try
{
    // mutations...
    await context.SaveChangesAsync(cancellationToken);
    await transaction.CommitAsync(cancellationToken);
}
catch
{
    await transaction.RollbackAsync(cancellationToken);
    throw;
}
```

### C. Connection Lifecycle & Pooling
- Always dispose connections using `await using` or `using` to ensure connections return to the ADO.NET connection pool immediately.
- Never store database connections in static or singleton fields.

## 4. Anti-Patterns
- **String Interpolated Raw SQL**: Using `$""` directly into `FromSqlRaw()` without parameter wrappers.
- **Leaked Connections**: Opening a `SqlConnection` without wrapping in a `using` block.

## 5. Verification Checklist
- [ ] Zero unparameterized string concatenations in SQL commands.
- [ ] Connections disposed immediately via `using`.
- [ ] Transactions scoped tightly around database operations only.
