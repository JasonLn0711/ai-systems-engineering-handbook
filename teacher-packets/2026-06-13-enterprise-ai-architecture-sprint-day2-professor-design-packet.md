# Enterprise AI Architecture Sprint Day 2 教程設計委託包

日期：2026-06-13

對象：協助設計 `AI Systems Engineering Handbook` accelerator 教程的資訊工程學系教師

目標讀者：資訊工程大二學生，具備基礎程式設計、HTTP/JSON、JSON schema、資料庫權限、軟體工程與系統設計概念，但尚未具備 enterprise AI agent governance 經驗

Repo：`ai-systems-engineering-handbook`

指定 accelerator：`accelerators/enterprise-ai-architecture-sprint/`

指定 Day 2 主題：`Agent Governance Framework`

正式課程包目標路徑：

```text
accelerators/enterprise-ai-architecture-sprint/day-02-agent-governance/
```

---

## 1. 給老師的第一個結論

這份資料包的目的，是請老師協助我們設計 `Enterprise AI Architecture Sprint`
第二天的完整教程。Day 2 的課程任務不是教學生「agent 很聰明、可以自動做事」，
而是讓學生用軟體工程與系統工程角度理解：enterprise agent 必須先被註冊、
授權、限制工具、限制資料來源、限制記憶體使用範圍、記錄 policy decision、
保留 audit evidence，才能進入企業系統。

Day 2 的核心句子是：

```text
An enterprise agent is not governed by intention.
It is governed by registry, policy, tool boundaries, memory scope, audit events,
evaluation hooks, and review states.
```

請老師協助設計的不是單一講義，而是一組可放進 repo 的 Day 2 教學組件：

1. 學生版教程。
2. 教師授課指南。
3. 課前閱讀與 Day 1 銜接。
4. 課堂 worksheet。
5. Day 2 governance artifacts 的模板。
6. Campus IT Helpdesk Agent 參考答案。
7. 100 分評分規準。
8. Day 3 red-team framework 銜接。

Day 2 要讓學生建立一個關鍵工程判斷：prompt 不是 permission boundary。
如果 agent 可以查資料、呼叫工具、寫記憶、建立 ticket、查詢資料庫或呼叫外部 API，
那麼系統需要的是可檢查的 governance contract，而不是只在 system prompt 中寫
「請遵守規則」。

---

## 2. Repo 是什麼

`ai-systems-engineering-handbook` 是一套 AI 系統工程教程型知識庫。它的正式定位是：

```text
AI 系統工程完整教程：
從地端部署、AI Gateway、Agent Governance、RAG、語音 AI 到企業交付
```

本 repo 的核心公式是：

```text
AI system
= model
+ data
+ infrastructure
+ workflow
+ governance
+ security
+ evaluation
+ delivery
```

這個 repo 不是純 machine learning textbook，也不是 prompt engineering cookbook。
它要訓練的是：學生可以把一個 AI demo 拆解成可部署、可測試、可治理、可交付的
software system。

Day 2 位於這個 repo 的 `AI Gateway and Agent Governance` 主軸，對應到：

```text
modules/07-ai-gateway-agent-governance/
labs/ai-gateway/
accelerators/enterprise-ai-architecture-sprint/02-agent-governance-framework.md
accelerators/enterprise-ai-architecture-sprint/day-02-agent-governance/
```

老師撰寫 Day 2 教程時，請把每個概念落到可檢查的工程物件：

- agent registration record。
- allowed users / roles / tenants。
- allowed tools。
- tool schema。
- read-only tool 與 side-effect tool。
- allowed data sources。
- memory read/write scope。
- policy gate。
- allow / deny / review decision。
- audit event。
- human review state。
- evaluation hook。
- red-team seed。

---

## 3. Accelerators 是什麼

`accelerators/` 是短期 evidence-generation learning paths。它的任務是把多個
modules 的知識壓縮成可展示、可討論、可審查、可延伸到 lab 的 architecture
evidence packet。

Accelerator 不是完整 module 的替代品。它不負責把所有底層知識教到最深，而是
負責在有限時間內讓學生產出一組能證明系統工程能力的 artifact。

簡化比較：

| 類型 | 主要任務 | 產出 |
|---|---|---|
| Module | 深入教一個知識域 | 概念、機制、workflow、failure modes、exercises |
| Lab | 驗證一個可執行能力 | code、commands、expected output、debug guide |
| Case Study | 整合多個知識域 | 情境、需求、架構、trade-off、monitoring |
| Accelerator | 短期產出 evidence | architecture diagram、governance table、policy map、audit schema、review packet |

`Enterprise AI Architecture Sprint` 的總目標是：

