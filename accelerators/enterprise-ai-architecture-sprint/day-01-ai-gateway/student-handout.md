# Student Handout: AI Gateway Architecture Evidence

This is the summarized Day 1 handout. It keeps the full chapter structure of
the detailed handout, but each section is reduced to the first-principle idea
students need before the worksheet.

For deeper examples, protocol details, and extended comparisons, use
`student-handout-detailed.md`.

## 1. First Conclusion

A working LLM demo is not yet an enterprise AI system.

An enterprise AI system must make every AI request governable, reviewable, and
traceable. The architecture must show who sent the request, what they can
access, which agent may act, which data and tools are allowed, which controls
run before and after the model call, what needs human review, and what audit
record proves the lifecycle later.

Day 1 is therefore an evidence exercise. You are not proving that a model can
reply. You are proving that the system can control the request.

## 2. Read The AI Request Before The Architecture

Before drawing boxes, read one AI interaction as a system request:

```text
Client
-> HTTP request
-> backend route
-> handler
-> policy / retrieval / tool / model workflow
-> audit log
-> HTTP response
-> Client
```

The first-principle question is:

```text
What must the system know, decide, do, record, and return for this request?
```

### 2.1 HTTP Request And Response

An HTTP request is the client asking the server to do something. In an AI
Gateway, the request is not only the user message. It should also connect to
identity, role, requested action, allowed tools, risk class, source metadata,
and a `trace_id`.

Example request:

```http
POST /ai/chat
Authorization: Bearer demo-user-token
Content-Type: application/json

{
  "message": "I cannot log in to VPN. Please find the setup steps."
}
```

HTTP is useful because browsers, mobile apps, backend services, bots, webhooks,
load balancers, firewalls, API gateways, IAM systems, and logging systems
already understand it.

The beginner model is:

```text
HTTP request  = one AI task entering the system
AI Gateway    = the control entrypoint that checks, routes, governs, and logs it
HTTP response = the result, denial, error, or review status returned to the client
```

Common gateway status meanings:

| Status | Gateway meaning |
|---:|---|
| 200 | Request completed or review status returned |
| 400 | Request body or schema is malformed |
| 401 | Login/session/token is missing or invalid |
| 403 | User is authenticated but lacks permission |
| 404 | Route or resource is not found |
| 429 | Rate limit is reached |
| 500 | Backend, model, retrieval, or tool service failed |

### 2.2 JSON Object And Schema

JSON is a common API data format. A JSON object is a key-value structure:

```json
{
  "user_id": "student_001",
  "role": "student",
  "message": "I cannot log in to VPN"
}
```

A schema is the expected shape of that JSON. Schema validation is a control:
it lets the gateway reject incomplete, malformed, or unsafe requests before
they reach an agent, tool, or model.

The first principle is:

```text
If the system cannot inspect the fields, it cannot reliably govern the action.
```

### 2.2.1 Free Text, Selected Lists, And Hybrid Requests

Users often prefer free text because it feels natural:

```text
I cannot log in to VPN. If it still fails, help me create an IT ticket.
```

Governed systems prefer structure because policy needs fields:

```text
category = vpn
requested_action = create_ticket
urgency = medium
```

The strongest beginner design is hybrid:

```text
free_text = user explanation
controlled_fields = category, requested_action, channel, urgency
server_resolved_fields = identity, role, permission, allowed_tools, policy
```

Client-provided fields are useful hints. They are not trusted authority. The
gateway resolves identity, permission, tool access, and policy from trusted
server-side sources such as verified tokens, identity providers, permission
databases, agent registries, and policy engines.

### 2.2.2 Serverless API Boundary

A serverless API is a backend handler that runs as a managed function instead
of a long-running server process. "Serverless" means the platform manages the
runtime, scaling, routing, and execution environment. It does not remove backend
responsibility.

The gateway boundary still exists:

```text
Client
-> HTTP request
-> API Gateway / Vercel Function / Cloudflare Worker
-> trusted handler code
-> response
```

Serverless can host lightweight gateway routes, webhooks, scheduled jobs,
notifications, and event-driven automation. It still needs token validation,
authorization, schema validation, durable state, secret handling, idempotency,
observability, and audit logging.

#### Localhost, Emulators, And Serverless-Like Platforms

Localhost is a development environment. It helps you test logic on your own
machine, but it is not the production trust boundary.

Emulators simulate cloud behavior locally. They are useful for testing, but
students must still identify what the real deployment platform will enforce.

Serverless-like platforms such as OpenFaaS or Knative can run function-style
workloads on infrastructure you manage. The design question remains the same:

```text
Where is the trusted handler, and which controls does it enforce?
```

#### Minimal Serverless AI Gateway Shape

A minimal serverless gateway route should:

1. Receive the HTTP request.
2. Verify authentication.
3. Resolve trusted user context.
4. Validate the request schema.
5. Normalize the requested action.
6. Evaluate policy.
7. Call retrieval, tool, model, or review workflow only when allowed.
8. Write an audit event.
9. Return a response, denial, error, or review status.

