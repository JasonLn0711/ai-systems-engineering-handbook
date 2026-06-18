# AI Gateway Architecture

## Purpose

Produce a clear AI Gateway architecture that explains how clients, agents,
tools, models, knowledge sources, policies, memory, logs, and evaluation fit
together in an enterprise AI system.

## Prerequisite Contract View

Before drawing the gateway, the learner should be able to read one minimal AI
request as a backend contract:

```text
HTTP method + route
headers and JSON body
free text, selected fields, client hints
user identity, role, permission, requested action
backend route -> handler -> log
schema validation and intent normalization
task risk classification
policy decision: allow | deny | review_required
RAG permission filtering before model context
model serving engine as data plane: vLLM / SGLang / hosted model API
tool call as controlled API action
database-backed audit evidence
HTTP response status and JSON body
OWASP / NIST access-control mental model
serverless API as trusted backend boundary
gateway type separation: API gateway, AI/LLM gateway, tool broker, policy engine
```

The architecture should make those fields governable and traceable. The gateway
is not only a prompt-forwarding proxy; it is the request lifecycle control plane.
HTTP is the usual external boundary because clients, enterprise network tools,
auth systems, status codes, routing, and observability already understand it.
The internal gateway implementation can still use streaming, queues, gRPC,
database connections, model-server protocols, and connectors when those are the
right fit.

Model serving engines such as vLLM and SGLang belong behind the gateway as
model inference data-plane services. They load model weights, manage GPU memory
and KV cache, batch requests, stream tokens, and expose model APIs. They do not
replace the AI Gateway. The gateway still owns authentication, tenant and user
context, policy decisions, tool permissions, source boundaries, audit evidence,
quota, and review workflows.

Security and governance fields must come from trusted server-side context, not
from browser-provided payload. Client fields such as category, urgency, or
requested action are useful hints, but `user_id`, `role`, `permission`,
`allowed_tools`, `risk_class`, and `policy_decision` must be resolved by the
gateway from token claims, identity providers, permission databases, agent/tool
registries, and policy data. The relevant OWASP mental model is
deny-by-default, least privilege, server-side authorization, and permission
checks on every request. The relevant NIST mental model is access-control
policy plus ABAC-style subject, object, operation, and environment attributes.

Serverless API deployment does not change the trust model. It changes how the
trusted handler is hosted:

```text
Client
  -> API Gateway / Vercel Function / Cloudflare Worker route
  -> trusted handler
     verify token -> resolve role/permission -> validate schema -> policy -> audit
```

Serverless means the handler runs as a managed function rather than a
long-running server process. The platform manages runtime startup, scaling,
routing, and isolation, but the gateway still owns token validation, permission
lookup, schema validation, policy evaluation, tool brokering, secret handling,
durable state, idempotency for side effects, and audit evidence.

Do not define serverless as "backend server placed on the cloud." That is cloud
hosting. Serverless changes the ownership boundary:

```text
cloud hosting = the team provisions compute and runs a long-lived app server
serverless API = the team deploys handler code; the platform invokes it per event
```

Localhost can simulate serverless with tools such as AWS SAM local, Vercel dev,
Cloudflare Wrangler, Serverless Framework offline, or LocalStack. A private
cluster can run serverless-like platforms such as OpenFaaS or Knative. But a
plain local FastAPI/Express process listening on `localhost` is a local backend
server, not serverless. Serverless is serverless for the application team; the
platform operator still runs routers, schedulers, runtimes, logs, metrics, and
capacity.

Use serverless API for gateway entrypoints, webhook receivers, policy checks,
job creation, short RAG calls, and audit writes. Do not use a single synchronous
function for long AI jobs such as large audio transcription, batch evaluation,
or GPU inference. Those flows should become:

```text
HTTP request -> serverless handler -> queue / workflow -> worker / container / GPU service -> result store
```

This keeps the gateway inspectable while moving long-running work to a system
designed for retries, timeouts, and partial failure.

For enterprise AI, the expected target is usually hybrid:

```text
containers / Kubernetes / managed services:
  AI Gateway core, agent registry, tool registry, policy service, memory
  service, streaming sessions, GPU inference, high-volume services

serverless:
  webhooks, file intake, scheduled jobs, notification handlers, job triggers,
  lightweight audit/policy extensions, internal automation
```

The decision is workload-driven. Low-volume, short, event-driven tasks often fit
serverless. High-volume, long-running, latency-sensitive, stateful, streaming,
or GPU-heavy workloads usually fit containers, Kubernetes, managed services, or
dedicated inference infrastructure.

Keep identity, role, and permission separate:

```text
identity = the specific person/account/service to authenticate and audit
role = the category assigned to that identity
permission = the concrete action allowed, denied, or routed to review_required
```

## Architecture View

