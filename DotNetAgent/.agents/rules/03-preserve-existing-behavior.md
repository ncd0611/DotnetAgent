# Rule 03: Preserve Existing Behavior

## Rule Statement
Any enhancement, refactoring, or bug fix must preserve existing behavioral contracts, return schemas, status codes, and backward compatibility unless the user explicitly requested a breaking change.

## Why It Exists
Internal enterprise software and public APIs often have downstream clients, undocumented integrations, and UI consumers that rely on exact JSON casing, status codes, and error formats. Silently altering behavior breaks production systems.

## Good Example
```csharp
// Preserving original HTTP 404 response payload while enhancing lookup logic:
if (entity == null)
{
    // Returns identical JSON shape { "error": "Entity not found", "id": 123 }
    return NotFound(new { error = "Entity not found", id = id });
}
```

## Bad Example
```csharp
// Unilaterally altering an existing endpoint to return RFC 7807 ProblemDetails 
// when the legacy frontend parser expects a flat { error: "..." } string.
```

## Exception Cases
When the existing behavior is the explicit bug being addressed, or when the user explicitly instructs an API contract upgrade.

## Enforcement Guidance
The Test Engineer must author regression tests validating that existing response shapes and status codes remain invariant.
