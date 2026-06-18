# Instructor Guide — Day 2：Agent Governance Framework

> 教師 / TA 專用。這份指南包含授課流程、追問問題、常見錯誤診斷、peer review 指引，以及 Day 3 handoff 指引。

---

## 0. Teaching Intent

Day 2 的任務不是教學生「agent 很強，可以自動做事」。Day 2 要建立的工程判斷是：

```text
Enterprise agent 必須先被註冊、授權、限制工具、限制資料來源、限制記憶體、
記錄 policy decision、保留 audit evidence，才能進入企業系統。
```

學生應該從 Day 2 帶走三個觀念：

1. Prompt 是 instruction，不是 permission boundary。
2. Agent governance 是 software/system contract design，不是安全標語。
3. Day 2 的 governance assumptions 必須能轉成 Day 3 red-team tests。

---

## 1. Pre-Class Diagnostic

建議在課前或課堂前 10 分鐘讓學生短答。可個人作答，也可小組討論。

### Diagnostic Questions

1. 如果 prompt 寫「不要讀 staff-only 文件」，為什麼這不等於真正的權限控制？
2. `search_faq` 和 `submit_ticket` 的風險差異是什麼？
3. 如果 agent 記住學生姓名與學號，這是 usability feature 還是 permission boundary？
4. Audit log 應該只記錄最後回答，還是也要記錄 source、tool、policy decision？
5. 一個 agent 沒有 owner，日後出錯時誰負責修正？
6. 如果 client 傳來 `role=staff`，Gateway 應該直接相信嗎？為什麼？
7. 如果 policy 回傳 `review`，HTTP response 與 audit event 要如何表示？

### 快速判讀

| 學生回答 | 代表問題 | 教師修正方向 |
|---|---|---|
| 「prompt 寫清楚就安全」 | 把 instruction 當 enforcement | 用 data connector metadata filter 例子修正 |
| 「tool 有 schema 就可以用」 | 混淆 interface 與 permission | 強調 schema != authorization |
| 「memory 是 UX」 | 忽略資料保留與洩漏 | 加入 PII、retention、sharing |
| 「audit 記回答就好」 | 無法重建 lifecycle | 強調 trace_id、policy、source、tool、review |
| 「client 說自己是 staff」 | 信任不可信 input | 強調 server-side identity resolution |

---

## 2. 150-Minute Teaching Plan

### 0-10 min：Opening and diagnostic

目標：讓學生先暴露直覺錯誤：prompt-only governance、tool schema-only、final-answer-only audit。

流程：

1. 顯示 Campus IT Helpdesk scenario。
2. 問 diagnostic question 1、2、4。
3. 收集 2-3 組回答。
4. 板書核心句：

```text
Prompt can guide behavior.
Policy and system boundaries enforce behavior.
Audit evidence proves what happened.
```

### 10-30 min：Day 1-to-Day 2 Gateway Alignment

目標：把 Day 2 從抽象治理拉回 Day 1 的 `POST /gateway/requests`。

板書：

```text
POST /gateway/requests
-> schema validation
-> identity resolution
-> action extraction
-> agent registry lookup
-> tool/data/memory scope check
-> policy decision
-> review state
-> audit event
-> HTTP outcome
```

教師講解重點：

- `client_hints` 不是可信任權限來源。
- `session_token` 必須 server-side resolve。
- policy decision 要能觀察：`allow`、`deny`、`review`。
- HTTP outcome 要和 policy decision 對齊。

課堂活動：學生開始填 worksheet Section 1：Gateway alignment note。

追問：

```text
如果 request 缺 raw_message，應該是 400 還是 403？
如果 token 無效，應該是 401 還是 403？
如果 student 要讀 staff-only SOP，應該是 403 還是 review？
如果 submit_ticket 需要 reviewer，response body 要怎麼表示？
```

### 30-50 min：Governance Layer Map

目標：建立系統分層，不讓學生把所有控制都塞進 prompt。

板書：