```text
Client / Channel
  |
  v
API Gateway / Serverless API boundary
  |
  v
AI Gateway
  |-- Auth
  |-- RBAC / permission boundary
  |-- Schema validator
  |-- Intent normalizer
  |-- Risk classifier
  |-- Request policy
  |-- Policy engine
  |-- Agent registry
  |-- Tool broker
  |-- MCP server connectors
  |-- Skill / adapter router
  |-- Model router
  |-- Memory manager
  |-- Guardrail layer
  |-- Audit log
  |-- Evaluation hooks
  |
  v
Agent / Workflow Runtime
  |
  |-- RAG / KB / SQL
  |-- Tools / APIs / workflows
  v
Model Serving Layer / Hosted Model API
  |
  |-- vLLM server for open-weight models
  |-- SGLang server for structured / prefix-heavy workloads
  |-- Hosted model API
  v
Human review / customer acceptance evidence
```

## Evidence Output

- One architecture diagram.
- One request/response contract reading.
- One component responsibility table.
- One request lifecycle.
- One risk-control map.

## Component Responsibilities

| Component | Responsibility | Failure if missing |
|---|---|---|
| API gateway / serverless API boundary | Receive HTTP traffic, expose routes, attach auth/rate-limit/logging controls, invoke the trusted handler, and hand long work to queues or workflows | Browser or client traffic reaches AI logic without a stable server-side boundary; long AI jobs block synchronous requests |
| Auth | Identify user, service, or agent caller | Anonymous or spoofed calls enter the system |
| RBAC | Enforce user and agent permissions | Agents access data or tools outside scope |
| Schema validator | Check request and tool argument shape | Malformed requests become policy or tool ambiguity |
| Intent normalizer | Convert free text and client hints into actions, resources, and tools | Natural language drives tools without inspectable policy input |
| Risk classifier | Label read-only, restricted, side-effect, external, or high-stakes actions | High-risk actions bypass review |
| Request policy / policy engine | Decide allow, deny, or review_required from structured input | Unsafe or unsupported tasks proceed |
| Agent registry | Track available agents and owners | Agent behavior becomes untraceable |
| Tool broker | Mediate tool calls | Tools are called without schema, timeout, or audit |
| MCP connectors | Expose shared data/tools through governed interfaces | Ad hoc integrations multiply |
| Skill / adapter router | Map shared capabilities to task-specific behavior | Every project forks the same logic |
| Model router / serving boundary | Route allowed model requests to hosted APIs or serving engines such as vLLM and SGLang; record model, version, latency, token usage, and failure state | Model endpoint choice, cost, latency, and version become unmanaged; serving engines may be mistaken for governance layers |
| Memory manager | Control storage, retrieval, sharing, and deletion | Cross-agent memory leaks or poisons decisions |
| Guardrail layer | Check input, retrieval, tool use, and output | Prompt injection and data leakage bypass controls |
| Audit log | Record decisions, calls, sources, and outcomes | Customer cannot reconstruct system behavior |
| Evaluation hooks | Measure correctness, safety, latency, and policy pass/fail | Demo cannot become managed service |

## Action Extraction

The gateway may use an LLM to help interpret free text, but the LLM should only
propose structured actions. The gateway still validates schema, maps actions to
registered tools/resources, evaluates policy, and enforces decisions.

The hardest practical issue is that users do not speak in schemas. A user may
write:

```text
幫我處理一下 VPN，那個帳號好像又壞了，順便開單給 IT。
```

That single sentence may contain a read-only FAQ lookup, an account-status
question, a restricted identity-access request, a ticket draft request, and a
possible side-effect ticket submission. A gateway classifier therefore should
not be treated as a single-label component that returns only `vpn_issue`.
Production-grade extraction is closer to:

```text
multi-label classification
+ action decomposition
+ slot extraction
+ risk classification
+ ambiguity detection
+ recommended next step
```

The user interface can stay natural-language-first, but the internal gateway
must be policy-first:

```text
free text prompt
-> action candidates
-> slot filling
-> risk scoring
-> schema validation
-> policy decision
-> execute, draft, confirm, clarify, deny, or review
```

The gateway should not do:

```text
user prompt -> LLM judgment -> direct tool execution
```

Common action extraction methods:

| Method | Best fit | Control needed |
|---|---|---|
| UI controlled fields | Stable workflows with clear choices | Keep them optional where possible; treat client fields as hints unless produced by trusted server-side code |
| Rules | High-precision phrases such as delete, send, reset, export, staff-only, salary, diagnosis | Use rules as risk signals, not as the only understanding engine |
| Traditional classifier | High-volume repeated task categories with labeled examples | Prefer multi-label probabilities; track confidence and fallback paths |
| Transformer classifier | Semantic variants and enterprise intent categories | Use sigmoid multi-label outputs for mixed intent; measure false positives and false negatives |
| LLM structured output | Complex natural-language intent, slot extraction, and action proposal | Validate JSON schema; retry, clarify, review, or deny on invalid output |
| Embedding retrieval over action registry | Constraining possible tools before planner output | Retrieve known tools only; do not let the model invent authority |
| Workflow planner / graph | Multi-step agent workflows | Pause before sensitive tools and preserve state for human review |

