---
name: evidence-first
description: Enforces an empirical, evidence-driven engineering workflow where root causes, build failures, and performance claims must be verified before modifying code.
---

# Evidence First Skill

## 1. When to Use
- Before proposing any bug fix, optimization, architectural change, or dependency update.
- When diagnosing unexpected runtime behavior, test failures, or compiler errors.
- When evaluating competing technical hypotheses.

## 2. When NOT to Use
- Never disable this skill. It is an overarching engineering invariant.

## 3. Workflow & Procedure
1. **Gather Empirical Evidence**:
   - Collect exact error messages, stack traces, compiler diagnostic IDs (e.g. `CS0103`), or HTTP response codes.
   - For performance issues, obtain profiling traces, execution plans, or BenchmarkDotNet results.
2. **Reproduce & Confirm**:
   - Formulate a test case or script reproducing the reported failure.
   - Verify that the symptom matches the user's report under clean conditions.
3. **Isolate Root Cause**:
   - Trace the exact line and state mutation causing the defect.
   - Distinguish between symptom (e.g., `NullReferenceException`) and root cause (e.g., missing repository null guard).
4. **Formulate Hypothesis & Verify**:
   - Verify the proposed fix mentally or via targeted test before committing changes.

## 4. Decision Guidance
- Never accept "I think this is why it failed" as sufficient justification for an edit.
- If profiling data is unavailable, explicitly state the assumption and quantify uncertainty.

## 5. Anti-Patterns
- **Shotgun Debugging**: Modifying multiple lines of code blindly hoping the test passes.
- **Speculative Blame**: Blaming a framework or external library before inspecting local code.

## 6. Verification Checklist
- [ ] Root cause identified with concrete file and line reference.
- [ ] Reproducing condition confirmed.
- [ ] Fix addresses root cause rather than merely masking the symptom.
