# Enterprise AI Architecture Sprint — Day 2：Agent Governance Framework

> 目標：讓大二資訊工程學生理解並產出一組可被 AI Gateway 使用、可被 TA 評分、可銜接 Day 3 red-team 的 enterprise agent governance artifacts。

---

## 0. Day Metadata

| 欄位 | 內容 |
|---|---|
| Repo | `ai-systems-engineering-handbook` |
| Accelerator | `accelerators/enterprise-ai-architecture-sprint/` |
| Day | Day 2 |
| 主題 | `Agent Governance Framework` |
| 目標路徑 | `accelerators/enterprise-ai-architecture-sprint/day-02-agent-governance/` |
| 目標讀者 | 資訊工程大二學生 |
| 建議課程長度 | 150 分鐘或 180 分鐘 |
| 主要案例 | Campus IT Helpdesk Assistant |
| Day 1 前置 | AI Gateway lifecycle 與 minimal gateway mock contract |
| Day 3 後續 | Red Teaming Framework |

---

## 1. 第一結論

Enterprise agent 不是「會呼叫工具的 chatbot」。在企業系統中，一個 agent 能不能被使用，不是由 prompt 裡面寫「請遵守規則」決定，而是由以下工程物件共同決定：

```text
agent registry
+ identity / RBAC
+ tool boundary
+ data boundary
+ memory scope
+ message mediation
+ declassification
+ policy gate
+ human review state
+ audit event
+ evaluation hook
+ red-team seed
```

Day 2 的核心句子：

```text
An enterprise agent is not governed by intention.
It is governed by registry, policy, tool boundaries, memory scope, audit events,
evaluation hooks, and review states.
```

學生完成 Day 2 後，應該能把一個「AI helpdesk demo」轉成可治理、可測試、可審查、可銜接 gateway mock 的系統設計。

---

## 2. Target Learner

這份 Day 2 教程假設學生已具備：

- 基礎 Python 或 JavaScript 程式能力。
- HTTP request / response。
- JSON 與簡單 JSON Schema。
- 使用者角色與權限概念。
- 資料庫基本觀念：table、query、permission、log。
- 軟體工程基本觀念：module、interface、contract、test、logging。
- Day 1 的 AI Gateway request lifecycle。

學生尚未需要具備：

- 完整 enterprise IAM 經驗。
- OPA / Cedar 實作經驗。
- Kubernetes production policy deployment 經驗。
- 真實企業 incident response 經驗。

---

## 3. Learning Objectives

Day 2 的學習目標必須可觀察、可評分、可由 artifact 證明。

| 編號 | 學習目標 | 學生 evidence | 評分項目 |
|---:|---|---|---|
| LO1 | 說明為什麼 enterprise agent 需要 registration、ownership、task scope、tool/data/memory boundary、policy gate、audit event 與 review state | worksheet 短答與 governance layer map | Governance layer map |
| LO2 | 把 Day 1 gateway lifecycle 對應到 Day 2 的 route、schema、identity、policy、tool、message mediation、review 與 audit contract | Gateway alignment and message mediation note | Gateway mock continuity |
| LO3 | 區分 common governance rules 與 adapter-specific behavior | Common-vs-adapter table | Common-vs-adapter separation |
| LO4 | 為 public-safe enterprise agent 撰寫 agent registration record | YAML/JSON registration | Agent registration |
| LO5 | 撰寫 policy gate record，讓 decision 可回傳 `allow`、`deny` 或 `review` | Policy gate record | Policy gate |
| LO6 | 設計 audit event schema，記錄 identity、agent、tool、source、memory、policy、guardrail、review 與 outcome | Audit event schema | Audit event schema |
| LO7 | 把 tool abuse、memory leakage、permission bypass、prompt-only approval、missing audit detail 對應到具體 controls | Risk-control map | Risk-control reasoning |
| LO8 | 產出 Day 3 red-team seeds，使治理假設變成可測試案例 | Red-team seed list | Day 3 readiness |
| LO9 | 說明為什麼跨信任邊界的 agent、process、tool、data store 必須透過可授權、可降敏、可稽核的 mediation layer | Gateway alignment and message mediation note、risk-control map | Gateway mock continuity / Risk-control reasoning |

