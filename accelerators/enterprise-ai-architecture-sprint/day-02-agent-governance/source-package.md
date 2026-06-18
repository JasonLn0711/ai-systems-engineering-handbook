# Source Package — Day 2：Agent Governance Framework

> 教師、TA 與 repo 維護者使用。此檔說明本課程包的來源邊界、官方技術語言校準來源，以及 public-safe 案例設計原則。

---

## 0. Purpose

本 source package 的目的不是把官方文件變成學生必讀，而是協助老師校準技術語言，避免 Day 2 變成單純的 prompt engineering 或抽象安全口號。

Day 2 的主軸：

```text
Enterprise agent governance is a system contract problem.
```

因此，本課程包使用以下技術語言：

```text
AI Gateway
Agent Registry
Policy Gate
Tool Boundary
Data Boundary
Memory Scope
Mediated Message Boundary
Declassification
Human Review
Audit Event
Evaluation Hook
Red-Team Seed
```

---

## 1. Source Boundary

### 1.1 Allowed source categories

可以使用：

- 校園 IT helpdesk。
- 銀行內部知識助理。
- 醫療 staff-review intake support。
- 製造場域維修助理。
- 一般化 enterprise support workflow。
- 官方公開文件。
- public-safe synthetic examples。

### 1.2 Disallowed source categories

不要使用：

- 私人訪談逐字稿。
- 客戶秘密。
- credentials。
- personal contact routes。
- salary 或 offer detail。
- 未公開公司主張。
- 可識別個資。
- 真實 helpdesk ticket。
- 真實內部 SOP 內容。
- 真實系統內部路徑或 token。

### 1.3 Generalization rule

如果有私人來源啟發，請改寫成一般化系統需求：

```text
enterprise customer requires approval-gated side-effect actions
```

不要保留原始私人情境：

```text
某公司某客戶要求某部門某人批准某個內部 API。
```

### 1.4 Imported package archive

This Day 2 package was imported from a prepared archive and then aligned with the repo's accelerator-day structure:

```text
teacher-packets/source-archives/day-02-agent-governance-course-package.zip
teacher-packets/source-archives/extracted-day-02-agent-governance-course-package/
```

The extracted `manifest.json` is retained in the source archive folder as delivery metadata. The canonical teaching files live in:

```text
accelerators/enterprise-ai-architecture-sprint/day-02-agent-governance/
```

---

## 2. Official References for Technical Language Calibration

### 2.1 OWASP GenAI Security Project / LLM Top 10

Use for:

- prompt injection。
- sensitive information disclosure。
- excessive agency。
- vector and embedding weaknesses。
- supply chain / plugin / tool 風險。
- AI app security taxonomy。

Reference:

```text
https://genai.owasp.org/llm-top-10/
https://owasp.org/www-project-top-10-for-large-language-model-applications/
```

How it informs Day 2:

```text
Day 2 的 risk-control map 與 Day 3 red-team seeds 應包含 prompt injection、
permission bypass、tool abuse、memory leakage、audit evasion、excessive agency、
confused deputy、broker payload leakage、replay attack。
```

Teaching caveat:

```text
不要把 OWASP list 當 checklist 背誦。要把風險映射到具體 governance controls。
```

---

### 2.2 NIST AI Risk Management Framework Core

Use for:

- govern。
- map。
- measure。
- manage。
- risk lifecycle。
- accountability and risk management language。

Reference:

```text
https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
https://www.nist.gov/itl/ai-risk-management-framework
```

How it informs Day 2:

```text
Day 2 的 governance artifacts 對應 Govern / Map。
Audit event 與 evaluation hook 對應 Measure。
Policy updates 與 red-team feedback 對應 Manage。
```

Teaching caveat:

```text
大二學生不需要完整背 NIST AI RMF。只需理解 AI risk management 是 lifecycle，不是一次性文件。
```

---

### 2.3 Open Policy Agent / Rego

Use for:

- policy-as-code。
- structured data decision。
- externalized policy engine。
- decoupling policy decision from application code。

Reference:

```text
https://www.openpolicyagent.org/docs
https://www.openpolicyagent.org/docs/policy-language
```

How it informs Day 2:

```text
Policy gate 可被教成 decision API：input 是 structured data，output 是 allow / deny / review。
OPA / Rego 是工程例子，不是 Day 2 必修實作。
```

Teaching caveat:

```text
不要讓工具名稱取代概念。學生要先懂 decision boundary，再認識 OPA。
```

---

### 2.4 Cedar Policy Language

Use for:

- authorization mental model。
- principal。
- action。
- resource。
- context。
- allow / forbid / conditions。

Reference:

