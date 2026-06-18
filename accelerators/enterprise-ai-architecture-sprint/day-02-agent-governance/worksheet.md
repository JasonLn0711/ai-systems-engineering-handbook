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
Classifier output fields: intent labels / action candidates / risk labels / missing slots / ambiguity / confidence / recommended next step
Safe-default rule for low-risk high-confidence action:
Safe-default rule for high-risk or low-confidence action:

Policy decisions needed:

Registered agent:

Read-only tool:

Side-effect tool:

Allowed data sources:

Memory rule:

Message mediation path:

Declassification or redaction rule:

Replay or expiration rule:

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
| Mediated Message Boundary |  |  |  |
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
| Message Mediation |  |  |
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
allowed_message_channels:
  produce:
  consume:
output_classification:
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
| allowed_message_channels 是否避免 low-trust agent 讀 raw privileged topic？ |  |
| output_classification 是否符合 user role？ |  |
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
message_rule:
declassification_rule:
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
  "message_channel": "",
  "requested_output_classification": "",
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

## 8. Message Mediation Contract

請填寫跨 agent、process、tool 或 broker/queue 的受控通訊規則。若你的設計不使用
Kafka、Redpanda、RabbitMQ 或 NATS，也要為 gateway path 或 tool gateway 填寫同等欄位。

```yaml
message_mediation:
  request_channel_or_topic:
  result_channel_or_topic:
  producer_identity:
  consumer_identity:
  allowed_message_classification:
  raw_payload_allowed: yes | no
  resource_reference_pattern:
  required_schema_fields:
    -
  retention_rule:
  replay_protection:
  dead_letter_handling:
  audit_event_name:
declassification:
  high_sensitivity_input:
  allowed_output_classification:
  redaction_rule:
  human_review_required_for:
```

檢查問題：

```text
低權限 agent 是否能直接讀 high-privilege raw result？
raw secret payload 是否會進入 shared topic、log、cache、trace 或 DLQ？
message 是否有 classification、purpose、expires_at、trace_id？
consumer 是否在處理前重新檢查 policy？
```

---

## 9. Audit Event Schema

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
  "message_channel": "",
  "output_classification": "",
  "human_review_status": "",
  "outcome": ""
}
```

### 9.1 Audit Completeness Check

| Question | Your answer |
|---|---|
| 是否能重建 request lifecycle？ |  |
| 是否記錄 policy decision？ |  |
| 是否記錄 retrieved source IDs？ |  |
| 是否記錄 tool 是否執行？ |  |
| 是否記錄 memory decision？ |  |
| 是否記錄 message channel 與 output classification？ |  |
| 是否記錄 human review status？ |  |
| 是否避免保存不必要 PII？ |  |

---

## 10. Risk-Control Map

至少填五個必要風險，也可以增加更多。

| Risk | Example | Required control | Evidence |
|---|---|---|---|
| Tool abuse |  |  |  |
| Memory leakage |  |  |  |
| Permission bypass |  |  |  |
| Confused deputy |  |  |  |
| Broker payload leakage |  |  |  |
| Replay of privileged result |  |  |  |
| Missing schema field |  |  |  |
| Prompt-only approval |  |  |  |
| Missing audit detail |  |  |  |
| HTTP outcome mismatch |  |  |  |
| Stale retrieval |  |  |  |
| Prompt injection |  |  |  |
| Excessive agency |  |  |  |

---

## 11. Day 3 Red-Team Seed List

請把 Day 2 的治理假設轉成可測試案例。

```yaml
- test_id:
  threat_category:
  target_control:
  input_message:
  expected_policy_decision:
  expected_message_channel:
  expected_output_classification:
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
|  | confused deputy |  |  |  |
|  | broker payload leakage |  |  |  |
|  | replay / expired capability |  |  |  |

---

## 12. Final Checklist

```text
[ ] Gateway alignment and message mediation note 明確接回 POST /gateway/requests 或等價 route。
[ ] Request schema fields 至少包含 session_token、channel、raw_message、client_hints、requested_agent。
[ ] Trusted identity 由 server-side 解析，不相信 client role。
[ ] 至少有 allow、deny、review_required 三條 decision path。
[ ] 至少有 200、400、401、403 四種 HTTP outcome。
[ ] Governance layer map 包含 identity、registry、tool、data、memory、policy、audit、review、evaluation、red-team。
[ ] Governance layer map 包含 mediated message boundary。
[ ] Common governance 和 adapter-specific behavior 有清楚分離。
[ ] Agent registration record 欄位完整。
[ ] Tool boundary 分清 read-only、side-effect、high-risk side-effect。
[ ] Memory scope 有 read/write/retention/sharing/PII rule。
[ ] Message mediation contract 有 producer、consumer、classification、schema、retention、replay、DLQ 規則。
[ ] Raw privileged payload 不會進入 low-trust agent 可讀的 topic、queue、log、cache、trace 或 DLQ。
[ ] Declassification 或 redaction rule 清楚。
[ ] Policy gate 可回傳 allow、deny、review。
[ ] Audit event 能重建 request lifecycle，不只記 final answer。
[ ] Risk-control map 有 control 與 evidence。
[ ] Day 3 red-team seeds 有 expected decision、HTTP outcome、audit fields。
[ ] 沒有使用私人資料、credential、客戶秘密或可識別個資。
```