---

## 4. Day 1-to-Day 2 Gateway Alignment

Day 1 建立的 minimal gateway mock mental model：

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

Day 1 的實作錨點：

```text
POST /gateway/requests
-> schema validation
-> token and identity resolution
-> action extraction
-> policy decision
-> agent selection
-> RAG and tool boundary
-> guardrail and human review
-> audit event
```

Day 2 要回答的問題：

```text
Gateway 收到 request 後，要怎麼知道：
1. 哪個 agent 可以處理？
2. 這個 user 是否可以呼叫該 agent？
3. agent 可以讀哪些資料來源？
4. agent 可以呼叫哪些 tools？
5. 哪些 tools 是 read-only，哪些 tools 有 side effect？
6. 什麼情況要 allow、deny 或 review？
7. 是否可以寫入 memory？
8. 跨 agent、process、tool 或 retrieval service 的 request 要走哪個 mediated path？
9. 高敏感資料如何 declassify / redact 後才能回到低權限 zone？
10. audit event 要記錄哪些 evidence？
11. 哪些 governance assumptions 要交給 Day 3 red-team？
```

---

## 5. File Map

本 day package 包含以下檔案：

```text
day-02-agent-governance/
├── README.md
├── student-handout-detailed.md
├── student-handout-detailed.zh-TW.md
├── student-handout.md
├── instructor-guide.md
├── worksheet.md
├── reference-answer-campus-it-agent.md
├── rubric.md
├── day-03-red-team-handoff.md
├── glossary-updates.md
├── source-package.md
└── youtube-learning-map.md
```

| 檔案 | 對象 | 用途 |
|---|---|---|
| `README.md` | 所有人 | Day 2 總覽、學習目標、檔案導覽 |
| `student-handout-detailed.md` | 學生 / 老師 | canonical long-form student explanation；新學生材料先加到這裡 |
| `student-handout-detailed.zh-TW.md` | 學生 / 老師 | 台灣繁體中文完整詳細版，保留 detailed 版全部章節與細節 |
| `student-handout.md` | 學生 | 由 detailed 版摘要而成的正常課堂講義，不含完整參考答案與詳細 rubric |
| `instructor-guide.md` | 老師 / TA | 授課流程、提問、常見錯誤診斷、peer review |
| `worksheet.md` | 學生 | 課堂與作業產出模板 |
| `reference-answer-campus-it-agent.md` | 老師 / TA | Campus IT Helpdesk Agent 完整參考答案 |
| `rubric.md` | 老師 / TA | 100 分量化評分規準 |
| `day-03-red-team-handoff.md` | 學生 / 老師 / TA | 將 Day 2 artifact 轉成 Day 3 red-team test cases |
| `glossary-updates.md` | repo 維護者 | 後續整併到 global glossary |
| `source-package.md` | 老師 / repo 維護者 | source boundary、官方參考與課程設計邊界 |
| `youtube-learning-map.md` | AI agent / 學生 / 老師 | Day 2 所有細節與知識概念的 YouTube 學習順序與前十名影片 |

---

## 6. Recommended Use Order

### 學生使用順序

1. 先讀 `student-handout.md`。
2. 需要完整例子時查 `student-handout-detailed.md` 或 `student-handout-detailed.zh-TW.md`。
3. 填寫 `worksheet.md` 的第 1 到第 4 區。
4. 小組 peer review：檢查 gateway alignment、agent registration、common-vs-adapter。
5. 填寫 `worksheet.md` 的第 5 到第 10 區。
6. 依照 `day-03-red-team-handoff.md`，把 Day 2 policy assumptions 轉成 Day 3 seeds。
7. 交作業前使用 `worksheet.md` final checklist。

### 老師 / TA 使用順序

1. 先讀本 `README.md`。
2. 閱讀 `instructor-guide.md`，選擇 150 分鐘或 180 分鐘流程。
3. 課前閱讀 `student-handout-detailed.md`、`student-handout-detailed.zh-TW.md` 與 `student-handout.md`，確認學生版不含完整參考答案。
4. 課堂中使用 `worksheet.md`。
5. 課後用 `rubric.md` 評分。
6. 如需校準評分，可參考 `reference-answer-campus-it-agent.md`。
7. Day 3 開課前使用 `day-03-red-team-handoff.md`。

