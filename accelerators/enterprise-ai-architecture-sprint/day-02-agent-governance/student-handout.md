# Student Handout: Agent Governance Framework

## 1. First Conclusion

An enterprise agent is not safe because the prompt says it is safe. An
enterprise agent is governable when its identity, owner, task scope, allowed
tools, allowed data sources, memory scope, policy gates, audit events, and
review states are explicit.

Day 1 taught the AI Gateway as a control plane. Day 2 defines what the Gateway
needs to know about each agent before routing work to it.

## 2. Why This Day Exists

A simple agent may look like this:

```text
user request -> agent -> model -> tool -> answer
```

That is not enough for enterprise use. The system must answer:

1. Who owns this agent?
2. What task is it allowed to perform?
3. Which users can invoke it?
4. Which tools can it call?
5. Which data sources can it retrieve?
6. What memory can it read or write?
7. Which actions require review?
8. What audit event proves what happened?
9. What red-team cases should test this policy?

## 3. Governance Layer Mental Model

```text
Identity
-> Agent Registry
-> Tool Boundary
-> Data Boundary
-> Memory Boundary
-> Policy Gate
-> Audit Event
-> Evaluation Hook
-> Red-Team Seed
```

The AI Gateway can route requests only when these layers are explicit.

## 4. Core Terms

| Term | Beginner definition | Engineering meaning |
|---|---|---|
| Agent Registry | A list of available agents | Records owner, scope, risk class, tools, data, memory, evals |
| Task Scope | What the agent is allowed to do | Prevents one agent from becoming a general-purpose actor |
| Tool Boundary | Tool access rules | Separates read-only tools from side-effect tools |
| Memory Scope | Memory read/write rule | Controls retention, sharing, deletion, and cross-agent leakage |
| Policy Gate | allow/deny/review decision point | Enforces task, data, tool, memory, and review rules |
| Adapter | Task-specific mapping layer | Converts common governance into scenario-specific behavior |
| Audit Event | Lifecycle evidence | Records identity, agent, tool, source, memory, policy, review |
| Evaluation Hook | Measurement point | Connects success, safety, coverage, latency, and regression checks |
| Red-Team Seed | A future attack/test idea | Turns governance assumptions into Day 3 tests |

## 5. Main Public-Safe Scenario

Campus IT Helpdesk Assistant continues from Day 1.

```text
A student asks the helpdesk agent for VPN setup steps and may request ticket
submission when troubleshooting fails.
```

We define one governed agent:

```text
campus_it_helpdesk_agent
```

It can:

- answer public IT FAQ questions
- retrieve public VPN guide chunks
- draft a ticket summary

It cannot:

- read staff-only account-lock SOPs
- submit tickets without review
- store private student details in shared memory
- call tools outside its registered scope

## 6. Common Governance Vs Adapter-Specific Behavior

Common governance is reusable across agents. Adapter-specific behavior changes
by scenario.

| Layer | Common governance | Campus IT adapter behavior |
|---|---|---|
| Identity | user ID, role, tenant, service account | `student`, `staff`, `it_reviewer` |
| Tool | schema, permission, timeout, side-effect class | `search_it_faq`, `submit_ticket` |
| Data | access level, source IDs, metadata filtering | public FAQ allowed; staff SOP denied |
| Memory | scope, retention, sharing, deletion | short session notes; no shared PII |
| Policy | allow/deny/review, risk class, review trigger | ticket submission requires review |
| Audit | trace ID, source IDs, tool decisions, policy | one audit event per request |
| Evaluation | success/safety/latency checks | VPN answer cites active guide |
| Red teaming | threat taxonomy and test cases | malicious FAQ, ticket spam, staff SOP bypass |

## 7. Agent Registration Template

```yaml
agent_id:
owner:
task_scope:
risk_class: low | medium | high
allowed_users:
allowed_tools:
allowed_data_sources:
memory_scope:
approval_required_for:
evaluation_set:
red_team_suite:
audit_events:
```

If a field is blank, the Gateway cannot enforce that part of governance.

## 8. Policy Gate Template

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

A policy gate should return:

```text
allow | deny | review
```

## 9. Audit Event Shape

```json
{
  "trace_id": "req-0001",
  "user_id": "student_001",
  "user_role": "student",
  "agent_id": "campus_it_helpdesk_agent",
  "policy_decision": "review",
  "retrieved_source_ids": ["vpn-guide-2026-01"],
  "tool_decisions": [
    {
      "tool_name": "submit_ticket",
      "decision": "review",
      "reason": "side-effect action"
    }
  ],
  "memory_decision": "session_only_no_shared_pii",
  "human_review_status": "pending",
  "outcome": "answer_returned_ticket_pending"
}
```

The audit event is not only a log line. It is evidence that the governance
contract was followed.

## 10. Risk-Control Map

| Risk | Example | Governance control | Evidence |
|---|---|---|---|
| Tool abuse | agent submits tickets repeatedly | tool boundary, approval gate, rate limit | tool decision log |
| Memory leakage | student PII becomes shared memory | memory scope, retention, deletion rule | memory decision field |
| Permission bypass | student reads staff SOP | retrieval rule, metadata filter | source filter log |
| Prompt-only approval | model says "approved" | policy gate enforces review | policy decision = review |
| Missing audit detail | answer has no source/tool record | audit schema requires source IDs and tool decisions | complete audit event |

## 11. Day 2 Submission

Submit one packet with:

1. Governance layer map.
2. Common-vs-adapter table.
3. Agent registration record.
4. Policy gate record.
5. Audit event schema.
6. Risk-control map.
7. Three Day 3 red-team seeds.

## 12. Key Rules To Remember

```text
An unregistered agent is not governable.
A side-effect tool must go through a broker and review rule.
Memory is a permission boundary, not only a convenience feature.
Policy returns allow, deny, or review; the prompt does not enforce approval.
Audit events must record decisions, not only final text.
```
