# C4 Model Video Notes: Visualising Software Architecture

```yaml
artifact_type: ai_agent_readable_video_note
agent_readable: true
accelerator: enterprise-ai-architecture-sprint
day: 1
video_title: "Visualising software architecture with the C4 model - Simon Brown, Agile on the Beach 2019"
primary_topic: C4 model for software architecture communication
primary_language: zh-TW
recorded_at: 2026-06-21
canonical_note_path: accelerators/enterprise-ai-architecture-sprint/day-01-ai-gateway/c4-model-video-notes.md
source_boundary:
  - Public video note
  - Public C4 Model references
  - Public-safe enterprise AI examples
  - No customer secrets
  - No credentials
  - No identifiable personal data
agent_use:
  - Use this as Day 1 companion material for architecture evidence.
  - Keep the Day 1 required artifacts unchanged.
  - Use the C4 examples to improve architecture diagrams, not to add new grading categories.
downstream_outputs:
  - C4 notes
  - System Context Diagram
  - Container Diagram
  - AI Gateway Component Diagram
  - Runtime Sequence Diagram
  - Deployment Diagram
  - ADR
  - Runbook
  - Risk-Control Map
```

## Agent Reading Contract

```yaml
reading_contract:
  purpose: "Record the C4 Model video notes as reusable course evidence for Day 1 architecture literacy."
  do_not_treat_as:
    - new Day 1 grading requirement
    - complete architecture reference answer
    - customer-specific VOISS design
  use_as:
    - companion note for Day 1 architecture diagram work
    - source for C4 terminology explanations
    - source for enterprise voice AI architecture practice prompts
    - source for interview-prep answers about architecture diagrams and AI Gateway boundaries
  required_student_artifacts_still_owned_by_day_1:
    - AI Gateway architecture diagram
    - Component responsibility table
    - Request lifecycle
    - Risk-control map
  stable_section_ids:
    conclusion: "0"
    problem: "1"
    c4_levels: "2"
    engineering_principles: "3"
    enterprise_ai_delivery: "4"
    one_week_practice: "5"
    tools: "6"
    box_line_templates: "7"
    enterprise_voice_context_example: "8"
    enterprise_voice_container_example: "9"
    ai_gateway_component_example: "10"
    engineering_practices: "11"
    systems_thinking: "12"
    minimum_demo: "13"
    interview_answers: "14"
    weekly_priorities: "15"
    compressed_summary: "16"
```

## 0. 第一結論

這支影片真正教的不是「怎麼畫漂亮的圖」，而是怎麼用工程化方法把軟體系統講清楚。

對 VOISS、enterprise AI、on-prem AI deployment 類型工作來說，這件事很關鍵。公司需要的不是只會跑模型的人，而是能把以下鏈條串起來的人：

```text
客戶需求
-> 系統架構
-> API
-> 部署
-> 監控
-> 交付文件
```

Simon Brown 的核心主張可以濃縮成兩句：

```text
Architecture diagrams should reflect the real software system.
Abstractions first, notation second.
```

C4 Model 用四層抽象描述同一個軟體系統：

```text
Context -> Container -> Component -> Code
```

它是 notation-independent、tooling-independent 的方法。重點不是用哪個工具畫圖，而是讓不同讀者在正確縮放倍率上理解系統邊界、責任、互動與風險。

## 1. 影片在解決的問題

很多工程團隊說「白板畫一下就好」，但多數工程師沒有受過 architecture diagram 訓練。結果圖上有方塊、線、顏色、縮寫與 icon，卻沒有標題、legend、方向、責任邊界與關係描述。

這會直接變成交付成本：

- 新同事看不懂系統。
- PM 看不懂技術風險。
- 客戶看不懂交付範圍。
- 工程師自己也不確定系統如何運作。
- 每次 onboarding、debug、交接、需求變更都要重新開會解釋。

工程原則：

```text
架構圖不是藝術品，而是團隊溝通與系統交付工具。
```

