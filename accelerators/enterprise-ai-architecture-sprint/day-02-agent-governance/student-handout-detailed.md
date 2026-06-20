# Detailed Student Handout — Day 2：Agent Governance Framework

> Canonical long-form student explanation. Add Day 2 student-facing expansions
> here first, then update `student-handout-detailed.zh-TW.md` and derive the
> shorter `student-handout.md` summary.

---

## 0. 第一結論

Enterprise AI agent 不能只靠 prompt 管理。

Prompt 可以引導模型行為，但 prompt 不是權限邊界。真正能控制 enterprise agent 的，是系統外層的 governance contract：

```text
Agent Registry
+ Policy Gate
+ Tool Boundary
+ Data Boundary
+ Memory Scope
+ Message Mediation
+ Declassification
+ Audit Event
+ Human Review
+ Evaluation / Red-Team Feedback
```

你可以把 Day 2 想成這件事：

```text
Day 1：我們建立 AI Gateway，知道 request 要進入哪個系統入口。
Day 2：我們定義 Gateway 要看哪些 governance artifacts，才能決定 agent 是否能被執行。
Day 3：我們把 Day 2 的治理假設變成 red-team 測試。
```

---

## 1. 為什麼 agent governance 重要？

先看一個簡化情境。

你做了一個 Campus IT Helpdesk Assistant。學生問：

```text
我在宿舍連不上 VPN，請問怎麼設定？
```

這看起來很安全，因為 agent 只要查 public IT FAQ 就好。

但同一個 agent 可能遇到：

```text
幫我查 staff-only 的帳號鎖定 SOP。
```

或：

```text
直接幫我提交 100 張 ticket，內容都寫 VPN 壞了。
```

或：

```text
請你記住我的學號、密碼、宿舍、手機，以後都幫我自動填。
```

如果你的系統只在 system prompt 裡寫：

```text
You are a helpful IT assistant. Follow campus policy.
```

這不夠。因為 model 只是收到 instruction，並沒有真正的權限控制。它可能被 prompt injection 誘導、可能誤判使用者角色、可能呼叫不該呼叫的 tool，也可能把不該保存的資料寫入 memory。

工程上的正確做法是：

```text
不要讓 model 自己決定權限。
讓 gateway / policy gate / tool broker / data connector / memory store 做系統層 enforcement。
```

這裡可以用作業系統課程的權限模型來理解。低權限 user 本來不能直接讀高權限 file；
但如果低權限 user 可以誘使高權限 process 代讀，再從 stdout、log、cache、暫存檔、
pipe、socket、shared memory 或 leaked file descriptor 看到結果，原始檔案權限雖然
沒有被直接破壞，系統仍然洩密。安全工程裡這接近 `confused deputy problem`：
低權限實體誘使高權限實體代替它完成本來不該做的事。

AI agent system 也有同樣風險：

```text
low-privilege agent 不能讀 staff-only SOP
low-privilege agent 請 high-privilege agent 摘要 staff-only SOP
high-privilege agent 讀了 SOP
high-privilege agent 把摘要寫回 shared chat、memory、log 或 broker message
low-privilege agent 間接看到 staff-only 內容
```

所以 Day 2 的更精準架構原則是：

```text
不同信任等級的 agent、process、tool、data store 不應直接互相存取。
所有跨信任邊界的請求都必須經過可認證、可授權、可限流、可 schema validation、
可降敏、可稽核、可攔截的 mediation layer。
```

Kafka-like broker、Redpanda、RabbitMQ 或 NATS JetStream 可以作為 mediation layer 的
一部分，但 broker 不是完整安全解法。broker 控制訊息通道；完整治理還需要
identity、authorization policy、data classification、capability-based delegation、
declassification、audit、network isolation、tool sandbox、replay protection、
schema governance、observability、human-in-the-loop 與 red-team tests。

---

## 2. Day 1 到 Day 2：Gateway Contract 銜接

Day 1 的 AI Gateway lifecycle：

```text
User
-> Channel/API
-> Auth/RBAC
-> AI Gateway
-> Policy
-> Agent/Tool/RAG/Model
-> Guardrail
-> Audit
-> Human Review
```

Day 1 的 minimal gateway mock route：

```http
POST /gateway/requests
```

可能收到的 request：

```json
{
  "session_token": "demo-token-abc",
  "channel": "web",
  "raw_message": "我在宿舍連不上 VPN，請問怎麼設定？",
  "client_hints": {
    "locale": "zh-TW",
    "requested_department": "campus_it"
  },
  "requested_agent": "campus_it_helpdesk_agent"
}
```

這裡有一個重要觀念：

```text
client_hints 只是提示，不是可信任權限來源。
```

