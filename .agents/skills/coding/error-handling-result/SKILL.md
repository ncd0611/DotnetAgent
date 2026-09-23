---
name: error-handling-result
description: Implements structured error handling using the Result pattern for expected domain failures, reserving exceptions strictly for truly exceptional or unrecoverable scenarios.
---

# Error Handling & Result Pattern Skill

## 1. When to Use
- When authoring application use cases, domain logic, command/query handlers, or API endpoints.
- When replacing exception-based control flow (e.g., throwing `NotFoundException` or `ValidationException` inside normal business workflows).
- When standardizing error responses (ProblemDetails) in ASP.NET Core endpoints.

## 2. When NOT to Use
- In existing legacy codebases that strictly use exception filters or where changing return types would break public library APIs.
- For unexpected, unrecoverable system failures (e.g. `OutOfMemoryException`, database connectivity crashes, disk failure).

## 3. Core Philosophy
Exceptions are for **exceptional circumstances** (unexpected crashes, hardware failure, fatal bug).
Domain outcomes (validation errors, entity not found, unauthorized, duplicate entity) are **expected business possibilities** and should be represented explicitly via return types (`Result<T>`).

## 4. Pattern Structure
```csharp
public class Error
{
    public static readonly Error None = new(string.Empty, string.Empty);
    public string Code { get; }
    public string Message { get; }

    public Error(string code, string message)
    {
        Code = code;
        Message = message;
    }
}

public class Result<TValue>
{
    public bool IsSuccess { get; }
    public bool IsFailure => !IsSuccess;
    public TValue? Value { get; }
    public Error Error { get; }

    protected Result(TValue? value, bool isSuccess, Error error)
    {
        Value = value;
        IsSuccess = isSuccess;
        Error = error;
    }

    public static Result<TValue> Success(TValue value) => new(value, true, Error.None);
    public static Result<TValue> Failure(Error error) => new(default, false, error);
}
```

## 5. API Endpoint Mapping (Minimal APIs / Controllers)
```csharp
// In Controller / Endpoint:
var result = await customerService.GetByIdAsync(id, cancellationToken);
if (result.IsFailure)
{
    return result.Error.Code switch
    {
        "Customer.NotFound" => Results.NotFound(new { error = result.Error.Message }),
        "Customer.InvalidId" => Results.BadRequest(new { error = result.Error.Message }),
        _ => Results.StatusCode(StatusCodes.Status500InternalServerError)
    };
}
return Results.Ok(result.Value);
```

## 6. Anti-Patterns
- **Exceptions as Control Flow**: Throwing an exception inside a loop to break out, or throwing `UserNotFoundException` on a standard login attempt.
- **Null Object Abuse**: Returning `null` to indicate a failure without any context on why the operation failed.

## 7. Verification Checklist
- [ ] Business failures modeled as explicit errors or `Result<T>`.
- [ ] Exceptions reserved for truly fatal/unexpected states.
- [ ] HTTP status codes mapped cleanly from domain error types.