```text
Identity
-> Agent Registry
-> Tool Boundary
-> Data Boundary
-> Memory Boundary
-> Policy Gate
-> Audit Event
-> Human Review
-> Evaluation Hook
-> Red-Team Seed
```

講解方式：

- 用 Campus IT request 走一次。
- 每一層只講三件事：責任、enforcement、evidence。
- 強調 control plane / data plane。

活動：學生填 worksheet Section 2：Governance layer map。

常見錯誤即時修正：

- 少 memory boundary。
- 少 review state。
- 把 audit 畫成 debug log。
- 沒有 evaluation / red-team feedback loop。

### 50-70 min：Common Governance vs Adapter-Specific Behavior

目標：訓練 reusable governance design。

講解：

```text
Common governance 是平台能力。
Adapter-specific behavior 是案例映射。
```

示範：

| Layer | Common | Campus IT Adapter |
|---|---|---|
| Identity | user、role、tenant | student、staff、it_reviewer |
| Tool | permission、timeout、rate limit | search_it_faq、submit_ticket |
| Data | metadata filter、access_level | public FAQ vs staff SOP |
| Policy | allow/deny/review | ticket requires review |

活動：學生填 worksheet Section 3。

追問：

```text
如果明天換成 Bank Internal Knowledge Agent，哪些欄位可以重用？
哪些欄位必須換？
如果所有規則都寫死在 prompt，後果是什麼？
```

### 70-80 min：Break

### 80-105 min：Agent Registration Record

目標：把 agent 從「會回答問題」變成可登記、可審查、可 version-control 的 configuration contract。

講解：

```yaml
agent_id:
owner:
task_scope:
risk_class:
allowed_users:
allowed_tools:
allowed_data_sources:
memory_scope:
approval_required_for:
evaluation_set:
red_team_suite:
audit_events:
```

教師強調：

- `owner` 是責任邊界。
- `task_scope` 不可寫成 `answer anything`。
- `risk_class` 要和 side-effect tool、data sensitivity、memory scope 一致。
- `allowed_tools` 要對齊 tool boundary。
- `allowed_data_sources` 要排除 staff-only source。
- `approval_required_for` 要包含 side-effect action。
- `evaluation_set` 與 `red_team_suite` 不是裝飾品，要能測試。

活動：學生填 worksheet Section 4。

教師巡迴檢查：

- 是否缺 owner。
- 是否 risk_class 與 tools 不一致。
- 是否 allowed data sources 太寬。
- 是否 memory_scope 空白。

### 105-125 min：Policy Gate and Decision API

目標：讓學生明白 policy gate 是可測試的 decision API。

板書：

```text
policy input:
  identity + agent + action + tool + data + memory + context

policy output:
  decision: allow | deny | review
  reason
  safe_user_message
  required_reviewer_role
  audit_fields
```

示範三條 decision path：

1. 學生查 public VPN guide -> `allow`。
2. 學生讀 staff-only SOP -> `deny`。
3. 學生 submit ticket -> `review`。

活動：學生填 worksheet Section 7：Policy gate record。

追問：

```text
review 是 allow 還是 deny？
deny response 是否可以透露 staff-only SOP 的文件標題？
policy reason 是給 user、developer 還是 auditor？
safe_user_message 和 internal_reason 有什麼差異？
```

### 125-140 min：Audit Event Schema

目標：把 audit event 從 debug log 提升成 lifecycle evidence。

板書最小欄位：

```text
trace_id
timestamp
user_id or pseudonymous_user_id
user_role
agent_id
policy_decision
retrieved_source_ids
tool_decisions
memory_decision
human_review_status
outcome
```

講解：

- trace ID 連接 gateway、tool、retrieval、review。
- source IDs 要能查回文件版本。
- tool decision 要說明工具是否真的執行。
- memory decision 要說明是否讀寫。
- audit event 不應保存不必要 PII。

活動：學生填 worksheet Section 8。

