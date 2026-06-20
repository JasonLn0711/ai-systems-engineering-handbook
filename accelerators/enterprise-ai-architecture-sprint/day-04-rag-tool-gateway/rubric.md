# Rubric — Day 4: RAG Tool Gateway

## Scoring Summary

| Category | Points |
|---|---:|
| RAG schema quality | 25 |
| Tool governance | 25 |
| Lifecycle and audit | 20 |
| Gateway integration | 15 |
| Adapter and evaluation | 10 |
| Source boundary | 5 |
| **Total** | **100** |

## Criteria

| Category | Full-credit standard |
|---|---|
| RAG schema quality | Metadata supports ACL, freshness, citation, rerank threshold, and abstain. |
| Tool governance | At least two tools, typed schemas, permissions, side effects, approval, timeout, retry, idempotency, audit. |
| Lifecycle and audit | Lifecycle includes proposal, validation, policy, review, execution, output validation, redaction, audit. |
| Gateway integration | Route, trusted identity, data/tool/memory boundary, policy decisions, review, HTTP outcomes. |
| Adapter and evaluation | Three adapters with taxonomy, tools, policy, evaluator. |
| Source boundary | Synthetic and public-safe. |

## TA Workflow

1. Verify required artifacts exist.
2. Grade RAG and tool contracts before prose quality.
3. Inspect whether Gateway, not model, owns the decision boundary.
4. Apply source-boundary score last.
