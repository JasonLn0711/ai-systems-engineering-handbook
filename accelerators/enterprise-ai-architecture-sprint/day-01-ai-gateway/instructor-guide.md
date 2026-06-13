# Instructor Guide: Day 1 AI Gateway Architecture

## Teaching Goal

Move students from model-centric thinking to system-centric AI architecture.
The lesson is successful when students can explain why a working chatbot demo is
not enough for enterprise delivery and can produce four reviewable artifacts.

## Pre-Class Diagnostic

Use these five questions before lecture or in the first 10 minutes:

1. What is the difference between an HTTP request and a response?
2. In a JSON object, where would you put `user_id`, `role`, and `message`?
3. What is a role, and why might `student` and `staff` have different access?
4. What should a log record if an API request fails?
5. What is an API route such as `POST /gateway/requests` used for?
6. Why is a browser-provided `role=admin` not trusted?
7. What does "serverless API" still have to do for authorization?

If many students miss questions 1-3, slow down during request lifecycle and
schema sections. If many miss questions 4-5, emphasize route, handler, audit,
and API contract before drawing the gateway.

Use these follow-up checks only when the room needs more grounding:

| Area | Check question | Expected baseline |
|---|---|---|
| Gateway boundary | Why do gateways commonly use HTTP? | HTTP is a common client/server API boundary with auth headers, routes, status codes, logs, and enterprise network support. |
| HTTP | What is the difference between `401` and `403`? | `401` means not authenticated; `403` means authenticated but not authorized. |
| JSON | Why is a tool call better represented as JSON than free text? | The broker can validate fields, types, and required arguments. |
| Input mode | Can the UI accept free text? | Yes, but the gateway must normalize it into structured actions/resources before policy. |
| OWASP / NIST | Is OWASP a law? | No. It is a security guideline and verification resource; NIST provides formal risk/control frameworks. |
| Serverless API | Does serverless mean no backend? | No. It means the trusted handler runs as a managed function; auth, policy, validation, state, idempotency, and audit still run there. |
| Action extraction | Can the LLM split a prompt into actions? | Yes, but the output must be schema-validated and policy-checked before execution. |
| Backend | What does a handler do after a route receives a request? | Reads body, checks identity/policy, calls services, writes log, returns response. |
| Identity | What is the difference between user identity and role? | Identity is the specific person/account/service; role is the access category assigned to it. |
| Authorization | Why does login not imply access to every document? | Authorization still checks role, permission, resource, and action. |
| RAG | Why filter before retrieval context reaches the model? | Staff-only or out-of-scope content should not enter model context. |
| API | What is an API contract? | Agreed method, route, schema, status, and error behavior. |
| Database | Why does the gateway need storage? | To preserve identity, policy, metadata, audit, review, and evaluation evidence. |

## Request-Contract Bridge

Before the gateway diagram, walk through one request:

```text
POST /gateway/requests
JSON body: raw_message, client_hints, requested_agent
server-side context: identity, role, permissions, policy, agent registry
handler: authenticate -> validate schema -> normalize intent -> classify risk -> authorize -> filter data -> broker tools -> log
response: 200, 400, 401, 403, 429, or 500 with a JSON body
```

Then add the standards bridge:

```text
OWASP is not law. It is engineering guidance.
NIST is a formal control and risk-management vocabulary.
AI Gateway turns those ideas into code:
deny-by-default, server-side authorization, least privilege, ABAC-style policy input, audit evidence.
```

For serverless, draw:

```text
Client -> API Gateway / Vercel Function / Cloudflare Worker -> trusted handler
trusted handler = verify token -> resolve role/permission -> validate schema -> policy -> broker tools -> audit
```

Make the distinction explicit:

```text
Serverless changes hosting:
- no self-managed long-running server process
- platform handles function invocation, runtime startup, routing, scaling

Serverless does not remove backend work:
- API contract
- authentication and authorization
- schema validation
- durable state
- queue / workflow for long AI jobs
- idempotency for side-effect actions
- observability and audit
```

Use one concrete flow before students start drawing:

```text
short request:
POST /gateway/requests -> function handler -> policy -> short RAG/model call -> response

long AI job:
POST /summary-jobs -> function handler -> enqueue job -> 202 Accepted
worker -> LLM / ASR / evaluation -> result store
GET /summary-jobs/{job_id} -> status/result
```

