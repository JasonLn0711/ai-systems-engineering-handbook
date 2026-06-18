# Rubric — Day 2：Agent Governance Framework

> 100 分量化評分規準。TA 應依學生提交的 artifacts 評分，不依學生口頭感覺評分。

---

## 0. Scoring Summary

| 項目 | 分數 |
|---|---:|
| Gateway mock continuity | 10 |
| Governance layer map | 12 |
| Common-vs-adapter separation | 13 |
| Agent registration | 17 |
| Policy gate | 18 |
| Audit event schema | 15 |
| Risk-control and Day 3 readiness | 10 |
| Source boundary | 5 |
| **Total** | **100** |

---

## 1. Gateway Mock Continuity — 10 分

評分重點：學生是否能把 Day 1 的 `POST /gateway/requests` lifecycle 接到 Day 2 governance artifacts，並說明跨 agent、process、tool、broker 的 request 如何透過 mediated path 執行。

| 分數 | 標準 |
|---:|---|
| 9-10 | 明確寫出 route、request schema、server-side identity resolution、action extraction/action proposal fields、agent registry lookup、policy decision、tool/data/memory/message boundary、declassification、human review、audit event 與 HTTP outcomes；至少包含 allow、deny、review、400、401、403、200。 |
| 7-8 | 有 route 與主要 lifecycle；identity、policy、message mediation 有說明；HTTP outcome 大致正確，但 review、declassification 或 audit 欄位略不足。 |
| 5-6 | 有提到 Gateway 與 policy，但 route/schema/HTTP outcome 不完整；trusted identity 與 client hints 邊界不清。 |
| 3-4 | 只抽象描述「Gateway 會檢查規則」；缺少具體 request/response contract。 |
| 0-2 | 沒有連回 Day 1 gateway mock，或把所有控制交給 prompt/model。 |

扣分指標：

- 信任 client-provided role：最多只能得 6 分。
- Action extraction 只有單一 label，沒有 action candidates、slots、risk、confidence 或 fallback：最多只能得 8 分。
- 沒有 400/401/403 outcome：最多只能得 7 分。
- 沒有 review_required 路徑：最多只能得 8 分。
- 沒有 message mediation / declassification 欄位：最多只能得 8 分。
- 完全沒有 `POST /gateway/requests` 或等價 route：最多只能得 5 分。

---

## 2. Governance Layer Map — 12 分

評分重點：學生是否能畫出 governance control plane 與 evidence flow。

| 分數 | 標準 |
|---:|---|
| 11-12 | 包含 identity、agent registry、tool boundary、data boundary、memory boundary、mediated message boundary、policy gate、human review、audit event、evaluation hook、red-team seed；每層有責任、enforcement、evidence。 |
| 9-10 | 主要層都有，但 evaluation/red-team 或 review 說明略弱。 |
| 7-8 | 有 identity、registry、policy、tool、audit，但 data/memory boundary 或 evidence 說明不足。 |
| 5-6 | 只有概念圖，缺少 enforcement/evidence。 |
| 3-4 | 把 governance 畫成 prompt + model + tool，缺少 control plane。 |
| 0-2 | 沒有 layer map，或完全無法看出治理分層。 |

扣分指標：

- 缺 memory boundary：扣 2-3 分。
- 缺 mediated message boundary：扣 2-3 分。
- 缺 audit event：扣 3-4 分。
- 缺 human review：扣 2 分。
- 沒說 enforcement/evidence：最多得 7 分。

---

## 3. Common-vs-Adapter Separation — 13 分

評分重點：學生是否理解 reusable governance，而不是每個情境重寫一套治理。

| 分數 | 標準 |
|---:|---|
| 12-13 | 清楚區分 common governance 與 adapter-specific behavior；涵蓋 identity、tool、data、memory、message mediation、policy、audit、evaluation、red-team；common layer 可跨 Campus IT、Bank、Healthcare、Manufacturing 重用。 |
| 10-11 | 大多數 layer 區分正確；少數案例把 adapter 細節放到 common。 |
| 8-9 | 有表格但重用性不足；common layer 偏像 Campus IT 特例。 |
| 5-7 | 只列出幾個 common/adapted examples，沒有系統性。 |
| 3-4 | 大量混淆 common 與 adapter；看不出平台化治理。 |
| 0-2 | 沒有此 artifact 或完全不正確。 |

扣分指標：

