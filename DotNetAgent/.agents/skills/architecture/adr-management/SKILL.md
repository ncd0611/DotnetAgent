---
name: adr-management
description: Guides authoring, updating, and maintaining Architecture Decision Records (ADRs) to document significant architectural choices and trade-offs.
---

# ADR Management Skill

## 1. When to Use
- When making significant architectural decisions (introducing a library, altering persistence strategies, changing auth mechanisms, defining multi-tenancy models).
- When a decision involves non-trivial trade-offs that future engineers or agents need to understand.

## 2. When NOT to Use
- For trivial implementation details, routine bug fixes, or minor formatting changes.

## 3. Workflow & Procedure
1. **Identify Decision Need**:
   - Determine if the change alters system boundaries, security models, data storage, or runtime requirements.
2. **Follow Standard ADR Template**:
   - Create a new document in `docs/adr/` named `NNNN-short-title.md` (e.g., `0001-use-ambient-tenant-context.md`).
   - Use sections:
     - **Title & Metadata**: Date, Status (Proposed, Accepted, Superseded, Deprecated), Deciders.
     - **Context & Problem Statement**: What technical dilemma prompted this decision?
     - **Decision Drivers**: Forces, constraints, performance requirements.
     - **Considered Options**: Alternative 1, Alternative 2, Alternative 3.
     - **Decision Outcome**: Chosen option and detailed rationale.
     - **Consequences**: Positive, negative, and neutral trade-offs.
3. **Keep ADRs Immutable**:
   - When a decision changes, do not rewrite the old ADR; create a new ADR that explicitly supersedes the former.

## 4. Decision Guidance
- Always state the trade-offs honestly. No architecture choice is free of downsides.

## 5. Anti-Patterns
- **Post-hoc Justification**: Writing an ADR just to document personal preference without evaluating alternatives.
- **Vague Rationale**: Stating "this is cleaner" without articulating the technical consequence.

## 6. Verification Checklist
- [ ] Numbered ADR created in `docs/adr/`.
- [ ] At least two alternatives evaluated.
- [ ] Concrete consequences and trade-offs documented.
