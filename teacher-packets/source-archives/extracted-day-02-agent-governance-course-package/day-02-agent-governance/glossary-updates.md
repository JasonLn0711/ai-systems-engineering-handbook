# Glossary Updates — Day 2：Agent Governance Framework

> 建議後續整併到 global glossary。每個詞彙包含學生版定義、工程版定義、常見誤解與 Day 2 artifact 關聯。

---

## 1. Gateway Mock Continuity

學生版定義：

```text
Day 2 的設計要能接回 Day 1 的 gateway mock，而不是變成獨立表格。
```

工程版定義：

```text
The alignment between Day 1 `POST /gateway/requests` lifecycle and Day 2 governance artifacts, including schema validation, identity resolution, policy decision, tool/data/memory enforcement, review state, audit event, and HTTP outcome.
```

常見誤解：只要畫出 governance 圖就算接回 Gateway。

修正：必須寫出 route、request fields、trusted identity source、decision paths、HTTP outcomes、audit fields。

Artifact：Day 1-to-Day 2 Gateway Alignment Note。

---

## 2. Gateway Alignment Note

學生版定義：一份把 Gateway request 流程對應到治理設計的對照表。

工程版定義：

```text
An implementation bridge that maps a gateway route and request schema to identity resolution, action extraction, agent registry lookup, policy decisions, tool/data/memory boundary checks, review triggers, audit fields, and HTTP outcomes.
```

常見誤解：把它寫成心得或摘要。

修正：它應該像 implementation contract，可以讓工程師開始寫 handler。

---

## 3. Agent Registry

學生版定義：Agent 的登記表，記錄它可以做什麼、誰負責、能用哪些工具和資料。

工程版定義：

```text
A version-controlled configuration contract used by the AI Gateway to route requests and enforce governance constraints for an agent.
```

常見誤解：Registry 只是 agent inventory。

修正：Registry 要包含 owner、task_scope、risk_class、allowed_users、allowed_tools、allowed_data_sources、memory_scope、approval_required_for、evaluation_set、red_team_suite、audit_events。

---

## 4. Task Scope

學生版定義：Agent 被允許處理的任務範圍。

工程版定義：

```text
An explicit boundary describing which actions, intents, and workflows an agent may handle, used by routing, policy, review, evaluation, and red-team tests.
```

常見誤解：task_scope 寫越廣越方便。

修正：過寬 scope 會導致 excessive agency。Scope 要能轉成 allowed/blocked action。

---

## 5. Tool Boundary

學生版定義：規定 agent 能不能用某個 tool、誰能用、什麼情況要審核。

工程版定義：

```text
A control boundary that enforces tool permission, side-effect classification, timeout, retry, rate limit, idempotency, review requirement, and audit behavior.
```

常見誤解：Tool schema 等於 tool boundary。

修正：Tool schema 是 interface；tool boundary 是 permission and execution control。

---

## 6. Side-Effect Tool

學生版定義：會改變外部系統狀態的工具。

工程版定義：

```text
A tool that creates, updates, deletes, sends, submits, resets, charges, or otherwise mutates external state.
```

例子：`submit_ticket`、`send_email`、`reset_password`、`create_invoice`、`update_customer_record`。

常見誤解：只要不是刪資料就不是 side effect。

修正：建立 ticket、寄信、送出表單也都是 side effect。

---

## 7. Memory Scope

學生版定義：Agent 可以讀寫什麼記憶、保存多久、能不能分享。

工程版定義：

```text
A rule set defining memory read scope, write scope, retention, deletion, sharing, PII handling, and audit behavior.
```

常見誤解：Memory 只是 UX 功能。

修正：Memory 也是資料保留、權限、隱私與洩漏邊界。

---

## 8. Policy Gate

學生版定義：系統在執行前判斷 allow、deny 或 review 的地方。

工程版定義：

```text
A decision API that evaluates identity, agent, action, tool, data, memory, and context, then returns an enforceable decision with reason, review requirement, safe message, and audit fields.
```