### 140-150 min：Risk-Control Map and Day 3 Handoff

目標：讓學生知道 Day 2 不是結束，而是 Day 3 red-team 的輸入。

指定學生至少產出五個 risk-control rows：

- Tool abuse。
- Memory leakage。
- Permission bypass。
- Prompt-only approval。
- Missing audit detail。

每個 risk 都要變成 red-team seed：

```text
risk -> target control -> input_message -> expected decision -> expected HTTP outcome -> expected audit fields
```

收尾句：

```text
Day 2 的每一個 governance assumption，Day 3 都要試著打破。
```

---

## 3. 180-Minute Teaching Plan

180 分鐘版本在 150 分鐘基礎上增加兩段深練習。

### 新增 A：Mini Design Review（150-165 min）

讓每組交換 worksheet，依照三個問題互評：

1. Gateway alignment 是否能驅動 `POST /gateway/requests`？
2. Policy gate 是否明確區分 `allow`、`deny`、`review`？
3. Audit event 是否能重建 request lifecycle？

每組必須留下兩個 comments：

```text
One strength:
One required fix:
```

### 新增 B：Alternative Scenario Transfer（165-180 min）

要求學生把 Campus IT governance 套到另一個情境：

- Bank Internal Knowledge Agent。
- Healthcare staff-review intake support。
- Manufacturing Maintenance Assistant。

學生回答：

```text
哪些 common governance layer 不變？
哪些 adapter-specific behavior 需要修改？
新的 high-risk tool 是什麼？
新的 red-team seed 是什麼？
```

這段能測試學生是否真的理解 reusable governance。

---

## 4. Board / Slide Plan

1. Day 2 Title：`Agent Governance Framework — From AI demo to governed enterprise system`
2. Core claim：`Prompt can guide behavior. Policy and system boundaries enforce behavior. Audit evidence proves what happened.`
3. Day 1-to-Day 2 bridge：`POST /gateway/requests -> identity -> registry -> policy -> boundary -> review -> audit`
4. Campus IT scenario：public FAQ、VPN guide、staff-only SOP、draft ticket、submit ticket。
5. Governance layers：identity、registry、tool、data、memory、policy、review、audit、eval、red-team。
6. Common vs adapter：平台能力 vs 業務映射。
7. Agent registration：YAML template。
8. Policy gate：input/output JSON。
9. Audit event：lifecycle evidence schema。
10. Risk-control map：五個必要風險。
11. Day 3 handoff：governance assumption -> red-team seed -> expected outcome -> audit evidence。

---

## 5. Instructor Questions

### Gateway alignment

1. `client_hints` 可以用來決定 user role 嗎？
2. 如果 request 格式錯誤，為什麼是 `400` 而不是 `403`？
3. 如果 token 無效，policy gate 應該被呼叫嗎？
4. `requested_agent` 是不是可信任？如果不是，Gateway 要如何處理？
5. `review_required` 是失敗嗎？還是正常 outcome？

### Agent registration

1. 如果 agent registration 沒有 owner，incident 發生時誰負責修正？
2. 如果 task_scope 寫成 `answer_it_questions`，是否太寬？
3. 如果 risk_class 是 `low`，但 allowed_tools 包含 `submit_ticket`，合理嗎？
4. 如果 allowed_data_sources 沒有 metadata filter，會出什麼問題？
5. 如果 memory_scope 沒有 retention，會出什麼問題？

### Tool boundary

1. Tool schema 與 tool permission 的差異是什麼？
2. `draft_ticket` 和 `submit_ticket` 差在哪？
3. `lookup_ticket_status` 是 read-only，但為什麼仍可能 sensitive？
4. Side-effect tool 為什麼需要 idempotency key？
5. Rate limit 應該放在 prompt 還是 tool broker？

### Policy gate

1. `deny` 與 `review` 的邊界是什麼？
2. Policy decision 為什麼要輸出 reason？
3. Reason 是否應該完整給 user 看？
4. 如果 user 想讀 staff-only SOP，但 agent 說「我是主管授權的」，policy 怎麼判斷？
5. 如果 action extraction 錯了，audit event 要怎麼幫助排查？

