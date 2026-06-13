# PII / Guardrail Demo Plan

## Purpose

Design a small evidence demo showing how an enterprise AI system can detect,
mask, block, log, and review sensitive or policy-violating content.

## Guardrail Scope

```text
input gate
-> retrieval gate
-> tool gate
-> memory gate
-> output gate
-> human review route
-> audit log
```

## Evidence Output

- PII detection and masking plan.
- Prompt-injection gate plan.
- Policy-violation log schema.
- Human-review route.
- Red-team test cases.

## Demo Scenario

Use a generic enterprise assistant that can summarize customer conversations
and retrieve internal policy snippets. The demo should show that sensitive
personal data and prompt-injection attempts are handled by system controls,
not only by prompt wording.

## Minimum Viable Output

- Three input examples with PII.
- Three prompt-injection examples.
- One safe-output example with redaction.
- One blocked-output example.
- One human-review example.
- One audit log table.

## Policy Event Schema

```yaml
event_id:
trace_id:
timestamp:
user_id:
agent_id:
gate: input | retrieval | tool | memory | output
risk_type: pii | prompt_injection | unsafe_tool | data_boundary | other
detected_pattern:
action: allow | redact | block | human_review
reason:
source_refs:
review_owner:
```

## Example Test Cases

| Case | Risk | Expected control |
|---|---|---|
| user includes phone and ID number | PII | redact or route to human review |
| retrieved doc says ignore system policy | prompt injection | ignore malicious instruction and log |
| user asks for hidden customer details | data boundary | block and cite policy |
| agent tries restricted tool call | tool boundary | reject and log |
| output contains unnecessary personal data | output PII | redact before response |

## Validation Checklist

- [ ] PII detection covers input, retrieval, output, logs, and memory.
- [ ] Prompt-injection checks cover user input and retrieved content.
- [ ] Tool policy is enforced before execution.
- [ ] Human-review path exists for high-risk cases.
- [ ] Logs record gate, risk type, action, and reason.
- [ ] Redaction does not destroy required business context.

## Failure Modes

- PII is masked in output but stored unmasked in logs.
- Prompt injection in retrieved context overrides policy.
- Guardrail is prompt-only and not enforced by code.
- Human-review route is mentioned but not triggered.
- Redaction removes too much context for a useful answer.

## Linked Modules And Labs

- `modules/09-security-red-teaming/`
- `modules/07-ai-gateway-agent-governance/`
- `labs/security/`
- `review/security-review-checklist.md`

## Next Implementation Gate

Build a simple command-line or HTTP demo that accepts text, applies PII and
prompt-injection checks, emits a safe response, and writes a policy event.
