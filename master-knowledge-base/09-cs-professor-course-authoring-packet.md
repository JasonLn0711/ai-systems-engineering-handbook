# 資訊工程教師協作資料包：AI Systems Engineering Handbook 教程撰寫指南

## 1. 給老師的核心說明

這個 repository 是一套 `AI Systems Engineering Handbook`，目標是把 AI
能力從單一模型或 demo，提升成可以設計、部署、治理、測試、維運、交付的
enterprise AI system 教程。

本 repo 的核心主張是：

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

對大二資訊工程學生來說，這個 repo 要補上的能力不是「會呼叫一個 LLM
API」而已，而是能用軟體工程與系統工程的方式回答：

- 這個 AI 功能如何被包成 service？
- request 從使用者進來後會經過哪些 component？
- 資料來源、模型、tool、agent、memory、policy、log 如何被分層管理？
- 系統如何部署到 Docker、Kubernetes、on-prem 或 private cloud？
- GPU/VRAM、latency、throughput、timeout、retry 如何影響設計？
- Prompt injection、PII leakage、tool abuse、cross-agent memory leakage 如何被測試與控制？
- 什麼 evidence 可以證明這不是一個一次性 demo，而是可交付、可維護的系統？

老師可以把這個 repo 當成一門「AI 系統工程實作」課程的教材骨架。它不是
純 ML textbook，也不是 prompt cookbook，而是把 OS、networking、database、
distributed systems、software engineering、security、DevOps 與 AI application
architecture 串成一條可實作的學習路徑。

## 2. 這個 repo 的教學定位

本 repo 是一個 tutorial-oriented knowledge system，內容分成六種主要層次：

| 層次 | 作用 | 老師可協助的內容 |
|---|---|---|
| Master Knowledge Base | 建立全局地圖與學習路線 | 補強概念導讀、課程順序、初學者先備知識 |
| Modules | 每個主題的深度教程 | 撰寫章節、加入機制圖、補充 exercises |
| Labs | 把概念變成可執行驗證 | 設計 Docker、API、RAG、Gateway、security labs |
| Accelerators | 短期 evidence-generation sprint | 把多個主題壓縮成可展示的 architecture packet |
| Case Studies | 真實世界情境整合 | 設計銀行、醫療、製造、校園 IT 等 public-safe 案例 |
| Review Rubrics | 控制教材品質 | 建立評分規準、TA 檢查表、學生驗收表 |

老師撰寫教程時，請以「一個大二學生能從已知 CS 基礎走到 AI
system 設計」為主線。每個章節都要把 abstract concept 落到工程物件：
HTTP request、JSON schema、Docker container、SQL query、vector store、
policy rule、audit event、Kubernetes deployment、GPU memory estimate、
test case、runbook。

## 3. 軟體工程與系統工程視角

### 3.1 軟體工程視角

AI application 仍然是軟體系統。老師可以用學生已熟悉的軟體工程概念銜接：

| 軟體工程概念 | 在 AI 系統中的對應 |
|---|---|
| API contract | model API、tool call schema、MCP server interface |
| Modularity | model、retrieval、gateway、policy、tool broker 分層 |
| Separation of concerns | prompt 不負責權限；gateway/policy engine 負責權限 |
| Testing | unit test、integration test、retrieval eval、red-team test |
| Logging | request log、tool call log、policy decision log、audit log |
| Error handling | timeout、retry、fallback、human review、safe failure |
| Maintainability | registry、versioning、config、runbook、rollback |

對學生要強調：LLM 回答文字只是 output。真正的 software engineering
問題是 interface、state、permission、failure、observability、change control。

### 3.2 系統工程視角

AI system 的成功來自多層 component 一起成立：

```text
user / channel
-> API service
-> AI Gateway
-> policy / registry / audit
-> RAG / tools / MCP
-> model serving
-> infrastructure
-> evaluation / operation / delivery
```

老師可以把每個 component 當成系統工程中的 subsystem：

- `AI Gateway` 是控制面，負責 request routing、permission、policy、audit。
- `RAG pipeline` 是資料面，負責 ingestion、chunking、metadata、retrieval、citation。
- `Model serving` 是推論面，負責 model loading、batching、latency、VRAM。
- `Tool broker` 是動作面，負責工具 schema、timeout、approval、side effects。
- `Security and governance` 是操作邊界，負責 PII、prompt injection、tool abuse、auditability。
- `Delivery workflow` 是交付面，負責 deployment、acceptance criteria、handoff、rollback。

系統工程的重點是 trade-off。學生要學會看見延遲、安全、成本、維護性、
可部署性、可驗證性之間的關係。

## 4. 大二學生的先備知識與教學腳手架

這門教材可以面向大二學生，但要明確建立先備知識橋梁。

### 4.1 最低先備知識

