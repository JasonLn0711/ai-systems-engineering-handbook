# Worksheet: Agent Governance Framework

## 1. Scenario Selection

```text
Scenario name:
Primary user:
Primary task:
Agent ID:
High-risk action:
Main data sources:
Expected response or outcome:
```

## 2. Governance Layer Map

Draw or list the flow:

```text
Identity:
Agent Registry:
Tool Boundary:
Data Boundary:
Memory Boundary:
Policy Gate:
Audit Event:
Evaluation Hook:
Red-Team Seed:
```

## 3. Common-Vs-Adapter Table

| Layer | Common governance | Adapter-specific behavior |
|---|---|---|
| Identity |  |  |
| Tool |  |  |
| Data |  |  |
| Memory |  |  |
| Policy |  |  |
| Audit |  |  |
| Evaluation |  |  |
| Red teaming |  |  |

## 4. Agent Registration Record

```yaml
agent_id:
owner:
task_scope:
risk_class:
allowed_users:
allowed_tools:
allowed_data_sources:
memory_scope:
approval_required_for:
evaluation_set:
red_team_suite:
audit_events:
```

## 5. Policy Gate Record

```yaml
policy_id:
applies_to:
preconditions:
allowed_actions:
blocked_actions:
pii_rule:
retrieval_rule:
tool_rule:
memory_rule:
human_review_trigger:
failure_response:
audit_fields:
```

## 6. Audit Event Schema

List at least 10 fields:

```text
trace_id:
user_id:
user_role:
agent_id:
task_scope:
policy_decision:
retrieved_source_ids:
tool_decisions:
memory_decision:
guardrail_result:
human_review_status:
evaluation_hook:
outcome:
```

## 7. Risk-Control Map

| Risk | Example | Governance control | Evidence |
|---|---|---|---|
| Tool abuse |  |  |  |
| Memory leakage |  |  |  |
| Permission bypass |  |  |  |
| Prompt-only approval |  |  |  |
| Missing audit detail |  |  |  |

## 8. Day 3 Red-Team Seeds

Write three test ideas that Day 3 should turn into red-team cases:

```text
Seed 1:
Seed 2:
Seed 3:
```

## 9. Short Explanation

Answer in 5-8 sentences:

```text
Why is an agent registry not enough unless it is connected to policy, tools,
memory, audit, evaluation, and red-team tests?
```

## 10. Peer Review Checklist

- [ ] Agent has owner, task scope, risk class, users, tools, data, memory.
- [ ] At least one read-only tool and one side-effect tool are classified.
- [ ] Policy gate returns allow, deny, or review.
- [ ] Memory scope includes retention and sharing rules.
- [ ] Audit event records decisions, not only final answer.
- [ ] Risk-control map includes concrete system-enforced controls.
- [ ] Day 3 red-team seeds are testable.
- [ ] Scenario is public-safe.
