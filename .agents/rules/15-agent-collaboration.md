# Rule 15: Agent Collaboration & Handoff Contract

## Rule Statement
All communication, delegation, and state transfer between agents must utilize the standardized, machine-readable Handoff Protocol (`templates/handoff-protocol.md`). Unstructured or conversational handoffs ("Looks good!", "I'm done") are strictly prohibited.

## Why It Exists
In multi-agent systems, ambiguous or conversational summaries cause loss of context, missed compilation errors, dropped risks, and redundant rework. Structured contracts ensure reliable task progression and clear accountability.

## Standard Contract Format
Every agent handoff report must contain:
```text
STATUS: READY | BLOCKED | FAILED
SUMMARY: <High-level summary of outcome>
FINDINGS:
  - <Bulleted empirical observations>
FILES_INSPECTED:
  - <Clickable file link>
CHANGES:
  - <Clickable file link>: <Description of change>
TESTS:
  - <Execution command>: <Result>
RISKS:
  - <Residual risks or caveats>
DECISIONS:
  - <Key technical or architectural decisions>
RECOMMENDATION: <Actionable next steps>
RETRY_COUNT: <Integer: increments on each review remediation cycle>
CIRCUIT_BREAKER: <NORMAL | TRIPPED>
NEXT_AGENT: <Target specialist or tech-lead>
```

## Circuit Breaker Invariant
To prevent infinite autonomous ping-pong loops between implementers and the Code Reviewer, `RETRY_COUNT` must not exceed **3**. If a review cycle fails 3 times consecutively, the specialist must trip the circuit breaker (`CIRCUIT_BREAKER: TRIPPED`), set `STATUS: BLOCKED`, and yield directly to `tech-lead` to request human user guidance.

## Exception Cases
None. Every inter-agent message must adhere to this contract.

## Enforcement Guidance
The Tech Lead will reject any specialist output that omits required fields or fails to provide concrete file links and evidence.