把 C4 Model 想成軟體系統的地圖系統。地圖不需要畫出每一顆樹，但要讓人知道自己在哪裡、要去哪裡、有哪些路、哪些東西不能忽略。

## 2. C4 Model 四層

C4 四層不是設計順序，而是描述同一個系統的不同縮放倍率。

```text
Level 1: System Context
Level 2: Container
Level 3: Component
Level 4: Code
```

### 2.1 Level 1: System Context Diagram

這一層回答：

```text
我們正在做的系統是什麼？
誰會用它？
它跟哪些外部系統互動？
```

適合讀者：

- PM
- 主管
- 客戶
- 業務
- 非技術利害關係人
- 新進工程師

System Context Diagram 不急著講技術細節，而是先釐清系統邊界。

VOISS / enterprise voice AI 對應：

```text
中心系統:
Enterprise Voice AI Coach Platform

使用者:
- 客服人員
- 客服主管
- 企業 IT 管理員
- 稽核人員
- 最終受訓員工

外部系統:
- 企業 CRM
- LMS
- 知識庫
- SSO / IdP
- 電話系統
- 錄音系統
- 內部資料庫

外部限制:
- on-prem 機房
- GPU server
- 企業資安政策
- PII / 個資規範
- 客戶網路隔離
```

Level 1 的目的不是炫技，而是讓對方立刻知道：

```text
這個系統活在哪個商業與技術環境裡。
```

### 2.2 Level 2: Container Diagram

這一層回答：

```text
這個系統裡有哪些可執行的應用程式與資料儲存？
它們怎麼互相溝通？
用什麼技術？
```

C4 的 container 不是 Docker container。它指的是 application 或 datastore，也就是需要部署、執行、或保存資料的單元。

可能的 container：

- Web app
- Mobile app
- API service
- Database schema
- Python service/script
- Object storage bucket
- Message queue
- Model serving endpoint

VOISS / enterprise AI Level 2 範例：

```text
Audio Ingestion Service
[Python / WebSocket]
接收麥克風、電話、錄音檔或 streaming audio。

ASR Service
[faster-whisper / Breeze ASR / SenseVoice / FunASR]
把語音轉文字。

Diarization / VAD Service
[pyannote.audio / WebRTC VAD]
判斷誰在說話、何時有語音。

AI Gateway
[FastAPI / gateway service]
所有 LLM / Agent / Tool call 的入口，負責 auth、policy、routing、audit。

Agent Runtime
[LangGraph / LangChain / custom workflow]
負責工作流程與 tool orchestration。

RAG Service
[LlamaIndex / LangChain / custom retriever]
連接企業知識庫。

Vector Database
[Qdrant / Milvus / pgvector / Elasticsearch]
保存 embeddings 與檢索 metadata。

Model Serving Service
[vLLM / Ollama / llama.cpp / Triton]
提供 LLM inference。

TTS Service
[BreezyVoice / Fish-Speech / Coqui TTS]
產生語音回覆。

Dashboard / Admin Console
[Next.js / React]
主管查看訓練結果、稽核紀錄與 AI 評分。

Audit Log Database
[PostgreSQL / ClickHouse / OpenSearch]
保存對話、模型輸入輸出、policy decision、tool call。

Object Storage
[MinIO / S3-compatible storage]
保存音檔、逐字稿、報表與模型 artifacts。

Monitoring Stack
[Prometheus / Grafana / Loki / OpenTelemetry]
收集 metrics、logs、traces 與 alerts。
```

Level 2 的重點是 runtime reality。不要只畫一個「AI 模組」；要說清楚每個 deployable unit 的責任、資料流、協定、資料儲存位置與部署邊界。

### 2.3 Level 3: Component Diagram

這一層回答：

```text
某一個 container 裡面的程式碼高階結構是什麼？
```

Component Diagram 必須開始對應到 codebase。打開 repo 時，應該能看到相對應的 controller、service、component、package、module 或 namespace。

