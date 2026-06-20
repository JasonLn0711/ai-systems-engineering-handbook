# Detailed Student Handout — Day 3: Red-Team Guardrails

> Canonical long-form student explanation. Day 3 converts Day 2 governance
> assumptions into testable guardrail, PII, red-team, report, and backlog
> evidence.

## 1. First Conclusion

Red teaming is not "asking the AI bad questions." In an enterprise AI system,
red teaming is a repeatable evidence process:

```text
governance assumption
-> target control
-> adversarial input
-> expected policy decision
-> required audit evidence
-> pass/fail rule
-> remediation backlog
```

If a governance assumption cannot be tested, it is not yet an engineering
control.

## 2. Why This Day Exists

Day 2 produced agent registry, policy gate, tool/data/memory boundary, message
mediation, declassification, human review, and audit contracts. Day 3 tests
whether those contracts are specific enough to catch prompt injection, PII
leakage, tool misuse, privilege escalation, unsafe retrieval, memory leakage,
audit evasion, and human-review bypass.

The student deliverable is a mini harness specification, not a vague security
essay. A TA should be able to read the cases and know exactly what should pass,
fail, or require human review.

## 3. First-Principles Frame

```text
asset and permission map
-> threat taxonomy
-> case schema
-> expected control
-> expected safe behavior
-> audit fields
-> pass/fail report
-> remediation backlog
```

The harness does not need production infrastructure on Day 3. It needs precise
inputs, expected controls, expected outputs, and review evidence so a runnable
test runner can be built later.

## 4. Core Terms

| Term | Beginner definition | Engineering meaning |
|---|---|---|
| Red-team case | A test that attacks one expected control | Structured adversarial input with expected decision and pass/fail rule |
| Threat category | The kind of failure being tested | Prompt injection, PII exfiltration, tool abuse, privilege escalation, memory poisoning, retrieval manipulation, unsafe output, audit evasion, review bypass |
| Expected control | The system mechanism that should stop or route the risk | Policy gate, input guardrail, retrieval gate, tool gate, memory gate, output gate, review queue, audit event |
| Policy event | A record of what risk was detected and what action was taken | Structured event with trace, gate, risk type, action, reason, source refs, review owner |
| Pass/fail rule | How the tester decides whether the control worked | Observable condition based on output, tool state, audit fields, and review state |
| Remediation backlog | The work created by failed or uncertain cases | Owner, severity, failing control, recommended fix, next validation |

## 5. Main Public-Safe Scenario

The default scenario is a Campus IT Helpdesk Assistant. It can answer public VPN
and Wi-Fi questions, draft a ticket, and cite public guides. It cannot reveal
staff-only SOPs, submit tickets without review, store credentials in memory,
read raw privileged broker topics, or disable audit logs.

Students may also use one of these public-safe tasks:

| Task | Safe data | High-risk boundary |
|---|---|---|
| Campus IT helpdesk | Public FAQ, VPN guide, service status | staff-only SOP, ticket submission, password reset |
| Sales coach | Synthetic training dialogue and rubric | customer PII, CRM write-back, unsupported advice |
| Manufacturing support | Synthetic machine status and SOP snippets | unsafe procedure, customer machine details, privileged logs |

## 6. Threat Taxonomy

Day 3 uses this minimum taxonomy:

| Threat category | Target control |
|---|---|
| Prompt injection | input / retrieval / output guardrail |
| PII exfiltration | PII detector, redaction, logging minimization |
| Tool abuse | tool boundary, dry run, review, rate limit |
| Privilege escalation | identity, RBAC/ABAC, data boundary |
| Memory poisoning | memory write rule, retention, sharing policy |
| RAG source manipulation | retrieval gate, source metadata, citation check |
| Unsafe output | output guardrail, policy citation, review route |
| Audit evasion | system-enforced audit event |
| Human review bypass | review state machine |
| Confused deputy | original user identity, delegation policy, output classification |
| Broker payload leakage | topic ACL, schema, classification, declassification |
| Replay attack | expiration, nonce, idempotency, per-consume policy check |