### Student Handout Maintenance

新增 Day 2 學生材料時，先更新 `student-handout-detailed.md`，再同步
`student-handout-detailed.zh-TW.md`，最後把 `student-handout.md` 維持為保留章節
結構的 first-principle summary。

---

## 7. Minimum Deliverables

Day 2 最小可交付成果是八個 artifacts：

1. Day 1-to-Day 2 gateway alignment and message mediation note。
2. Governance layer map。
3. Common-vs-adapter table。
4. Agent registration record。
5. Policy gate record。
6. Audit event schema。
7. Risk-control map。
8. Day 3 red-team seed list。

這八個 artifact 應該能讓 TA 不靠口頭說明，也能判斷學生是否真的理解 enterprise agent governance。

---

## 8. Objective-to-Assessment Map

| Artifact | 主要評分問題 |
|---|---|
| Gateway alignment and message mediation note | 是否明確接回 `POST /gateway/requests`、schema validation、trusted identity、policy decision、tool broker、message mediation、declassification、human review、audit event 與 HTTP outcomes？ |
| Governance layer map | 是否包含 identity、registry、tool/data/memory boundary、mediated message boundary、policy、audit、review、evaluation、red-team？ |
| Common-vs-adapter table | 是否能重用 common layer，而不是每個情境重寫治理邏輯？ |
| Agent registration record | 是否有 owner、task scope、risk class、allowed users/tools/data、memory scope、approval、eval、red-team、audit？ |
| Policy gate record | 是否有明確 `allow`、`deny`、`review` 條件？ |
| Audit event schema | 是否能重建 request lifecycle，而不是只記 final answer？ |
| Risk-control map | 是否能把 tool abuse、memory leakage、permission bypass、confused deputy、broker payload leakage、replay、schema bypass 等風險連到 control 與 evidence？ |
| Red-team seed list | 是否能直接成為 Day 3 測試案例？ |

---

## 9. Student / Instructor Separation

學生版材料應該包含概念解釋、範例片段、填寫模板、submission checklist 與 public-safe scenario。

學生版材料不應該包含完整 Campus IT reference answer、100 分詳細 rubric、instructor-only failure diagnosis 或 TA grading calibration notes。

教師版材料可以包含參考答案、常見錯誤 gallery、詳細評分規準、課堂時間安排、peer review 設計與 Day 3 handoff 診斷。

---

## 10. Source Boundary

Day 2 案例必須 public-safe。可以使用校園 IT helpdesk、銀行內部知識助理、醫療 staff-review intake support、製造場域維修助理，以及一般化 enterprise support workflow。

不要使用私人訪談逐字稿、客戶秘密、credentials、personal contact routes、salary 或 offer detail、未公開公司主張、可識別個資。

---

## 11. Background References

本課程包的技術語言校準來源放在 `source-package.md`。學生不需要先讀完所有官方文件，但老師與 TA 可用它們校準 OWASP GenAI / LLM Top 10 風險類別、NIST AI RMF 的 govern / map / measure / manage、OPA / Rego、Cedar 與 OpenTelemetry 的語言。

---

## 12. Completion Definition

Day 2 可以視為完成，當它滿足以下條件：

- 學生不用看參考答案也能完成 worksheet。
- 老師可用 instructor guide 上完 150 或 180 分鐘課程。
- TA 可用 100 分 rubric 評分。
- reference answer 有完整 public-safe Campus IT Helpdesk Agent 範例。
- 所有 learning objectives 都對應 artifact 與 rubric。
- student-facing material 沒有洩漏完整 reference answer。
- Gateway alignment and message mediation note 能清楚連接 `POST /gateway/requests`、schema validation、trusted identity、policy decision、tool broker、message mediation、declassification、review state、audit event 與 HTTP outcomes。
- Policy gate、tool boundary、memory scope、message mediation、audit event 都有具體 schema 或 template。
- Risk-control map 能銜接 Day 3 red-team seeds。
- Source boundary 清楚。
