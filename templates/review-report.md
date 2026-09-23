# Code Review Report

- **Task**: {{TASK_TITLE}}
- **Reviewer**: `code-reviewer`
- **Reviewed Commit / Diff**: `{{DIFF_REFERENCE}}`
- **Overall Status**: `APPROVED` | `CHANGES_REQUESTED`

---

## 1. Executive Summary
{{EXECUTIVE_SUMMARY}}

## 2. Review Findings Summary
| Severity | Category | Count | Blocking? |
| :--- | :--- | :--- | :--- |
| **P0: Critical** | BUG / RISK | {{P0_COUNT}} | **YES** |
| **P1: Major** | BUG / RISK | {{P1_COUNT}} | **YES** |
| **P2: Moderate** | IMPROVEMENT | {{P2_COUNT}} | NO |
| **P3: Minor** | STYLE | {{P3_COUNT}} | NO |

---

## 3. Detailed Findings

### [{{SEVERITY}}] {{FINDING_TITLE}}
- **Category**: `{{CATEGORY}}` (BUG | RISK | IMPROVEMENT | STYLE)
- **Location**: `[{{FILE_PATH}}#L{{LINE_NUMBER}}](file:///{{FILE_PATH}}#L{{LINE_NUMBER}})`
- **Problem**: {{PROBLEM_STATEMENT}}
- **Evidence**:
  ```csharp
  {{EVIDENCE_CODE_SNIPPET}}
  ```
- **Impact**: {{CONCRETE_IMPACT}}
- **Recommended Action**: {{REMEDIATION_GUIDANCE}}

---

## 4. Verification Check
- [ ] Builds with 0 errors: `{{BUILD_STATUS}}`
- [ ] Tests executed and passing: `{{TEST_STATUS}}`
- [ ] No P0/P1 defects remaining: `{{SIGN_OFF_STATUS}}`
