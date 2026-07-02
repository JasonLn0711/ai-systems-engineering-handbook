# VOISS-Style Agent Platform Onboarding Sprint - 2026-07-02

## Purpose

This note turns Jason's VOISS onboarding preparation into a public-safe
accelerator bridge. It preserves the learning priority without copying private
interview text into the handbook curriculum.

The target is not "learn all AI." The target is:

```text
turn an AI Coach / Agent system into an enterprise customer platform that is
integratable, governable, deployable, and acceptable for review.
```

## Source Boundary

Allowed here:

- generalized enterprise AI Coach platform requirements
- public-safe technical learning tasks
- public documentation routes
- synthetic artifact names and schemas
- source links already suitable for training

Not included here:

- private interview transcript text
- private LINE wording
- offer, salary, employment, or contact details
- customer secrets
- unpublished company claims

The private source capture lives in:

```text
../../../career-application-system/applications/2026-06-foptwasg-edge-ai-deployment-engineer/source/2026-07-02-voiss-max-onboarding-bootcamp-training-source.md
```

The synthesized private prep packet lives in:

```text
/home/jnclaw/Downloads/voiss-max-onboarding-knowledge-packet-2026-07-02/VOISS_Max_Onboarding_Knowledge_Packet_2026-07-02.md
```

## Connection Map

| Route | File | Use |
| --- | --- | --- |
| Accelerator parent | `README.md` | Enterprise AI Architecture Sprint overview and public-safe boundary. |
| Sprint evidence map | `00-sprint-map.md` | Existing 7-day and 30-day evidence routing. |
| Day 1 | `day-01-ai-gateway/README.md` | Gateway architecture and contract foundation. |
| Day 2 | `day-02-agent-governance/README.md` | Agent governance, memory, approval, and policy thinking. |
| Day 3 | `day-03-red-team-guardrails/README.md` | Red-team and guardrail learning path. |
| Day 4 | `day-04-rag-tool-gateway/README.md` | RAG, tool registry, and gateway integration. |
| Day 5 | `day-05-k8s-gpu-serving/README.md` | Docker, K8s, GPU sizing, vLLM serving. |
| Day 6 | `day-06-integrated-demo-memo/README.md` | Integrated demo and architecture memo packaging. |
| Day 7 | `day-07-onboarding-pack/README.md` | First-week questions, first-30-days plan, evidence index. |
| Existing tutorial | `7-day-consulting-onboarding-tutorial.zh-TW.md` | Broad 7-day overview; use as base vocabulary and artifact pattern. |
| Expanded plan | `30-day-spiral-bootcamp.zh-TW.md` | 30-day spiral depth path after the platform slice is defined. |

## Adopted Priority Order

| Priority | Capability | Why it comes here |
| --- | --- | --- |
| `P0` | Agent API / SDK / embed / CLI platformization | This is the product-platform layer that lets enterprise customers integrate an AI Coach into web, mobile, CRM, LMS, HRD, ERP, and support workflows. |
| `P1` | AI Gateway / Guardrail / RBAC / audit / on-prem architecture | This makes the platform governable, secure, observable, reviewable, and acceptable to enterprise IT and compliance teams. |
| `P2` | AWQ / LoRA / finetune / pruning / Docker / K8s / GPU sizing runtime | This supports deeper runtime ownership after the platform and governance contracts are clear. |

Interview-tested topics route under those priorities:

| Topic | Route |
| --- | --- |
| ASR, TTS latency, hotwords | Route into P0/P2 only when the AI Coach interface or voice runtime needs evidence. |
| RAG | Route into P0 context/report contracts and P1 source-governance controls. |
| Tool use | Route into P0 tool registry and P1 permission/guardrail checks. |
| PII | Route into P1 guardrail and audit. |
| Red teaming | Route into P1 regression harness and risk taxonomy. |
| KV cache | Route into P2 serving and GPU sizing. |
| Docker / K8s | Route into P2 deployment proof, not the first platform contract. |

## Current Project Leverage

This repo already contains most learning rails needed for the sprint:

- `day-01-ai-gateway/`: API gateway, request/response lifecycle, RBAC/ABAC,
  C4 model, and hypothesis-based problem solving.
- `day-02-agent-governance/`: agent authority, memory, approval, audit, and
  governance framework.
- `day-03-red-team-guardrails/`: red-team taxonomy, guardrail tests, failure
  gallery.
- `day-04-rag-tool-gateway/`: RAG schema, tool registry, gateway integration,
  permissioned tool calls.
- `day-05-k8s-gpu-serving/`: Docker/K8s/GPU/vLLM serving evidence.
- `day-06-integrated-demo-memo/`: packaging an integrated demo into reviewable
  architecture evidence.
- `day-07-onboarding-pack/`: first-week questions and first-30-days plan.

The current gap is not missing curriculum. The gap is that the existing
accelerator is broad enterprise voice AI, while this sprint needs a sharper
platformization artifact:

