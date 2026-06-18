# Worksheet — Day 2：Agent Governance Framework

> 學生課堂與作業產出模板。請直接在每一區填寫。不要填私人資料、credential、未公開客戶資料或可識別個資。

---

## 0. Team / Submission Metadata

```text
Team name:
Members:
Scenario:
Date:
```

建議 scenario：

```text
Campus IT Helpdesk Assistant
```

---

## 1. Day 1-to-Day 2 Gateway Alignment Note

請把 Day 1 的 minimal gateway mock contract 對應到 Day 2 governance artifacts。

```text
Route:

Request schema fields:

Trusted identity source:

Action extraction method:

Policy decisions needed:

Registered agent:

Read-only tool:

Side-effect tool:

Allowed data sources:

Memory rule:

Human review trigger:

Required audit fields:

Expected HTTP outcomes:
```

### 1.1 Decision Paths

請至少列出三條：

| Path | Example request | Expected decision | Expected HTTP outcome | Required audit evidence |
|---|---|---|---|---|
| Allow path |  |  |  |  |
| Deny path |  |  |  |  |
| Review path |  |  |  |  |

### 1.2 HTTP Outcomes

| Condition | HTTP status | Response status/body summary |
|---|---:|---|
| malformed input | 400 |  |
| invalid token | 401 |  |
| permission denied | 403 |  |
| completed | 200 |  |
| pending review | 200 or 202 |  |

---

## 2. Governance Layer Map

請填寫每層的責任、enforcement、evidence。

| Layer | Responsibility | Enforcement | Evidence |
|---|---|---|---|
| Identity |  |  |  |
| Agent Registry |  |  |  |
| Tool Boundary |  |  |  |
| Data Boundary |  |  |  |
| Memory Boundary |  |  |  |
| Policy Gate |  |  |  |
| Human Review |  |  |  |
| Audit Event |  |  |  |
| Evaluation Hook |  |  |  |
| Red-Team Seed |  |  |  |

請用文字或 diagram 補充 request flow：

```text
User / Channel
->
->
->
```

---

## 3. Common-vs-Adapter Table

請區分 common governance 與 scenario-specific adapter behavior。

| Layer | Common Governance | Adapter-Specific Behavior |
|---|---|---|
| Identity |  |  |
| Tool |  |  |
| Data |  |  |
| Memory |  |  |
| Policy |  |  |
| Audit |  |  |
| Evaluation |  |  |
| Red Team |  |  |

檢查問題：

```text
如果換成銀行內部知識助理，哪些 common governance 不需要改？
如果換成醫療 intake support，哪些 adapter-specific behavior 必須改？
```

---

## 4. Agent Registration Record

請填 YAML 或 JSON。

```yaml
agent_id:
owner:
task_scope:
  -
risk_class:
allowed_users:
  -
allowed_tools:
  -
allowed_data_sources:
  -
memory_scope:
  read:
  write:
  retention:
  shared_memory:
  pii_rule:
approval_required_for:
  -
evaluation_set:
  -
red_team_suite:
  -
audit_events:
  -
```

### 4.1 Consistency Check

| Check | Your answer |
|---|---|
| risk_class 是否符合 allowed tools 的風險？ |  |
| side-effect tools 是否有 approval rule？ |  |
| allowed_data_sources 是否排除不該讀的資料？ |  |
| memory_scope 是否避免不必要 PII？ |  |
| audit_events 是否覆蓋 policy、tool、memory、review？ |  |

---

## 5. Tool Boundary Table

| Tool name | Type | Allowed roles | Required policy decision | Review required? | Rate limit / timeout | Audit fields |
|---|---|---|---|---|---|---|
|  | read-only / side-effect / high-risk side-effect |  |  |  |  |  |
|  | read-only / side-effect / high-risk side-effect |  |  |  |  |  |
|  | read-only / side-effect / high-risk side-effect |  |  |  |  |  |

請回答：

```text
哪一個 tool 風險最高？為什麼？

哪一個 tool 是 read-only 但仍然可能 sensitive？為什麼？

tool schema 與 tool permission 在你的設計中如何分開？
```

---

## 6. Memory Scope Rule

請填寫 memory 規則。

```yaml
memory_scope:
  read:
  write:
  retention:
  shared_memory:
  pii_rule:
  deletion_rule:
  audit_required:
```

請回答：

```text
這個 agent 可以記住什麼？

這個 agent 不可以記住什麼？

memory 是否可以跨 agent 分享？為什麼？

如果 user 要求刪除 session memory，系統應如何處理？
```

