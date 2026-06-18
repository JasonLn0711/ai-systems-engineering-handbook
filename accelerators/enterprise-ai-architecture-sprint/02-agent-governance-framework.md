# Agent Governance Framework

## Purpose

Create a reusable governance framework for enterprise AI agents and connect it
to the Day 1 minimal gateway mock contract. The framework separates common
controls from task-specific adapters so new agents can be added without
rebuilding governance each time. It also prevents lower-trust agents from
using higher-trust agents, tools, message channels, logs, memory, or retrieval
services as indirect readers for data they cannot access directly.

## Governance Layers

```text
Identity
-> Agent Registry
-> Memory
-> Mediated Message Boundary
-> Tool
-> Policy
-> Audit
-> Evaluation
-> Red Teaming
```

## Common Layer Vs Adapter Layer

| Layer | Common governance | Adapter-specific behavior |
|---|---|---|
| Identity | user, role, tenant, service account, agent identity | customer role mapping |
| Memory | storage scope, retention, deletion, sharing rule | task-specific memory fields |
| Message mediation | schema, broker/topic or gateway path, producer/consumer identity, retention, replay control | support-safe topics, raw privileged topic isolation |
| Tool | schema, permission, timeout, retry, idempotency | tool parameters and workflow mapping |
| Policy | allowed tasks, blocked tasks, risk class, approval rule | domain-specific policy checks |
| Audit | event schema, trace ID, source IDs, tool calls, decisions | customer report format |
| Evaluation | success criteria, safety checks, latency, coverage | domain eval set |
| Red teaming | threat taxonomy and test harness | task-specific attack cases |

## Evidence Output

- Day 1-to-Day 2 gateway alignment and message mediation note.
- Governance layer map.
- Common-vs-adapter table.
- Agent registration template.
- Message mediation contract.
- Policy-gate checklist.
- Audit-event checklist.

## Agent Registration Template

```yaml
agent_id:
owner:
task_scope:
risk_class: low | medium | high
allowed_users:
allowed_tools:
allowed_data_sources:
memory_scope:
allowed_message_channels:
output_classification:
approval_required_for:
evaluation_set:
red_team_suite:
audit_events:
```

## Policy Gate Template

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
message_rule:
declassification_rule:
human_review_trigger:
failure_response:
audit_fields:
```

## Minimum Viable Output

- One `POST /gateway/requests` alignment note that names schema, identity,
  policy, tool, mediated message path, review, audit, and HTTP outcome
  requirements.
- One registered agent.
- Two tools: one read-only and one approval-gated action.
- One memory scope rule.
- One message mediation rule that prevents raw privileged payloads from
  flowing to low-trust agents.
- One policy gate.
- One audit event schema.
- One red-team test case linked to the policy.

## Failure Modes

- Agent has tool access without permission boundary.
- Memory is shared across agents without scope.
- Low-trust agent induces a high-trust agent to read and return privileged data
  as a confused deputy.
- Raw privileged content is copied into a shared broker topic, cache, log,
  trace, or dead-letter queue.
- Old privileged results can be replayed after the original decision expires.
- Approval is prompt-only and not enforced by system logic.
- Logs record text output but not source/tool decisions.
- Every new customer requires a new governance design.

## Validation Checklist

- [ ] Day 1 gateway lifecycle maps to Day 2 route, schema, policy, tool,
      message mediation, review, audit, and HTTP outcomes.
- [ ] Each agent has a clear owner and task scope.
- [ ] Each tool has schema, timeout, permission, and audit behavior.
- [ ] Each memory store has retention and sharing rules.
- [ ] Cross-boundary agent communication uses a mediated path with identity,
      schema, classification, replay protection, and audit.
- [ ] High-risk outputs route to human review.
- [ ] Evaluation and red-team tests are attached to the agent.
- [ ] Common governance rules are reusable across at least two tasks.

## Linked Modules And Labs

- `modules/07-ai-gateway-agent-governance/`
- `modules/09-security-red-teaming/`
- `modules/11-spec-sdd-ai-coding-workflow/`
- `labs/ai-gateway/`
- `labs/security/`

## Next Implementation Gate

Implement one simple registry file for an example enterprise agent and use it
to drive gateway routing, tool permission, message mediation, memory scope,
review state, declassification, and audit output in the minimal gateway mock.
