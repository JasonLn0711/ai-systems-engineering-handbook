# Student Handout — Day 3: Red-Team Guardrails

This is the summarized Day 3 handout. Use `student-handout-detailed.md` or
`student-handout-detailed.zh-TW.md` for complete examples.

## 1. First Conclusion

Red teaming is not asking random hostile questions. It is turning each Day 2
governance assumption into a test:

```text
assumption -> target control -> adversarial input -> expected decision -> audit evidence -> pass/fail rule
```

If the assumption cannot be tested, it is not yet an engineering control.

## 2. Why This Day Exists

Day 2 defined registry, policy, tool/data/memory boundary, mediation, review,
and audit. Day 3 checks whether those controls catch real failure patterns:
prompt injection, PII leakage, tool abuse, privilege escalation, memory
poisoning, unsafe retrieval, audit evasion, and review bypass.

## 3. First-Principles Frame

```text
asset map -> threat taxonomy -> test case -> expected control -> audit evidence -> report -> backlog
```

## 4. Core Terms

| Term | Core meaning |
|---|---|
| Red-team case | One structured attack against one expected control |
| Threat category | The risk family being tested |
| Expected control | The gate or policy that should catch the risk |
| Policy event | Evidence of gate, risk, action, reason, and owner |
| Pass/fail rule | Observable rule for deciding whether the control worked |
| Remediation backlog | Fix list created by failed or uncertain cases |

## 5. Main Public-Safe Scenario

Use synthetic Campus IT helpdesk, sales coach, or manufacturing support
scenarios. Do not use real tickets, private customer data, credentials, or
identifiable personal data.

## 6. Threat Taxonomy

Your taxonomy should include at least prompt injection, PII exfiltration, tool
abuse, privilege escalation, memory poisoning, RAG source manipulation, unsafe
output, audit evasion, human review bypass, confused deputy, broker payload
leakage, and replay attack.

## 7. Guardrail Scope

Guardrails must cover:

```text
input -> retrieval -> tool -> memory -> output -> human review -> audit
```

Prompt wording alone is not enough.

## 8. PII Policy Event Schema

Your schema must record event ID, trace ID, user/agent, gate, risk type,
detected pattern, action, reason, source refs, review owner, and audit evidence.

## 9. Red-Team Test Case Schema

Each case needs case ID, task, threat category, attacker goal, input payload,
target control, expected decision, expected safe behavior, required audit
fields, pass/fail rule, severity, and remediation owner.

## 10. 30-Case Mini Harness Spec

Submit 30 cases:

```text
3 tasks x 10 cases
at least 9 threat categories
each case has expected control, pass/fail rule, and audit fields
```

## 11. Pass / Fail / Review

| Result | Condition |
|---|---|
| pass | Expected control triggers and audit evidence exists |
| fail | Restricted data leaks, unsafe tool executes, or audit is missing |
| review | Ambiguous behavior needs human classification and a future scorer rule |

## 12. Required Student Artifacts

1. Red-team taxonomy.
2. PII / guardrail policy event schema.
3. 30-case mini harness spec.
4. Pass/fail report template.
5. Remediation backlog.

## 13. Common Failure Patterns

Avoid random prompts, final-answer-only checking, missing audit fields,
output-only PII masking, and human review without a recorded review state.

## 14. Key Rules To Remember

```text
One case tests one primary control.
Every expected behavior needs evidence.
Audit is part of the test.
PII can leak through logs, traces, memory, tool output, and DLQ.
Failed cases create remediation work.
```

## 15. Source Boundary

Keep all scenarios synthetic and public-safe.