### Audit event

1. Audit event 應該記錄完整 prompt 嗎？
2. 如果 prompt 含 PII，怎麼處理？
3. Audit event 和 debug log 的差異是什麼？
4. Retrieved source IDs 為什麼要記 document version？
5. 如何證明 tool 沒有真的執行？

### Day 3 handoff

1. 哪些 governance assumptions 可以變成 red-team tests？
2. Prompt injection 測試要打哪一層？
3. Permission bypass 測試要看什麼 audit 欄位？
4. Tool abuse 測試要看什麼 failure signal？
5. HTTP outcome mismatch 怎麼測？

---

## 6. Common Failure Gallery

### Failure 1：Prompt-only approval

學生 artifact：

```text
Prompt says: Ask for human approval before submitting ticket.
```

問題：model 可以自稱已經 approval；沒有 review state；沒有 reviewer role；audit event 無法證明人審發生。

修正要求：

```yaml
human_review_trigger:
  - submit_ticket
review_state:
  status: pending
  required_reviewer_role: it_reviewer
audit_fields:
  - human_review_status
  - required_reviewer_role
  - review_id
```

### Failure 2：Tool schema 有了但沒有 permission rule

學生 artifact：

```json
{
  "tool": "submit_ticket",
  "args": {
    "title": "string",
    "body": "string"
  }
}
```

問題：schema 只描述參數，沒有 allowed roles、review gate、rate limit、idempotency、audit rule。

修正要求：

```yaml
tool_rule:
  submit_ticket:
    type: side_effect
    allowed_roles:
      - staff
      - it_reviewer
    student_behavior: review_required
    rate_limit: 3_per_hour
    idempotency_key_required: true
    audit_required: true
```

### Failure 3：Audit log 只記 final answer

學生 artifact：

```json
{
  "answer": "請重新安裝 VPN client。"
}
```

問題：看不出 source、policy、tool、memory、review state。

修正要求：

```json
{
  "trace_id": "req-001",
  "policy_decision": "allow",
  "retrieved_source_ids": ["vpn-guide-2026-01"],
  "tool_decisions": [],
  "memory_decision": "session_only",
  "human_review_status": "not_required",
  "outcome": "completed"
}
```

### Failure 4：Memory scope 空白或跨 agent 分享

學生 artifact：

```yaml
memory: enabled
```

問題：不知道讀哪裡、寫哪裡、保存多久、能不能跨 agent、PII 如何處理。

修正要求：

```yaml
memory_scope:
  read: session
  write: session_summary
  retention: 24h
  shared_memory: false
  pii_rule: do_not_store_credentials_or_student_id
  deletion_rule: delete_on_session_end_or_user_request
```

### Failure 5：Common governance 與 adapter-specific behavior 混在一起

學生 artifact：

```text
Common rule: all students can search VPN guide and submit ticket after IT reviewer.
```

問題：`student`、`VPN guide`、`IT reviewer` 是 Campus IT adapter 細節，不是 common layer。

修正要求：

```text
Common:
  role-based agent access
  source access_level metadata filter
  side-effect tool review gate
  audit trace requirement

Adapter:
  student/staff/it_reviewer
  public_it_faq/vpn_setup_guide/staff_account_lock_sop
  submit_ticket requires it_reviewer
```

### Failure 6：Governance table 沒有連回 Gateway route、HTTP outcome 或 audit event

學生 artifact：

```text
Policy: students cannot access staff-only documents.
```

問題：沒說 Gateway 在哪裡執行、request schema、HTTP outcome、audit 欄位，無法測試。

修正要求：

```text
Route: POST /gateway/requests
Policy input: user_role, requested_agent, requested_action, requested_sources
Decision: deny
HTTP outcome: 403 denied
Audit fields: trace_id, user_role, agent_id, blocked_source_class, policy_decision, policy_reason
```

