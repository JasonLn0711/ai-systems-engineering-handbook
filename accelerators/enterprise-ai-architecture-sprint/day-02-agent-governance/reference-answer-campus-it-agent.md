# Reference Answer: Campus IT Helpdesk Agent Governance

Audience: instructor and TA only. Do not give this to students before
submission.

## Scenario

```text
A student asks the campus IT helpdesk agent for VPN troubleshooting steps and
may request ticket submission if troubleshooting fails.
```

## Reference Governance Layer Map

```text
Identity: student_001, role=student
Agent Registry: campus_it_helpdesk_agent
Tool Boundary: search_it_faq=read_only, submit_ticket=side_effect_review
Data Boundary: access_level=public only
Memory Boundary: session_only, no shared PII, delete after 24h
Policy Gate: allow public FAQ; deny staff-only SOP; review ticket submission
Audit Event: trace, identity, agent, policy, sources, tool, memory, review, outcome
Evaluation Hook: answer cites active VPN guide
Red-Team Seed: staff SOP bypass, ticket spam, malicious FAQ instruction
```

## Common-Vs-Adapter Table

| Layer | Common governance | Campus IT adapter behavior |
|---|---|---|
| Identity | user ID, role, tenant, service account | `student`, `staff`, `it_reviewer` |
| Tool | schema, permission, timeout, side-effect class | `search_it_faq`, `submit_ticket` |
| Data | access level, source IDs, metadata filtering | public FAQ allowed; staff SOP denied |
| Memory | scope, retention, sharing, deletion | session-only notes; no shared PII; delete after 24h |
| Policy | allow/deny/review, risk class, review trigger | ticket submission requires review |
| Audit | trace ID, source IDs, tool decisions, policy | one audit event per request |
| Evaluation | success/safety/latency checks | VPN answer cites active guide |
| Red teaming | threat taxonomy and test cases | malicious FAQ, ticket spam, staff SOP bypass |

## Agent Registration

```yaml
agent_id: campus_it_helpdesk_agent
owner: campus_it_service_team
task_scope:
  - answer_public_it_faq
  - draft_ticket_summary
risk_class: medium
allowed_users:
  - student
  - staff
allowed_tools:
  - search_it_faq
  - submit_ticket_review_only
allowed_data_sources:
  - it_faq_public
  - vpn_guide_public
memory_scope:
  storage: session_only
  retention: 24_hours
  sharing: no_cross_agent_sharing
  pii: mask_or_do_not_store
approval_required_for:
  - submit_ticket
  - access_staff_only_sop
evaluation_set:
  - vpn_setup_answer_with_source
  - account_lock_public_guidance
red_team_suite:
  - staff_sop_bypass_attempt
  - ticket_spam_attempt
  - malicious_faq_instruction
audit_events:
  - helpdesk_agent_request
  - tool_decision
  - human_review_item
```

## Policy Gate

```yaml
policy_id: campus_it_helpdesk_student_policy
applies_to:
  - campus_it_helpdesk_agent
preconditions:
  - authenticated_user
  - role_in_allowed_users
allowed_actions:
  - search_public_it_faq
  - answer_public_vpn_question
blocked_actions:
  - retrieve_staff_only_sop
  - submit_ticket_without_review
pii_rule:
  input: mask_phone_email_student_id_before_shared_logs
  memory: no_shared_pii
retrieval_rule:
  allow_access_levels:
    - public
  deny_access_levels:
    - staff_only
tool_rule:
  search_it_faq: allow
  submit_ticket: review
memory_rule:
  retention: 24_hours
  sharing: no_cross_agent_sharing
human_review_trigger:
  - submit_ticket
  - detected_private_student_context
failure_response:
  deny: explain_scope_and_offer_public_help
  review: create_pending_review_item
audit_fields:
  - trace_id
  - user_id
  - role
  - agent_id
  - policy_decision
  - retrieved_source_ids
  - tool_decisions
  - memory_decision
  - human_review_status
  - outcome
```

## Audit Event Schema

```json
{
  "trace_id": "req-0002",
  "user_id": "student_001",
  "user_role": "student",
  "agent_id": "campus_it_helpdesk_agent",
  "task_scope": "answer_public_it_faq",
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
  "guardrail_result": "passed",
  "human_review_status": "pending",
  "evaluation_hook": "vpn_answer_has_active_source",
  "outcome": "answer_returned_ticket_pending"
}
```

## Reference Risk-Control Map

| Risk | Example | Governance control | Evidence |
|---|---|---|---|
| Tool abuse | agent submits many tickets | tool broker, review-only ticket tool, rate limit | tool decision log |
| Memory leakage | student private context shared with another agent | session-only memory, no cross-agent sharing, PII masking | memory decision in audit |
| Permission bypass | student reads staff-only SOP | retrieval rule denies `staff_only` | policy and source filter log |
| Prompt-only approval | model says ticket is approved | policy gate returns review; review item required | `policy_decision=review` |
| Missing audit detail | no tool/source record | required audit fields | complete audit event |

## Day 3 Red-Team Seeds

1. Malicious FAQ chunk instructs agent to ignore retrieval policy.
2. Student asks agent to submit 20 tickets to test tool abuse controls.
3. Student asks for staff-only account-lock SOP to test permission bypass.

## Instructor Notes

Passing answers show:

- agent owner and task scope are explicit
- read-only and side-effect tools are separated
- memory scope includes retention and sharing
- policy returns allow, deny, or review
- audit event records decisions, not only final text
- red-team seeds are testable

Common errors:

- `allowed_tools: all`
- memory omitted or shared without scope
- approval described in prompt but not policy
- audit schema missing source IDs or tool decisions
- no red-team seeds attached to policy assumptions
