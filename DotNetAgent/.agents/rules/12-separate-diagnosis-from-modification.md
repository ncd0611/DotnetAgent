# Rule 12: Separate Diagnosis From Modification

## Rule Statement
Discovery and diagnosis must be conducted as an isolated, read-only phase before any source code edits begin. Never edit code while still attempting to diagnose the system or locate entry points.

## Why It Exists
Mixing exploration with code modification leads to exploratory "trial-and-error" edits that leave partial artifacts, dirty git trees, and confusing regressions in the codebase.

## Good Example
```text
Phase 1: Project Profiler and Legacy Analyst inspect solution and generate architecture map. No source code touched.
Phase 2: Formulate implementation plan and present to user.
Phase 3: Execute targeted modifications only after plan approval.
```

## Bad Example
```text
"Let me change this method in Service.cs to see if it fixes the compiler error... wait, now there's another error in Controller.cs, let me change that too... wait, what was the original error?"
```

## Exception Cases
None. Discovery agents are strictly read-only.

## Enforcement Guidance
The Project Profiler and Legacy Analyst have tool permissions restricted strictly to read/search commands to guarantee adherence.
