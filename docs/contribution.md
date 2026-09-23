# Contribution Guide

We welcome contributions to the Universal .NET AI Core Team! Follow these standards to maintain high quality and compatibility across Google Antigravity environments.

---

## 1. Authoring New Skills

1. **Location**: Create your skill inside `.agents/skills/<category>/<skill-name>/`.
2. **Frontmatter**: Every `SKILL.md` must start with valid YAML frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: >-
     Third-person concise description explaining WHAT the skill does and
     WHEN an agent should activate it.
   ---
   ```
3. **Progressive Disclosure**:
   - Keep `SKILL.md` under 400 lines. Focus on procedures, decisions, and checklists.
   - Place bulky documentation or specifications in `references/<topic>.md`.
   - Place executable scripts in `scripts/<helper>.sh` or `scripts/<helper>.ps1`.
4. **Validation**: Run `python scripts/validate.py` to confirm schema and link validity.

---

## 2. Authoring New Agents

1. **Location**: Create your agent inside `.agents/agents/<agent-name>/`.
2. **Contract**: Provide `agent.md` defining:
   - YAML frontmatter: `name`, `role`, `description`, `tools`.
   - Role & Purpose.
   - Strict Responsibilities and **Non-Responsibilities**.
   - Inputs, Outputs, and Allowed Tools (Least Privilege).
   - Handoff & Decision rules.

---

## 3. Authoring New Rules

1. **Location**: Create in `.agents/rules/<number>-<name>.md`.
2. **Structure**: Must include:
   - Rule Statement
   - Why It Exists
   - Good Example
   - Bad Example
   - Exception Cases
   - Enforcement Guidance

---

## 4. Running Validation
Before submitting any pull request:
```bash
python scripts/validate.py
pytest tests/
```
All tests, fixtures, and schema checks must pass with zero errors.