- 把 `student`、`VPN guide`、`IT reviewer` 寫成 common governance：扣 2-4 分。
- 沒有 evaluation/red-team row：扣 1-2 分。
- 無法說明換情境如何重用：最多得 8 分。

---

## 4. Agent Registration — 17 分

評分重點：registration 是否是可被 Gateway 使用的 configuration contract。

| 分項 | 分數 | 標準 |
|---|---:|---|
| Identity and ownership | 3 | 有穩定 `agent_id`、owner、description 或 owner group。 |
| Task scope and risk class | 3 | task_scope 清楚、不過寬；risk_class 與工具/資料/記憶風險一致。 |
| Allowed users/tools/data | 4 | allowed users、allowed tools、allowed data sources 完整，且有 blocked 或 metadata filter 概念。 |
| Memory and approval | 3 | memory_scope 有 read/write/retention/shared/PII；side-effect actions 有 approval_required_for；message/output 權限不與 memory 混淆。 |
| Eval/red-team/audit hooks | 4 | evaluation_set、red_team_suite、audit_events 可測試、可審查。 |

總分等級：

| 分數 | 標準 |
|---:|---|
| 15-17 | 欄位完整且一致，可直接作為 gateway mock config。 |
| 12-14 | 大多完整，但 memory、approval 或 eval/audit 有小缺口。 |
| 9-11 | 有 registration 但像 inventory；部分欄位過寬或不一致。 |
| 5-8 | 缺多個關鍵欄位；side-effect、data、memory 邊界不清。 |
| 0-4 | 沒有有效 registration，或全部寫成 prompt。 |

扣分指標：

- 沒 owner：扣 2 分。
- task_scope 寫 `answer anything`：扣 2-3 分。
- side-effect tool 無 approval：扣 3-4 分。
- memory_scope 空白：扣 3 分。
- allowed_message_channels 或 output_classification 空白且案例有跨 agent / broker flow：扣 2 分。
- audit_events 空白：扣 2 分。

---

## 5. Policy Gate — 18 分

評分重點：policy 是否可測試、可回傳 `allow`、`deny`、`review`，並可銜接 Gateway outcome。

| 分項 | 分數 | 標準 |
|---|---:|---|
| Policy structure | 3 | 有 `policy_id`、`applies_to`、preconditions。 |
| Decision coverage | 5 | 明確涵蓋 allow、deny、review 三種 decision。 |
| Tool/data/memory/message rules | 4 | retrieval_rule、tool_rule、memory_rule、message_rule、declassification_rule 可執行且彼此一致。 |
| Human review and failure response | 3 | review trigger、required reviewer、safe user message、failure response 清楚。 |
| Audit fields | 3 | audit fields 足以支持日後 review。 |

總分等級：

| 分數 | 標準 |
|---:|---|
| 16-18 | Policy gate 像 decision API；input/output 條件明確，可映射 HTTP outcome 與 audit。 |
| 13-15 | 有三種 decision；部分條件或 audit fields 不夠細。 |
| 10-12 | 有規則但像自然語言 policy；decision 邊界不夠清楚。 |
| 6-9 | 只描述 allowed/blocked，缺 review 或 memory/tool/data rule。 |
| 0-5 | Policy 只是 prompt 或口號，無法測試。 |

扣分指標：

- 缺 `review`：最多得 12 分。
- 沒有 deny 條件：最多得 10 分。
- 沒有 memory_rule：扣 2 分。
- 沒有 message_rule 或 declassification_rule，且設計包含跨邊界 agent/tool/broker：扣 2-3 分。
- failure response 洩漏敏感資訊：扣 2-4 分。
- policy 不輸出 reason：扣 1-2 分。

---

## 6. Audit Event Schema — 15 分

評分重點：audit event 是否能重建 request lifecycle，不只是 debug log。

| 分項 | 分數 | 標準 |
|---|---:|---|
| Core identity/trace fields | 3 | trace_id、timestamp、user_id/hash、user_role、tenant、agent_id。 |
| Policy and source evidence | 3 | policy_decision、policy_reason、retrieved_source_ids、source metadata/filter。 |
| Tool and memory evidence | 3 | tool_decisions、executed status、memory_decision、message_channel、output_classification。 |
| Review and outcome evidence | 3 | human_review_status、review_id、http_status、outcome、declassification/rejection reason。 |
| PII minimization | 3 | 不保存不必要 PII、credential、token；有 summary/hash/source ID 概念。 |