AI Gateway component 範例：

```text
API Router
接收 /chat、/score、/transcribe、/tool-call 等請求。

Auth Middleware
驗證 JWT、API key、企業 SSO token。

Tenant Resolver
判斷是哪個客戶、部門、deployment。

Policy Engine Adapter
連接 OPA、Cedar 或自訂 policy service。

PII Redactor
偵測姓名、電話、身分證字號、病歷號、信用卡等。

Prompt Builder
根據任務、角色、企業規則組 prompt。

Model Router
決定送到 vLLM、Ollama、OpenAI-compatible endpoint 或 local model。

Tool Registry
列出 agent 可以呼叫哪些工具，例如 CRM 查詢、LMS 寫入、報表生成。

MCP Adapter
如果採用 MCP，負責把 tool call 轉成 MCP server 呼叫。

Audit Event Emitter
把每次請求、policy decision、model response 寫到 audit log。

Evaluation Hook
把輸入輸出送去做品質評估、toxicity、hallucination、policy violation 檢查。
```

這一層很適合建立工作上的可信度。很多人只會說「我們有 AI Gateway」，但不會拆成可維護的 components。能把 component boundary 說清楚，代表你能把 AI 名詞轉成可交付系統。

### 2.4 Level 4: Code Diagram

影片的判斷很直接：

```text
不要手動畫大多數 Level 4。
```

Level 4 通常是 class diagram、interface diagram 或低階程式碼結構。多數情況下不值得手畫，應該從 IDE 或工具自動產生。只有在某個 component 特別複雜、演算法特別難、或有不尋常設計時才畫。

工作上先掌握 Level 1、Level 2、Level 3。Level 4 只在 debug 或設計核心模組時使用。

## 3. 影片的工程原則

### 3.1 不要只畫名字，要寫責任

差的圖只寫：

```text
API
DB
Backend
Service
```

好的 box 至少包含：

```text
Name
[Type / Technology]
Responsibility in one short sentence.
```

範例：

```text
AI Gateway
[FastAPI service]
Routes tenant requests to approved models/tools, enforces policy, logs all prompt/tool events.
```

### 3.2 線要有方向與文字

不要畫沒有箭頭的線。線代表關係，關係要說清楚。

格式：

```text
A -> B: action + protocol + data
```

範例：

```text
Dashboard -> AI Gateway: calls REST API over HTTPS
AI Gateway -> Policy Engine: asks whether request is allowed
Agent Runtime -> CRM: reads customer profile via tool call
ASR Service -> Transcript Store: writes timestamped transcript
```

不要只寫：

```text
uses
connects to
talks to
data
```

這些字太模糊，不能支援交付與維護。

### 3.3 圖要能獨立存在

每張圖都要有：

- 標題：圖的種類 + 範圍。
- 圖例：顏色、形狀、線條代表什麼。
- 責任說明：每個 box 做什麼。
- 關係說明：每條 line 是什麼呼叫、資料流或依賴。
- 版本日期：目前設計、目標設計，還是舊設計。
- owner：誰維護這張圖。

不要把白板照片直接丟進文件後就結束。幾個月後看不懂的圖，等於沒有留下工程證據。

### 3.4 顏色、icon、雲端符號只能輔助

AWS / Azure icon 可以輔助視覺辨識，但不能取代文字。客戶與新同事真正需要知道的是：

- 資料流有沒有出內網？
- PII 有沒有被送到外部模型？
- GPU server 跑在哪裡？
- 模型輸入輸出有沒有 audit log？
- 失敗時怎麼 fallback？
- 哪個服務負責驗證權限？
- 哪個元件可以水平擴充？

## 4. 轉成 enterprise AI delivery 能力

C4 不是單純畫圖技巧。它要轉成 enterprise AI delivery 的輸出能力。

面對客戶或主管時，你要能產出：