The teaching thesis is:

```text
AI Gateway is not "send prompt to model."
It is the lifecycle layer that makes each AI request verifiable, governable,
and traceable.
```

Clarify that HTTP is the external gateway boundary, not the model's essence.
Inside the gateway, streaming, WebSocket, gRPC, queues, event streams,
databases, model-server protocols, and MCP connectors may all appear. Day 1
starts with HTTP because it is the most teachable and inspectable API boundary.

## 180-Minute Flow

| Time | Activity | Goal | Instructor emphasis |
|---:|---|---|---|
| 0-15 min | Diagnostic and request-contract bridge | Surface existing mental models | HTTP/JSON/role/log are the entry vocabulary |
| 15-35 min | AI system formula | Model + data + infra + workflow + governance | AI system is a composed system |
| 35-60 min | Gateway mental model | Explain control plane | Gateway controls policy, tool, data, audit |
| 60-85 min | Request lifecycle | Walk from request to audit event | Ordering matters; filtering before retrieval |
| 85-110 min | Campus IT case | Ground concepts in familiar scenario | read-only tool vs side-effect tool |
| 110-145 min | Workshop | Students draft four artifacts | Push for component boundaries |
| 145-170 min | Peer review | Use checklist to find missing controls | Evidence, not decoration |
| 170-180 min | Wrap-up | Connect to Day 2 mock lab | Architecture becomes API contract |

## 150-Minute Flow

| Time | Activity | Goal |
|---:|---|---|
| 0-10 min | Diagnostic | Confirm HTTP/JSON/role/log assumptions |
| 10-30 min | Core frame | AI system formula and gateway boundary |
| 30-55 min | Components | identity, policy, agent, tool, RAG, model, guardrail, audit |
| 55-75 min | Lifecycle | Campus IT request to audit event |
| 75-115 min | Workshop | Students complete four artifacts |
| 115-140 min | Peer review | Use rubric and failure gallery |
| 140-150 min | Handoff | Day 2 minimal gateway mock |

## Blackboard Diagrams

Start with the oversimplified design:

```text
User -> Web App -> LLM -> Response
```

Then add system boundaries:

```text
User
-> Gateway
-> Identity
-> Policy
-> Agent
-> Data / Tool
-> Model
-> Guardrail
-> Audit
-> Response or Review
```

Then contrast tools:

```text
search_it_faq: read-only -> allow
create_it_ticket: side-effect -> review_required
```

Then contrast input modes:

```text
free text: natural for the user, unstable for policy
selected list/form: stable for policy, less flexible for the user
hybrid: free text + controlled fields -> normalized gateway envelope
```

Then contrast gateway types:

```text
API Gateway: HTTP traffic, auth integration, rate limits.
AI / LLM Gateway: model routing, fallback, cache, cost, observability.
Tool Broker: schema, side effects, approval, idempotency.
Policy Engine: allow / deny / review_required.
```

## Common Failure Gallery

Use these intentionally flawed designs for critique.

### Failure 1: Model-Only Flow

```text
User -> LLM -> Response
```

Missing controls:

- no identity
- no policy gate
- no data boundary
- no tool boundary
- no audit trail

Student critique prompt: "If the answer is wrong, what evidence can you inspect?"

### Failure 2: Tool Directly Executed

```text
User -> Agent -> create_it_ticket tool -> Ticket created
```

Missing controls:

- no tool broker
- no side-effect classification
- no approval gate
- no rate limit
- no tool decision log

Student critique prompt: "Who decided the ticket was allowed?"

### Failure 3: RAG Without Metadata Filtering

```text
User -> Vector Search -> All matching chunks -> LLM -> Response
```

Missing controls:

- no `access_level`
- no `document_version`
- no pre-retrieval permission filtering
- no source IDs in audit
- possible staff-only data in model context

Student critique prompt: "At which step should staff-only documents be removed?"

### Failure 4: Free Text Directly Drives Policy

```text
User free text -> LLM decides action -> Tool executes
```

Missing controls:

- no schema validation
- no intent normalization
- no action/resource split
- no risk classification
- no server-side policy decision
- no review queue for side effects

Student critique prompt: "Which structured fields should the gateway create before policy?"