常見誤解：Policy 是 prompt 裡的一段規則。

修正：Policy gate 應該是 system-enforced decision point。

---

## 9. Review State

學生版定義：需要人審的操作目前處於 pending、approved、rejected 等狀態。

工程版定義：

```text
A workflow state representing human approval lifecycle for high-risk or side-effect actions, including reviewer role, review ID, status, and final decision.
```

常見誤解：模型說「已核准」就算 approved。

修正：Approval 必須由 server-side reviewer identity 與 review queue 狀態決定。

---

## 10. Audit Event

學生版定義：系統留下的可審查證據，不只是 debug log。

工程版定義：

```text
A structured, append-only lifecycle event that records trace ID, identity, agent, policy decision, retrieved sources, tool decisions, memory decision, review status, guardrail decision, HTTP status, and outcome.
```

常見誤解：Audit 只要記最後回答。

修正：Audit event 要能重建 request lifecycle。

---

## 11. Evaluation Hook

學生版定義：把治理規則接到自動測試的地方。

工程版定義：

```text
A connection point between governance assumptions and evaluation tests, including regression sets for correctness, safety, latency, source citation, policy compliance, and review behavior.
```

常見誤解：Evaluation 只測回答好不好。

修正：Enterprise AI evaluation 也要測 policy、tool、data、memory、audit 與 review。

---

## 12. Red-Team Seed

學生版定義：下一堂課攻防測試的初始案例。

工程版定義：

```text
A testable adversarial scenario derived from a governance assumption, including target control, input message, expected policy decision, expected HTTP outcome, expected audit fields, pass condition, and failure signal.
```

常見誤解：Red-team seed 只是攻擊 prompt。

修正：Seed 要能測出某個 control 是否失效。

---

## 13. Common Governance

學生版定義：可以跨不同情境重用的治理規則。

工程版定義：

```text
Reusable platform-level governance capabilities such as identity model, policy decision pattern, tool permission framework, memory retention rules, audit schema, and red-team taxonomy.
```

常見誤解：把 Campus IT 的 student/VPN/ticket 規則寫進 common layer。

修正：student/VPN/ticket 是 adapter-specific；role-based access、metadata filter、review gate 是 common。

---

## 14. Adapter-Specific Behavior

學生版定義：某個情境自己的角色、工具、資料來源與流程映射。

工程版定義：

```text
Scenario-specific mapping of common governance primitives to concrete roles, tools, data sources, actions, review workflows, report formats, and tests.
```

常見誤解：每個 adapter 都重寫整套 governance。

修正：Adapter 只映射業務情境，不應重做平台治理。

---

## 15. Data Boundary

學生版定義：Agent 可以查哪些資料、不能查哪些資料。

工程版定義：

```text
A retrieval and access control boundary implemented through source allowlists, access level metadata, document version constraints, freshness requirements, and role/tenant filters.
```

常見誤解：資料查出來後再叫模型不要說。

修正：受限資料不應進入 model context；要在 retrieval 前用 metadata filter 阻擋。

---

## 16. Tool Broker

學生版定義：管理 agent 呼叫工具的中介層。

工程版定義：

```text
A service layer that validates tool calls, checks permission, enforces timeouts/rate limits/idempotency, handles retries, blocks unauthorized tools, and records audit evidence.
```

常見誤解：讓 model 直接呼叫任何 function。

修正：Model 可以提出 tool intent，但 tool broker 必須 enforcement。

---

## 17. Source Boundary

學生版定義：課程案例只能用公開、安全、一般化資料。

工程版定義：

```text
A content boundary requiring examples and artifacts to avoid credentials, personal data, customer secrets, private interview transcripts, unpublished claims, and identifiable contact routes.
```

常見誤解：把真實公司或真實人員資料匿名化就一定安全。

修正：優先改寫成一般化系統需求，而不是保留原始私人情境。
