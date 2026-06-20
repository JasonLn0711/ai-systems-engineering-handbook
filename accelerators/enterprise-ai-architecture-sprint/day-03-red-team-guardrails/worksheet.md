# Worksheet — Day 3: Red-Team Guardrails

Use this worksheet to produce every Day 3 artifact. Do not use real customer
data, credentials, real tickets, private transcripts, or identifiable personal
data.

## 1. Scenario And Asset Map

Scenario:

```text
Campus IT helpdesk / sales coach / manufacturing support / other public-safe scenario:
```

Assets and boundaries:

| Asset | Classification | Allowed users | Blocked users | Control |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 2. Threat Taxonomy

| Threat category | Target control | Example attacker goal | Evidence required |
|---|---|---|---|
| Prompt injection |  |  |  |
| PII exfiltration |  |  |  |
| Tool abuse |  |  |  |
| Privilege escalation |  |  |  |
| Memory poisoning |  |  |  |
| RAG source manipulation |  |  |  |
| Unsafe output |  |  |  |
| Audit evasion |  |  |  |
| Human review bypass |  |  |  |

## 3. PII / Guardrail Policy Event Schema

```yaml
event_id:
trace_id:
timestamp:
user_id:
agent_id:
gate:
risk_type:
detected_pattern:
action:
reason:
source_refs:
review_owner:
audit_evidence:
  policy_id:
  case_id:
  expected_control:
  outcome:
```

## 4. Test Case Template

```yaml
case_id:
task:
threat_category:
attacker_goal:
input_payload:
retrieved_context_payload:
target_control:
expected_control:
expected_policy_decision:
expected_safe_behavior:
required_audit_fields:
  -
pass_fail_rule:
severity:
remediation_owner:
```

## 5. 30-Case Harness Matrix

Fill 30 rows across 3 public-safe tasks.

| Case ID | Task | Threat | Target control | Expected decision | Required audit fields | Pass/fail rule |
|---|---|---|---|---|---|---|
| RT-001 |  |  |  |  |  |  |
| RT-002 |  |  |  |  |  |  |
| RT-003 |  |  |  |  |  |  |
| RT-004 |  |  |  |  |  |  |
| RT-005 |  |  |  |  |  |  |
| RT-006 |  |  |  |  |  |  |
| RT-007 |  |  |  |  |  |  |
| RT-008 |  |  |  |  |  |  |
| RT-009 |  |  |  |  |  |  |
| RT-010 |  |  |  |  |  |  |
| RT-011 |  |  |  |  |  |  |
| RT-012 |  |  |  |  |  |  |
| RT-013 |  |  |  |  |  |  |
| RT-014 |  |  |  |  |  |  |
| RT-015 |  |  |  |  |  |  |
| RT-016 |  |  |  |  |  |  |
| RT-017 |  |  |  |  |  |  |
| RT-018 |  |  |  |  |  |  |
| RT-019 |  |  |  |  |  |  |
| RT-020 |  |  |  |  |  |  |
| RT-021 |  |  |  |  |  |  |
| RT-022 |  |  |  |  |  |  |
| RT-023 |  |  |  |  |  |  |
| RT-024 |  |  |  |  |  |  |
| RT-025 |  |  |  |  |  |  |
| RT-026 |  |  |  |  |  |  |
| RT-027 |  |  |  |  |  |  |
| RT-028 |  |  |  |  |  |  |
| RT-029 |  |  |  |  |  |  |
| RT-030 |  |  |  |  |  |  |

## 6. Pass / Fail Report Template

| Case ID | Result | Evidence | Missing evidence | Remediation |
|---|---|---|---|---|
|  | pass / fail / review |  |  |  |

## 7. Remediation Backlog

| Item ID | Failed case | Owner | Severity | Required control change | Next validation |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## 8. Final Checklist

- [ ] 30 cases exist.
- [ ] At least 3 tasks exist.
- [ ] At least 9 threat categories appear.
- [ ] Every case has expected control.
- [ ] Every case has pass/fail rule.
- [ ] Every case has required audit fields.
- [ ] PII policy event schema covers input, retrieval, tool, memory, and output.
- [ ] Report template separates pass, fail, and review.
- [ ] Failed or review cases create remediation work.
- [ ] Source boundary is public-safe.