---

## 7. Policy Gate Record

請填寫 policy gate。

```yaml
policy_id:
applies_to:
preconditions:
  -
allowed_actions:
  -
blocked_actions:
  -
pii_rule:
retrieval_rule:
tool_rule:
memory_rule:
human_review_trigger:
failure_response:
audit_fields:
  -
```

### 7.1 Policy Decision Examples

| Input situation | Decision | Reason | Safe user message | Audit fields |
|---|---|---|---|---|
|  | allow |  |  |  |
|  | deny |  |  |  |
|  | review |  |  |  |

### 7.2 Optional JSON Shape

Policy input：

```json
{
  "request_id": "",
  "user": {
    "id": "",
    "role": "",
    "tenant": ""
  },
  "agent_id": "",
  "requested_action": "",
  "data_sources": [],
  "tool": "",
  "memory_write": "",
  "client_context": {}
}
```

Policy output：

```json
{
  "decision": "",
  "reason": "",
  "safe_user_message": "",
  "required_reviewer_role": "",
  "audit_fields": []
}
```

---

## 8. Audit Event Schema

請設計 audit event schema。

```json
{
  "trace_id": "",
  "timestamp": "",
  "user_id": "",
  "user_role": "",
  "tenant": "",
  "agent_id": "",
  "request_summary": "",
  "policy_decision": "",
  "policy_reason": "",
  "retrieved_source_ids": [],
  "tool_decisions": [
    {
      "tool_name": "",
      "decision": "",
      "reason": "",
      "executed": false
    }
  ],
  "memory_decision": "",
  "human_review_status": "",
  "outcome": ""
}
```

### 8.1 Audit Completeness Check

| Question | Your answer |
|---|---|
| 是否能重建 request lifecycle？ |  |
| 是否記錄 policy decision？ |  |
| 是否記錄 retrieved source IDs？ |  |
| 是否記錄 tool 是否執行？ |  |
| 是否記錄 memory decision？ |  |
| 是否記錄 human review status？ |  |
| 是否避免保存不必要 PII？ |  |

---

## 9. Risk-Control Map

至少填五個必要風險，也可以增加更多。

| Risk | Example | Required control | Evidence |
|---|---|---|---|
| Tool abuse |  |  |  |
| Memory leakage |  |  |  |
| Permission bypass |  |  |  |
| Prompt-only approval |  |  |  |
| Missing audit detail |  |  |  |
| HTTP outcome mismatch |  |  |  |
| Stale retrieval |  |  |  |
| Prompt injection |  |  |  |
| Excessive agency |  |  |  |

---

## 10. Day 3 Red-Team Seed List

請把 Day 2 的治理假設轉成可測試案例。

```yaml
- test_id:
  threat_category:
  target_control:
  input_message:
  expected_policy_decision:
  expected_http_outcome:
  expected_audit_fields:
    -
  pass_condition:
  failure_signal:
```

請至少填五個：

| Test ID | Threat category | Target control | Expected decision | Expected HTTP outcome |
|---|---|---|---|---|
|  | prompt injection |  |  |  |
|  | permission bypass |  |  |  |
|  | tool abuse |  |  |  |
|  | memory leakage |  |  |  |
|  | audit evasion |  |  |  |

---

## 11. Final Checklist

```text
[ ] Gateway alignment note 明確接回 POST /gateway/requests 或等價 route。
[ ] Request schema fields 至少包含 session_token、channel、raw_message、client_hints、requested_agent。
[ ] Trusted identity 由 server-side 解析，不相信 client role。
[ ] 至少有 allow、deny、review_required 三條 decision path。
[ ] 至少有 200、400、401、403 四種 HTTP outcome。
[ ] Governance layer map 包含 identity、registry、tool、data、memory、policy、audit、review、evaluation、red-team。
[ ] Common governance 和 adapter-specific behavior 有清楚分離。
[ ] Agent registration record 欄位完整。
[ ] Tool boundary 分清 read-only、side-effect、high-risk side-effect。
[ ] Memory scope 有 read/write/retention/sharing/PII rule。
[ ] Policy gate 可回傳 allow、deny、review。
[ ] Audit event 能重建 request lifecycle，不只記 final answer。
[ ] Risk-control map 有 control 與 evidence。
[ ] Day 3 red-team seeds 有 expected decision、HTTP outcome、audit fields。
[ ] 沒有使用私人資料、credential、客戶秘密或可識別個資。
```