也就是說，client 送來的 `requested_department`、`requested_agent`、`role`、`tenant` 都不能直接相信。真正可信任的 identity、role、permission 必須由 server-side 解析，例如：

```text
session_token
-> server-side session store
-> user_id
-> user_role
-> tenant
-> permission set
```

Day 2 要補上的 governance artifacts，會被 Gateway 用在這些位置：

```text
POST /gateway/requests
-> schema validation
-> token and identity resolution
-> action extraction
-> agent registry lookup
-> tool/data/memory scope check
-> message mediation and declassification check
-> policy gate decision
-> optional human review
-> audited execution
-> HTTP outcome
```

如果 Day 2 進一步設計 multi-agent 或 queue-based workflow，跨 agent 溝通也應該走
同一套 contract：

```text
Agent A -> Gateway / Broker / Tool Gateway -> Policy Gate -> Agent B or Tool Service
```

不要讓低信任 agent 直接 HTTP call 高信任 agent，也不要讓所有 agent 共用一個
`agent.messages` topic。broker 應該傳遞 structured request、metadata、
resource reference、policy decision、redacted result 與 audit event；除非 topic、
retention、encryption、consumer ACL、audit、DLQ 都經過嚴格設計，否則不要把 raw
secret payload 或 staff-only 原文放進 message。

---

## 3. Day 2 的核心 mental model

請先記住這張圖：

```text
User / Channel
-> Auth / RBAC
-> AI Gateway
-> Agent Registry
-> Policy Gate
-> Tool Broker
-> RAG Connector
-> Memory Store
-> Message Broker / Mediation Layer
-> Declassifier
-> Model Runtime
-> Guardrail
-> Audit Event Store
-> Human Review Queue
-> Evaluation / Red-Team Feedback
```

每個元件有不同責任：

| Subsystem | 學生版定義 | 工程版定義 | Day 2 Artifact |
|---|---|---|---|
| Auth / RBAC | 確認你是誰、你是什麼角色 | Resolve authenticated principal, role, tenant, permission set | allowed users |
| Agent Registry | 記錄 agent 的可用範圍 | Version-controlled configuration contract for routing and governance | registration record |
| Policy Gate | 執行前判斷可不可以做 | Decision API returning `allow` / `deny` / `review` | policy gate record |
| Tool Broker | 管理工具能不能被呼叫 | Enforces tool schema, permission, timeout, retry, idempotency, audit | tool boundary table |
| RAG Connector | 控制可以查哪些資料 | Retrieval layer with metadata filters and access control | data boundary |
| Memory Store | 控制可讀寫哪些記憶 | Memory read/write/retention/sharing rules | memory scope |
| Message Broker / Mediation Layer | 控制 agent、process、tool 之間怎麼傳遞請求 | Kafka/Redpanda/RabbitMQ/NATS topic or queue governance with identity, schema, ACL, retention, replay control | message mediation contract |
| Declassifier | 決定高敏感資料能否降敏後交給低權限角色 | Redaction, summarization, output classification, review before crossing trust zones | declassification rule |
| Model Runtime | 實際產生回答 | LLM inference or agent runtime | model boundary |
| Guardrail | 檢查輸出是否違規或需審查 | Output and action safety checks | guardrail decision |
| Audit Store | 保存可審查 evidence | Append-only event store for lifecycle reconstruction | audit event schema |
| Human Review Queue | 高風險動作等待人審 | State machine for pending/approved/rejected review | review state |
| Evaluation / Red Team | 測試治理是否有效 | Regression tests, adversarial tests, policy tests | red-team seeds |

---

## 4. 核心術語

