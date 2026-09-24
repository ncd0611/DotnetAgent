# Rule 06: Prefer Existing Project Patterns

## Rule Statement
Match the existing conventions, idioms, directory layouts, and design patterns already established in the codebase. Do not introduce foreign patterns merely because they are recommended in generic online guides.

## Why It Exists
Consistency is essential for software maintainability. A codebase that mixes 5 different repository abstractions, 3 validation libraries, and disparate naming conventions becomes fragile and unmaintainable.

## Good Example
```text
Existing project uses FluentValidation and MediatR handlers inside a Features/ folder.
New feature: Created CustomerCreateCommand, CustomerCreateValidator, and CustomerCreateHandler in Features/Customers/.
```

## Bad Example
```text
Existing project uses direct DbContext in controllers.
Agent introduces a generic IRepository<T>, IUnitOfWork, and MediatR specifically for one new controller while the rest of the app uses direct DbContext.
```

## Exception Cases
When the existing pattern has a severe security flaw or when the user explicitly requests introducing a new pattern.

## Enforcement Guidance
The Architect and Code Reviewer will check proposed additions against existing neighbor classes.
