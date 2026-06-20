# Worksheet — Day 4: RAG Tool Gateway

## 1. RAG Schema

```json
{
  "doc_id": "",
  "chunk_id": "",
  "department": "",
  "scenario": "",
  "source_type": "",
  "effective_date": "",
  "owner": "",
  "approved_by": "",
  "acl": [],
  "risk_level": "",
  "citation_required": true,
  "abstain_below_score": 0.0,
  "text": ""
}
```

## 2. Tool Registry

```yaml
tool_id:
description:
owner:
input_schema:
output_schema:
allowed_agents:
allowed_roles:
data_classification:
side_effect:
timeout_ms:
retry_policy:
idempotency_key_required:
approval_required:
audit_fields:
```

## 3. Agent-Tool Lifecycle

| Step | Decision | Evidence |
|---|---|---|
| Agent proposes tool call |  |  |
| Gateway validates tool exists |  |  |
| Gateway validates caller role |  |  |
| Gateway validates input schema |  |  |
| Gateway checks approval |  |  |
| Tool executes or routes review |  |  |
| Gateway validates output |  |  |
| Gateway writes audit |  |  |

## 4. Connector Responsibility Map

| Connector | Resource | Allowed roles | Boundary | Audit evidence |
|---|---|---|---|---|
|  |  |  |  |  |

## 5. Gateway Integration Note

```text
Route:
Trusted identity:
RAG sources and ACL:
Allowed tools:
Blocked tools:
Memory rule:
Policy decisions:
Human review trigger:
Audit fields:
HTTP outcomes:
```

## 6. Adapter / Evaluation Map

| Adapter | Taxonomy | Tools | Policy | Evaluator |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

## 7. Final Checklist

- [ ] Metadata supports ACL and freshness.
- [ ] Retrieval has citation and abstain behavior.
- [ ] Tools have permissions and side-effect classification.
- [ ] Side-effect tools have approval and idempotency.
- [ ] Gateway integration includes audit and HTTP outcomes.
- [ ] Source boundary is public-safe.