| 詞彙 | 初學者解釋 | 工程解釋 |
|---|---|---|
| `AI Gateway` | AI 系統的入口，負責接 request、驗證、路由、記錄 | A service boundary that validates requests, resolves identity, applies policy, routes to agents/tools/models, records audit events |
| `Agent Registry` | agent 的登記表 | Versioned configuration contract describing owner, scope, risk, allowed users, tools, data sources, memory, evaluation, audit |
| `Task Scope` | agent 被允許做的事情 | Explicit task boundary used by routing, policy, review, and evaluation |
| `Tool Boundary` | agent 能用哪些工具、在什麼條件下用 | Enforcement rules for tool permission, side effects, timeout, retries, rate limits, idempotency, audit |
| `Read-only Tool` | 只查資料，不改變外部狀態 | Tool that does not mutate external system state, such as search or lookup |
| `Side-effect Tool` | 會改變外部狀態的工具 | Tool that creates, updates, deletes, sends, submits, charges, resets, or triggers external actions |
| `Data Boundary` | agent 可以查哪些資料 | Retrieval constraints using source allowlist, metadata filters, document version, access level |
| `Memory Scope` | agent 可以記住什麼、記多久、能不能分享 | Read/write/retention/sharing/deletion rule for conversational or long-term memory |
| `Mediated Message Boundary` | agent 之間或 agent 到 tool 之間的受控通道 | Gateway, broker, queue, or tool gateway path with identity, schema, policy, ACL, retention, replay protection, and audit |
| `Confused Deputy` | 高權限 helper 被低權限 caller 誘導去做不該做的事 | A low-privilege agent induces a high-privilege agent/tool to read, write, or reveal data on its behalf |
| `Declassification` | 把高敏感資料轉成可釋出的低敏感輸出 | Redaction, summarization, field removal, policy check, and review before returning data to a lower trust zone |
| `Capability-Based Delegation` | 一次性、小範圍、短時間的授權 | Short-lived token, signed URL, decision token, or scoped credential instead of broad standing privilege |
| `Policy Gate` | 執行前做 allow / deny / review 判斷 | Decision API that evaluates request, identity, action, agent, tool, data, memory, and context |
| `Audit Event` | 留下可審查證據 | Structured event that reconstructs request lifecycle, policy decisions, source IDs, tool decisions, memory decision, review state, outcome |
| `Human Review` | 需要人核准才能繼續 | Workflow state for high-risk or side-effect actions |
| `Evaluation Hook` | 自動測試點 | Connection from production assumptions to tests, eval sets, and regression checks |
| `Red-Team Seed` | 下次攻防測試的種子案例 | Testable adversarial scenario derived from governance assumptions |

---

## 5. 真實世界案例：Campus IT Helpdesk Assistant

### 5.1 情境

校園 IT helpdesk 想做一個 AI assistant。學生可以問 VPN、Wi-Fi、帳號登入、服務狀態等問題。

安全邊界：

```text
學生可以查 public IT FAQ。
學生可以查 VPN setup guide。
學生可以查 service status page。
學生不能查 staff-only SOP。
agent 可以草擬 ticket。
agent 不能未經 review 直接 submit ticket。
agent 不能把學生 PII 寫入 shared memory。
```

### 5.2 資料來源

| Data Source | 類型 | 允許對象 | metadata 範例 |
|---|---|---|---|
| `public_it_faq` | public FAQ | student、staff | `access_level=public`, `department=it`, `version=2026-01` |
| `vpn_setup_guide` | public guide | student、staff | `access_level=public`, `topic=vpn`, `effective_date=2026-01-15` |
| `service_status_page` | public status | student、staff | `access_level=public`, `freshness=live` |
| `staff_account_lock_sop` | staff-only SOP | staff、it_reviewer | `access_level=staff_only`, `topic=account_lock` |

### 5.3 Tools

| Tool | 類型 | 作用 | 風險 | Governance control |
|---|---|---|---|---|
| `search_it_faq` | read-only | 查 public IT FAQ | 查到過期或錯誤文件 | metadata filter、source version、citation |
| `lookup_service_status` | read-only | 查服務狀態 | 狀態延遲或錯誤 | freshness check、source timestamp |
| `draft_ticket` | no external side effect | 產生 ticket 草稿 | 草稿內容錯誤 | user confirmation、audit |
| `submit_ticket` | side-effect | 建立 ticket | spam、錯誤提交、冒用身分 | human review、rate limit、audit |
| `reset_password` | high-risk side-effect | 重設密碼 | 帳號被惡意操作 | deny by default、strong auth、staff-only workflow |

重點：

```text
tool schema 只描述怎麼呼叫 tool。
tool permission 決定誰可以呼叫 tool。
這兩件事不能混在一起。
```

---

## 6. Common Governance vs Adapter-Specific Behavior

Enterprise system 不應該每接一個客戶就重寫一套 governance。你要把「可重用治理邏輯」與「情境特定行為」分開。

| Layer | Common Governance | Adapter-Specific Behavior |
|---|---|---|
| Identity | user、role、tenant、service account、agent identity | 校園角色：student、staff、it_reviewer |
| Tool | schema、permission、timeout、retry、rate limit、idempotency | `search_it_faq`、`submit_ticket` |
| Data | metadata filter、access level、document version | public FAQ vs staff SOP |
| Memory | retention、sharing、deletion、PII handling | Helpdesk 只保留 session note |
| Message Mediation | schema、topic/queue ACL、producer/consumer identity、classification、retention、replay control | support-safe request/result channel；student agent 不能讀 raw staff-only topic |
| Policy | allowed tasks、blocked tasks、risk class、approval rule | ticket submission requires review |
| Audit | trace ID、source IDs、tool decisions、policy decision | helpdesk audit report format |
| Evaluation | success、safety、latency、coverage | VPN 答案需引用最新 guide |
| Red Team | threat taxonomy、test harness | staff SOP bypass、ticket spam |