學生需要具備：

- 基本 Python 或 JavaScript 程式能力。
- HTTP request/response 與 JSON 基礎。
- Linux command line 基礎：process、port、file、environment variable。
- Database 基礎：table、query、permission 的概念。
- Web backend 基礎：route、handler、middleware、log。
- 軟體工程基礎：module、interface、test、version control。

### 4.2 可以一邊補的知識

以下內容可以透過 repo 的 modules 與 labs 補強：

- Docker image、container、volume、network。
- Kubernetes Pod、Deployment、Service、Ingress。
- GPU、VRAM、batch、KV cache、model serving runtime。
- Embedding、vector search、reranker、metadata、citation。
- Auth、RBAC、policy engine、audit log。
- Prompt injection、PII、guardrail、red-team taxonomy。

### 4.3 教學語氣

請用 Traditional Chinese 撰寫主要教程，保留 common engineering terms
的英文，例如 `AI Gateway`、`RAG`、`MCP server`、`tool broker`、
`audit log`、`policy gate`、`Kubernetes Deployment`。每個英文術語第一次
出現時要定義，並給一個學生能理解的系統例子。

## 5. 每篇教程應該怎麼寫

每篇教程至少要包含以下結構：

1. **Why this chapter exists**：這個主題解決什麼真實工程問題。
2. **Mental model**：用一張圖或一個比喻建立初學者心智模型。
3. **Core terms**：先定義術語，再進入機制。
4. **Mechanism**：解釋底層怎麼運作，不只列工具名稱。
5. **System context**：放到 enterprise AI system 的完整 request lifecycle。
6. **Engineering workflow**：工程師實際設計、實作、驗證的步驟。
7. **Security and governance**：權限、資料、工具、log、approval、red-team。
8. **Failure modes**：常見失敗模式與原因。
9. **Minimal example**：小型可理解例子。
10. **Production-grade example**：更接近真實世界的版本。
11. **Checklist**：學生或 TA 可檢查的具體項目。
12. **Exercises**：概念題、設計題、實作題。
13. **Related modules/labs**：指回 repo 中的相關路徑。

每篇教程都要區分 toy example 與 production reality。例如：

- Toy chatbot：單一 prompt、單一 model、無權限、無 log。
- Enterprise AI assistant：user identity、role、policy、data permission、
  tool schema、audit event、red-team tests、deployment plan。

## 6. 真實世界案例方向

老師可以使用 public-safe、generalized 的真實世界情境。以下案例適合大二學生：

### 6.1 校園 IT Helpdesk Assistant

學生熟悉的情境：同學問「如何設定 VPN？」、「選課系統無法登入怎麼辦？」。

技術細節：

- Data source：IT FAQ、PDF 操作手冊、服務公告。
- RAG：chunk FAQ，metadata 包含 `department`、`last_updated`、`access_level`。
- AI Gateway：依 user role 決定能否查詢內部維修 SOP。
- Tool：建立 ticket 是 side-effect action，需要 approval 或 rate limit。
- Audit：記錄 query、retrieved source IDs、answer、policy decision。

教學價值：學生能從熟悉問題理解 RAG、policy、tool boundary、audit log。

### 6.2 銀行內部知識助理

企業情境：行員查詢內部產品規則、合規條文、客戶服務流程。

技術細節：

- Data source 有敏感等級，不能讓所有角色讀同一份資料。
- AI Gateway 要檢查 user role、branch、task type。
- Output 要引用來源文件與版本。
- 高風險回答進入 staff-review workflow。
- Red-team tests 包含 prompt injection、policy bypass、PII leakage。

教學價值：學生能理解 enterprise AI 不是「回答得像」就足夠，而是要可追蹤、
可審查、可驗證。

### 6.3 醫療預問診支援系統

公共安全表述：系統協助整理病人輸入與公開衛教資料，輸出進入 staff-review
intake support，不做診斷取代。

技術細節：

- Voice AI：ASR 將語音轉文字。
- RAG：查詢公開衛教資料或院內流程文件。
- PII guardrail：log 中遮罩姓名、電話、身分證字號。
- Human review：輸出提供醫護人員確認。
- Evaluation：檢查摘要完整性、引用正確性、PII masking。

教學價值：學生能理解 safety-critical 系統中的 positive operating scope：
支援整理與審查，不把模型輸出當成最終醫療決策。

### 6.4 製造場域異常聲音偵測

企業情境：半導體或工廠設備產生異常聲音，系統協助標記可能事件。

技術細節：

- Audio pipeline：sampling rate、noise reduction、VAD、event detection。
- Edge deployment：可能需要在機房或產線旁部署小型 inference service。
- Latency：警示系統要控制延遲與誤報率。
- Audit：記錄音訊片段 ID、時間、模型版本、confidence、operator review。
- Delivery：site survey、network constraints、GPU/CPU capacity、rollback。