```text
System Context Diagram
說明系統邊界、使用者、外部系統。

Container Diagram
說明主要服務、資料庫、模型服務、通訊協定。

Component Diagram
針對 AI Gateway 或 Agent Runtime 拆內部組件。

Runtime Sequence Diagram
說明一個請求從語音進來到回覆出去的流程。

Deployment Diagram
說明 on-prem / K8s / GPU / DB / monitoring 怎麼部署。

ADR
記錄關鍵技術決策，例如 FastAPI、vLLM、Qdrant、PostgreSQL。

Runbook
系統壞掉時怎麼查 log、重啟服務、檢查 GPU、確認 API。

Risk-Control Map
PII、權限、latency、model hallucination、tool misuse 怎麼控管。
```

這是從「會寫程式」升級到「能交付企業 AI 系統」的差異。

## 5. 一週補習班式練習規劃

### Day 1: 看懂 C4 Model 與架構圖目的

目標：建立正確心智模型。

要理解：

- 架構圖是服務某種讀者的溝通工具。
- Context 是系統邊界。
- Container 是可部署應用或資料儲存，不是 Docker。
- Component 是 container 內部模組結構。
- Code 是 class/interface 等低階細節，通常不要手畫。

產出：

```text
docs/architecture/00-c4-notes.md
```

驗收：

- 能解釋 C4 container 為什麼不是 Docker container。
- 能解釋為什麼不要一開始畫 class diagram。
- 能解釋為什麼圖上每條線都要有文字。

### Day 2: 畫 Level 1 System Context Diagram

目標：練邊界感。

問題：

- 誰使用系統？
- 誰管理系統？
- 系統讀哪些外部資料？
- 系統寫哪些外部資料？
- 哪些系統是我們控制的？
- 哪些系統是客戶控制的？
- 哪些資料不能出內網？
- 哪些功能是 out of scope？

產出：

```text
docs/architecture/01-system-context.md
```

驗收：

- 系統包含什麼、不包含什麼。
- 誰是主要使用者。
- 哪些外部系統故障會影響我們。
- 哪些資料有合規風險。

### Day 3: 畫 Level 2 Container Diagram

目標：進入工程現實，拆 deployable/runtime units。

建議版本：

```text
Frontend Dashboard: Next.js + React
API Gateway / BFF: FastAPI or NestJS
Audio Ingestion Service: WebSocket / gRPC streaming
ASR Service: faster-whisper / Breeze ASR / SenseVoice
Diarization / VAD Service: pyannote.audio / WebRTC VAD
Agent Runtime: LangGraph or custom workflow engine
RAG Service: LlamaIndex / LangChain + retriever
Vector Database: Qdrant / Milvus / pgvector
Relational Database: PostgreSQL
Object Storage: MinIO
Model Serving: vLLM / Ollama / Triton
TTS Service: BreezyVoice / Fish-Speech
Policy / Guardrail Service: OPA / Presidio / custom policy engine
Audit Log Store: PostgreSQL / ClickHouse / OpenSearch
Monitoring: Prometheus + Grafana + Loki + OpenTelemetry
```

產出：

```text
docs/architecture/02-container-diagram.md
```

驗收：

- 每個服務為什麼獨立。
- 哪些服務需要 GPU。
- 哪些服務是 stateful。
- 哪些資料庫保存什麼。
- 哪些路徑 latency-critical。
- 哪些地方要 audit log。

### Day 4: 畫 Level 3 Component Diagram，以 AI Gateway 為核心

目標：練工程拆解。

AI Gateway 不是單純 reverse proxy。它治理模型、agent、工具、資料、權限、審計、成本與風險。

可拆成：

```text
Request Router
Authentication Middleware
Tenant Resolver
Policy Decision Client
PII Detector / Redactor
Prompt Builder
Model Router
Tool Router
Audit Logger
Evaluation Hook
Error Handler / Fallback Manager
```

產出：

```text
docs/architecture/03-component-ai-gateway.md
```

驗收：