The function is small, but the responsibility is real.

#### Synchronous And Asynchronous APIs

Synchronous APIs return the result in the same request/response cycle. They fit
short interactions such as a quick answer or a validation result.

Asynchronous APIs accept work, return a job or review status, and finish later.
They fit long-running work, human review, batch processing, external ticketing,
or workflows with side effects.

The architecture should show which path each action uses.

#### Idempotency

Idempotency means retrying the same request should not accidentally create the
same side effect twice.

This matters for AI Gateway because tool calls can create tickets, send
messages, update records, or trigger workflows. A gateway should use request
IDs, action IDs, or idempotency keys for side-effecting actions.

#### Security And Observability

Security controls decide what the request may do. Observability controls prove
what happened.

At minimum, the gateway should record:

- `trace_id`
- user or service identity
- route and action
- policy decision
- selected agent, tool, model, and source IDs
- risk class and review status
- latency, errors, and final response status

#### Real-World Flow: AI Intake Summary

An intake summary flow may read a user's description, classify the issue,
retrieve allowed knowledge, draft a summary, and route it for review.

The first-principle control is that the summary is not trusted because it sounds
fluent. It is trusted only when the system can show source permissions, review
status, audit trail, and claim-evidence alignment.

#### Real-World Flow: Webhook Receiver

A webhook receiver accepts events from another system. For AI Gateway design,
that event is still a request.

The receiver must verify source authenticity, validate schema, map the event to
an allowed action, enforce policy, process or queue the work, and log the
result.

#### When Serverless Is A Poor Fit

Serverless is less suitable for long-running inference, large model hosting,
heavy GPU workloads, persistent low-latency sessions, or workflows that need
fine control over runtime state.

Use serverless where the function boundary helps: event handling, lightweight
API routes, glue automation, scheduled jobs, and review notifications.

#### Cloud Hosting Vs Serverless In Enterprise AI

Cloud hosting is the broader category: containers, virtual machines,
Kubernetes, managed databases, managed queues, object storage, model APIs, and
serverless functions can all be part of cloud hosting.

Enterprise AI systems are often hybrid:

```text
core gateway / inference / long-running services
-> containers, Kubernetes, managed services, or dedicated model serving

event-driven edges / webhooks / scheduled jobs / notifications
-> serverless functions
```

The design goal is not to choose one hosting style everywhere. The goal is to
place each workload behind the right reliability, security, cost, and audit
boundary.

### 2.2.3 How Free Text Becomes Actions

Free text becomes system action through normalization.

The gateway or agent workflow should extract:

- actor
- task
- requested action
- resource
- environment
- risk class
- confidence
- fallback or review path

Common strategies include rules, classifiers, LLM structured outputs, and
workflow planners. Rules are predictable for narrow cases. Classifiers help
route known categories. LLM structured outputs help map flexible language into
schemas. Workflow planners can coordinate multi-step actions, but need strong
policy, tool, and review controls.

The first principle is:

```text
Natural language can start the interaction.
Structured action contracts must govern execution.
```

#### UI Hints Without Annoying Users

Good UX can help governance without forcing users into rigid forms.

Examples:

- suggest categories while the user types
- preview the interpreted action before execution
- ask one clarifying question when confidence is low
- require confirmation before side effects
- show review status for high-risk actions

The user can speak naturally, but the system must execute deliberately.

### 2.3 Route, Handler, And Log

A route maps a URL and method to backend code:

```text
POST /ai/chat -> chat_handler()
```

A handler performs the controlled work: validation, policy, retrieval, tool
calls, model calls, review routing, response construction, and audit logging.

A log records what happened. Good logs allow a reviewer to reconstruct the
request lifecycle after the fact.

### 2.4 Login, Role, Permission

Authentication answers:

```text
Who is this caller?
```

Authorization answers:

```text
What is this caller allowed to do?
```

A role is a grouping such as `student`, `staff`, `admin`, or `auditor`.
Permission is the actual allowed operation, such as reading a knowledge article,
creating a ticket, approving an action, or viewing audit records.

Being logged in is not enough. A logged-in user can still receive `deny` or
`review_required` if the requested action exceeds their permission or risk
scope.

### 2.5 LLM, RAG, API, And Database

The LLM generates or transforms language. RAG retrieves relevant knowledge.
APIs and tools perform controlled actions. Databases store identity, policy,
metadata, tickets, documents, audit logs, and system state.

The gateway coordinates these pieces. It should not let the model become the
source of permission, policy, or audit truth.

#### 2.5.1 Model Serving: vLLM And SGLang

vLLM and SGLang are model-serving engines. They load model weights and serve
inference requests efficiently.

They belong in the inference data plane:

```text
AI Gateway
-> policy / routing / quota / audit / review controls
-> model-serving engine such as vLLM or SGLang
-> generated output
-> gateway checks and response
```

