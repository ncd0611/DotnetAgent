# Rule 08: Secure by Default

## Rule Statement
All code, endpoints, database access, and configurations must be secure by default. Endpoints require authentication unless explicitly intended to be public; inputs must be sanitized; SQL must be parameterized; secrets must never be committed.

## Why It Exists
Security flaws in enterprise codebases lead to severe data breaches, ransomware infections, regulatory penalties, and compromised user trust. Defensive security is non-negotiable.

## Good Example
```csharp
[Authorize]
[HttpPost("api/documents/upload")]
public async Task<IActionResult> UploadDocument([FromForm] IFormFile file)
{
    string safeName = Path.GetFileName(file.FileName);
    // sanitize, validate magic bytes, store outside web root
}
```

## Bad Example
```csharp
[AllowAnonymous]
[HttpPost("api/documents/upload")]
public async Task<IActionResult> UploadDocument([FromForm] IFormFile file)
{
    // Path traversal vulnerability:
    string path = Path.Combine("wwwroot/uploads", file.FileName);
    using var stream = File.Create(path);
    await file.CopyToAsync(stream);
}
```

## Exception Cases
None. A project-specific convention must never silently weaken fundamental security invariants.

## Enforcement Guidance
The Security Engineer and Code Reviewer will classify any security lapse as a blocking P0 defect.