```text
Agent session contract
-> SDK/embed/CLI surface
-> tenant/user/role/context model
-> RBAC and audit
-> report callback
-> customer integration README
```

## First Deliverable: Agent Platform Slice v0

Build the first proof as a small but complete enterprise integration slice:

```text
session API
+ SDK/embed mock
+ CLI smoke test
+ tenant/user/role/context
+ RBAC
+ audit log
+ report callback
+ customer integration README
```

Do not start with AWQ, K8s, full mobile apps, or deep model training. Those are
valid later paths, but they do not prove the core platform-integration question.

### Required Artifacts

| Artifact | Minimum content | Evidence value |
| --- | --- | --- |
| `openapi.yaml` | `/v1/sessions`, `/v1/sessions/{id}/messages`, `/v1/sessions/{id}/report`, `/v1/sessions/{id}/events` | Proves the customer-facing contract. |
| `context.schema.json` | tenant, user, role, scenario, page/app context, policy context | Proves data-format discipline. |
| RBAC matrix | trainee, coach, supervisor, compliance reviewer, admin, support | Proves enterprise permission thinking. |
| Audit event schema | request id, tenant, actor, event type, policy/model/scenario version | Proves traceability. |
| SDK/embed mock | script tag and React-style component with context/contextLabel | Proves platform surface. |
| CLI smoke example | create session, send message, fetch report, verify audit event | Proves support/debug readiness. |
| Customer integration README | auth, context, callback, errors, acceptance checks | Proves handoff quality. |

## P0 Task Breakdown

### P0.1 Contract First

Learn and produce:

- REST API contract basics
- OpenAPI 3.1
- JSON Schema
- request / response examples
- idempotency keys
- error codes
- request IDs

Deliverable:

```text
openapi.yaml + sample request/response directory
```

Acceptance criteria:

- The four core endpoints are documented.
- Every request has tenant, session, scenario, and context handling.
- Errors include stable codes and request IDs.

### P0.2 Identity and Context

Learn and produce:

- JWT/OIDC basics
- tenant isolation
- user/role claims
- context vs visible context label
- scenario versioning
- policy context

Deliverable:

```text
context.schema.json + identity-flow.md
```

Acceptance criteria:

- A customer can understand which fields they must provide.
- Sensitive user identity is separated from visible training context.
- Session context can support web, mobile, CRM, LMS, and HRD integrations.

### P0.3 SDK / Embed / CLI Surface

Learn and produce:

- script tag integration pattern
- React component wrapper pattern
- callback/webhook pattern
- CLI command shape
- customer smoke test pattern

Deliverable:

```text
embed-example.html + react-example.tsx + cli-examples.md
```

Acceptance criteria:

- The same session API supports web embed and CLI.
- `onScoreReady` or equivalent report callback exists.
- CLI can validate API reachability, auth, scenario availability, report
  callback, and audit emission.

### P0.4 Report and Scoring Contract

Learn and produce:

- report schema
- rubric versioning
- score provenance
- source trace
- callback payload

Deliverable:

```text
report.schema.json + scoring-rubric-contract.md
```

Acceptance criteria:

- A score is traceable to scenario, rubric version, model version, and session.
- Report callback can be mapped to CRM/LMS/HRD writeback.
- Report contract supports human review and audit.

## P1 Task Breakdown

### P1.1 Gateway Request Lifecycle

Learn and produce:

- API gateway request flow
- authn/authz
- rate limit and quota
- model routing
- fallback and circuit breaker
- semantic caching concept
- request/response enrichment

Deliverable:

```text
gateway-request-lifecycle.md + architecture.mmd
```

Acceptance criteria:

- The request path shows gateway, auth/RBAC, guardrail, agent runtime, RAG,
  tools, model, audit, and report.
- Cloud, hybrid, and on-prem variants are named.

### P1.2 RBAC / ABAC / Audit

Learn and produce:

- RBAC vs ABAC
- support access grant
- data retention classes
- audit event taxonomy
- SIEM handoff vocabulary

Deliverable:

```text
rbac-abac-matrix.md + audit-event-schema.json
```

Acceptance criteria:

- Denied access is explicitly testable.
- Support access is scoped and audited.
- Audit events include policy, model, scenario, and actor identity.

### P1.3 Guardrail Mini Harness

Learn and produce:

- input guardrail
- retrieval guardrail
- tool guardrail
- output guardrail
- review gate
- prompt injection tests
- PII detection/redaction reference path

Deliverable:

```text
guardrail-test-cases.jsonl + guardrail-report.md
```

Acceptance criteria:

- At least 20 test cases exist.
- Each case has expected control and pass/fail condition.
- PII, prompt injection, tool misuse, missing citation, and high-risk output
  are represented.

### P1.4 Customer Acceptance Criteria

Learn and produce:

