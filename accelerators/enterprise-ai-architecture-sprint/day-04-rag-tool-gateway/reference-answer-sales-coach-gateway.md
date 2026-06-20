# Reference Answer — Sales Coach RAG Tool Gateway

> Instructor / TA only.

## RAG Schema Example

```json
{
  "doc_id": "sales_training_q2",
  "chunk_id": "sales_training_q2_0031",
  "department": "sales",
  "scenario": "objection_handling",
  "source_type": "training_manual",
  "effective_date": "2026-04-01",
  "owner": "HRD",
  "approved_by": "Legal",
  "acl": ["sales", "manager"],
  "risk_level": "medium",
  "citation_required": true,
  "abstain_below_score": 0.72,
  "text": "Synthetic training guidance..."
}
```

## Tool Registry Example

```yaml
tool_id: create_coaching_report
description: Create a synthetic coaching report for a completed role-play session.
owner: sales_enablement
input_schema:
  session_id: string
  score_items: list
output_schema:
  report_id: string
  status: draft | pending_review | created
allowed_agents:
  - sales_coach_agent
allowed_roles:
  - sales_manager
data_classification: synthetic_internal
side_effect: write
timeout_ms: 5000
retry_policy: no_retry_without_idempotency_key
idempotency_key_required: true
approval_required: true
audit_fields:
  - trace_id
  - tool_id
  - user_role
  - decision
  - review_id
```

## Common Mistakes

- Treating `acl` as documentation instead of enforcement input.
- Missing `idempotency_key_required` on write tool.
- No `review_id` for approval-gated report creation.
- Adapter has tools but no evaluator.