```text
potential
-> architecture evidence
-> deployable system reasoning
-> governance and security proof
-> customer-delivery readiness
```

Day 1 建立 AI Gateway architecture。Day 2 把 Gateway 需要管理的 agent、
tool、memory、policy、audit、evaluation 與 review contract 定義出來。
Day 3 會把 Day 2 的治理假設轉成 red-team test cases。

---

## 4. Accelerators 的目標

這個 accelerator 要讓學生在 7-14 天內產出一套 public-safe enterprise AI
architecture evidence packet。Day 2 的角色是補上 enterprise agent governance
evidence。

學生完成 Day 2 後，應該能向老師、TA、mentor 或面試官說明：

- 我知道 enterprise agent 不能只是「會呼叫工具的 chatbot」。
- 我能設計 agent registry，記錄 owner、task scope、risk class、allowed tools、
  allowed data sources、memory scope、evaluation set、red-team suite。
- 我能區分 common governance layer 與 adapter-specific behavior。
- 我能設計 policy gate，讓系統回傳 `allow`、`deny` 或 `review`。
- 我能說明 read-only tool 與 side-effect tool 的差異。
- 我能設計 audit event，不只記錄最後回答，也記錄 policy decision、retrieved source、
  tool decision、memory decision 與 human review status。
- 我能把 tool abuse、memory leakage、permission bypass、prompt-only approval、
  missing audit detail 對應到具體 governance controls。
- 我能把 Day 2 的 policy 假設轉成 Day 3 red-team seeds。

Day 2 的最小可交付成果是：

1. Governance layer map。
2. Common-vs-adapter table。
3. Agent registration record。
4. Policy gate record。
5. Audit event schema。
6. Risk-control map。
7. Day 3 red-team seed list。

---

## 5. Accelerators 需要什麼

每個 accelerator day 都要把知識轉成 evidence。Day 2 至少需要：

1. **Architecture or governance view**：學生能畫出 identity、agent registry、
   tool boundary、data boundary、memory boundary、policy gate、audit event、
   evaluation hook、red-team seed 的關係。
2. **Contract or schema**：學生能寫出 agent registration、policy gate、
   audit event 的欄位。
3. **Mechanism explanation**：學生能說明為什麼 prompt 不等於權限控制。
4. **Failure-mode reasoning**：學生能把缺少 governance 的狀態對應到具體風險。
5. **Review evidence**：TA 能從學生 artifact 判斷設計是否合格。
6. **Next-day handoff**：Day 2 產出的 policy assumption 可以直接變成 Day 3
   red-team test cases。

老師設計 Day 2 時，請使用這個固定流程：

```text
Day 1 AI Gateway lifecycle
-> why agents need governance
-> governance layers
-> common vs adapter separation
-> agent registration
-> tool and memory boundaries
-> policy gate
-> audit event
-> risk-control map
-> red-team seed handoff
```

---

## 6. Accelerators 的重點

Accelerator 的重點是 evidence quality，不是速度本身。Day 2 的 evidence quality
可以用以下問題判斷：

- 這個 agent 的 owner 是誰？
- 這個 agent 允許處理什麼 task scope？
- 哪些 user role 可以呼叫它？
- 哪些工具是 read-only？哪些工具有 side effect？
- 哪些 action 需要 human review？
- 這個 agent 能查哪些 data source？metadata filter 是什麼？
- 這個 agent 能讀寫哪種 memory？保留多久？能否跨 agent 分享？
- policy gate 的 input 是什麼？output 是什麼？
- `allow`、`deny`、`review` 的條件是否清楚？
- audit event 是否能重建 request lifecycle？
- 失敗模式是否能轉成 Day 3 red-team test？

Day 2 最重要的觀念是：

```text
Prompt can guide behavior.
Policy and system boundaries enforce behavior.
Audit evidence proves what happened.
```

---

## 7. Day 2 的指定主題

指定主題是：

```text
Agent Governance Framework
```

Day 2 要銜接 Day 1：

```text
Day 1: AI Gateway Architecture Evidence
Day 2: Agent Governance Framework
Day 3: Red Teaming Framework
```

Day 1 已建立 Gateway mental model：

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

Day 2 要回答 Gateway 要怎麼知道一個 agent 是否可以被使用：

```text
request
-> identity
-> agent registry lookup
-> tool/data/memory scope check
-> policy decision
-> optional human review
-> audited execution
-> evaluation/red-team feedback
```

這一天的課程不是要學生實作完整 policy engine。它要讓學生產出能驅動後續 lab
與 red-team 測試的 governance contract。

---

## 8. Day 2 學習目標