簡單說：

```text
Common governance 是平台能力。
Adapter-specific behavior 是業務情境映射。
```

---

## 7. Control Plane vs Data Plane

這是系統工程裡很重要的分層。

| 平面 | 責任 | Day 2 例子 |
|---|---|---|
| Control Plane | 決定是否可以做、誰可以做、是否需要審查、要留下什麼 evidence | registry、policy、approval、audit、review queue |
| Data Plane | 實際處理資料、查文件、呼叫工具、產生回答 | RAG retrieval、tool execution、model response |

常見錯誤是把高風險 decision 放到 data plane，例如讓 model 自己決定：

```text
「我覺得使用者應該可以看這份 SOP。」
```

工程上更好的做法是：

```text
model 可以提出 intent。
policy gate 做 decision。
tool broker / data connector 執行 enforcement。
audit event 留下 evidence。
```

---

## 8. Artifact 1：Day 1-to-Day 2 Gateway Alignment Note

你要填出一份 alignment note，說明 Day 1 的 `POST /gateway/requests` 如何使用 Day 2 governance artifacts。

### 8.1 Template

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
Message mediation path:
Declassification or redaction rule:
Replay or expiration rule:
Human review trigger:
Required audit fields:
Expected HTTP outcomes:
```

### 8.2 填寫提醒

你的 note 至少要包含：

- `POST /gateway/requests` 或等價 route。
- request schema 如何包含 `session_token`、`channel`、`raw_message`、`client_hints`、`requested_agent`。
- 可信任 identity 由 server-side 解析，而不是相信 client。
- 至少一個 `allow` 路徑。
- 至少一個 `deny` 路徑。
- 至少一個 `review_required` 路徑。
- 至少 `200`、`400`、`401`、`403` 四種 HTTP outcome。
- audit fields 能證明 policy、retrieval、tool、memory、review decision。
- message mediation path 能說明跨 agent、process、tool、retrieval service 的請求
  走 gateway、broker、queue 或 tool gateway，而不是直接跨信任邊界呼叫。
- declassification rule 能說明高敏感資料如何 redacted、summarized、reviewed
  後才可回到低權限角色。
- replay 或 expiration rule 能說明舊的高權限結果不會在授權過期後再次生效。

### 8.3 實作角度

如果你用 Python 實作 gateway mock，可以使用：

- `FastAPI`：建立 `POST /gateway/requests` route。
- `Pydantic`：定義 request / response schema。
- `SQLAlchemy` 或 `psycopg`：讀 agent registry 或 audit event store。
- `OpenTelemetry SDK`：產生 trace / span。
- `structlog` 或 Python `logging`：輸出結構化 log。
- `OPA`：作為外部 policy decision engine 的例子。
- `Redpanda` / `Apache Kafka` / `RabbitMQ` / `NATS JetStream`：作為 message mediation 或 job queue 的例子。
- `Confluent Schema Registry` 或 JSON Schema validation：管理 message schema 與 required fields。
- `Redis`：短期 session memory 或 rate limit。
- `PostgreSQL`：audit event store。

注意：Day 2 不要求你完成完整實作，但你的 artifacts 要能讓這些元件被實作出來。

---

## 9. Artifact 2：Governance Layer Map

### 9.1 你要畫什麼？

請畫出或用文字列出：

```text
Identity
-> Agent Registry
-> Tool Boundary
-> Data Boundary
-> Memory Boundary
-> Mediated Message Boundary
-> Policy Gate
-> Audit Event
-> Human Review
-> Evaluation Hook
-> Red-Team Seed
```

### 9.2 每層要寫什麼？

每層至少寫：

1. 這層的責任。
2. 這層 enforce 什麼。
3. 這層留下什麼 evidence。

範例格式：

| Layer | Responsibility | Enforcement | Evidence |
|---|---|---|---|
| Identity | 確認 user 與 role | server-side token resolution | `user_id`, `user_role`, `tenant` |
| Mediated Message Boundary | 控制跨 agent / process / tool 的請求路徑 | broker topic ACL, producer/consumer identity, schema validation, retention | `message_channel`, `producer`, `consumer`, `classification` |
| Policy Gate | 決定 allow / deny / review | decision API | `policy_decision`, `reason` |
| Audit Event | 保存 request lifecycle evidence | append-only event record | `trace_id`, `tool_decisions`, `outcome` |

---

## 10. Artifact 3：Common-vs-Adapter Table

你要展示哪些 governance 是共用平台能力，哪些是 Campus IT 這個情境的映射。

Template：

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

檢查原則：

```text
如果換成銀行內部知識助理還能沿用，通常是 common governance。
如果只跟校園 IT 情境有關，通常是 adapter-specific behavior。
```

---

## 11. Artifact 4：Agent Registration Record

Agent Registry 是 configuration contract，不是單純 agent 名單。

### 11.1 Template

```yaml
agent_id:
owner:
task_scope:
  -