The gateway remains the control plane. Model serving helps produce outputs; it
does not replace identity, authorization, quota, audit, source filtering, or
human review.

## 3. AI System Formula

Use this formula for Day 1:

```text
AI system =
user request
+ trusted identity
+ policy decision
+ allowed data
+ allowed tools
+ model or agent workflow
+ guardrails
+ human review when needed
+ audit evidence
```

An enterprise-deliverable AI system is this formula packaged so another person
can review, operate, validate, and improve it.

## 4. Why AI Gateway Exists

AI Gateway exists because enterprise AI requests need a control plane.

The gateway reduces practical engineering pain:

| Pain | Gateway control |
|---|---|
| Unknown caller | authentication and identity resolution |
| Permission bypass | authorization and policy evaluation |
| RAG leaks | source filtering before context construction |
| Tool abuse | tool broker, schemas, allowlists, review gates |
| Prompt injection | input/output checks and scoped tool access |
| Cost blowup | quotas, routing, rate limits, model selection |
| Missing evidence | trace IDs, audit logs, lifecycle records |
| Risky actions | human review and approval workflow |

The gateway is not only a proxy. It is where identity, policy, routing,
retrieval, tools, guardrails, audit, and review meet.

## 5. Core Terms

| Term | First-principle meaning |
|---|---|
| AI Gateway | Control entrypoint for AI requests |
| Agent | Workflow component that plans or performs bounded tasks |
| Tool | API action the system can call under policy |
| RAG | Retrieval of allowed knowledge before or during generation |
| Policy | Rule or decision logic for allow, deny, or review |
| Guardrail | Control that checks input, output, tool use, or risk |
| Human review | Approval path for actions that exceed automatic scope |
| Audit log | Durable evidence of request lifecycle and decisions |
| Trace ID | Identifier linking logs and events for one request |
| Model serving | Infrastructure that runs inference for a model |

## 6. Main Scenario: Campus IT Helpdesk Assistant

Design for a public-safe campus IT assistant.

The user may ask for help with VPN, MFA, password reset, Wi-Fi, account access,
or ticket creation. The system may retrieve approved help articles, summarize
steps, classify the request, draft a ticket, and route high-risk actions to
staff review.

The scenario is intentionally simple. Its purpose is to make the control
boundaries visible:

```text
student request
-> identity and role
-> allowed knowledge
-> ticket tool rules
-> review threshold
-> audit record
```

## 7. Minimum Architecture Diagram

Your diagram must include:

- client
- AI Gateway route and handler
- identity provider or token verification
- policy engine or policy database
- agent or workflow layer
- retrieval/data source boundary
- tool broker/API boundary
- model or model-serving boundary
- guardrail checks
- human-review path
- audit log

The diagram should show control flow, not just product names.

## 8. Request Lifecycle Template

Write a 10-15 step lifecycle. A good lifecycle usually includes:

1. Client sends request with message and token.
2. Gateway receives route and assigns `trace_id`.
3. Gateway verifies token.
4. Gateway resolves user, role, and permissions from trusted sources.
5. Gateway validates JSON schema.
6. Gateway normalizes intent, action, resource, and risk.
7. Policy returns `allow`, `deny`, or `review_required`.
8. Gateway retrieves only allowed sources.
9. Agent prepares bounded plan or tool call.
10. Tool broker validates schema and side-effect scope.
11. Model or model server generates output.
12. Guardrails check output and source alignment.
13. Human review runs if required.
14. Gateway writes audit event.
15. Gateway returns answer, denial, error, or review status.

## 9. Risk-Control Map Template

Map each risk to a concrete system control.

| Risk | Control |
|---|---|
| Prompt injection | scoped retrieval, tool limits, output checks |
| PII leakage | data classification, source filtering, redaction |
| Tool abuse | tool broker, schemas, allowlists, review gates |
| Permission bypass | server-side authorization and deny-by-default policy |
| Action extraction failure | confidence threshold and clarification path |
| RAG ACL drift | permission-filtered retrieval and source metadata checks |
| Cost blowup | quotas, model routing, rate limits |
| Missing audit trail | trace ID, structured logs, durable audit events |

## 10. Key Rules To Remember

1. A model demo proves output; an AI system proves control.
2. Client fields are hints; server-side identity and policy are authority.
3. Natural language can start the request; structured contracts govern action.
4. RAG must filter by permission before building model context.
5. Tool calls are API actions and need schemas, policy, and audit.
6. Serverless still needs security, durable state, idempotency, and logs.
7. Model serving is not the same as AI Gateway.
8. Prompt-only governance is not enough for enterprise delivery.

## 11. Day 1 Submission

Submit four artifacts:

1. AI Gateway architecture diagram.
2. Component responsibility table.
3. Request lifecycle.
4. Risk-control map.

Your submission should make the system reviewable. A TA should be able to see
what the gateway controls, what each component owns, where human review enters,
and which audit evidence proves the request lifecycle.