- AI Gateway 和普通 API Gateway 差在哪。
- policy enforcement 應該放在哪。
- tool call 為什麼要經過 registry。
- audit log 要記什麼。
- PII redaction 何時執行。

### Day 5: 補 Runtime / Sequence Diagram

目標：說清楚 request runtime flow。

語音進來到 AI 回覆出去的流程：

```text
使用者開始說話
-> Audio Client 用 WebSocket 傳 audio chunks
-> VAD 判斷語音片段
-> ASR 產生 partial transcript
-> Diarization 標記 speaker
-> Transcript Normalizer 清理標點、時間戳、熱詞
-> PII Guard 檢查敏感資料
-> RAG Service 查企業知識庫
-> Prompt Builder 組 prompt
-> Policy Engine 判斷模型與工具呼叫是否允許
-> Model Serving 回傳 LLM response
-> Tool Router 必要時查 CRM / LMS
-> Evaluation Hook 檢查回答品質與風險
-> TTS Service 產生語音
-> Dashboard 顯示逐字稿、評分、建議
-> Audit Logger 記錄完整事件
```

產出：

```text
docs/architecture/04-runtime-voice-flow.md
```

驗收：

- 能用 5 分鐘白板畫完整流程。
- 每一步都能說出 failure mode。

### Day 6: 補 Deployment / Operations View

目標：進入 AI deployment engineering。

部署圖要回答：

- 服務跑在哪裡？
- GPU 在哪裡？
- 哪些服務需要 GPU？
- 哪些服務 CPU-only？
- 資料庫在哪台機器？
- 客戶內網怎麼連？
- 是否能出網？
- 模型檔放哪？
- log 放哪？
- backup、upgrade、rollback、monitoring 怎麼做？

典型 on-prem 部署：

```text
GPU server: ASR, LLM, TTS, embedding
CPU app server: API Gateway, Agent Runtime, Dashboard
PostgreSQL: users, settings, tasks, audit metadata
MinIO / NAS: audio, reports, model artifacts
Kubernetes: deployment, scaling, restart, secret
Ingress / NGINX / Kong / Envoy: routing, TLS, rate limit
Prometheus / Grafana: latency, GPU utilization, QPS, error rate
Loki / OpenSearch: logs
OpenTelemetry: traces
```

產出：

```text
docs/architecture/05-deployment-onprem.md
```

驗收：

- GPU OOM 怎麼查。
- vLLM timeout 怎麼查。
- ASR latency 變高怎麼查。
- 客戶說系統沒反應，第一步查什麼。
- 客戶機房沒有 internet，模型與套件怎麼安裝。
- 版本更新失敗怎麼 rollback。

### Day 7: 整理 Architecture Pack

目標：整理成公司能用的交付物。

建議資料夾：

```text
docs/
  architecture/
    00-c4-notes.md
    01-system-context.md
    02-container-diagram.md
    03-component-ai-gateway.md
    04-runtime-voice-flow.md
    05-deployment-onprem.md
    06-risk-control-map.md
    adr/
      0001-use-fastapi-for-ai-gateway.md
      0002-use-vllm-for-local-llm-serving.md
      0003-use-qdrant-for-vector-search.md
      0004-use-opentelemetry-for-tracing.md
  runbooks/
    gpu-debugging.md
    service-restart.md
    model-upgrade-rollback.md
    customer-onprem-installation.md
```

10 分鐘簡報結構：

```text
1 min: 系統目的與客戶場景
2 min: Context Diagram
2 min: Container Diagram
2 min: AI Gateway Component Diagram
2 min: Runtime + Deployment
1 min: 風險、監控、下一步
```

## 6. 工具建議

優先順序：

1. Structurizr DSL：正式 architecture docs；models-as-code；適合 C4。
2. C4-PlantUML：文字描述架構，適合放進 Git repo。
3. Mermaid：適合 Markdown / GitHub README / 文件網站；C4 syntax 仍要注意穩定性。
4. 白板：適合臨時討論；討論後要整理成 diagram-as-code。