risk_class: low | medium | high
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

### 11.2 欄位說明

| 欄位 | 目的 | 常見錯誤 |
|---|---|---|
| `agent_id` | Gateway routing 與 audit 用的唯一 ID | 使用自然語言名稱，無法穩定引用 |
| `owner` | incident 發生時的負責單位 | 留空或寫「AI team」但沒有責任邊界 |
| `task_scope` | agent 被允許做的工作 | 寫太大，例如 `answer anything` |
| `risk_class` | 決定 review / monitoring 強度 | 工具有 side effect 卻標 low |
| `allowed_users` | 可呼叫此 agent 的角色 | 只寫 `all users` |
| `allowed_tools` | 可使用工具 | 沒區分 read-only 與 side-effect |
| `allowed_data_sources` | 可查資料來源 | 忘記排除 staff-only source |
| `memory_scope` | 可讀寫 memory 範圍 | 寫入 shared memory 但沒有 PII rule |
| `allowed_message_channels` | 可讀寫哪些 topic、queue、gateway path | 所有 agent 共用 `agent.messages` |
| `output_classification` | agent 可輸出的最高資料等級 | 高權限 agent 直接回傳 raw staff-only content |
| `approval_required_for` | 需要審核的 action | submit 類工具沒有 review |
| `evaluation_set` | 回歸測試與品質測試 | 沒有可測試名稱 |
| `red_team_suite` | 攻防測試 seed | 只寫「安全測試」 |
| `audit_events` | 必須記錄的事件類型 | 只記 final answer |

---

## 12. Artifact 5：Policy Gate Record

Policy gate 是 decision API。它不是一句「請遵守校園政策」。

### 12.1 Policy Input Shape

```json
{
  "request_id": "req-001",
  "user": {
    "id": "student_001",
    "role": "student",
    "tenant": "campus_demo"
  },
  "agent_id": "campus_it_helpdesk_agent",
  "requested_action": "submit_ticket",
  "data_sources": ["public_it_faq"],
  "tool": "submit_ticket",
  "memory_write": "session_summary",
  "message_channel": "agent.requests.support",
  "requested_output_classification": "student_support_safe",
  "client_context": {
    "channel": "web",
    "locale": "zh-TW"
  }
}
```

### 12.2 Policy Output Shape

```json
{
  "decision": "review",
  "reason": "submit_ticket is a side-effect action and requires human review",
  "required_reviewer_role": "it_reviewer",
  "safe_user_message": "此動作需要 IT reviewer 審核後才會提交。",
  "audit_fields": [
    "request_id",
    "user.role",
    "agent_id",
    "tool",
    "decision",
    "reason"
  ]
}
```

### 12.3 Policy Gate Template

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

### 12.4 allow / deny / review 的差異

| Decision | 意義 | Campus IT 範例 | HTTP outcome |
|---|---|---|---|
| `allow` | 可以執行 | 學生查 public VPN guide | `200 completed` |
| `deny` | 不可執行 | 學生要求 staff-only SOP | `403 denied` |
| `review` | 暫停，等待人審 | 建立 ticket 或高風險 side-effect | `200 pending_review` 或 `202 pending_review` |
| schema failure | request 格式不合 | 缺 `raw_message` | `400 malformed_input` |
| auth failure | token 無效 | `session_token` 無效 | `401 invalid_token` |

---

## 13. Artifact 6：Audit Event Schema

Audit event 不是 debug log。

Debug log 主要幫工程師排錯；audit event 要能讓未來的人重建：

```text
誰提出 request？
Gateway 解析出什麼 identity？
選到哪個 agent？
查了哪些資料？
policy gate 做了什麼 decision？
tool 是否被呼叫？
memory 是否被讀寫？
是否進 human review？
最後 outcome 是什麼？
```

### 13.1 最小 audit event shape

```json
{
  "trace_id": "req-0001",
  "timestamp": "2026-06-14T10:00:00+08:00",
  "user_id": "student_001",
  "user_role": "student",
  "tenant": "campus_demo",
  "agent_id": "campus_it_helpdesk_agent",
  "request_summary": "User asked for VPN setup help",
  "policy_decision": "review",
  "policy_reason": "submit_ticket is a side-effect action",
  "retrieved_source_ids": ["vpn-guide-2026-01"],
  "tool_decisions": [
    {
      "tool_name": "submit_ticket",
      "decision": "review",
      "reason": "side-effect action requires IT reviewer"
    }
  ],
  "memory_decision": "session_only_no_shared_pii",
  "message_channel": "agent.results.support.redacted",
  "output_classification": "student_support_safe",
  "human_review_status": "pending",
  "outcome": "answer_returned_ticket_pending"
}
```

