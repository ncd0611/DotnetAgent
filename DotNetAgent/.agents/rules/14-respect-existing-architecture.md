# Rule 14: Respect Existing Architecture

## Rule Statement
Adapt to and preserve the host project's architectural paradigm. If a project is structured as Vertical Slice, author new features as vertical slices. If it is N-Tier, author features across N tiers. If it is ABP, follow ABP module and DDD guidelines. Never unilaterally impose a different architectural doctrine.

## Why It Exists
Imposing modern architectural dogmas (such as Clean Architecture, CQRS, or DDD) onto repositories built around other valid architectural patterns creates architectural fragmentation, increases cognitive load for the human engineering team, and introduces fragile boundaries.

## Good Example
```text
Inspected ABP Framework solution: Created CustomerAppService in MyProject.Application, Customer entity in MyProject.Domain, and ICustomerRepository in MyProject.Domain.
```

## Bad Example
```text
Inspected ABP Framework solution: Decided ABP is too heavy and created a Minimal API endpoint in Program.cs that directly instantiates DbContext, bypassing ABP unit-of-work, audit logging, and authorization filters.
```

## Exception Cases
When the user explicitly requests an architectural redesign or migration.

## Enforcement Guidance
The Software Architect and Tech Lead ensure that all feature proposals strictly match the project's detected architectural pattern.
