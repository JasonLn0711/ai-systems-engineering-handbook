# Student Handout — Day 2：Agent Governance Framework

This is the summarized Day 2 handout. It preserves the chapter structure of
`student-handout-detailed.md`, but shortens each section to the core idea,
student action, and review evidence.

For complete examples, schemas, and deeper engineering notes, use
`student-handout-detailed.md` or `student-handout-detailed.zh-TW.md`.

---

## 0. 第一結論

Enterprise AI agent 不能只靠 prompt 管理。Prompt 可以引導模型，但真正的
enterprise boundary 必須由 registry、policy gate、tool/data/memory boundary、
message mediation、declassification、audit event、human review 與 evaluation
feedback 共同執行。

Day 2 的任務是把 Day 1 的 AI Gateway 入口，接到可被執行、可被審查、可被
Day 3 red-team 測試的 governance artifacts。

---

## 1. 為什麼 agent governance 重要？

一個 Campus IT Helpdesk Assistant 可以回答 VPN 問題，也可能被要求讀取
staff-only SOP、提交大量 ticket、保存學生密碼，或跨 agent 取得高權限資料。

系統原則：

```text
不要讓 model 自己決定權限。
讓 gateway / policy gate / tool broker / data connector / memory store 做 enforcement。
```

Review evidence: 學生必須能指出哪些權限由 server-side identity、policy、
tool/data/memory boundary 與 audit event 控制，而不是由 prompt 宣告控制。

---

## 2. Day 1 到 Day 2：Gateway Contract 銜接

Day 1 的核心 route 是：

```http
POST /gateway/requests
```

Day 2 要補上這條 route 需要查詢或執行的 governance contract：

