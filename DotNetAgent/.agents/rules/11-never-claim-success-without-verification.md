# Rule 11: Never Claim Success Without Verification

## Rule Statement
An agent must never claim that a task, feature, or bug fix is complete until the implementation has been built, tested, and independently reviewed by the `Code Reviewer`.

## Why It Exists
Premature declarations of victory erode trust and leave developers to discover broken builds or failing tests.

## Good Example
```text
"The customer lookup feature has been implemented, verified with `dotnet build` (0 warnings), validated by 4 integration tests (all passing), and approved by Code Reviewer with 0 P0/P1 findings."
```

## Bad Example
```text
"Done! I have created the files and everything should work as expected."
```

## Exception Cases
Pure documentation or markdown authoring tasks where executable code is not involved.

## Enforcement Guidance
The Tech Lead enforces this rule as the final completion gate. Any premature status assertion will be rejected.