### Failure 5: Client Hints Trusted As Truth

```text
Client sends role=admin -> Gateway trusts it -> Audit log access allowed
```

Missing controls:

- role and permission are trusted from the browser
- no server-side identity provider lookup
- no permission database or policy table
- no deny-by-default posture for unknown or tampered fields

Student critique prompt: "Which fields may come from the client, and which must be resolved server-side?"

### Failure 6: LLM Planner Executes Actions Directly

```text
User text -> LLM extracts create_ticket -> create_it_ticket runs
```

Missing controls:

- no canonical tool registry check
- no JSON schema validation
- no confidence or ambiguity handling
- no side-effect policy gate
- no human-review queue

Student critique prompt: "What can the LLM propose, and what must the gateway enforce?"

### Failure 7: Serverless Means No Backend

```text
Browser -> serverless function -> model provider
```

Missing controls:

- no token signature verification
- no server-side permission lookup
- no deny-by-default behavior
- no audit event
- no durable state for policy, audit, review, or job status
- no idempotency key for side-effect tools
- no queue or workflow for long-running AI work
- no timeout, secret, rate-limit, or log privacy plan

Student critique prompt: "Which backend controls still run inside the function, and which long-running work should move to a queue or workflow?"

## Instructor Questions

1. If a chatbot answer is wrong, how do we know which source IDs it used?
2. If an agent creates a ticket, who authorized it?
3. If a student should not read staff-only SOPs, where is that blocked?
4. If a retrieved document contains malicious instructions, which layer handles it?
5. If output contains PII, what happens before the response returns?
6. If a second agent is added, which governance rules can be reused?
7. Which controls can live in a prompt, and which must be enforced by the system?
8. Is human review a workflow node or a disclaimer?
9. Which field in the JSON request tells the gateway who the user is?
10. Which fields in the audit log let the operator reconstruct the lifecycle?
11. Which field is the specific identity, and which field is the role?
12. Why can a request be authenticated and still receive `deny`?
13. Which HTTP status or review state should the client see for missing login,
    forbidden access, malformed JSON, and side-effect review?
14. Which parts of a hybrid request are user hints, and which are trusted
    server-side facts?
15. Where does intent normalization happen before policy evaluation?
16. What state should a side-effect tool enter before a staff member approves it?
17. Which OWASP recommendation explains why client-side access control is not enough?
18. How does an ABAC policy input map subject, object, operation, and environment?
19. Which gateway type solves model fallback, and which gateway type solves tool side effects?
20. What is the most painful part of this design for users, and what is the most painful part for operators?
21. In a serverless API, which work should stay synchronous and which work should become a job?
22. Which side-effect actions need an idempotency key?
23. Which observability fields help debug a failed serverless invocation without leaking PII?

## Teaching Notes

- When students say "the prompt will prevent it," ask for the enforcing
  component and log evidence.
- When students draw a diagram without audit, ask how a TA would grade the
  system after a failure.
- When students put all data into the model context, ask whether permission was
  checked before or after retrieval.
- When students say "the agent calls a tool," ask whether the tool is read-only
  or side-effecting.
- When students confuse authentication and authorization, use the student/staff
  SOP example: login proves identity; permission decides access.
- When students describe logs as debug prints, ask which audit fields would
  prove source access, tool decisions, policy decisions, and review status.
- When students say "HTTP is for chatting with the model," redirect them:
  HTTP is the client-facing API boundary that makes identity, routing, status,
  logs, and enterprise controls inspectable.
- When students say "the LLM decides allow or deny," redirect them: the LLM may
  propose intent or draft tool arguments, but the policy engine decides
  `allow`, `deny`, or `review_required`, and the gateway/tool broker enforces.
- When students cite OWASP as "the law," redirect them: OWASP is a practical
  security guideline; NIST/ISO/EU AI Act provide broader control, management,
  and regulatory vocabularies depending on context.
- When students say "serverless has no server," redirect them: serverless still
  has trusted backend code; the platform manages the server process, but the
  team still owns API contracts, permissions, durable state, idempotency,
  secrets, logs, and audit.
- When students list only product gateways, ask what pain each gateway type
  actually controls: HTTP traffic, model routing, tool enforcement, or policy
  decision.