總分等級：

| 分數 | 標準 |
|---:|---|
| 14-15 | 可重建完整 lifecycle；欄位完整且避免 PII。 |
| 11-13 | 大致完整；少數欄位如 memory 或 review 不夠細。 |
| 8-10 | 有 audit schema，但偏 logging；source/tool/policy 有缺口。 |
| 5-7 | 只記 request/answer 或少數 debug 欄位。 |
| 0-4 | 沒有 audit event 或保存敏感原始資料。 |

扣分指標：

- 只記 final answer：最多得 5 分。
- 缺 policy_decision：扣 3 分。
- 缺 tool_decisions：扣 2-3 分。
- 缺 retrieved_source_ids：扣 2 分。
- 缺 message_channel 或 output_classification，且設計包含 broker/tool gateway：扣 1-2 分。
- 保存 password/token：最多得 6 分。

---

## 7. Risk-Control and Day 3 Readiness — 10 分

評分重點：是否能把風險轉成 controls、evidence 與 red-team seeds。

| 分項 | 分數 | 標準 |
|---|---:|---|
| Required risks | 3 | 至少包含 tool abuse、memory leakage、permission bypass、confused deputy、broker payload leakage、replay、missing schema field、prompt-only approval、missing audit detail。 |
| Controls and evidence | 3 | 每個 risk 有 required control 與 evidence。 |
| Red-team seed quality | 3 | 至少 8 個 seeds，含 input、target_control、expected decision、message/output expectation、HTTP outcome、audit fields、pass/failure。 |
| Day 2-to-Day 3 traceability | 1 | 每個 seed 能追溯到 Day 2 governance assumption。 |

總分等級：

| 分數 | 標準 |
|---:|---|
| 9-10 | risk-control map 完整，red-team seeds 可直接執行。 |
| 7-8 | 主要風險完整，部分 seeds expected outcome 不夠細。 |
| 5-6 | 有風險清單，但 control/evidence 或 red-team 欄位不足。 |
| 3-4 | 只有安全口號，缺可測試性。 |
| 0-2 | 沒有 risk-control 或 red-team handoff。 |

---

## 8. Source Boundary — 5 分

評分重點：是否保持 public-safe，沒有私人資料與不該使用的敏感來源。

| 分數 | 標準 |
|---:|---|
| 5 | 完全 public-safe；明確避免個資、credential、客戶秘密；案例一般化。 |
| 4 | 大致 public-safe；有少數不必要細節但無敏感資訊。 |
| 3 | 案例偏具體，可能需要泛化；無明顯 secret。 |
| 1-2 | 出現疑似私人情境、可識別資訊或內部路徑。 |
| 0 | 包含 credential、可識別個資、客戶秘密或明確違反 source boundary。 |

扣分指標：

- 使用真實 credential：source boundary 直接 0，並要求移除。
- 使用可識別個資：source boundary 直接 0，並要求重交。
- 使用未公開客戶資料：source boundary 直接 0，並要求重交。

---

## 9. Quick Grading Sheet

```text
Gateway mock continuity: ___ / 10
Governance layer map: ___ / 12
Common-vs-adapter separation: ___ / 13
Agent registration: ___ / 17
Policy gate: ___ / 18
Audit event schema: ___ / 15
Risk-control and Day 3 readiness: ___ / 10
Source boundary: ___ / 5

Total: ___ / 100

Required fixes:
1.
2.
3.

Optional improvement:
1.
```

---

## 10. TA Feedback Templates

### High-performing submission

```text
你的設計已經把 Day 1 gateway route 與 Day 2 governance artifacts 接起來。registration、policy gate、tool/data/memory boundary 與 audit event 彼此一致，red-team seeds 也能直接進入 Day 3 測試。下一步可加強的是把 evaluation hooks 寫成更具體的 regression test names。
```

### Mid-level submission

```text
你的主要 governance artifacts 已經存在，但目前有幾個 decision boundary 不夠清楚。請優先修正 policy gate 的 allow/deny/review 條件、tool side-effect review rule，以及 audit event 中的 tool/memory/review 欄位。
```

### Low-performing submission

```text
目前設計仍偏 prompt-only，缺少可由 Gateway 執行的 governance contract。請先補上 POST /gateway/requests alignment、agent registration、policy gate decision API、tool/data/memory boundary 與完整 audit event，再處理 red-team seeds。
```