### 13.2 不要存什麼？

Audit event 不是把所有東西都存下來。尤其要小心：

- 不必要的密碼、token、完整 credential。
- 完整 PII，例如身分證字號、手機、地址。
- private document content。
- 原始 prompt 裡的敏感內容。

更好的做法：

```text
存 summary、hash、source ID、document version、policy reason、decision metadata。
```

---

## 14. Artifact 7：Risk-Control Map

Template：

| Risk | Example | Required Control | Evidence |
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

你至少要包含這五個：

| Risk | Example | Required Control | Evidence |
|---|---|---|---|
| Tool abuse | agent 重複提交 ticket | tool boundary、approval、rate limit | tool decision log |
| Memory leakage | PII 進入 shared memory | memory scope、retention、deletion | memory decision |
| Permission bypass | student 讀 staff SOP | retrieval rule、metadata filter | source filter log |
| Confused deputy | student agent 請 staff agent 讀 staff-only SOP 並回傳摘要 | policy 同時檢查 original user、requesting agent、resource、purpose、output classification | denied delegation decision |
| Broker payload leakage | staff-only 原文被 publish 到 shared topic 或 DLQ | topic ACL、no raw secret payload、consumer allowlist、short retention | broker audit、schema validation |
| Replay of privileged result | 舊 approval 或高權限結果在過期後被重新 consume | `expires_at`、nonce、idempotency key、policy re-check on consume | replay denial audit |
| Missing schema field | message 沒有 classification 卻被當 public | required schema fields、schema registry、default deny | schema rejection event |
| Prompt-only approval | model 自稱 approved | policy gate | policy decision |
| Missing audit detail | 無法知道 tool 是否執行 | audit schema | complete audit event |

---

## 15. Artifact 8：Day 3 Red-Team Seed List

Day 3 會把你今天的治理假設拿來測試。

Red-team seed 不是隨便寫「攻擊」。它要能被執行、被判斷成功或失敗。

### 15.1 Template

```yaml
test_id:
threat_category:
target_control:
input_message:
expected_policy_decision: allow | deny | review
expected_http_outcome:
expected_audit_fields:
pass_condition:
failure_signal:
```

### 15.2 範例 seed 方向

| Threat Category | 測試目的 |
|---|---|
| prompt injection | 測試 model 是否會被誘導忽略 policy |
| permission bypass | 測試 student 是否能讀 staff-only SOP |
| tool abuse | 測試 side-effect tool 是否被濫用 |
| memory leakage | 測試 PII 是否被寫入 shared memory |
| audit evasion | 測試 audit event 是否缺欄位 |
| HTTP outcome mismatch | 測試 policy decision 與 HTTP response 是否一致 |
| confused deputy | 測試低權限 agent 是否能誘使高權限 agent 代讀資料 |
| broker payload leakage | 測試 raw privileged content 是否進入 shared topic、DLQ、cache、trace |
| replay / expired capability | 測試過期 message、decision_id 或 idempotency key 是否被拒絕 |

---

## 16. 真實世界技術流程：從 Request 到 Audit

以下是一個實際系統可能採用的流程。你不需要完整實作，但要理解每一步為什麼存在。

### Step 1：Client 發 request

```http
POST /gateway/requests
Content-Type: application/json
Authorization: Bearer demo-token
```

```json
{
  "session_token": "demo-token",
  "channel": "web",
  "raw_message": "我連不上 VPN，可以直接幫我提交 ticket 嗎？",
  "client_hints": {
    "locale": "zh-TW"
  },
  "requested_agent": "campus_it_helpdesk_agent"
}
```

### Step 2：Gateway 做 schema validation

技術選型例子：

- Python：`FastAPI` + `Pydantic`
- TypeScript：`Express` / `Fastify` + `zod`

檢查：

```text
session_token 是否存在？
channel 是否為允許值？
raw_message 是否為非空字串？
requested_agent 是否符合 ID 格式？
client_hints 是否只作 hint，不當作權限？
```

失敗 outcome：

```http
400 malformed_input
```

### Step 3：Server-side identity resolution

技術選型例子：

- demo：in-memory session store。
- production：OIDC / SSO / IAM。
- backend：PostgreSQL / Redis / IAM service。

重點：

```text
不要相信 client 傳來的 role。
role 必須由 token 或 session server-side 解析。
```

失敗 outcome：

```http
401 invalid_token
```

### Step 4：Action extraction

