# Rule 04: No Speculative Refactoring

## Rule Statement
Never refactor code based on speculative future requirements, personal aesthetic taste, or architectural fashion. Refactoring is permitted only when strictly required to implement the current task safely or when explicitly commanded by the user.

## Why It Exists
Speculative refactoring wastes token budget, bloats changes, introduces regressions, and distracts from delivering immediate value to the user.

## Good Example
```text
Task: "Add a discount field to the Order invoice."
Action: Added `decimal DiscountAmount` to the Invoice entity and updated the calculation method. Left surrounding legacy calculation engine intact.
```

## Bad Example
```text
Task: "Add a discount field to the Order invoice."
Action: "I noticed this calculation logic would be better as a Strategy Pattern with a Mediator bus, so I created 8 new classes, interfaces, and handlers."
```

## Exception Cases
When the existing structure makes fulfilling the user's explicit request impossible without localized structural adjustment.

## Enforcement Guidance
The Tech Lead will immediately reject plans proposing structural reorganizations that are not strictly demanded by the incoming requirement.