老師設計教程時，請把 learning objectives 寫成可觀察、可評分的能力，而不是
抽象的「理解 agent governance」。

建議學習目標如下：

1. 學生能說明為什麼 enterprise agent 需要 registration、ownership、task scope、
   allowed tools、allowed data sources、memory scope、policy gates、audit events
   與 review states。
2. 學生能區分 common governance rules 與 adapter-specific behavior。
3. 學生能為一個 public-safe enterprise agent 撰寫 agent registration record。
4. 學生能撰寫 policy gate，並讓 policy decision 明確回傳 `allow`、`deny` 或
   `review`。
5. 學生能設計 audit event schema，記錄 identity、agent、tool、source、memory、
   policy、guardrail、review 與 outcome。
6. 學生能把 tool abuse、memory leakage、permission bypass、prompt-only approval、
   missing audit detail 對應到具體 governance controls。
7. 學生能產出 Day 3 red-team seeds，讓治理假設變成可測試案例。

每個目標都要對應到學生 artifact 與 rubric category：

| 學習目標 | 學生 evidence | 評分項目 |
|---|---|---|
| Governance purpose | worksheet 短答 | beginner clarity |
| Common vs adapter | common-vs-adapter table | governance separation |
| Agent registration | YAML/JSON registration record | registration completeness |
| Policy gate | policy gate record | enforceable decision design |
| Auditability | audit event schema | traceability |
| Risk-control | risk-control map | engineering reasoning |
| Day 3 readiness | red-team seed list | testability |

---

## 9. Day 2 學生先備知識

Day 2 可以面向大二學生，但老師需要在課程中補上橋接知識。

### 9.1 最低先備知識

學生需要具備：

- 基本 Python 或 JavaScript 程式能力。
- HTTP request / response。
- JSON 與簡單 JSON schema。
- 使用者角色與權限概念。
- 基礎資料庫觀念：table、query、permission、log。
- 軟體工程概念：module、interface、contract、test、logging。
- Day 1 AI Gateway request lifecycle。

### 9.2 課前要補的概念

老師可以用簡短課前閱讀補上：

- Auth 與 RBAC：誰可以使用系統。
- Policy gate：系統在執行前做 allow / deny / review 判斷。
- Tool calling：agent 呼叫外部 function/API 的能力。
- Side effect：會改變外部狀態的動作，例如送出 ticket、寄信、更新資料庫。
- Memory：agent 保留或讀取先前互動資訊的狀態。
- Audit log：可追蹤與可審查的 evidence，不是單純 debug print。

### 9.3 建議課前診斷題

請老師在上課前或課堂一開始問學生：

1. 如果 prompt 寫「不要讀 staff-only 文件」，為什麼這不等於真正的權限控制？
2. `search_faq` 和 `submit_ticket` 這兩個 tool 的風險差異是什麼？
3. 如果 agent 記住學生姓名與學號，這是 usability feature 還是 permission boundary？
4. audit log 應該只記錄最後回答，還是也要記錄 source、tool、policy decision？
5. 一個 agent 沒有 owner，日後出錯時誰負責修正？

---

## 10. 軟體工程實踐角度

Day 2 應該把 agent governance 教成 software engineering contract design。

### 10.1 Agent Registry 是 configuration contract

Agent registry 不是一份「agent 名單」而已。它是 Gateway 判斷 agent 是否可用的
configuration contract。

建議學生使用 YAML 或 JSON：

```yaml
agent_id: campus_it_helpdesk_agent
owner: campus_it_service_desk
task_scope:
  - answer_public_it_faq
  - draft_ticket_summary
risk_class: medium
allowed_users:
  - student
  - staff
allowed_tools:
  - search_it_faq
  - draft_ticket
allowed_data_sources:
  - public_it_faq
  - vpn_setup_guide
memory_scope:
  read: session
  write: session
  shared_memory: false
approval_required_for:
  - submit_ticket
evaluation_set:
  - vpn_setup_answer_cites_current_guide
  - password_reset_refuses_staff_sop
red_team_suite:
  - staff_sop_bypass
  - ticket_spam_attempt
audit_events:
  - agent_request_started
  - policy_decision_recorded
  - tool_decision_recorded
  - human_review_required
```

軟體工程重點：

- registry 可以 version control。
- registry 可以被測試。
- registry 可以被 review。
- registry 可以驅動 Gateway routing。
- registry 可以讓新 agent 重用 common governance。

### 10.2 Tool Boundary 是 side-effect control

老師需要讓學生區分 tool 的風險：