一般畫圖工具可以用於臨時溝通，但它們不理解 software architecture。正式文件要讓圖和文字責任一起進 Git。

## 7. 可直接使用的 box 與 line 寫法

Box 格式：

```text
Name
[Type / Technology]
Responsibility in one short sentence.
```

範例：

```text
AI Gateway
[FastAPI service]
Routes tenant requests to approved models and tools, enforces policies, and writes audit events.

ASR Service
[Python service / faster-whisper or Breeze ASR]
Converts streaming or uploaded audio into timestamped transcripts.

Vector Database
[Qdrant / pgvector]
Stores embeddings for enterprise documents and retrieves relevant chunks for RAG.
```

Line 格式：

```text
A -> B: action + protocol + data
```

範例：

```text
Dashboard -> AI Gateway: calls REST API over HTTPS
Audio Client -> Audio Ingestion Service: streams PCM audio over WebSocket
AI Gateway -> Policy Service: checks model/tool permission
Agent Runtime -> RAG Service: retrieves enterprise knowledge chunks
AI Gateway -> Audit Log DB: writes request, response, policy result, latency
```

## 8. Enterprise Voice AI Level 1 初稿

```text
Title:
System Context Diagram for Enterprise Voice AI Coach Platform

Scope:
Shows the Enterprise Voice AI Coach Platform, its users, and external enterprise systems.

People:
- Customer Service Agent: practices conversations and receives AI coaching feedback.
- Team Supervisor: reviews training results, risk cases, and performance analytics.
- Enterprise IT Admin: manages deployment, identity integration, permissions, and monitoring.
- Compliance Officer: reviews audit logs and verifies policy compliance.

External Systems:
- Enterprise Identity Provider: provides SSO and user identity.
- CRM System: stores customer records and interaction history.
- Learning Management System: stores training courses and employee progress.
- Enterprise Knowledge Base: provides approved internal documents for RAG.
- Telephony / Recording System: provides call audio or recording files.
- Notification System: sends reports or alerts to Email, Slack, or Teams.

Main System:
- Enterprise Voice AI Coach Platform: analyzes conversations, provides AI coaching, supports retrieval over enterprise knowledge, and records auditable decisions.
```

## 9. Enterprise Voice AI Level 2 初稿

```text
Dashboard Web App
[Next.js / React]
Allows supervisors and admins to review transcripts, scores, reports, and system settings.

API Gateway
[FastAPI]
Provides REST/WebSocket APIs, authenticates requests, routes traffic, and enforces basic request policies.

Audio Ingestion Service
[Python / WebSocket]
Receives audio streams or uploaded recordings and forwards chunks to ASR pipeline.

ASR Service
[Python / faster-whisper / Breeze ASR]
Converts speech to timestamped text.

Diarization Service
[pyannote.audio]
Separates speakers and attaches speaker labels to transcript segments.

Agent Runtime
[LangGraph or custom workflow]
Runs coaching workflows, prompt construction, RAG retrieval, model calls, and tool orchestration.

RAG Service
[LlamaIndex / LangChain]
Retrieves relevant enterprise knowledge chunks.

Vector Database
[Qdrant / pgvector]
Stores document embeddings.

Model Serving
[vLLM / Ollama / Triton]
Serves local LLM inference on GPU.

Policy Guardrail Service
[OPA / Presidio / custom rules]
Checks PII, tool permissions, model permissions, and output safety.

Audit Log Store
[PostgreSQL / ClickHouse]
Stores request metadata, policy decisions, tool calls, model outputs, and evaluation results.

Object Storage
[MinIO]
Stores audio files, transcript artifacts, exported reports, and model files.

Monitoring Stack
[Prometheus / Grafana / Loki / OpenTelemetry]
Collects metrics, logs, traces, and alert signals.
```

## 10. AI Gateway Component Diagram 初稿