教學價值：學生能看到 AI system 不只文字，也包含 audio、edge、latency、
deployment、operator workflow。

## 7. Accelerators 的目標

`accelerators/` 是短期 evidence-generation sprints。它不是完整教材的替代品，
而是把多個 modules 的知識壓縮成可展示、可討論、可驗證的 architecture
evidence packet。

目前主要 accelerator 是：

```text
accelerators/enterprise-ai-architecture-sprint/
```

它的目標是讓學生在 7-14 天內產出一組 public-safe enterprise AI architecture
證據。這組 evidence 要證明學生不只是知道工具名稱，而是能把 AI system
拆成 architecture、governance、deployment、security、capacity、validation。

## 8. Accelerators 需要什麼

每個 accelerator artifact 都需要五件事：

1. **Architecture view**：圖解 component 與資料/控制流程。
2. **Minimum viable output**：可以在短時間內交出的最小成果。
3. **Validation checklist**：如何檢查成果不是空泛描述。
4. **Failure modes**：常見失敗與對應控制。
5. **Next implementation gate**：下一步如何走向 lab、demo 或 production-like implementation。

Enterprise AI Architecture Sprint 的核心產出包含：

| Sprint artifact | 主要問題 | Evidence |
|---|---|---|
| AI Gateway architecture | 多個 agent、tool、model、data source 如何被統一控制 | architecture diagram、request lifecycle、component table |
| Agent governance framework | agent 如何註冊、授權、審計、評估 | registry template、policy gate、audit schema |
| Red teaming framework | 如何測 prompt injection、tool abuse、data leakage | test taxonomy、attack cases、pass/fail criteria |
| GPU capacity model | model serving 需要多少 VRAM/throughput buffer | capacity table、assumptions、risk notes |
| K8s inference lab | inference service 如何部署與檢查健康 | deployment checklist、service boundary |
| PII / guardrail demo | 敏感資料如何被偵測、遮罩、審查 | masking plan、guardrail flow、audit fields |
| MCP / tool / memory governance | tool/data/memory 如何跨 agent 受控共享 | permission map、memory scope table |
| Real-time voice-agent evidence | ASR -> LLM -> TTS 如何符合延遲與審查 | latency budget、pipeline map、review path |

## 9. Accelerators 的重點

Accelerator 的重點不是速度本身，而是 evidence quality。

學生交出的成果要能回答：

- 這個 artifact 降低哪一種 system risk？
- 哪個 module/lab 負責後續深度學習？
- 最小可驗證 output 是什麼？
- 如何由 TA、老師或工程 mentor 驗證？
- 哪些內容是 architecture evidence，哪些只是 future implementation plan？

老師撰寫 accelerator 教程時，請把每一天設計成「教學 + artifact production」：

```text
concept explanation
-> component mechanism
-> real-world case
-> artifact template
-> student exercise
-> validation checklist
-> review rubric
```

Day 1 的重點是 AI Gateway architecture。學生不需要先寫完整系統，但要能畫出
一個合理 architecture，並說明 request 如何通過 auth、policy、agent registry、
tool broker、RAG/MCP connector、model、guardrail、audit log、human review。

## 10. 老師可以怎麼幫我們寫教程

### 10.1 優先撰寫順序

建議老師先協助以下內容：

1. `accelerators/enterprise-ai-architecture-sprint/day-01-ai-gateway/README.md`
2. `modules/07-ai-gateway-agent-governance/chapters/01-why-ai-gateway-exists.md`
3. `labs/ai-gateway/` 的 minimal mock lab。
4. `modules/09-security-red-teaming/` 的 prompt injection 與 tool abuse 初學者教程。
5. `modules/03-container-k8s-devops/` 的 inference service deployment 教程。
6. `modules/04-gpu-inference-infrastructure/` 的 VRAM/KV cache capacity 教程。

### 10.2 每份老師交付物的建議格式

每份教程請包含：

- `title`
- `target learner`
- `prerequisites`
- `learning objectives`
- `core terms`
- `mechanism`
- `architecture diagram`
- `workflow`
- `real-world example`
- `technical detail`
- `failure modes`
- `security and governance implications`
- `student exercises`
- `expected deliverables`
- `grading rubric`
- `related repo paths`

### 10.3 老師寫作時要遵守的 source boundary

本 repo 可以使用 generalized public-safe learning requirements，但不存放：

- raw private transcripts
- customer secrets
- credentials
- private contact routes
- salary or offer details
- 未公開公司內部產品宣稱
- 可識別個人或客戶的敏感資料

如果老師要用真實案例，請改寫成 generalized system scenario。例如把「某公司某客戶」
改成「bank internal knowledge assistant」或「manufacturing audio monitoring」。

