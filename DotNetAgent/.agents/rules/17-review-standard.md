# Rule 17: Objective Code Review Standard

## Rule Statement
The `Code Reviewer` must operate independently from the implementer, prioritizing findings strictly by objective severity (P0 $\rightarrow$ P1 $\rightarrow$ P2 $\rightarrow$ P3). Subjective stylistic nitpicks ("I would have written this differently") are strictly forbidden.

## Why It Exists
Review feedback often devolves into subjective debates over personal coding preferences, wasting engineering cycles and distracting from genuine bugs, security vulnerabilities, or concurrency defects. Objective severity standards ensure reviews protect system correctness.

## Review Priority Hierarchy

| Severity | Category | Focus Areas | Action |
| :--- | :--- | :--- | :--- |
| **P0: Critical** | `BUG` / `RISK` | Correctness defects, security vulnerabilities, crash hazards | **Blocks completion** |
| **P1: Major** | `BUG` / `RISK` | Architecture violations, data corruption, concurrency hazards | **Blocks completion** |
| **P2: Moderate** | `IMPROVEMENT` | Measurable performance regressions, missing tests | Non-blocking |
| **P3: Minor** | `STYLE` | Naming, cosmetic formatting | Non-blocking (Informational) |

## Required Finding Elements
Every review finding must provide:
1. **Severity**: P0, P1, P2, or P3
2. **Category**: `BUG`, `RISK`, `IMPROVEMENT`, or `STYLE`
3. **Location**: File and line number link (`[file.cs#L20-L25](file:///...)`)
4. **Problem**: Objective statement of defect
5. **Evidence**: Snippet or trace illustrating failure mode
6. **Impact**: Concrete risk to system
7. **Recommended Fix**: Actionable remediation steps

## Anti-Patterns
- Submitting stylistic advice as a P0 blocker.
- Vague findings like "The code could be improved."
