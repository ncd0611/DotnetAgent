---
name: secure-by-default
description: Enforces secure-by-default design principles across ASP.NET endpoints, authentication/authorization boundaries, input validation, CSRF, and multi-tenancy isolation.
---

# Secure by Default Skill

## 1. When to Use
- When authoring or modifying API endpoints, MVC controllers, Razor pages, or authentication handlers.
- When handling user-supplied files, query strings, headers, or external URLs.
- When implementing multi-tenant filtering or authorization policies.

## 2. When NOT to Use
- When writing offline build or profiling scripts that do not expose network services or handle untrusted input.

## 3. Core Security Rules

### A. Authorization Boundaries
- Endpoints must be closed by default. Require explicit authentication (`[Authorize]`) unless intentionally public (`[AllowAnonymous]`).
- Validate claims or roles explicitly on sensitive operations:
```csharp
[Authorize(Policy = "RequireAdminRole")]
[HttpPost("api/v1/tenants")]
public async Task<IActionResult> CreateTenant([FromBody] CreateTenantDto dto)
```

### B. Anti-Forgery Protection (CSRF)
- State-changing actions (`POST`, `PUT`, `DELETE`) in MVC/Razor apps must enforce `[ValidateAntiForgeryToken]` or `AutoValidateAntiforgeryTokenAttribute`.

### C. Path Traversal & File Uploads
- Never trust `file.FileName` directly. Strip directory sequences via `Path.GetFileName()`.
- Validate file extensions against an explicit whitelist (e.g. `.png`, `.pdf`).
- Store files outside the web root (`wwwroot`).
```csharp
string safeFileName = Path.GetFileName(file.FileName);
string destination = Path.Combine(_storageDirectory, safeFileName);
```

### D. Server-Side Request Forgery (SSRF)
- When issuing outbound HTTP requests using user-supplied URLs, validate that the host is not a private IP address (`127.0.0.1`, `169.254.169.254`, `10.*.*.*`, `192.168.*.*`).

### E. Multi-Tenancy Data Isolation
- Enforce global query filters in EF Core (`modelBuilder.Entity<T>().HasQueryFilter(e => e.TenantId == _currentTenant.Id)`).
- Never permit a tenant to query or mutate another tenant's data by spoofing an `X-Tenant-Id` header.

## 4. Anti-Patterns
- **Trusting Client Data for Auth**: Checking if `dto.IsAdmin == true` sent from the client JSON payload.
- **Raw SQL Injection**: String concatenation in database queries.

## 5. Verification Checklist
- [ ] Endpoints require authorization by default.
- [ ] Anti-forgery validated on state-changing browser requests.
- [ ] File operations sanitize paths.
- [ ] Multi-tenant isolation verified with tenant filter tests.