Gateway 或 lightweight classifier 從 `raw_message` 擷取意圖：

```json
{
  "requested_action": "submit_ticket",
  "topic": "vpn_connectivity",
  "risk_hint": "side_effect_requested"
}
```

Day 2 要承接 Day 1 的原則：複雜 prompt 不應只變成一個 label。Gateway
應該產生 action proposals，包含 intent labels、action candidates、risk
labels、missing slots、ambiguity、confidence、recommended next step。Policy
gate 針對每個 action 分別決定 allow、deny、review、clarify 或 require
confirmation。

注意：

```text
action extraction 可以用 model 幫忙，但最後 policy decision 不應由 model 單獨決定。
```

### Step 5：Agent Registry lookup

Gateway 查 registry：

```text
requested_agent = campus_it_helpdesk_agent
```

確認：

```text
agent 是否存在？
agent 是否 enabled？
user role 是否在 allowed_users？
requested_action 是否在 task_scope？
```

### Step 6：Tool / Data / Memory boundary check

Tool：

```text
submit_ticket 是 side-effect tool。
```

Data：

```text
public_it_faq、vpn_setup_guide 可查。
staff_account_lock_sop 不可查。
```

Memory：

```text
只能 session read/write。
不能 shared memory。
不能保存 credential。
```

Message mediation：

```text
student-facing agent 只能 publish 到 support-safe request channel。
student-facing agent 只能 consume redacted result channel。
不能讀 staff-only raw result topic。
高權限 agent 的 raw output 必須先經過 declassifier 或 human review。
```

### Step 7：Policy gate decision

Policy input：

```json
{
  "user_role": "student",
  "agent_id": "campus_it_helpdesk_agent",
  "requested_action": "submit_ticket",
  "tool": "submit_ticket",
  "data_sources": ["public_it_faq", "vpn_setup_guide"],
  "memory_write": "session_summary",
  "message_channel": "agent.requests.support",
  "requested_output_classification": "student_support_safe"
}
```

Policy output：

```json
{
  "decision": "review",
  "reason": "submit_ticket requires human review for student users",
  "required_reviewer_role": "it_reviewer"
}
```

### Step 8：Message mediation and declassification

如果工作需要跨 agent、tool service 或 broker topic 傳遞，系統要先檢查 message
contract：

```json
{
  "request_channel": "agent.requests.support",
  "result_channel": "agent.results.support.redacted",
  "producer_identity": "campus_it_helpdesk_agent",
  "consumer_identity": "declassifier_service",
  "allowed_message_classification": "student_support_safe",
  "raw_payload_allowed": false,
  "expires_at": "2026-06-14T10:30:00+08:00"
}
```

如果某個 high-privilege retrieval service 讀到 staff-only 原文，它不能直接把原文
publish 到 student agent 可讀的 topic。正確流程是：

```text
staff-only raw result
-> privileged internal channel
-> declassifier / redaction / review
-> support-safe redacted result channel
-> student-facing agent
```

這一步防止 high-privilege agent 變成 low-privilege agent 的代讀器，也避免 broker、
DLQ、log、trace、cache 變成敏感資料外洩面。

### Step 9：Human review state

因為 `submit_ticket` 是 side-effect action，系統不直接提交，而是建立 review item：

```json
{
  "review_id": "rev-001",
  "status": "pending",
  "reviewer_role": "it_reviewer",
  "draft_action": "submit_ticket"
}
```

### Step 10：Audit event

系統寫入 audit event：

```json
{
  "trace_id": "req-001",
  "policy_decision": "review",
  "tool_decisions": [
    {
      "tool_name": "submit_ticket",
      "decision": "review"
    }
  ],
  "message_channel": "agent.results.support.redacted",
  "output_classification": "student_support_safe",
  "human_review_status": "pending",
  "outcome": "pending_review"
}
```

### Step 11：HTTP response

```http
200 OK
```

```json
{
  "status": "pending_review",
  "message": "我已經整理好 ticket 草稿，但提交 ticket 需要 IT reviewer 審核。",
  "trace_id": "req-001"
}
```

---

## 17. 初學者常見錯誤

### 錯誤 1：只靠 prompt 控制權限

錯誤寫法：

```text
Prompt：學生不可以讀 staff-only SOP。
```

問題：

```text
model 可能被 prompt injection 誘導。
retrieval layer 可能已經把 staff-only SOP 查出來。
audit event 可能看不出 policy 是否真的執行。
```

修正：

```text
data connector 用 metadata filter 阻擋 staff-only SOP。
policy gate 對 student + staff_only source 回傳 deny。
audit event 記錄 denied source class 與 policy reason。
```

### 錯誤 2：tool schema 有了，但沒有 permission rule

錯誤：

