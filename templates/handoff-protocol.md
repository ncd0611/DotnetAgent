# Standard Agent Handoff Protocol

Every agent yielding control or transferring tasks within the Universal .NET AI Core Team MUST output a structured Markdown report conforming to this schema.

```text
STATUS:
READY | BLOCKED | FAILED

SUMMARY:
<Concise 1-2 sentence description of what was completed or the blocker encountered>

FINDINGS:
  - <Concrete empirical observation 1>
  - <Concrete empirical observation 2>

FILES_INSPECTED:
  - [<relative_path>](file:///<relative_path>)

CHANGES:
  - [<relative_path>](file:///<relative_path>): <Specific surgical description of edit>

TESTS:
  - <Command executed (e.g. dotnet test --filter CustomerTests)>: <Result (e.g. 5 passed, 0 failed)>

RISKS:
  - <Identified residual risk, performance caveat, or security consideration>

DECISIONS:
  - <Key architectural, data modeling, or syntax choice made>

RECOMMENDATION:
  - <Actionable next steps>

RETRY_COUNT:
<Integer: 0 for initial delivery, increments on each review remediation cycle>

CIRCUIT_BREAKER:
<NORMAL | TRIPPED - If RETRY_COUNT reaches 3, specialist MUST set STATUS: BLOCKED and route to tech-lead for human guidance>

NEXT_AGENT:
  - <Target agent: tech-lead | architect | dotnet-engineer | database-engineer | test-engineer | security-engineer | performance-engineer | migration-engineer | legacy-analyst | code-reviewer>
```
