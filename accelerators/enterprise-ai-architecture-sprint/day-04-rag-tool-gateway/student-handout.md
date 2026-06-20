# Student Handout — Day 4: RAG Tool Gateway

This is the summarized Day 4 handout. It preserves the chapter structure of
`student-handout-detailed.md`.

## 1. 第一結論

Enterprise RAG/tool use is governed by schema, permission, policy, audit, and
evaluation. The model may propose retrieval or a tool call; the Gateway decides
whether it is allowed.

## 2. Why This Day Exists

Day 4 connects RAG, tool registry, MCP-style connectors, and adapters to the AI
Gateway control plane so data/tool/memory access is enforceable.

## 3. RAG Schema

Your RAG schema must include document/chunk ID, department, scenario, source
type, effective date, owner, approved_by, ACL, risk level, citation rule,
threshold, and abstain behavior.

## 4. Tool Registry

Your tool registry must include owner, input/output schema, allowed agents,
allowed roles, data classification, side effect, timeout, retry, idempotency,
approval, and audit fields.

## 5. Agent-Tool Lifecycle

```text
propose -> validate tool -> validate caller -> validate schema -> check policy
-> review if needed -> execute -> validate output -> redact -> audit -> bounded result
```

## 6. MCP / Connector Responsibility Map

Every connector needs owner, resource, allowed roles, boundary, and audit
evidence. Do not let agents directly read KB/SQL/files/workflows without the
Gateway boundary.

## 7. Gateway Integration Note

Submit route, trusted identity, RAG sources, allowed/blocked tools, memory rule,
policy decisions, review trigger, audit fields, and HTTP outcomes.

## 8. Adapter / Evaluation Map

Define three adapters and name taxonomy, tools, policy, and evaluator for each.

## 9. Required Student Artifacts

1. RAG schema.
2. Tool registry.
3. Agent-tool lifecycle.
4. Gateway integration note.
5. Adapter/evaluation map.

## 10. Common Failure Patterns

Avoid decorative metadata, tool schemas without permissions, write retries
without idempotency, unauthorized citation sources, and memory without scope.

## 11. Source Boundary

Use synthetic data only.