```json
{
  "name": "submit_ticket",
  "parameters": {
    "title": "string",
    "description": "string"
  }
}
```

問題：

```text
這只說明怎麼呼叫 tool，沒有說誰可以呼叫、什麼情況需要 review、失敗怎麼 audit。
```

修正：

```yaml
tool_rule:
  submit_ticket:
    type: side_effect
    allowed_roles: [staff, it_reviewer]
    student_behavior: review_required
    rate_limit: 3_per_hour
    audit_required: true
```

### 錯誤 3：audit 只記 final answer

錯誤：

```json
{
  "final_answer": "請依照 VPN guide 設定。"
}
```

問題：

```text
看不出查了哪份資料、是否試圖呼叫 tool、policy 是否 allow、是否需要 review。
```

修正：

```json
{
  "trace_id": "req-001",
  "retrieved_source_ids": ["vpn-guide-2026-01"],
  "policy_decision": "allow",
  "tool_decisions": [],
  "memory_decision": "session_only",
  "outcome": "completed"
}
```

### 錯誤 4：memory scope 空白

問題：

```text
agent 可能把 PII、credential、ticket details 寫入 shared memory。
```

修正：

```yaml
memory_scope:
  read: session
  write: session_summary
  retention: 24h
  shared_memory: false
  pii_rule: do_not_store_credentials_or_student_id
```

### 錯誤 5：把 broker 當成安全邊界

錯誤：

```text
所有 agent 都 publish / consume agent.messages。
高權限 agent 把 staff-only SOP 原文放進 agent.messages。
低權限 agent 也能讀 agent.messages。
```

問題：

```text
Kafka-like broker 降低耦合，但不會自動做資料降敏、原始使用者授權、schema governance、
DLQ 保護或 output classification。raw secret payload 進入 broker 後，可能被 replica、
consumer buffer、debug trace、dead-letter queue、monitoring system 保存。
```

修正：

```yaml
message_rule:
  support_agent:
    produce: [agent.requests.support]
    consume: [agent.results.support.redacted]
    denied_consume: [agent.results.staff_only.raw]
  raw_privileged_payloads: deny
  required_fields:
    - trace_id
    - origin.user_id
    - action
    - resource.classification
    - purpose
    - expires_at
declassification_rule:
  staff_only_content: deny_to_student
  support_summary: redact_before_return
```

### 錯誤 6：高權限 agent 變成低權限 agent 的代讀器

錯誤：

```text
student_agent 無法讀 staff-only SOP。
student_agent 請 staff_agent 摘要 staff-only SOP。
staff_agent 讀完後把摘要貼回 student_agent。
```

問題：

```text
資料庫 ACL 可能仍然正確，但系統在輸出路徑洩密。policy 應該檢查 original user、
requesting agent、resource、purpose、output classification，而不是只看 staff_agent
本身有沒有讀取權限。
```

修正：

```yaml
policy_check:
  original_user_role: student
  requesting_agent: student_agent
  privileged_agent: staff_agent
  resource_classification: staff_only
  requested_output_classification: student_visible
decision: deny
reason: high-privilege agent cannot declassify staff-only content to student role
```

---

## 18. Submission Checklist

交作業前請檢查：

```text
[ ] 我有寫出 Day 1-to-Day 2 gateway alignment and message mediation note。
[ ] 我的 route 有接回 POST /gateway/requests 或等價 route。
[ ] 我有說明 trusted identity 由 server-side 解析。
[ ] 我有至少一個 allow、deny、review_required 路徑。
[ ] 我有至少 200、400、401、403 HTTP outcome。
[ ] 我有 governance layer map。
[ ] 我有 common-vs-adapter table。
[ ] 我有 agent registration record。
[ ] registration 裡有 owner、task_scope、risk_class、allowed users/tools/data、memory、approval、eval、red-team、audit。
[ ] 我有 policy gate record。
[ ] policy gate 可以回傳 allow / deny / review。
[ ] 我有說明跨 agent / tool / process 的 mediated message path。
[ ] 我有說明 raw privileged payload 不會進入低權限可讀 topic、queue、log、cache 或 DLQ。
[ ] 我有 replay / expiration / idempotency 或 policy re-check 設計。
[ ] 我有 declassification 或 redaction rule。
[ ] 我有 audit event schema。
[ ] audit event 不只記 final answer。
[ ] audit event 不保存不必要 PII。
[ ] 我有 risk-control map。
[ ] 我有 Day 3 red-team seed list。
[ ] 我的案例是 public-safe，沒有私人資料、credential 或客戶秘密。
```

---

## 19. 一句話總結

```text
Prompt can guide behavior.
Policy and system boundaries enforce behavior.
Audit evidence proves what happened.
```