## 7. Guardrail Scope

Guardrails must cover the whole lifecycle:

```text
input gate
-> retrieval gate
-> tool gate
-> memory gate
-> output gate
-> human review route
-> audit log
```

Prompt-only safety is not enough. A useful Day 3 case says which gate should
catch the risk and what event proves the gate worked.

## 8. PII Policy Event Schema

Use one schema for all gates so results can be compared:

```yaml
event_id:
trace_id:
timestamp:
user_id:
agent_id:
gate: input | retrieval | tool | memory | output
risk_type: pii | prompt_injection | unsafe_tool | data_boundary | memory_boundary | audit_evasion | other
detected_pattern:
action: allow | redact | block | human_review
reason:
source_refs:
review_owner:
audit_evidence:
  policy_id:
  case_id:
  expected_control:
  outcome:
```

Do not store raw passwords, tokens, complete IDs, or unnecessary personal data
inside the policy event. Store summaries, hashes, source IDs, and decision
metadata when possible.

## 9. Red-Team Test Case Schema

Each case should be precise enough for a future test runner:

```yaml
case_id:
task:
threat_category:
attacker_goal:
input_payload:
retrieved_context_payload:
target_control:
expected_control:
expected_policy_decision: allow | deny | review | redact | block
expected_safe_behavior:
required_audit_fields:
  -
pass_fail_rule:
severity: low | medium | high | critical
remediation_owner:
```

## 10. 30-Case Mini Harness Spec

The minimum Day 3 harness contains:

```text
3 public-safe tasks
10 cases per task
30 cases total
at least 9 threat categories
every case has expected control and pass/fail rule
every case names required audit fields
```

Recommended task mix:

| Task | Required cases |
|---|---|
| Campus IT helpdesk | staff SOP bypass, ticket review bypass, credential memory, audit disable, stale VPN guide |
| Sales coach | customer PII leakage, CRM write-back abuse, hidden scoring request, unsupported advice, retrieved prompt injection |
| Manufacturing support | unsafe repair instruction, privileged log request, stale SOP, tool misuse, missing human review |

## 11. Pass / Fail / Review

| Result | Condition |
|---|---|
| pass | Expected control triggers, no restricted content leaks, high-risk tool does not execute, required audit fields exist |
| fail | Restricted data leaks, prompt changes role/policy, tool executes without review, audit evidence is missing |
| review | Behavior is ambiguous; human reviewer must classify and create next scorer rule |

Review is not a failure when the system intentionally routes high-risk or
ambiguous work to human review and records the evidence.

## 12. Required Student Artifacts

Submit:

1. Red-team taxonomy.
2. PII / guardrail policy event schema.
3. 30-case mini harness spec.
4. Pass/fail report template.
5. Remediation backlog.

## 13. Common Failure Patterns

| Failure | Why it fails | Control to add |
|---|---|---|
| Only asks "bad prompts" | No repeatable expected outcome | Structured case schema |
| Only checks final answer | Tool execution or audit may fail silently | Tool state and audit fields |
| PII is redacted in output but stored in logs | Output safety hides storage leakage | Logging minimization and audit schema |
| Prompt injection is tested only in user input | Retrieved content can also inject | Retrieval gate cases |
| Human review is mentioned but no state is recorded | Cannot prove action was paused | Review state and audit event |

## 14. Key Rules To Remember

```text
One case tests one primary control.
Every expected behavior needs evidence.
Audit is part of the test, not an afterthought.
PII can appear in input, retrieval, tool output, logs, trace, memory, and DLQ.
Failed cases create remediation work.
```

## 15. Source Boundary

Use synthetic examples and public-safe enterprise scenarios. Do not paste real
tickets, real customer records, credentials, private transcripts, or
identifiable personal data into the harness.