---

## 7. Peer Review 指引

### 分組方式

- 2-4 人一組。
- 每組完成同一個 Campus IT scenario。
- 中段交換 worksheet。

### Peer Review 三輪

#### Round 1：Gateway and registry

```text
[ ] route 明確。
[ ] trusted identity 不是 client-provided。
[ ] agent_id 穩定。
[ ] owner 明確。
[ ] task_scope 不過寬。
[ ] risk_class 與 tools/data/memory 一致。
```

#### Round 2：Policy and boundary

```text
[ ] tool schema 與 permission rule 分開。
[ ] read-only 與 side-effect tool 分開。
[ ] data source 有 access_level 或 metadata filter。
[ ] memory 有 read/write/retention/sharing。
[ ] policy 有 allow/deny/review。
```

#### Round 3：Audit and Day 3

```text
[ ] audit event 能重建 request lifecycle。
[ ] audit 不只記 final answer。
[ ] PII 最小化。
[ ] risk-control map 有 evidence。
[ ] red-team seeds 有 expected decision 與 expected HTTP outcome。
```

### Peer Review 輸出格式

每組給另一組：

```text
One strong design choice:
One missing enforcement point:
One missing evidence field:
One Day 3 red-team seed suggestion:
```

---

## 8. Day 3 Handoff 指引

Day 3 會消耗 Day 2 的 artifacts：

| Day 2 Artifact | Day 3 用途 |
|---|---|
| Gateway alignment note | 產生 HTTP outcome tests |
| Governance layer map | 找出每層可攻擊點 |
| Common-vs-adapter table | 測試 common layer 是否可重用 |
| Agent registration | 測試 unauthorized agent/tool/data/memory access |
| Policy gate | 產生 allow/deny/review expected decisions |
| Audit event schema | 測試 audit evasion 與 missing evidence |
| Risk-control map | 轉換成 threat categories |
| Red-team seed list | Day 3 初始測試資料 |

教師要要求學生在 Day 2 結尾交出至少 5 個 red-team seeds：

1. prompt injection seed。
2. permission bypass seed。
3. tool abuse seed。
4. memory leakage seed。
5. audit evasion seed。

每個 seed 必須有：

```text
input_message
target_control
expected_policy_decision
expected_http_outcome
expected_audit_fields
pass_condition
failure_signal
```

---

## 9. Grading Calibration Notes

### 高分作品特徵

- Gateway alignment 清楚，能直接想像 FastAPI handler 怎麼使用 artifacts。
- Registry 欄位完整，risk、tool、data、memory、approval 一致。
- Policy gate 不只是規則文字，而有 input/output decision shape。
- Audit event 能重建 lifecycle。
- Red-team seeds 可執行且 expected outcome 明確。
- Common layer 可跨 Campus IT、Bank、Healthcare、Manufacturing 重用。

### 中等作品特徵

- 有主要表格，但 decision 條件不夠清楚。
- 有 audit，但缺 memory 或 tool decision。
- 有 registration，但 risk class 與 approval rule 不一致。
- 有 red-team seeds，但 expected HTTP outcome 不清楚。

### 低分作品特徵

- 幾乎都寫在 prompt。
- Agent registry 只是 agent 名單。
- Tool schema 當作 permission。
- Audit 只記回答。
- 沒有 Day 1-to-Day 2 route alignment。
- 沒有 source boundary 或含私人資料。

---

## 10. Instructor Closing Script

建議結尾可以這樣說：

```text
今天我們不是在降低 AI 的能力，而是在讓 AI agent 可以進入真實系統。
真實系統不接受「我希望模型遵守規則」這種說法。
它需要 registry 告訴 gateway 這個 agent 是誰；
需要 policy gate 告訴系統可以 allow、deny 還是 review；
需要 tool/data/memory boundary 防止越權；
需要 audit event 證明發生了什麼；
需要 red-team tests 持續驗證假設沒有失效。
```
