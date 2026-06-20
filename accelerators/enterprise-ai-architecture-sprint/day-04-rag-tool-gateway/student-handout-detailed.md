# Detailed Student Handout — Day 4: RAG Tool Gateway

## 1. 第一結論

Day 4 的任務是把「會做 RAG / 會呼叫 tool」升級成 enterprise gateway integration。企業系統不是讓 agent 自由查資料、自由叫工具，而是讓 Gateway 先解析 identity、policy、data boundary、tool permission、memory scope、audit，再把受控結果交回 agent。

```text
user request
-> gateway identity and policy
-> RAG metadata / ACL filter
-> tool registry permission check
-> memory scope check
-> model / agent runtime
-> output guardrail
-> audit event
```

## 2. Why This Day Exists

Day 1 建立 Gateway 入口，Day 2 建立 governance contracts，Day 3 建立 red-team cases。Day 4 把 RAG、tool registry、MCP-style connector 與 adapter design 接到同一個 Gateway control plane。學生要能證明資料、工具與記憶不是模型自己決定，而是由可檢查的 schema 與 policy 控制。

## 3. RAG Schema

企業 RAG 的核心不是 vector DB，而是 metadata 能否支援權限、時效、引用與拒答。

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
  "text": "..."
}
```

正確區分：

```text
retrieval top-k = 找候選資料
reranker threshold = 判斷候選資料夠不夠好
abstain = 資料不足時拒答或要求澄清
generation top-p = LLM 生成文字的 sampling 參數
```

## 4. Tool Registry

Tool registry 是 Gateway 可讀的工具合約，不是工具名稱清單。

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

最少要有兩種工具：

| Tool | Type | Required control |
|---|---|---|
| `search_training_kb` | read-only | ACL, citation, source freshness |
| `create_coaching_report` | write / side-effect | approval rule, idempotency, audit |

## 5. Agent-Tool Lifecycle

```text
1. Agent proposes tool call.
2. Gateway validates tool exists.
3. Gateway validates caller role and agent scope.
4. Gateway validates input schema.
5. Gateway checks data classification.
6. Gateway checks approval requirement.
7. Tool executes with timeout and retry policy.
8. Gateway validates output schema.
9. Gateway redacts PII if needed.
10. Gateway writes audit event.
11. Agent receives bounded result.
```

重點：tool call 可以由 model 提議，但 tool permission 不能由 model 自己決定。

## 6. MCP / Connector Responsibility Map

MCP-style connector 可以把 KB、SQL、file、workflow 或 external API 暴露給 agent，但每個 connector 都要有 owner、allowed roles、schema、classification、timeout、audit 與 failure mode。

| Connector | Resource | Allowed roles | Boundary | Audit evidence |
|---|---|---|---|---|
| `kb_connector` | public training KB | sales, manager | metadata ACL | source IDs, scores |
| `crm_connector` | synthetic CRM record | manager | approval-gated write | tool decision, review ID |
| `memory_connector` | task memory | same task only | retention and PII rule | memory decision |

## 7. Gateway Integration Note

Gateway integration note 要說清楚：

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

## 8. Adapter / Evaluation Map

Adapter 把 common governance 套到不同任務。

| Adapter | Taxonomy | Tools | Policy | Evaluator |
|---|---|---|---|---|
| sales coach | 開場、探問、異議處理、成交 | KB search, report writer | no customer PII leak, write requires scope | rubric score, citation |
| fraud call analyzer | 假檢警、投資詐騙、釣魚 | risk report generator | high risk routes to review | risk label accuracy |
| HR coach | feedback, conflict, performance | LMS draft writeback | no discriminatory evaluation | feedback quality |

## 9. Required Student Artifacts

1. RAG schema.
2. Tool registry.
3. Agent-tool lifecycle.
4. Gateway integration note.
5. Adapter/evaluation map.

## 10. Common Failure Patterns

| Failure | System risk | Fix |
|---|---|---|
| Metadata is decorative | Retrieval ignores ACL/freshness | Make metadata required in policy input |
| Tool schema has no permission | Agent can call tool outside role | Add allowed roles/agents and approval |
| Retry on write tool duplicates action | Duplicate CRM/report write | Require idempotency key |
| Citation exists but source is not authorized | Data leakage | Filter before retrieval and cite source IDs |
| Memory has no scope | Cross-agent leakage | Define read/write/retention/sharing |

## 11. Source Boundary

Use synthetic records and public-safe workflows only. Do not use real customer
records, real CRM data, private transcripts, credentials, or identifiable
personal data.