## 11. Day 1 accelerator 交付標準

Day 1 結束時，學生應該交出四個 artifact：

1. **AI Gateway architecture diagram**
2. **Component responsibility table**
3. **One request lifecycle**
4. **Risk-control map**

最低合格標準：

- 圖中必須包含 client/channel、AI Gateway、auth、RBAC/policy、agent registry、
  tool broker、RAG/MCP connector、model serving、guardrail、audit log、human review。
- request lifecycle 必須從 user request 走到 audit event。
- risk-control map 必須至少涵蓋 prompt injection、PII leakage、tool abuse、
  permission bypass、missing audit trail。
- 每個 component 要有責任邊界，不可以把所有控制都寫成「prompt 會處理」。
- 所有案例必須 public-safe。

Day 1 正式課程包已放在：

```text
accelerators/enterprise-ai-architecture-sprint/day-01-ai-gateway/
```

如果要把需求交給資訊工程學系老師，請優先使用這份 self-contained
設計委託包：

```text
teacher-packets/2026-06-13-enterprise-ai-architecture-sprint-day1-professor-design-packet.md
```

這份 teacher packet 的定位不是學生講義，而是告訴老師如何協助設計 Day 1
accelerator 的學生版教程、教師授課指南、worksheet、artifact templates、
reference answer、rubric 與後續 lab handoff。

Day 2 正式課程包已放在：

```text
accelerators/enterprise-ai-architecture-sprint/day-02-agent-governance/
```

如果要請資訊工程學系老師協助設計 Day 2 `Agent Governance Framework`，
請使用這份 self-contained 設計委託包：

```text
teacher-packets/2026-06-13-enterprise-ai-architecture-sprint-day2-professor-design-packet.md
```

這份 Day 2 teacher packet 的定位，是協助老師設計 agent registry、tool boundary、
memory scope、policy gate、audit event、risk-control map、100 分 rubric 與
Day 3 red-team handoff。它延續 Day 1 的 AI Gateway architecture evidence，
把 Gateway 需要管理的 agent governance contract 轉成大二學生可完成、TA 可評分
的教程組件。

## 12. 給老師的可直接使用指令

老師可以用以下 prompt 請 AI agent 或 TA 協助產生某個章節草稿：

```text
請撰寫 ai-systems-engineering-handbook 的一篇教程。

目標讀者：資訊工程大二學生。
語言：Traditional Chinese，保留 common engineering terms in English。
角度：software engineering + systems engineering。
主題：<填入主題>
放置路徑：<填入 repo path>

請包含：
1. why this chapter exists
2. mental model
3. core terms
4. mechanism
5. system context
6. engineering workflow
7. real-world public-safe example
8. security and governance implications
9. failure modes
10. minimal example
11. production-grade example
12. checklist
13. exercises
14. related repo paths

請不要使用 raw private source material，不要發明未驗證公司事實，不要只列工具名稱。
```

## 13. 教學評分建議

每份學生成果可用 100 分評估：

| 類別 | 分數 | 評分重點 |
|---|---:|---|
| Concept clarity | 15 | 術語定義清楚，能區分 model、application、system、gateway |
| Architecture correctness | 20 | component 分層合理，request lifecycle 完整 |
| Software engineering discipline | 15 | interface、schema、logging、error handling、testability 明確 |
| Systems engineering trade-off | 15 | 能說明 latency、capacity、security、deployment、operation trade-off |
| Security and governance | 15 | policy、RBAC、PII、prompt injection、tool abuse、audit 有具體控制 |
| Evidence quality | 10 | artifact 可檢查、可討論、可延伸到 lab |
| Beginner communication | 10 | 對大二學生可理解，有例子、有圖、有練習 |

達到 80 分代表 artifact 可進入下一天 accelerator；達到 90 分代表可作為 repo
中的示範稿或 TA 參考答案。

## 14. 老師的最有價值貢獻

老師最能幫助這個 repo 的地方，是把學生已經學過的 CS 基礎轉成 AI system
judgment：

- OS 課學到 process、file、permission；這裡變成 deployment debugging 與 data boundary。
- Network 課學到 request、port、TLS；這裡變成 model service、gateway、on-prem constraints。
- Database 課學到 schema、query、transaction；這裡變成 RAG metadata、SQL tool boundary、auditability。
- Software engineering 課學到 modularity、testing、requirements；這裡變成 Spec/SDD、agent registry、policy gate。
- Security 課學到 auth、access control、logging；這裡變成 prompt injection defense、PII guardrail、red-team workflow。

這份 handbook 的目標，是讓學生建立「能把 AI 做成系統」的工程能力。老師的教程應該讓學生看到：

```text
working demo
-> engineered service
-> governed workflow
-> deployable system
-> validated delivery evidence
```

這就是 accelerators 與整個 repo 的共同方向。