The engineering rule is:

```text
LLM proposes.
Schema validates.
Policy engine decides.
Tool broker enforces.
Audit log records.
```

For beginner implementations, the classifier output should include at least:

```text
intent labels
action candidates
risk labels
required and missing slots
ambiguity signals
recommended next step
```

For the VPN example above, a strong gateway may produce:

```json
{
  "actions": [
    {
      "action_type": "search_vpn_faq",
      "risk_level": "read_only",
      "confidence": 0.91,
      "missing_slots": []
    },
    {
      "action_type": "check_account_status",
      "risk_level": "restricted",
      "confidence": 0.62,
      "missing_slots": ["account_id"]
    },
    {
      "action_type": "create_ticket_draft",
      "risk_level": "draft",
      "confidence": 0.84,
      "missing_slots": ["affected_user", "error_message", "device_type"]
    },
    {
      "action_type": "submit_ticket",
      "risk_level": "side_effect",
      "confidence": 0.55,
      "missing_slots": ["explicit_submit_confirmation"]
    }
  ],
  "recommended_next_step": "answer_vpn_faq_create_draft_and_ask_minimal_clarification"
}
```

The UI should translate this into a compact action preview, not a long form:

```text
我可以先查 VPN troubleshooting，並建立 IT ticket 草稿。
要查帳號狀態或送出 ticket 前，我會先請你確認。
```

This is the UX principle:

```text
Natural-language-first interface.
Policy-first execution.
Low risk + high confidence -> execute.
Low risk + low confidence -> ask one clarifying question.
High risk + high confidence -> preview and confirm.
High risk + low confidence -> clarify, deny, or escalate.
```

## Gateway Types

Real systems usually combine several gateway responsibilities:

| Gateway type | Examples | Main responsibility | Does not solve alone |
|---|---|---|---|
| API gateway | AWS API Gateway, Kong, Apigee, NGINX, Envoy, Azure API Management | HTTP routing, auth integration, rate limits, quotas, logs | LLM action extraction, RAG ACL drift, tool side effects |
| AI / LLM gateway | Cloudflare AI Gateway, LiteLLM, Portkey, Kong AI Gateway | Model routing, provider abstraction, fallback, cache, cost and token tracking, LLM observability | Business authorization and human review policy |
| Model serving engine, adjacent data plane | vLLM, SGLang, TensorRT-LLM, TGI | Load model weights, manage batching, KV cache, GPU inference, streaming, and OpenAI-compatible model endpoints | User authorization, RAG source policy, tool approval, audit ownership, and business workflow |
| Tool gateway / broker | MCP gateway, function-calling proxy, internal tool service | Tool schema validation, permission, side-effect controls, timeout, approval, audit | User identity and data-source policy by itself |
| Policy gateway / PDP | OPA, Casbin, Cedar / Amazon Verified Permissions, Cerbos | Centralized allow/deny/review_required decision | HTTP serving, tool execution, retrieval, or model inference |

AI Gateway is the AI request control plane that composes these boundaries.

## Hard Practical Problems

| Pain point | Why it is hard | Practical control |
|---|---|---|
| Free-text ambiguity | One message can mix read-only lookup, restricted retrieval, and side-effect requests | Hybrid UI hints, rules/classifier/LLM structured output, schema validation, confidence fallback |
| Ambiguous action extraction | A prompt such as "處理 VPN，帳號好像壞了，順便開單" can imply FAQ search, restricted account lookup, ticket draft, and ticket submission at once | Multi-label classification, action decomposition, slot extraction, risk scoring, minimal clarification, and per-action policy decisions |
| UX friction from structured inputs | Full forms reduce ambiguity but can make users feel blocked before they explain the problem | Natural-language-first input, optional smart chips, action preview, ask only missing required slots, confirm only side effects |
| RAG ACL drift | Source permissions change after documents are indexed | Metadata sync, retrieval-time permission checks, source IDs and document versions in audit |
| Side-effect tool risk | Agents can create tickets, send email, update records, or trigger external workflows | Tool registry, dry-run preview, idempotency key, approval gate, tool audit |
| Policy drift / privilege creep | Roles, groups, vendors, temporary staff, and service accounts change over time | Policy-as-code, versioning, authorization regression tests, periodic access reviews |
| Audit gaps | Final prompt/answer logs do not reconstruct the lifecycle | Trace IDs, policy IDs, source IDs, tool decisions, guardrail results, review states |
| Cost, latency, and UX trade-off | Safer flows add checks and review; faster flows can bypass controls | Risk-tiered automation, cache, budget limits, model routing, review only for high-risk actions |
| Serving/gateway confusion | Teams expose vLLM or SGLang as if it were the enterprise gateway | Put serving engines behind backend/gateway; enforce auth, policy, quota, and audit before model calls |
| KV cache, OOM, and latency variance | Long RAG prompts, many concurrent users, streaming, and JSON extraction stress prefill, decode, and GPU memory differently | Benchmark real prompt distributions; track TTFT, TPOT, queue length, cache hit rate, GPU memory, and failed requests |
| Serverless retry and timeout behavior | Functions, clients, and queues may retry work or fail halfway through a side-effect action | Idempotency keys, job state, DLQ, timeout budgets, durable audit/event records |
| Log privacy | Serverless logs are easy to emit but can accidentally store raw prompts, tokens, PII, or secrets | Structured logs, field allowlist, redaction, hashed user IDs, separate audit records |
| Hosting model mismatch | Teams put long-lived gateway core, streaming sessions, or GPU inference into short-lived functions | Hybrid design: containers/K8s for core services and inference; serverless for event edges |
| Localhost misconception | Students think a local web server is automatically serverless | Teach emulator vs self-hosted serverless platform vs plain local backend process |