```text
https://docs.cedarpolicy.com/
https://docs.cedarpolicy.com/policies/syntax-policy.html
```

How it informs Day 2:

```text
Cedar 可幫學生理解 authorization request 的形狀：
principal=user/role, action=requested operation, resource=tool/data/agent, context=request metadata。
```

Teaching caveat:

```text
Day 2 不要求學生寫 Cedar policy。只用它校準 authorization vocabulary。
```

---

### 2.5 OpenTelemetry

Use for:

- trace。
- metrics。
- logs。
- request lifecycle observability。
- trace ID / span mental model。

Reference:

```text
https://opentelemetry.io/docs/
https://opentelemetry.io/docs/concepts/signals/
```

How it informs Day 2:

```text
Audit event 與 observability 不完全相同，但 trace_id、request path、logs/traces mental model 有助於學生理解如何重建 request lifecycle。
```

Teaching caveat:

```text
OpenTelemetry 是 observability framework；audit event 是 governance evidence。兩者可以整合，但不能混為一談。
```

---

### 2.6 Apache Kafka / Message Broker Security

Use for:

- message broker as event backbone。
- topic ACL and principal/resource/operation mental model。
- producer / consumer identity。
- quotas and flow control。
- event replay and retention tradeoffs。

Reference:

```text
https://kafka.apache.org/documentation/#security
https://kafka.apache.org/documentation/#security_authz
https://docs.confluent.io/kafka/design/quotas.html
```

How it informs Day 2:

```text
Message mediation 可以用 Kafka-like broker 解釋，但 broker 不是完整安全解法。
Day 2 要強調 topic ACL、schema、retention、consumer allowlist、audit、raw payload 控制。
```

Teaching caveat:

```text
不要把所有中介層都稱為 Kafka。RabbitMQ、NATS JetStream、Redpanda、Temporal / LangGraph workflow
各自處理不同工程問題；Day 2 的核心是跨信任邊界的 mediation contract。
```

---

### 2.7 Confused Deputy and Capability Delegation

Use for:

- OS 權限類比。
- low-trust actor inducing high-trust service。
- original requester identity。
- capability-based delegation。
- expires_at / nonce / idempotency key。

Reference:

```text
https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html
https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html
```

How it informs Day 2:

```text
高權限 agent 即使可以讀資料，也不代表可以把資料交給任何請求者。
Policy input 應包含 original_user、requesting_agent、action、resource、purpose、
requested_output_classification、expires_at、trace_id。
```

Teaching caveat:

```text
OS 類比用來建立直覺；課程重點不是教學生利用 file descriptor，而是教他們辨識代理權限錯用。
```

---

## 3. Recommended Technical Stack Examples

Day 2 不要求完整實作，但可以使用以下技術名稱幫學生理解真實世界落地方式。

### 3.1 Python stack

| Concern | Package / Tool |
|---|---|
| HTTP gateway | `FastAPI`, `uvicorn` |
| Schema validation | `Pydantic` |
| Policy decision | OPA sidecar via HTTP, or simple Python policy function for mock |
| Database | `PostgreSQL`, `SQLAlchemy`, `psycopg` |
| Session / rate limit | `Redis` |
| Audit event | PostgreSQL append-only table, object storage, or event stream |
| Observability | `opentelemetry-sdk`, `opentelemetry-instrumentation-fastapi` |
| Structured logging | `structlog`, Python `logging` |
| Testing | `pytest`, `httpx`, `pytest-asyncio` |
| Message broker | `confluent-kafka`, `aiokafka`, Redpanda, Apache Kafka |
| Declassification / PII redaction | `presidio-analyzer`, `presidio-anonymizer`, deterministic policy checks |

### 3.2 TypeScript stack

| Concern | Package / Tool |
|---|---|
| HTTP gateway | `Fastify`, `Express`, `Hono`, `Next.js Route Handler` |
| Schema validation | `zod`, `typebox` |
| Policy decision | OPA HTTP API, Cedar service, or mock policy module |
| Database | `PostgreSQL`, `Prisma`, `Drizzle ORM` |
| Session / rate limit | `Redis`, `Upstash Redis` |
| Audit event | PostgreSQL append-only table, event queue |
| Observability | `@opentelemetry/api`, OpenTelemetry Node SDK |
| Testing | `vitest`, `jest`, `supertest` |
| Message broker | `kafkajs`, `amqplib`, NATS client |
| Schema validation for messages | `zod`, JSON Schema, Protobuf / Avro via schema registry |

### 3.3 Data / RAG stack examples

| Concern | Tool |
|---|---|
| Vector database | `pgvector`, `Qdrant`, `Weaviate`, `Pinecone` |
| Document metadata | PostgreSQL table or object metadata |
| Retrieval enforcement | metadata filter before context assembly |
| RAG framework | `LlamaIndex`, `LangChain`, custom retriever |
| Source citation | source_id, document_version, effective_date |

