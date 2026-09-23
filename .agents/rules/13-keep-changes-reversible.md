# Rule 13: Keep Changes Reversible

## Rule Statement
All changes should be structured as clean, self-contained atomic diffs that can be easily understood, reviewed, and cleanly reverted if necessary. Avoid destructive operations (e.g. dropping database columns, deleting legacy endpoints) without deprecation warnings and backward-compatibility buffers.

## Why It Exists
In complex enterprise systems, production rollbacks must be safe and seamless. Irreversible schema or code changes introduce severe downtime risk.

## Good Example
```text
Step 1: Added new nullable column `TaxCode` to table.
Step 2: Dual-write to old and new columns.
Step 3: Read from new column with fallback to old.
Old column remains intact until next release.
```

## Bad Example
```sql
-- Destructive migration executed immediately:
ALTER TABLE Invoices DROP COLUMN LegacyTaxCode;
```

## Exception Cases
When cleaning up deprecated code after the transition buffer period has passed and the user explicitly requests removal.

## Enforcement Guidance
The Database Engineer and Code Reviewer will reject any migration or PR that performs immediate, non-reversible data drops without staging.