```text
Request Router
Routes incoming chat, agent, transcription, scoring, and tool-call requests.

Auth Middleware
Validates JWT, API keys, and enterprise identity claims.

Tenant Resolver
Maps each request to customer, workspace, user role, policy profile, and model entitlement.

Rate Limit / Cost Meter
Tracks request rate, token usage, GPU usage, and tenant-level quota.

PII Detector
Detects and optionally redacts sensitive fields before model or tool execution.

Policy Client
Asks the policy engine whether a model call, retrieval, or tool call is allowed.

Prompt Builder
Constructs task prompts using role, policy, conversation context, retrieved evidence, and output schema.

Model Router
Selects approved model endpoint according to task, latency, cost, and security constraints.

Tool Router
Validates and dispatches tool calls to CRM, LMS, ticketing, or MCP servers.

Audit Logger
Writes immutable event records for compliance, debugging, and evaluation.

Evaluation Hook
Runs post-response checks for quality, groundedness, policy violation, and unsafe output.

Fallback Manager
Returns controlled fallback responses when model, retrieval, policy, or tool execution fails.
```

## 11. 補上的工程實踐

C4 是圖，但公司交付需要圖、文件、程式、測試與維運證據一起成立。

至少要會：

- API contract：OpenAPI / Swagger。
- Schema：Pydantic request / response。
- Config management：`.env`、Kubernetes Secret、Helm values。
- Database migration：Alembic。
- Testing：pytest、integration test。
- Load testing：k6 或 Locust。
- Observability：OpenTelemetry、Prometheus。
- CI/CD：GitHub Actions 或 GitLab CI。
- Containerization：Dockerfile / docker-compose。
- Deployment：Kubernetes manifests 或 Helm chart。
- ADR：Architecture Decision Record。
- Runbook：故障排除 SOP。

工程成熟度不在知道多少名詞，而在能不能讓系統可部署、可測試、可監控、可回滾、可交接。

## 12. 系統工程思維

推薦思考順序：

```text
需求: 誰用？解決什麼問題？成功指標是什麼？
邊界: 系統包含什麼？不包含什麼？
介面: 跟誰交換資料？格式是什麼？協定是什麼？
約束: latency、GPU、內網、資安、個資、可用性、成本。
風險: 哪裡會壞？壞了怎麼發現？怎麼降級？
驗收: 怎麼證明它能用？用什麼 test、metric、demo？
```

Enterprise voice AI 常見 non-functional requirements：

- ASR latency。
- LLM latency。
- GPU capacity。
- Data residency。
- Auditability。
- Availability。
- Security。
- Maintainability。
- Evaluation。
- Cost。

## 13. 最小可行實作練習

系統名稱：

```text
enterprise-voice-ai-c4-demo
```

功能：

- 上傳一段音檔。
- ASR 轉逐字稿。
- PII redaction。
- RAG 查一份公司 FAQ。
- LLM 產生客服教練建議。
- 寫入 audit log。
- Dashboard 顯示結果。

技術選型：

```text
Frontend: Next.js
Backend: FastAPI
ASR: faster-whisper or Breeze ASR pipeline
LLM: Ollama or vLLM OpenAI-compatible endpoint
RAG: LlamaIndex + Qdrant or pgvector
DB: PostgreSQL
Object Storage: MinIO
Observability: OpenTelemetry + Prometheus + Grafana
Local deployment: docker-compose
Docs: Structurizr DSL / Mermaid / C4-PlantUML
```

最小 API：

```text
POST /sessions
POST /sessions/{id}/audio
POST /sessions/{id}/transcribe
POST /sessions/{id}/analyze
GET /sessions/{id}
GET /sessions/{id}/audit
```

資料表：

```text
sessions
- id
- tenant_id
- user_id
- status
- created_at

transcripts
- id
- session_id
- speaker
- start_time
- end_time
- text
- pii_redacted_text

audit_events
- id
- session_id
- event_type
- actor
- input_hash
- output_hash
- policy_result
- latency_ms
- created_at

model_calls
- id
- session_id
- model_name
- prompt_tokens
- completion_tokens
- latency_ms
- status
```