### 3.4 Agent orchestration examples

| Concern | Tool |
|---|---|
| Agent state graph | `LangGraph` |
| Tool calling runtime | OpenAI Responses / Assistants style tool calling, custom function calling, LangChain tools |
| Guardrail | Custom policy checks, JSON schema validation, moderation/safety classifier |
| Human review | Internal queue, ticket system, admin UI |
| Durable workflow | `Temporal`, `LangGraph` durable execution |
| Message mediation | Kafka / Redpanda topic ACL, RabbitMQ vhost permissions, NATS subject permissions |

Teaching caveat:

```text
工具名稱只是落地例子。Day 2 的評分重點是 governance artifact quality，不是使用哪個套件。
```

---

## 4. Public-Safe Case Library

### 4.1 Campus IT Helpdesk Assistant

Use for Day 2 primary teaching.

Key controls:

```text
public FAQ allowed
staff-only SOP denied
student-facing agent cannot use staff-only agent as indirect reader
raw staff-only payload does not enter student-readable topic/log/cache/DLQ
ticket submission review-gated
session-only memory
audit source/tool/policy/review
```

### 4.2 Bank Internal Knowledge Assistant

Use for transfer exercise.

Key controls:

```text
role-based document access
department and access_level metadata
PII minimization
review for compliance-sensitive answers
source version citation
declassification before low-trust output
capability expiration for privileged requests
```

### 4.3 Healthcare Staff-Review Intake Support

Use with careful wording.

Key controls:

```text
patient-provided data separated from public education data
no final diagnosis
staff-review intake support
PII minimization
high-risk advice review
staff-only clinical workflow details do not cross into patient-visible answer without review
```

### 4.4 Manufacturing Maintenance Assistant

Use for operations context.

Key controls:

```text
equipment-line and site-specific permission
maintenance record as side-effect tool
supervisor approval for high-risk operations
equipment ID and SOP version audit
site-specific maintenance payloads do not leak across tenant/site topic boundaries
```

---

## 5. Course Design Principles

### 5.1 Evidence over vibes

Every concept should become an artifact:

```text
concept -> artifact -> rubric -> Day 3 test
```

Example:

```text
Tool abuse
-> tool boundary table
-> rubric checks review/rate limit/audit
-> red-team seed asks to submit 100 tickets

Confused deputy
-> message mediation contract
-> rubric checks original user and output classification
-> red-team seed asks low-trust agent to use high-trust agent as reader
```

### 5.2 Prompt is not boundary

Use this contrast repeatedly:

```text
Prompt can guide behavior.
Policy and system boundaries enforce behavior.
Audit evidence proves what happened.
Declassification controls what may cross from high-trust to low-trust output.
```

### 5.3 Teach as software contract design

Agent governance is closer to:

```text
API contract
configuration contract
authorization decision
message contract
declassification contract
audit schema
test harness
```

than to:

```text
chatbot personality tuning
```

### 5.4 Keep examples implementable

Students should be able to imagine:

```text
FastAPI handler reads registry YAML.
Policy function returns allow/deny/review.
Tool broker checks allowed_tools.
Retriever applies metadata filters.
Message broker accepts only schema-valid support-safe requests.
Declassifier turns privileged result into student-support-safe output.
Audit event is inserted into PostgreSQL.
Day 3 test uses pytest/httpx to hit POST /gateway/requests.
```

### 5.5 Separate student and instructor material

Student-facing material should not include:

```text
full reference answer
detailed grading rubric
instructor-only failure diagnosis
```

Instructor-facing material may include all of those.

---

## 6. Suggested Repo Placement

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

Supporting source archive:

```text
teacher-packets/source-archives/day-02-agent-governance-course-package.zip
teacher-packets/source-archives/extracted-day-02-agent-governance-course-package/
```

---

## 7. Maintenance Notes

When updating this package:

```text
[ ] Keep examples public-safe.
[ ] Update official reference links if standards move.
[ ] Keep student handout free of reference answer.
[ ] Keep rubric artifact-based.
[ ] Preserve Day 1-to-Day 2 gateway continuity.
[ ] Preserve Day 3 red-team handoff.
[ ] Preserve message mediation / confused deputy / declassification continuity across handout, worksheet, rubric, reference answer, and handoff.
[ ] Keep raw privileged payload out of student-facing examples unless the example is explicitly a denied failure case.
[ ] Avoid making OPA/Cedar/OpenTelemetry mandatory for beginners.
[ ] Keep tool names as examples, not conceptual substitutes.
```