- API reachable
- auth valid
- scenario available
- RBAC deny path
- report callback success
- audit log emitted
- health check
- error code and request ID

Deliverable:

```text
customer-it-acceptance-checklist.md
```

Acceptance criteria:

- A customer IT reviewer can run the checklist without reading source code.
- Every acceptance item has evidence path and failure-handling note.

## P2 Task Breakdown

### P2.1 Dockerized Runtime

Learn and produce:

- Dockerfile
- Docker Compose
- environment variables
- health endpoint
- structured logs
- model/mock service boundary

Deliverable:

```text
Dockerfile + compose.yaml + runtime-readme.md
```

Acceptance criteria:

- Service starts locally.
- Health endpoint works.
- Sample request logs request ID and latency.

### P2.2 K8s GPU-Ready Mini Lab

Learn and produce:

- Deployment
- Service
- Ingress or port-forward
- ConfigMap
- Secret placeholder
- readinessProbe / livenessProbe
- resource requests
- GPU vocabulary: `nvidia.com/gpu`, device plugin, GPU Operator

Deliverable:

```text
k8s/deployment.yaml + k8s/service.yaml + k8s-runbook.md
```

Acceptance criteria:

- The manifest is readable and runnable in a local or mock environment.
- GPU fields are clearly marked as GPU-ready, not falsely validated if no GPU
  cluster run happened.

### P2.3 GPU Sizing and KV Cache

Learn and produce:

- weights estimate
- quantization overhead
- KV cache drivers
- context length
- concurrency
- runtime overhead
- p50/p95 latency

Deliverable:

```text
gpu-sizing.csv + sizing-method.md
```

Acceptance criteria:

- Estimates separate weights, KV cache, overhead, concurrency, and safety
  buffer.
- The method states which numbers are measured and which are assumptions.

### P2.4 Model Adaptation Decision Tree

Learn and produce:

- when RAG is enough
- when prompt/schema/eval is enough
- when LoRA is justified
- when full finetune is justified
- when AWQ/quantization helps inference
- why pruning is usually not first response

Deliverable:

```text
model-adaptation-decision-tree.md
```

Acceptance criteria:

- The decision tree avoids treating LoRA/finetune as universal fixes.
- Each adaptation path names validation data, rollback, and model-card update.

## 30-Day Execution Shape

| Window | Focus | Deliverables |
| --- | --- | --- |
| Days 1-3 | P0 platform contract | `openapi.yaml`, context schema, RBAC matrix, audit schema, SDK/embed mock, CLI smoke examples, customer README. |
| Days 4-7 | P1 gateway and guardrails | gateway lifecycle, RBAC/ABAC table, guardrail test cases, PII redaction path, acceptance checklist. |
| Days 8-14 | P2 runtime mini lab | Docker/Compose, K8s GPU-ready manifest, GPU sizing table, model adaptation note. |
| Days 15-30 | Integrated portfolio demo | AI Coach integration demo with session API, context label, mock RAG trace, scoring report, RBAC, audit, callback, gateway policy, Docker, K8s manifest, customer IT README. |

## Additions to Keep

These additions should stay in the training plan because they are easy to miss
and directly improve enterprise readiness:

1. Acceptance criteria for customer IT review.
2. Scoring / rubric schema with version and provenance.
3. Support/debug runbook using CLI, request ID, audit event, error codes, and
   health checks.
4. Data-boundary controls for retention, de-identification, permissions,
   sources, audit, and support access.

## Deferred or Removed

Defer these until the platform slice and gateway design exist:

- full mobile app
- broad multi-model benchmark
- from-scratch training
- treating LoRA/finetune as universal fixes
- production-grade K8s platform
- dynamic frontend UI depth before API contract

## Public References

- VOISS official site: `https://www.voiss.cc/`
- Crow embed docs: `https://docs.usecrow.ai/embed-widget`
- Google Cloud Apigee AI: `https://cloud.google.com/solutions/apigee-ai`
- OpenAI Agents SDK guardrails: `https://openai.github.io/openai-agents-python/guardrails/`
- vLLM AutoAWQ: `https://docs.vllm.ai/en/latest/quantization/auto_awq.html`
- NIST AI RMF: `https://www.nist.gov/itl/ai-risk-management-framework`
- Kubernetes device plugins: `https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/`

## Next Gate

Choose the implementation home for `Agent Platform Slice v0`, then create the
P0 artifact skeleton. The smallest useful skeleton is:

```text
agent-platform-slice-v0/
├── openapi.yaml
├── schemas/
│   ├── context.schema.json
│   ├── report.schema.json
│   └── audit-event.schema.json
├── docs/
│   ├── rbac-matrix.md
│   ├── customer-integration-readme.md
│   └── cli-smoke-tests.md
└── examples/
    ├── embed-example.html
    └── react-example.tsx
```

Status: `source preserved`; `adopted decision`; `implementation pending`.
