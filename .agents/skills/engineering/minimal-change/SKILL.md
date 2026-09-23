---
name: minimal-change
description: Guides surgical, localized code modifications that solve the target problem with the smallest possible diff, preserving surrounding code, formatting, and reversibility.
---

# Minimal Change Skill

## 1. When to Use
- During any code editing, bug fixing, or feature addition task.
- When refactoring is tempting but not strictly requested or required for correctness.
- When authoring git commits and pull request diffs.

## 2. When NOT to Use
- When the user explicitly requests a large-scale architectural refactoring or total file rewrite.

## 3. Workflow & Procedure
1. **Scope Boundary Definition**:
   - Identify the exact symbol, function, or block requiring modification.
   - Forbid modifying adjacent functions or reformatting untouched code.
2. **Preserve Surrounding Conventions**:
   - Match existing indentation (tabs vs spaces, 2 vs 4 spaces).
   - Match existing brace style (Allman vs K&R).
   - Match existing naming idioms (camelCase, PascalCase, leading underscores).
3. **Keep Diffs Reviewable & Reversible**:
   - Prefer targeted block replacements (`replace_file_content`) over whole file rewrites.
   - Avoid deleting comments, docstrings, or license headers.
4. **Collataral Damage Check**:
   - Run `git diff` to verify that only lines directly related to the task have changed.

## 4. Decision Guidance
- If tempted to reformat an entire file while fixing a one-line bug: **DON'T**. Fix only the one-line bug.
- If an existing helper is slightly inefficient but working and not causing a bottleneck: **DO NOT TOUCH IT**.

## 5. Anti-Patterns
- **Drive-by Refactoring**: Renaming variables, moving methods, or converting syntax in unrelated sections of the file.
- **Whole-File Re-serialization**: Re-saving entire files causing noisy whitespace-only git diffs.

## 6. Verification Checklist
- [ ] Only target lines were edited.
- [ ] Whitespace and formatting style matches surrounding code.
- [ ] No unrelated methods or comments were altered.
- [ ] Diff is easily reviewable and cleanly reversible.