這個 demo 不需要一次做到 production。目標是把 C4 圖、程式、API、部署、監控、風險全部串起來。

## 14. 面試回答模板

### 14.1 Software architecture diagram

```text
我會把 architecture diagram 當成系統溝通工具，不是美術圖。我的做法會先用 C4 Model 分層：Context 先講系統邊界、使用者與外部系統；Container 講可部署的應用與資料儲存；Component 講某個服務內部的程式結構；Code 通常不手畫，除非有複雜設計。我會要求每個 box 有名稱、類型、技術與責任，每條線有方向與關係說明，讓圖可以獨立被新同事或客戶理解。
```

### 14.2 VOISS 類型 enterprise AI 系統

```text
我會先畫 Context，確認使用者、客服主管、IT admin、稽核、CRM、LMS、SSO、知識庫、錄音系統與 on-prem GPU 環境。再畫 Container，把系統拆成 Dashboard、API Gateway、Audio Ingestion、ASR、Diarization、Agent Runtime、RAG、Model Serving、Policy Guardrail、Audit Log、Object Storage、Monitoring。接著對 AI Gateway 畫 Component Diagram，拆出 auth、tenant resolver、policy client、PII detector、model router、tool router、audit logger、evaluation hook。最後補 runtime sequence 和 deployment view，用來說明 real-time voice request 怎麼走、GPU 怎麼部署、log 怎麼查、失敗怎麼 fallback。
```

### 14.3 AI Gateway 的價值

```text
AI Gateway 是企業 AI 系統的治理邊界。普通 API Gateway 主要處理 routing、auth、rate limit；AI Gateway 還要處理 model routing、prompt policy、PII redaction、tool permission、agent audit、cost tracking、evaluation hook、fallback。企業客戶真正需要的是可控、可追溯、可維護的 AI，而不是一個單純會回答的模型。
```

## 15. 這週優先順序

優先順序：

1. C4 Level 1、2、3。
2. AI Gateway component boundary。
3. Voice AI runtime flow。
4. On-prem deployment / GPU / K8s / observability。
5. ADR、runbook、risk-control map。

先不要陷入：

- 畫漂亮圖。
- 研究所有 UML notation。
- 做完整 class diagram。
- 一次支援太多模型。
- 一次做完整多租戶 SaaS。
- 一開始追求完美 K8s production。

一週內的目標：

```text
看懂別人的系統圖。
把模糊需求整理成 C4 架構圖。
把架構圖連到實際 repo、API、部署與風險控制。
```

## 16. 最終濃縮版

這支影片給的核心能力是：

```text
用分層抽象，把複雜系統講到不同角色都聽得懂。
```

大二學生先記住：

```text
Context 講「系統活在哪裡」。
Container 講「系統由哪些可部署單元組成」。
Component 講「某個服務裡面怎麼分工」。
Code 講「低階類別與函式」，通常自動產生，不要手畫。
```

VOISS / enterprise AI 工作要把這套方法用在：

```text
ASR
TTS
RAG
LLM
Agent
AI Gateway
Guardrail
Audit
K8s
GPU deployment
Monitoring
Customer on-prem delivery
```

這樣你才不是只會講 AI 名詞，而是能把 AI 系統變成可以交付、可以維護、可以被企業信任的工程產品。

## References

- C4 Model: <https://c4model.com/>
- System Context Diagram: <https://c4model.com/diagrams/system-context>
- Container Diagram: <https://c4model.com/diagrams/container>
- Structurizr: <https://structurizr.com/>
- C4-PlantUML: <https://github.com/plantuml-stdlib/C4-PlantUML>
- PlantUML: <https://plantuml.com/>
- Mermaid C4 diagrams: <https://mermaid.ai/open-source/syntax/c4.html>
