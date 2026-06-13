# MCP / Tool / Memory Governance

## Purpose

Define how enterprise agents should access shared tools, knowledge, SQL, and
memory without creating uncontrolled cross-agent behavior.

## Architecture View

```text
Agent
  |
  v
AI Gateway
  |
  |-- tool registry
  |-- MCP connector registry
  |-- permission policy
  |-- memory scope policy
  |-- audit event writer
  v
Tools / KB / SQL / workflows / memory stores
```

## Evidence Output

- Tool registration schema.
- MCP connector responsibility map.
- Memory scope matrix.
- Tool-call lifecycle.
- Audit checklist.

## Tool Registration Schema

```yaml
tool_id:
description:
owner:
input_schema:
output_schema:
allowed_agents:
allowed_roles:
data_classification:
side_effect: none | read | write | external_action
timeout_ms:
retry_policy:
idempotency_key_required: true | false
approval_required: true | false
audit_fields:
```

## Memory Scope Matrix

| Memory type | Example | Sharing rule | Retention | Risk |
|---|---|---|---|---|
| session memory | current conversation | same session only | short | leakage through transcript |
| user memory | preferences, history | user-scoped | policy-defined | over-personalization |
| task memory | project state | task/agent-scoped | project-defined | stale state |
| organization memory | shared KB facts | role-scoped | governed | broad leakage |
| audit memory | traces and decisions | reviewer/admin-scoped | compliance-defined | sensitive logs |

## Tool Call Lifecycle

```text
1. Agent proposes tool call.
2. Gateway validates tool exists.
3. Gateway validates caller role and agent scope.
4. Gateway validates input schema.
5. Gateway checks data classification.
6. Gateway checks approval requirement.
7. Tool executes with timeout and retry policy.
8. Gateway validates output schema.
9. Gateway writes audit event.
10. Agent receives bounded result.
```

## Minimum Viable Output

- Two registered tools:
  - read-only KB search
  - approval-gated external action
- One MCP connector map.
- One memory scope matrix.
- One audit event example.

## Validation Checklist

- [ ] Tool schemas are typed.
- [ ] Tool permissions are role- and agent-scoped.
- [ ] Write/external actions require explicit approval when high risk.
- [ ] Retry behavior is bounded.
- [ ] Idempotency is defined for side-effectful tools.
- [ ] Memory scope prevents cross-agent leakage.
- [ ] Audit log records caller, tool, arguments class, result class, and policy.

## Failure Modes

- Agent can call a tool that the user could not call directly.
- Tool output includes data outside the task scope.
- Memory from one customer/task appears in another task.
- Retry creates duplicate external actions.
- Tool arguments are not validated and cause unsafe behavior.

## Linked Modules And Labs

- `modules/07-ai-gateway-agent-governance/`
- `modules/09-security-red-teaming/`
- `modules/11-spec-sdd-ai-coding-workflow/`
- `labs/ai-gateway/`

## Next Implementation Gate

Create one registry-driven tool call demo where a policy check decides whether
the agent can call a read-only tool or must route an action tool to human
review.