## Request Lifecycle

```text
1. Client sends HTTP request with JSON body.
2. Gateway route receives request and calls handler.
3. Handler creates trace ID and authenticates caller.
4. Gateway resolves role, permission, tenant, agent scope, and server-side policy data.
5. Gateway validates schema and normalizes free text/client hints into structured actions.
6. Gateway classifies task and action risk.
7. Policy engine returns allow, deny, or review_required.
8. Gateway selects agent and skill.
9. RAG / KB / SQL access is filtered by metadata and policy before context.
10. Agent requests tools through tool broker.
11. Tool broker validates schema, permission, timeout, side effects, and review need.
12. Model router sends allowed context to a hosted model API or serving engine
    such as vLLM/SGLang; model response is generated from allowed context.
13. Output guardrail checks safety, citation, and data boundary.
14. Audit event records request, tools, sources, policy, guardrail, review, and outcome.
15. Gateway returns HTTP status plus JSON response or review status.
```

## Minimum Viable Output

- Mermaid or text diagram of the gateway.
- Table of components and responsibilities.
- One example request lifecycle for a sales-coaching or report-writing agent.
- One list of required logs.

## Validation Checklist

- [ ] The design identifies HTTP method, route, JSON body, response status, and error paths.
- [ ] The design says whether the trusted handler runs in a server, API gateway, or serverless API boundary.
- [ ] The design distinguishes cloud hosting from serverless API.
- [ ] The design says whether localhost use is emulation, a serverless-like platform, or a normal local backend server.
- [ ] The design separates short synchronous gateway work from long asynchronous AI jobs.
- [ ] The design uses a hybrid hosting model when AI Gateway core, streaming, or GPU inference would not fit serverless.
- [ ] The design treats vLLM/SGLang as model-serving engines behind the gateway, not as the enterprise policy boundary.
- [ ] Model-serving evidence includes endpoint/model version plus latency, token, queue, cache, GPU memory, or failed-request metrics where relevant.
- [ ] Side-effect actions have idempotency or duplicate-prevention behavior.
- [ ] Free text and selected-list/form inputs are normalized into structured actions/resources.
- [ ] Client-provided hints are separated from trusted server-side identity, role, permission, policy, and tool scope.
- [ ] Browser-provided role, permission, risk class, and allowed tools are not trusted.
- [ ] At least one OWASP idea and one NIST/ABAC idea are mapped to concrete gateway controls.
- [ ] Action extraction method and fallback are named.
- [ ] API gateway, AI/LLM gateway, tool broker, and policy engine responsibilities are separated.
- [ ] Every tool call passes through a broker.
- [ ] Every data source has a permission boundary.
- [ ] Every agent is registered with owner, scope, and allowed tools.
- [ ] Every request produces an audit event.
- [ ] Logs and audit records avoid raw tokens, secrets, and unnecessary PII.
- [ ] Memory scope is explicit.
- [ ] Human review path is defined for high-risk outputs.
- [ ] Evaluation hooks exist for safety, correctness, and latency.

## Linked Modules And Labs

- `modules/07-ai-gateway-agent-governance/`
- `modules/09-security-red-teaming/`
- `modules/10-enterprise-delivery-fae/`
- `labs/ai-gateway/`

## Next Implementation Gate

Build a minimal AI Gateway mock that accepts one task request, routes it to one
agent, verifies a token, resolves trusted identity/role/permission, validates
schema, extracts structured actions, checks one policy, calls one typed
read-only tool, routes one side-effect tool to review, and writes one audit
event.