| Tool | 類型 | 風險 | Governance control |
|---|---|---|---|
| `search_it_faq` | read-only | 查到錯誤或過期文件 | metadata filter、citation、source version |
| `lookup_ticket_status` | read-only but sensitive | 查到別人的 ticket | user binding、role check、audit |
| `submit_ticket` | side-effect | 大量建立 ticket、提交錯誤資料 | approval gate、rate limit、audit |
| `reset_password` | high-risk side-effect | 帳號被惡意操作 | strong auth、human review、deny by default |

學生要學到：tool schema 只描述怎麼呼叫 tool，不等於誰可以呼叫 tool。權限必須由
Gateway、policy engine 或 tool broker enforcement 決定。

### 10.3 Policy Gate 是 decision API

Policy gate 應該被教成一個 decision API。最小形狀可以是：

```json
{
  "request_id": "req-001",
  "user": {
    "id": "student_001",
    "role": "student"
  },
  "agent_id": "campus_it_helpdesk_agent",
  "requested_action": "submit_ticket",
  "data_sources": ["public_it_faq"],
  "tool": "submit_ticket",
  "memory_write": "session_summary"
}
```

policy output：

```json
{
  "decision": "review",
  "reason": "submit_ticket is a side-effect action",
  "required_reviewer_role": "it_reviewer",
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

老師可以把這裡連到 OPA 或 Cedar，但不要讓工具名稱取代核心概念。OPA 官方文件
將 OPA 定位為 general-purpose policy engine，並透過 Rego 對 structured data
做 policy decision；Cedar 則是用來撰寫 authorization policies 並做 authorization
decision 的 policy language。Day 2 只需要學生理解「policy decision 應該是
可測試的系統輸出」。

### 10.4 Audit Event 是 lifecycle evidence

audit event 不是 debug log。debug log 是工程師排錯用，audit event 是系統日後
審查責任、資料來源、工具行為、policy decision 的 evidence。

建議 audit event shape：

```json
{
  "trace_id": "req-0001",
  "user_id": "student_001",
  "user_role": "student",
  "agent_id": "campus_it_helpdesk_agent",
  "policy_decision": "review",
  "retrieved_source_ids": ["vpn-guide-2026-01"],
  "tool_decisions": [
    {
      "tool_name": "submit_ticket",
      "decision": "review",
      "reason": "side-effect action"
    }
  ],
  "memory_decision": "session_only_no_shared_pii",
  "human_review_status": "pending",
  "outcome": "answer_returned_ticket_pending"
}
```

軟體工程重點：

- log 要能連到 trace ID。
- policy decision 要能被重建。
- retrieved source IDs 要能被查回文件版本。
- tool decision 要能說明是否真的執行。
- human review status 要能說明輸出是否已經被核准。

---

## 11. 系統工程實踐角度

Day 2 應該把 agent governance 教成 control plane design，而不是單一 agent prompt。

### 11.1 系統分層

建議老師使用這張 mental model：

```text
User / Channel
-> Auth / RBAC
-> AI Gateway
-> Agent Registry
-> Policy Gate
-> Tool Broker
-> RAG Connector
-> Memory Store
-> Model Runtime
-> Guardrail
-> Audit Event Store
-> Human Review Queue
-> Evaluation / Red-Team Feedback
```

系統工程重點是：每個 subsystem 都有不同責任。

| Subsystem | 責任 | Day 2 相關 artifact |
|---|---|---|
| Auth / RBAC | 確認 user identity 與 role | allowed users |
| Agent Registry | 紀錄 agent owner、scope、risk | registration record |
| Policy Gate | 做 allow / deny / review | policy gate |
| Tool Broker | 控制工具 schema、permission、timeout | tool boundary |
| RAG Connector | 控制 data source 與 metadata filter | data boundary |
| Memory Store | 控制 read/write、retention、sharing | memory scope |
| Audit Store | 保存可審查 evidence | audit event |
| Human Review Queue | 處理高風險或 side-effect action | review state |
| Evaluation / Red Team | 持續驗證 governance 是否有效 | eval hook、red-team seed |

### 11.2 Common Layer Vs Adapter Layer

Day 2 的核心系統設計能力是 reusable governance。老師需要讓學生避免為每個
customer 或 task 重做一套 governance。

| Layer | Common governance | Adapter-specific behavior |
|---|---|---|
| Identity | user、role、tenant、service account、agent identity | 校園角色對應：student、staff、it_reviewer |
| Memory | storage scope、retention、deletion、sharing rule | IT helpdesk 只保留 session note |
| Tool | schema、permission、timeout、retry、idempotency | `search_it_faq`、`submit_ticket` |
| Policy | allowed tasks、blocked tasks、risk class、approval rule | ticket submission requires review |
| Audit | trace ID、source IDs、tool calls、decisions | campus IT report format |
| Evaluation | success、safety、latency、coverage | VPN 答案需引用最新 guide |
| Red teaming | threat taxonomy and test harness | staff SOP bypass、ticket spam |

系統工程重點：

- common layer 讓治理可重用。
- adapter layer 讓系統能接不同業務情境。
- 若所有規則都寫死在 prompt 或單一 agent code，系統會難以維護。

### 11.3 Control Plane 與 Data Plane

老師可以補充 control plane / data plane 的思考方式：

| 平面 | 責任 | Day 2 例子 |
|---|---|---|
| Control plane | 決定是否可以做、由誰做、怎麼審查 | registry、policy、approval、audit |
| Data plane | 實際處理資料與回應 | RAG retrieval、tool execution、model response |

學生常見錯誤是把所有東西都放到 data plane，例如讓 model 自己決定是否可以呼叫
工具。Day 2 要建立的工程習慣是：高風險決策要放在 system-enforced control plane。

---

## 12. Day 2 真實世界案例

請老師使用 public-safe、generalized 的真實世界情境。以下案例適合大二學生。

### 12.1 校園 IT Helpdesk Assistant

這是 Day 2 的主要建議案例，因為學生容易理解。

情境：

```text
學生詢問 VPN 設定方式。若排除問題仍無法連線，agent 可以協助草擬 ticket，
但不能未經確認直接提交 ticket，也不能讀 staff-only SOP。
```

資料來源：

- public IT FAQ。
- VPN setup guide。
- service status page。
- staff-only account-lock SOP。

工具：

- `search_it_faq`：read-only。
- `lookup_service_status`：read-only。
- `draft_ticket`：產生草稿，無 side effect。
- `submit_ticket`：side-effect，需要 review。

治理重點：

- student 可以查 public FAQ。
- student 不可以查 staff-only SOP。
- ticket submission 需要 human review。
- memory 只能保存 session summary，不進 shared memory。
- audit event 必須記錄 retrieved source IDs 與 tool decisions。

### 12.2 銀行內部知識助理

情境：

```text
行員查詢產品規則、合規流程與客戶服務 SOP。
```

治理重點：

- user role 影響資料可見範圍。
- policy gate 應阻擋跨角色資料查詢。
- output 需要引用文件版本。
- 高風險回答進 staff-review workflow。
- red-team seeds 包含 prompt injection、PII leakage、policy bypass。

技術細節：

- data source metadata 應包含 `access_level`、`document_version`、
  `department`、`effective_date`。
- audit event 應記錄 source IDs 與 policy reason。
- memory 不應跨分行或跨角色分享敏感內容。

### 12.3 醫療預問診支援系統

公共安全表述：

```text
系統協助整理病人輸入與公開衛教資料，輸出進入 staff-review intake support，
不作為最終診斷。
```

治理重點：

- patient-provided data 與 public education data 要分層。
- high-risk medical advice 進 human review。
- PII 需要遮罩或最小化保存。
- audit event 記錄 source、review status、scope boundary。
- agent registration 明確標示 staff-review intake support。

### 12.4 製造場域維修助理

情境：

```text
工程師詢問設備維修 SOP，agent 協助查詢公開或內部文件，並草擬維修紀錄。
```

治理重點：

- 不同設備線別與廠區有不同資料權限。
- `create_maintenance_record` 是 side-effect tool。
- 高風險操作需 supervisor approval。
- audit 要記錄設備 ID、文件版本、工具呼叫、review status。

---

## 13. Day 2 老師需要幫我們設計的完整教程組件

請老師依照 repo 的固定 day package 結構設計內容：

```text
accelerators/enterprise-ai-architecture-sprint/day-02-agent-governance/
├── README.md
├── student-handout.md
├── instructor-guide.md
├── worksheet.md
├── reference-answer-campus-it-agent.md
├── rubric.md
├── day-03-red-team-handoff.md
├── glossary-updates.md
└── source-package.md
```

### 13.1 `README.md`

用途：Day 2 的總覽與導覽。

請包含：

- Day metadata。
- target learner。
- learning objectives。
- file map。
- recommended use order。
- objective-to-assessment map。
- student/instructor separation。
- minimum deliverables。
- source boundary。
- background references。

### 13.2 `student-handout.md`

用途：學生主要講義。

請包含：

- 第一結論。
- Day 1 到 Day 2 的銜接。
- governance layer mental model。
- core terms table。
- Campus IT Helpdesk Assistant scenario。
- common governance vs adapter behavior。
- agent registration template。
- policy gate template。
- audit event shape。
- risk-control map。
- Day 2 submission checklist。

請不要包含：

- 完整參考答案。
- 詳細評分規準。
- instructor-only failure diagnosis。

### 13.3 `instructor-guide.md`

用途：老師與 TA 的授課指南。

請包含：

- pre-class diagnostic。
- 150 分鐘與 180 分鐘授課流程。
- board / slide plan。
- instructor questions。
- common failure gallery。
- peer review 指引。
- Day 3 handoff 指引。

common failure gallery 至少要包含：

1. prompt-only approval。
2. tool schema 有了但沒有 permission rule。
3. audit log 只記錄 final answer。
4. memory scope 空白或跨 agent 分享。
5. common governance 與 adapter-specific behavior 混在一起。

### 13.4 `worksheet.md`

用途：學生課堂產出模板。

請包含以下填寫區：

1. governance layer map。
2. common-vs-adapter table。
3. agent registration record。
4. tool boundary table。
5. memory scope rule。
6. policy gate record。
7. audit event schema。
8. risk-control map。
9. Day 3 red-team seed list。
10. final checklist。

### 13.5 `reference-answer-campus-it-agent.md`

用途：教師與 TA 參考答案。

請使用 Campus IT Helpdesk Agent，提供一份 public-safe 完整範例。

需要包含：

- scenario boundary。
- governance layer map。
- common-vs-adapter table。
- registration record。
- policy gate。
- audit event。
- risk-control map。
- Day 3 red-team seeds。
- common mistakes。

### 13.6 `rubric.md`

用途：100 分量化評分。

建議配分：

| 項目 | 分數 |
|---|---:|
| Governance layer map | 15 |
| Common-vs-adapter separation | 15 |
| Agent registration | 20 |
| Policy gate | 15 |
| Audit event schema | 15 |
| Risk-control and Day 3 readiness | 10 |
| Beginner clarity | 5 |
| Source boundary | 5 |

Rubric 必須讓 TA 可以從 artifact 評分，而不是從學生口頭感覺評分。

### 13.7 `day-03-red-team-handoff.md`

用途：把 Day 2 轉成 Day 3 red-team framework。

請包含：

- Day 3 會消耗哪些 Day 2 artifacts。
- threat categories。
- red-team test case schema。
- policy-to-test mapping。
- acceptance criteria。

### 13.8 `glossary-updates.md`

用途：後續整併到 global glossary。

建議詞彙：

- Agent Registry。
- Task Scope。
- Tool Boundary。
- Side-Effect Tool。
- Memory Scope。
- Policy Gate。
- Review State。
- Audit Event。
- Evaluation Hook。
- Red-Team Seed。
- Common Governance。
- Adapter-Specific Behavior。

---

## 14. Day 2 Artifact 詳細要求

### 14.1 Governance Layer Map

學生要畫出：

```text
Identity
-> Agent Registry
-> Tool Boundary
-> Data Boundary
-> Memory Boundary
-> Policy Gate
-> Audit Event
-> Evaluation Hook
-> Red-Team Seed
```

合格標準：

- 至少包含 identity、agent、tool、data、memory、policy、audit、review。
- 每層有一句責任說明。
- 能說明哪一層負責 enforcement，哪一層負責 evidence。

### 14.2 Common-Vs-Adapter Table

學生要能區分：

| Layer | Common governance | Adapter-specific behavior |
|---|---|---|
| Identity | user、role、tenant | 校園 IT role mapping |
| Tool | schema、timeout、permission | `search_it_faq`、`submit_ticket` |
| Data | metadata filter、access level | public FAQ vs staff SOP |
| Memory | retention、sharing、deletion | session-only note |
| Policy | allow / deny / review | ticket submission requires review |
| Audit | trace ID、source IDs、tool decisions | helpdesk audit report |

合格標準：

- common layer 可以跨兩個以上 scenario 重用。
- adapter layer 是情境映射，不是重新設計整套 governance。

### 14.3 Agent Registration Record

學生要填寫：

```yaml
agent_id:
owner:
task_scope:
risk_class: low | medium | high
allowed_users:
allowed_tools:
allowed_data_sources:
memory_scope:
approval_required_for:
evaluation_set:
red_team_suite:
audit_events:
```

合格標準：

- 每個欄位都有可檢查內容。
- tool、data、memory、approval 與 audit 彼此一致。
- risk class 與 review rule 有合理關係。

### 14.4 Policy Gate Record

學生要填寫：

```yaml
policy_id:
applies_to:
preconditions:
allowed_actions:
blocked_actions:
pii_rule:
retrieval_rule:
tool_rule:
memory_rule:
human_review_trigger:
failure_response:
audit_fields:
```

合格標準：

- policy 可以回傳 `allow`、`deny` 或 `review`。
- deny 與 review 的條件清楚。
- failure response 不洩漏敏感資訊。
- audit fields 能支持日後 review。

### 14.5 Audit Event Schema

學生要設計至少包含：

- trace ID。
- user ID or pseudonymous user ID。
- user role。
- agent ID。
- policy decision。
- retrieved source IDs。
- tool decisions。
- memory decision。
- human review status。
- outcome。

合格標準：

- 能重建 request lifecycle。
- 不只記錄 final answer。
- 不保存不必要的 PII。

### 14.6 Risk-Control Map

至少包含以下風險：

| Risk | Example | Required control | Evidence |
|---|---|---|---|
| Tool abuse | agent 重複提交 ticket | tool boundary、approval、rate limit | tool decision log |
| Memory leakage | PII 進入 shared memory | memory scope、retention、deletion | memory decision |
| Permission bypass | student 讀 staff SOP | retrieval rule、metadata filter | source filter log |
| Prompt-only approval | model 自稱 approved | policy gate | policy decision |
| Missing audit detail | 無法知道 tool 是否執行 | audit schema | complete audit event |

---

## 15. Day 2 的教師追問問題

老師授課時可以用這些問題逼學生做工程判斷：

1. 如果 agent registration 沒有 owner，incident 發生時誰負責修正？
2. 如果 `submit_ticket` 沒有 review gate，最壞情況是什麼？
3. tool schema 與 tool permission 有什麼差異？
4. 為什麼 memory scope 是治理問題，不只是 UX 問題？
5. policy decision 為什麼要輸出 reason？
6. audit event 應該記錄 prompt 嗎？如果 prompt 含 PII，怎麼處理？
7. 哪些 governance assumptions 可以變成 Day 3 red-team tests？
8. 如果要把 Campus IT Agent 改成 Bank Internal Knowledge Agent，哪些 layer 可重用？
9. 哪些控制應該由 system enforce，而不是由 model 自行判斷？

---

## 16. 常見學生誤解與修正

| 誤解 | 修正 |
|---|---|
| prompt 寫清楚就等於安全 | prompt 是 instruction，不是 permission boundary |
| agent registry 只是 inventory | registry 是 Gateway routing 與 governance contract |
| tool schema 定義參數就夠了 | schema 不等於權限、審核、timeout、audit |
| memory 是聊天體驗功能 | memory 也是資料保留、分享、刪除與洩漏邊界 |
| audit log 只要記錄最後回答 | audit 要記錄 source、tool、policy、review、outcome |
| 每個客戶都重寫治理邏輯 | common governance 應重用，adapter 只處理情境映射 |
| red-team 是 Day 3 才要想 | Day 2 policy 假設本身就是 Day 3 測試種子 |

---

## 17. 老師撰寫時的語氣與範圍

請使用 Traditional Chinese 撰寫主要內容，保留必要英文工程詞彙，例如：

- `AI Gateway`
- `Agent Registry`
- `Tool Broker`
- `Policy Gate`
- `Memory Scope`
- `Audit Event`
- `Human Review`
- `Evaluation Hook`
- `Red-Team Seed`
- `OPA`
- `Cedar`
- `OpenTelemetry`

每個英文詞第一次出現時，請給學生版定義與工程版定義。

請用正向、主動、可信任、邊界清楚的語氣。不要把 Day 2 寫成恐嚇式安全清單，
而是寫成可交付系統必備的 governance design。

建議表述：

```text
這個 agent 的可用範圍由 registry、policy gate、tool boundary 與 audit event
共同定義。
```

避免表述：

```text
AI 很危險，所以不要相信 agent。
```

---

## 18. Source Boundary

Day 2 的案例必須是 public-safe。可以使用：

- 校園 IT helpdesk。
- 銀行內部知識助理。
- 醫療 staff-review intake support。
- 製造場域維修助理。
- 一般化 enterprise support workflow。

不要使用：

- 私人訪談逐字稿。
- 客戶秘密。
- credentials。
- personal contact routes。
- salary 或 offer detail。
- 未公開公司主張。
- 可識別個資。

若有任何私人來源啟發，請改寫成一般化系統需求，例如：

```text
enterprise customer requires approval-gated side-effect actions
```

而不是保存原始私人情境。

---

## 19. 背景標準與官方參考

老師不需要把以下文件變成學生必讀，但撰寫教程時可以用它們校準技術語言。

截至 2026-06-13 的官方來源重點：

- OWASP GenAI Security Project 提供 2025 LLM and GenAI Apps Top 10 risks，
  包含 prompt injection、sensitive information disclosure、improper output handling、
  excessive agency、vector and embedding weaknesses 等風險類別。
- NIST AI RMF Core 將 AI risk management 組織成 govern、map、measure、manage
  四個功能，適合用來解釋 Day 2 的 governance、risk mapping、measurement 與
  management lifecycle。
- OPA 是 general-purpose policy engine，可用 structured data 做 policy-as-code
  decision；Day 2 可把它作為 policy gate 的工程例子。
- Cedar 是 authorization policy language，可用 principal、action、resource、
  context 的方式理解 authorization decision；Day 2 可用它補充 allow/deny 的
  policy mental model。

參考連結：

- OWASP Top 10 for LLM and GenAI Applications 2025：
  <https://genai.owasp.org/llm-top-10/>
- NIST AI RMF Core：
  <https://airc.nist.gov/airmf-resources/airmf/5-sec-core/>
- Open Policy Agent documentation：
  <https://www.openpolicyagent.org/docs>
- OPA Policy Language / Rego：
  <https://www.openpolicyagent.org/docs/policy-language>
- Cedar Policy Language Reference Guide：
  <https://docs.cedarpolicy.com/>
- OpenTelemetry documentation：
  <https://opentelemetry.io/docs/>

---

## 20. 老師最終交付建議

請老師最終交付一份完整 Day 2 course package，而不是單一長文。建議交付物：

```text
day-02-agent-governance/
├── README.md
├── student-handout.md
├── instructor-guide.md
├── worksheet.md
├── reference-answer-campus-it-agent.md
├── rubric.md
├── day-03-red-team-handoff.md
├── glossary-updates.md
└── source-package.md
```

交付時請同時說明：

- 哪些內容給學生。
- 哪些內容只給老師與 TA。
- 哪些 artifact 要在課堂中完成。
- 哪些 artifact 作為作業提交。
- 哪些內容銜接 Day 3 red teaming。
- 哪些術語需要整併到 global glossary。

---

## 21. Day 2 完成定義

Day 2 可以視為完成，當它滿足以下條件：

- 學生可以不用看參考答案完成 worksheet。
- 老師可以用 instructor guide 上完 150 或 180 分鐘課程。
- TA 可以用 100 分 rubric 評分。
- reference answer 有一個完整 public-safe Campus IT Helpdesk Agent 範例。
- 所有 learning objectives 都對應到 artifact 與 rubric。
- student-facing material 沒有洩漏 reference answer。
- policy gate、tool boundary、memory scope、audit event 都有具體 schema 或 template。
- risk-control map 能銜接 Day 3 red-team seeds。
- source boundary 清楚。

---

## 22. 給老師的直接委託文字

老師您好，我們想請您協助設計 `AI Systems Engineering Handbook` 中
`Enterprise AI Architecture Sprint` 的 Day 2 教程，主題是
`Agent Governance Framework`。

這份 Day 2 教程的目標讀者是資訊工程大二學生。他們已具備基礎程式設計、
HTTP/JSON、資料庫、log、role 與軟體工程概念，也已完成 Day 1 的
AI Gateway architecture mental model。Day 2 希望讓學生理解 enterprise agent
不是只靠 prompt 管理，而是要透過 agent registry、tool boundary、data boundary、
memory scope、policy gate、audit event、human review、evaluation hook 與
red-team seed 形成可治理、可測試、可審查的系統。

請您以軟體工程實踐與系統工程實踐的角度，為 Day 2 設計一套完整 course package，
包含學生版教程、教師授課指南、worksheet、Campus IT Helpdesk Agent 參考答案、
100 分 rubric、glossary updates 與 Day 3 red-team handoff。請特別針對初學者
大二學生，用清楚的 Traditional Chinese 解釋每個概念，保留必要英文工程詞彙，
並使用 public-safe 真實世界案例，例如校園 IT helpdesk、銀行內部知識助理、
醫療 staff-review intake support 或製造場域維修助理。

Day 2 的核心要學生完成七個 artifact：

1. Governance layer map。
2. Common-vs-adapter table。
3. Agent registration record。
4. Policy gate record。
5. Audit event schema。
6. Risk-control map。
7. Day 3 red-team seed list。

請讓每個 learning objective 都能對應到可提交 artifact 與可量化 rubric。請不要
把 reference answer 或詳細評分規準放進學生版教程。請確保 Day 2 的輸出可以直接
銜接 Day 3 red-team framework，讓學生把 governance assumptions 轉成可測試的
prompt injection、tool abuse、memory leakage、permission bypass 與 audit evasion
test cases。
