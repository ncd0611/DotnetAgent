---
name: regression-testing
description: Formulates regression tests for reported bugs, reproducing the defect before applying fixes and ensuring the defect cannot silently re-emerge in future releases.
---

# Regression Testing Skill

## 1. When to Use
- When fixing any reported functional defect, calculation error, or unexpected exception.
- When verifying that a bug fix has not broken existing adjacent functionality.

## 2. When NOT to Use
- For exploratory spike investigations or greenfield feature work where no prior behavior existed.

## 3. The 4-Step Regression Workflow
1. **Reproduce with a Failing Test**:
   - Write a new test capturing the exact input parameters and conditions that triggered the bug.
   - Run the test to confirm that it **FAILS** with the reported symptom (e.g. `AssertionFailedException`, `NullReferenceException`).
   - *If the test passes before fixing the code, the test does not reproduce the actual bug.*
2. **Apply the Surgical Fix**:
   - Implement the minimal fix in production code adhering to `minimal-change`.
3. **Verify the Test Passes**:
   - Re-run the regression test to verify that it now cleanly **PASSES**.
4. **Run Full Test Suite**:
   - Execute the entire test suite to ensure no collateral regressions were introduced.

## 5. Naming Convention
- Name regression tests explicitly to link back to the bug report:
  `[Fact] public void Bug_Issue402_NegativeDiscount_ThrowsValidationException()`
  or
  `[Fact] public void CustomerEndpoint_WhenTenantHeaderMissing_ReturnsUnauthorized()`

## 6. Anti-Patterns
- **Fix First, Test Never**: Modifying production code without creating an automated test that proves the fix.
- **Deleting Failing Tests**: Commenting out or deleting an existing test that broke because of a change.

## 7. Verification Checklist
- [ ] Failing test written and failure confirmed before fix.
- [ ] Production code modified surgically.
- [ ] Test passes cleanly after fix.
- [ ] Surrounding test suite passes without regressions.
