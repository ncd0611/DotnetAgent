# Rule 02: Minimal Change

## Rule Statement
All modifications must be strictly scoped to the lines and files necessary to fulfill the user's explicit request. Do not edit untouched neighboring methods, do not reformat files unnecessarily, and do not introduce collateral refactoring.

## Why It Exists
Large, unconstrained diffs introduce unexpected regressions, complicate code review, increase merge conflict risk, and obscure the actual bug fix or feature addition in git history.

## Good Example
```csharp
// In CustomerService.cs: Only updating the discount calculation block
- decimal discount = total * 0.05m;
+ decimal discount = total > 100m ? total * 0.10m : total * 0.05m;
```

## Bad Example
```csharp
// Changing the whole file from Allman braces to K&R, renaming variables, 
// reordering methods, and converting 15 methods to expression bodies while fixing a discount bug.
```

## Exception Cases
When the user explicitly commands a file-wide refactoring, cleanup, or formatting overhaul.

## Enforcement Guidance
The Code Reviewer will flag any PR containing changes to files or lines unrelated to the stated objective as a `RISK` or `IMPROVEMENT` and mandate reversion of the extraneous diffs.