```text
schema validation
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

Review evidence: alignment note 必須說明 trusted identity 來自 server-side
解析，不相信 `client_hints.role`、`requested_department` 或其他 client 提示。

---

## 3. Day 2 的核心 mental model

請把 enterprise agent 看成多個 control layer：

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

Student action: 對每一層寫出責任、enforcement、evidence。

---

## 4. 核心術語

| 詞彙 | 核心意思 |
|---|---|
| `AI Gateway` | 接 request、驗證、路由、治理、記錄的系統入口 |
| `Agent Registry` | agent 的版本化設定合約，不只是名稱清單 |
| `Tool Boundary` | 控制工具能否呼叫、是否有 side effect、是否需審核 |
| `Data Boundary` | 控制 retrieval 可讀哪些資料與 metadata |
| `Memory Scope` | 控制可記住什麼、多久、是否共享 |
| `Mediated Message Boundary` | 控制跨 agent/process/tool 的通道、ACL、schema、retention、audit |
| `Policy Gate` | 對 request/action/resource/context 回傳 `allow`、`deny` 或 `review` |
| `Audit Event` | 保存可重建 lifecycle 的 evidence，不是 debug log |
| `Human Review` | 高風險或 side-effect action 的審核狀態 |
| `Red-Team Seed` | 可執行、可判斷 pass/fail 的測試案例 |

---

## 5. 真實世界案例：Campus IT Helpdesk Assistant

### 5.1 情境

校園 IT assistant 可回答 public IT FAQ、VPN setup guide、service status。
學生不能讀 staff-only SOP；assistant 可以草擬 ticket，但不能未經 review
直接 submit ticket，也不能保存學生 PII 到 shared memory。

### 5.2 資料來源

| Data Source | 允許對象 | 核心 boundary |
|---|---|---|
| `public_it_faq` | student、staff | public |
| `vpn_setup_guide` | student、staff | public + versioned |
| `service_status_page` | student、staff | public + freshness |
| `staff_account_lock_sop` | staff、it_reviewer | staff-only |

### 5.3 Tools

| Tool | 類型 | Control |
|---|---|---|
| `search_it_faq` | read-only | source version、citation |
| `lookup_service_status` | read-only | freshness check |
| `draft_ticket` | no external side effect | user confirmation、audit |
| `submit_ticket` | side-effect | human review、rate limit、audit |
| `reset_password` | high-risk side-effect | deny by default、staff-only workflow |

---

## 6. Common Governance vs Adapter-Specific Behavior

Common governance 是平台能力；adapter-specific behavior 是業務情境映射。

| Layer | Common Governance | Adapter-Specific Behavior |
|---|---|---|
| Identity | user、role、tenant、agent identity | student、staff、it_reviewer |
| Tool | schema、permission、timeout、idempotency | `search_it_faq`、`submit_ticket` |
| Data | metadata filter、access level、version | public FAQ vs staff SOP |
| Memory | retention、sharing、PII rule | helpdesk session note |
| Policy | allowed/blocked/review conditions | ticket submission requires review |
| Audit | trace、source、tool、policy decision | helpdesk audit report format |
| Red Team | threat taxonomy、test harness | staff SOP bypass、ticket spam |

---

## 7. Control Plane vs Data Plane

Control plane 決定是否可以做、誰可以做、是否需要審查、要留下什麼
evidence。Data plane 實際查資料、呼叫工具、產生回答。

Student action: 不要讓 model 在 data plane 直接決定權限。Model 可以提出
intent；policy gate 做 decision；tool/data/memory boundary 做 enforcement；
audit event 留 evidence。

---

## 8. Artifact 1：Day 1-to-Day 2 Gateway Alignment Note

### 8.1 Template

必填欄位：

```text
Route
Request schema fields
Trusted identity source
Action extraction method
Policy decisions needed
Registered agent
Read-only tool
Side-effect tool
Allowed data sources
Memory rule
Message mediation path
Declassification or redaction rule
Human review trigger
Required audit fields
Expected HTTP outcomes
```

### 8.2 填寫提醒

至少包含 `allow`、`deny`、`review_required`、`400`、`401`、`403`、`200`，
並說明 audit fields 如何證明 policy、retrieval、tool、memory、review decision。

### 8.3 實作角度

Day 2 不要求完整實作，但 artifacts 應足以讓後續用 FastAPI/Pydantic、
policy engine、broker、Redis、PostgreSQL 或 OpenTelemetry 等工具實作出 mock。

---

## 9. Artifact 2：Governance Layer Map

### 9.1 你要畫什麼？

畫出 identity、agent registry、tool/data/memory boundary、mediated message
boundary、policy gate、audit event、human review、evaluation hook、red-team seed。

### 9.2 每層要寫什麼？

每層至少寫：

1. 這層的責任。
2. 這層 enforce 什麼。
3. 這層留下什麼 evidence。

---

## 10. Artifact 3：Common-vs-Adapter Table

展示哪些 governance 可跨情境重用，哪些只屬於 Campus IT。

Review evidence: 如果換成銀行內部知識助理還能沿用，通常是 common
governance；如果只跟校園 IT 情境有關，通常是 adapter-specific behavior。

---

## 11. Artifact 4：Agent Registration Record

### 11.1 Template

Registration 至少包含 `agent_id`、owner、task_scope、risk_class、
allowed_users/tools/data、memory_scope、allowed_message_channels、
output_classification、approval_required_for、evaluation_set、red_team_suite、
audit_events。

### 11.2 欄位說明

Review evidence: registration 必須像 Gateway 可讀的 configuration contract，
不能只是「這個 agent 會回答 IT 問題」。

---

## 12. Artifact 5：Policy Gate Record

### 12.1 Policy Input Shape

Policy input 應包含 request、user、agent、action、data source、tool、
memory write、message channel 與 client context。

### 12.2 Policy Output Shape

Policy output 應包含 decision、reason、required reviewer、safe user message、
audit fields。

### 12.3 Policy Gate Template

Policy record 至少包含 `policy_id`、`applies_to`、preconditions、
allowed_actions、blocked_actions、pii/retrieval/tool/memory/message rule、
declassification rule、human review trigger、failure response、audit fields。

### 12.4 allow / deny / review 的差異

| Decision | 意義 | HTTP outcome |
|---|---|---|
| `allow` | 可執行 | `200 completed` |
| `deny` | 不可執行 | `403 denied` |
| `review` | 等待人審 | `200 pending_review` 或 `202 pending_review` |
| schema failure | 格式不合 | `400 malformed_input` |
| auth failure | token 無效 | `401 invalid_token` |

---

## 13. Artifact 6：Audit Event Schema

Audit event 要能重建 request lifecycle：誰提出 request、解析出什麼 identity、
選到哪個 agent、查了哪些資料、policy 做了什麼 decision、tool/memory/review
如何處理、最後 outcome 是什麼。

### 13.1 最小 audit event shape

至少包含 `trace_id`、timestamp、user/role/tenant、agent_id、policy_decision、
policy_reason、retrieved_source_ids、tool_decisions、memory_decision、
message_channel、output_classification、human_review_status、outcome。

### 13.2 不要存什麼？

不要保存不必要的 password、token、完整 credential、完整 PII、private document
content 或原始敏感 prompt。優先保存 summary、hash、source ID、document version、
policy reason 與 decision metadata。

---

## 14. Artifact 7：Risk-Control Map

至少包含 tool abuse、memory leakage、permission bypass、confused deputy、
broker payload leakage、replay of privileged result、missing schema field、
prompt-only approval、missing audit detail、HTTP outcome mismatch、stale retrieval。

Review evidence: 每個 risk 都要有 example、required control、evidence。

---

## 15. Artifact 8：Day 3 Red-Team Seed List

Red-team seed 要能被執行、被判斷成功或失敗。

### 15.1 Template

必填欄位：

```text
test_id
threat_category
target_control
input_message
expected_policy_decision
expected_http_outcome
expected_audit_fields
pass_condition
failure_signal
```

### 15.2 範例 seed 方向

包含 prompt injection、permission bypass、tool abuse、memory leakage、audit
evasion、HTTP outcome mismatch、confused deputy、broker payload leakage、
replay / expired capability。

---

## 16. 真實世界技術流程：從 Request 到 Audit

### Step 1：Client 發 request

Client 以 `POST /gateway/requests` 送出 `session_token`、channel、
`raw_message`、client hints、requested agent。

### Step 2：Gateway 做 schema validation

檢查 required fields、型別、allowed values、agent ID 格式。失敗回
`400 malformed_input`。

### Step 3：Server-side identity resolution

用 token/session server-side 解析 user、role、tenant、permission set。失敗回
`401 invalid_token`。

### Step 4：Action extraction

從 raw message 產生 action proposal、risk label、missing slots、confidence、
recommended next step。Model 可以協助抽取，但 policy decision 不由 model 單獨決定。

### Step 5：Agent Registry lookup

確認 agent 存在、enabled、user role 在 allowed users、requested action 在
task scope。

### Step 6：Tool / Data / Memory boundary check

確認 tool side effect、data access level、memory retention/sharing/PII rule、
message channel 與 output classification。

### Step 7：Policy gate decision

Policy gate 回傳 allow、deny、review、reason、reviewer role 與 audit fields。

### Step 8：Message mediation and declassification

跨 agent/tool/broker 的資料必須經過 mediated path；高敏感資料需先 redaction、
summary 或 human review，才能回到低權限 zone。

### Step 9：Human review state

Side-effect action 建立 pending review item，不直接執行。

### Step 10：Audit event

記錄 trace、policy decision、tool decision、message channel、output
classification、review status、outcome。

### Step 11：HTTP response

回傳 completed、denied、malformed、invalid token 或 pending review，並帶回
`trace_id` 方便追蹤。

---

## 17. 初學者常見錯誤

### 錯誤 1：只靠 prompt 控制權限

修正：data connector 用 metadata filter；policy gate 回傳 deny；audit event
記錄 blocked source class。

### 錯誤 2：tool schema 有了，但沒有 permission rule

修正：tool schema 管格式，tool permission 管誰能呼叫、何時 review、是否 side
effect、怎麼 audit。

### 錯誤 3：audit 只記 final answer

修正：audit event 必須包含 identity、policy、retrieval、tool、memory、review、
outcome。

### 錯誤 4：memory scope 空白

修正：明確寫 read/write/retention/shared/PII/deletion rule。

### 錯誤 5：把 broker 當成安全邊界

修正：broker 只是一部分；仍需 identity、topic ACL、schema、classification、
retention、replay protection、audit。

### 錯誤 6：高權限 agent 變成低權限 agent 的代讀器

修正：policy 同時檢查 original user、requesting agent、resource、purpose、
output classification 與 declassification rule。

---

## 18. Submission Checklist

- [ ] Gateway alignment note 連回 `POST /gateway/requests`。
- [ ] Trusted identity 不相信 client hints。
- [ ] Governance layer map 有 responsibility、enforcement、evidence。
- [ ] Common-vs-adapter table 可跨情境重用。
- [ ] Agent registration 像 Gateway config。
- [ ] Policy gate 有 allow / deny / review。
- [ ] Audit event 可重建 lifecycle。
- [ ] Risk-control map 有 control 與 evidence。
- [ ] Day 3 red-team seeds 可執行、可判斷 pass/fail。
- [ ] Source boundary public-safe。

---

## 19. 一句話總結

Day 2 的交付不是一個更聰明的 agent，而是一組讓 agent 可被 Gateway 控制、
可被 TA 評分、可被 Day 3 攻防測試的治理合約。
