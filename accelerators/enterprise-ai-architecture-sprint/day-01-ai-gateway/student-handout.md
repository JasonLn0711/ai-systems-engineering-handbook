# Student Handout: AI Gateway Architecture Evidence

## 1. First Conclusion

A demo that calls an LLM API is not the same as an enterprise AI system.

A deliverable enterprise AI system must answer:

1. Who sent the request?
2. What can this user access?
3. Which agent is allowed to handle the task?
4. Which data sources can the agent retrieve?
5. Which tools can the agent call?
6. Which tool calls create side effects?
7. Which output checks run before the answer returns?
8. Which actions require human review?
9. Which audit record proves the request lifecycle later?

Day 1 is not about building a full backend. Day 1 is about producing
architecture evidence.

## 2. Read The AI Request Before The Architecture

Before drawing an AI Gateway, read one AI interaction as a system request.

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

### 2.1 HTTP Request And Response

An HTTP request is the client asking the server to do something. It usually has
a method, path, headers, and body:

```http
POST /ai/chat
Authorization: Bearer demo-user-token
Content-Type: application/json

{
  "message": "I cannot log in to VPN. Please find the setup steps."
}
```

In an AI Gateway, the request body is more than the user message. A real request
also carries user identity, role, requested agent, requested tools, task type,
metadata, and usually a `trace_id`.

AI Gateway commonly uses HTTP request/response because the gateway is a network
service entrypoint and control API. HTTP is the shared language of browsers,
mobile apps, backend services, Slack bots, webhooks, cloud load balancers,
enterprise network controls, security tools, and logging systems.

The gateway flow naturally matches HTTP:

```text
Client / Web App / Mobile App / Slack Bot
-> HTTP Request
-> AI Gateway
-> Policy / Agent / Tool / RAG / Model
-> HTTP Response
-> Client
```

HTTP is useful for AI Gateway design because it provides:

- a common integration boundary for many clients
- `Authorization` headers for identity and token checks
- method and route information for routing
- status codes for success, malformed input, missing login, denied access,
  rate limit, and service failure
- mature observability fields such as route, latency, status code, error, and
  `trace_id`
- compatibility with load balancers, reverse proxies, WAFs, firewalls, API
  gateways, IAM, rate limits, TLS, and service mesh tools

This does not mean every internal gateway connection must be simple
request/response HTTP. Production systems may also use HTTP streaming or SSE
for token streaming, WebSocket for realtime voice or agent sessions, gRPC for
internal service-to-service calls, queues for asynchronous work, event streams
for audit and monitoring, and database/model-server/MCP connections behind the
gateway.

The beginner mental model is:

```text
HTTP request  = one AI task entering the system
AI Gateway    = the control entrypoint that checks, authorizes, routes, and logs it
HTTP response = the result, denial reason, error, or review status returned to the client
```

An HTTP response is what the server returns. It usually has a status code,
headers, and a body:

```http
200 OK
Content-Type: application/json

{
  "answer": "Start by checking MFA, VPN client version, and account status.",
  "sources": ["vpn-guide-2026-01"],
  "ticket_status": "pending_review"
}
```

Common status codes are:

| Status | Meaning in gateway design |
|---:|---|
| 200 | Request completed or review status returned successfully |
| 400 | JSON body or schema is malformed |
| 401 | Login/session/token is missing or invalid |
| 403 | User is authenticated but lacks permission |
| 404 | Requested resource or route is not found |
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

JSON can contain strings, numbers, booleans, arrays, nested objects, and `null`.
AI Gateway contracts use JSON so the system can inspect fields such as role,
task type, requested tools, risk class, policy decision, source IDs, and audit
status.

Schema is the expected shape of the JSON. For example, a ticket tool may require
`title`, `description`, and `priority`. If an agent sends only
`{"text": "open a ticket"}`, the tool broker should reject it because the
contract is incomplete.

### 2.2.1 Free Text, Selected Lists, And Hybrid Requests

Students and staff may submit requests in three common ways.

Free-text chat is natural for users:

```text
I cannot log in to VPN. Please find the setup steps. If it still fails,
help me create an IT ticket.
```

This is flexible, but unstable for policy because one sentence can contain
knowledge retrieval, ticket creation, PII, and a side-effect request.

Selected lists or forms are easier to govern:

```text
category = vpn
requested_action = create_ticket
urgency = medium
```

This is structured, but less flexible. Real users often describe issues that do
not fit cleanly into one menu option.

The strongest beginner design is hybrid:

```text
free text:
"I cannot log in to VPN. If it still fails, create a ticket."

controlled fields:
category = vpn
requested_action = create_ticket
channel = student_portal
```

Client-provided fields are useful hints, but they are not final truth. The
gateway should resolve identity, role, permission, allowed tools, agent scope,
and policy rules from trusted server-side sources such as the token, identity
provider, permission database, agent registry, and policy database.

This is not only an AI design preference. It is the normal web security model.
OWASP is not a law or government regulation; it is a widely used application
security community that publishes guidelines, verification standards, cheat
sheets, and risk lists. For gateway design, the important OWASP lesson is:
client-side checks can improve UX, but the authorization decision must be made
in trusted server-side code, at a gateway, or in a serverless function. The
default posture should be deny-by-default: if the system cannot prove that the
caller may access a resource or run a tool, it should not allow it.

NIST gives the same idea in a more formal control language. NIST SP 800-53
access-control controls describe enforcing approved authorizations and least
privilege. NIST SP 800-162 describes ABAC, where a policy decision considers:

```text
subject     = user / service / agent identity
object      = document / database row / ticket / email / tool
operation   = read / create / update / send / approve
environment = tenant / time / network / channel / risk_class
```

That maps directly to AI Gateway policy input. A student request is not only a
message; it is a subject asking to perform operations on objects under a
specific environment.

The trusted identity flow usually looks like this:

```text
1. Client sends Authorization: Bearer <token>.
2. Gateway verifies token signature and expiration.
3. Gateway checks issuer and audience.
4. Gateway reads subject/user_id from verified token claims.
5. Gateway queries identity provider or user database for role/group.
6. Gateway queries permission database or policy engine.
7. Gateway ignores client-provided role, permission, risk_class, and allowed_tools.
8. Gateway evaluates allow / deny / review_required per action.
```

OIDC ID Tokens and JWTs are common ways to carry authentication claims, but the
gateway still has to verify them before trusting their content.

Serverless API means the gateway handler can run as a function instead of a
long-running server process. "Serverless" does not mean "there is no server."
It means the cloud platform manages the server process, runtime startup,
scaling, isolation, routing, and execution environment for you.

The HTTP boundary still exists:

```text
Client
-> HTTP request
-> API Gateway / Vercel Function / Cloudflare Worker
-> gateway handler code
-> response
```

Traditional backend hosting and serverless API hosting are different ways to
run the same backend responsibility:

```text
Traditional server:
Client
-> HTTP request
-> Load Balancer / Nginx
-> long-running backend server
-> route handler
-> database / external service
-> response

Serverless API:
Client
-> HTTP request
-> API Gateway / Edge Route / Function URL
-> function invocation
-> handler code
-> database / queue / external service
-> response
```

In AWS terms, Amazon API Gateway can publish and secure HTTP, REST, and
WebSocket APIs, then route requests to services such as AWS Lambda. Lambda can
be exposed through API Gateway so the function receives an HTTP request event
and returns an HTTP response. Vercel Functions and Cloudflare Workers follow
the same teaching model: a request invokes function code managed by the
platform.

Serverless does not remove the backend or the security responsibility. The
function still has to verify tokens, resolve permissions, validate schema,
evaluate policy, broker tools, write audit logs, and return clear status.
Examples:

```text
AWS:
Student Portal -> Amazon API Gateway -> Lambda authorizer / Lambda handler
-> policy table or OPA -> model/RAG/tool -> DynamoDB or RDS audit table

Vercel:
Next.js frontend -> /api/gateway -> Vercel Function
-> Auth.js / Clerk / Auth0 session check -> Prisma/Postgres policy/audit

Cloudflare:
Browser -> Cloudflare Worker
-> JWT or Cloudflare Access check -> Workers AI / external provider
-> D1 / KV / Vectorize / external audit store
```

### 2.2.2 Serverless API Boundary

For Day 1, treat serverless API as a hosting pattern for the trusted gateway
handler.

The complete request lifecycle is:

```text
1. Client sends HTTP request.
2. DNS, TLS, CDN, or edge network receives traffic.
3. API Gateway, route handler, or function URL matches method and path.
4. Authentication checks who is calling.
5. Authorization checks whether the caller can perform the action.
6. Rate limit or quota checks protect the system and cost.
7. Request validation checks headers, query parameters, and JSON body.
8. Platform converts the HTTP request into a function event.
9. Function runtime starts or reuses an execution environment.
10. Handler runs gateway logic.
11. Handler calls database, queue, object storage, RAG, model, or tool APIs.
12. Handler returns response body, headers, and status code.
13. Platform records logs, metrics, traces, and audit events.
```

Beginner terms:

| Term | Meaning |
|---|---|
| API | Contract that lets systems communicate |
| Endpoint | Callable URL such as `/gateway/requests` |
| Route | Method and path such as `POST /gateway/requests` |
| Handler | Code that processes the request |
| Function invocation | One execution of serverless handler code |
| Runtime | Language environment such as Python, Node.js, Go, or Java |
| Cold start | Extra startup time when the platform creates a fresh execution environment |
| Warm start | Faster invocation when the platform can reuse an existing environment |
| Stateless | Handler should not rely on local memory or local files for durable state |

The most important engineering rule is:

```text
Serverless changes the hosting model.
It does not change the trust model.
```

Serverless API is not the same as "put the backend server on the cloud." That
is cloud hosting.

```text
Cloud hosting:
You rent cloud compute and run a long-lived backend process such as FastAPI,
Express, Django, Spring Boot, or a containerized service.

Serverless API:
You deploy handler code and configuration. When a request or event arrives, the
platform invokes the function in a managed execution environment.
```

In other words:

```text
Cloud hosting = your app server is always running somewhere you provision.
Serverless API = your handler runs when the platform invokes it.
```

This distinction matters because the word "serverless" is about ownership, not
physics. Servers still exist. Platform infrastructure still exists. The change
is that the application team does not manage a dedicated, always-running app
server process for that function.

The cloud provider view is closer to this:

```text
Platform infrastructure that exists continuously:
API Gateway / router / scheduler / runtime manager / container or microVM pool
logs / metrics / IAM / deployment control plane

Your project normally exists as:
function code + config + route mapping + IAM / policy + environment variables

When a request arrives:
platform selects or creates an execution environment
-> loads or reuses your function
-> runs the handler
-> returns the response
-> keeps the environment warm for possible reuse or recycles it later
```

AWS Lambda describes this as an execution environment lifecycle: init, invoke,
and shutdown, with the environment sometimes frozen and reused for later
invocations. That reuse is why a second request may be a warm start, while a
new environment has cold-start latency.

The precise mental model is:

```text
not "no server"
but "no server process that this team directly manages"

not "no backend"
but "backend execution unit = event-triggered function invocation"

not "nothing is always running"
but "the always-running layer belongs to the platform, not to your app server"
```

#### Localhost, Emulators, And Serverless-Like Platforms

Can you make a serverless API on localhost?

There are three levels.

First, you can simulate serverless locally. Tools such as AWS SAM local,
Serverless Framework offline, Vercel dev, Cloudflare Wrangler, and LocalStack
can emulate parts of the cloud request/event flow. This is useful for class
labs because students can test handler code without deploying every change.

Second, you can run a serverless-like platform on your own machine, private
server, or Kubernetes cluster. OpenFaaS can deploy functions to Kubernetes and
run them on-premises or in cloud environments. Knative is a Kubernetes-based
platform for serverless workloads; Knative Serving can route HTTP requests,
autoscale services, and scale to zero when idle.

Third, if you only run `localhost:8000` with FastAPI or Express and no function
platform, then it is not really serverless. It is a local backend server. It
may be small and local, but a process is still running and listening for
requests.

So the rule is:

```text
Local emulator = good for development, but it simulates cloud serverless.
OpenFaaS / Knative / similar = serverless-like platform you operate yourself.
Plain localhost web server = cloud hosting style, just on your laptop.
```

Serverless is "serverless" from the application developer's point of view. From
the platform operator's point of view, someone still manages routers,
schedulers, runtimes, containers, logs, metrics, security patches, and capacity.

The trusted handler must still do:

```text
verify token
resolve identity / role / permission server-side
validate request schema
normalize intent into structured actions
evaluate policy
enforce tool decisions
write audit events
protect secrets and logs
return explicit HTTP status or review state
```

Do not trust a browser payload like this:

```json
{
  "user_id": "student_001",
  "role": "admin",
  "requested_tool": "view_audit_log"
}
```

The frontend may send user intent and UI hints. The serverless handler must
derive the real identity and permissions from a verified session or token.

#### Minimal Serverless AI Gateway Shape

An AI Gateway hosted as serverless functions usually has these pieces:

```text
API layer:
- Amazon API Gateway, Vercel Route Handler, Cloudflare Worker, or Google API Gateway

Identity layer:
- Cognito, Auth0, Clerk, Auth.js, Cloudflare Access, or internal OIDC

Schema layer:
- Pydantic for Python
- Zod for TypeScript
- JSON Schema for cross-language contracts

Policy layer:
- policy table first
- OPA, Casbin, Cedar / Amazon Verified Permissions, or Cerbos later

State layer:
- DynamoDB, PostgreSQL, Supabase, Neon, D1, KV, R2, S3, or Redis

Async layer:
- SQS, Pub/Sub, Cloudflare Queues, Step Functions, Temporal, or a job table

Observability layer:
- structured logs, request_id, trace_id, metrics, audit table, OpenTelemetry
```

For a small class project, a good path is:

```text
FastAPI + Pydantic locally
-> same handler shape wrapped by Mangum for AWS Lambda
-> API Gateway HTTP API
-> DynamoDB or PostgreSQL audit table
-> optional SQS worker for long-running AI jobs
```

For a TypeScript web app:

```text
Next.js route handler
-> Vercel Function
-> Zod validation
-> Auth.js / Clerk / Auth0 session check
-> Postgres / Prisma audit table
```

For edge-oriented demos:

```text
Cloudflare Worker
-> Hono router
-> JWT or Cloudflare Access check
-> D1 / KV / R2 / Vectorize
-> Workers AI or external model provider
```

#### Synchronous And Asynchronous APIs

Not every task should finish inside one HTTP request.

Short control-plane tasks can be synchronous:

```text
POST /gateway/requests
-> validate
-> policy
-> short RAG search
-> short model call
-> response
```

Long jobs should usually be asynchronous:

```text
POST /v1/summary-jobs
-> validate request
-> create job_id
-> enqueue job
-> return 202 Accepted

worker:
-> read job from queue
-> run ASR / RAG / LLM / evaluation
-> save result

GET /v1/summary-jobs/{job_id}
-> return queued / running / completed / failed
```

This matters for AI systems because audio transcription, long document
processing, batch evaluation, and multi-step review workflows can exceed normal
HTTP timeout expectations. Queue-based design also makes retry and failure
handling easier to reason about.

#### Idempotency

Serverless and queue-based systems can retry work. A client may retry after a
timeout. A queue message may be delivered again. A worker may fail halfway.

Idempotency means:

```text
The same request can be retried without creating duplicate side effects.
```

For side-effect tools such as `create_ticket`, `send_email`, `charge_card`, or
`update_record`, use an idempotency key:

```http
POST /gateway/tool-calls
Idempotency-Key: ticket-req-0001
```

The backend stores:

```text
idempotency_key
request_hash
status: processing | completed | failed
response_body
expires_at
```

If the same key appears again, the gateway returns the previous result instead
of creating a duplicate ticket or sending a duplicate email.

#### Security And Observability

A serverless AI Gateway still needs the same security controls as a traditional
backend:

```text
Authentication: who is calling?
Authorization: may this caller do this action?
Object-level authorization: may this caller access this ticket/file/session?
Input validation: does JSON match the schema?
Output filtering: are sensitive fields removed?
Least privilege IAM: can this function access only needed resources?
Secret management: are API keys outside source code?
Rate limiting: can one user create cost or abuse spikes?
Audit logging: can we reconstruct who did what?
PII redaction: do logs avoid leaking sensitive text?
```

Observability should include:

```json
{
  "trace_id": "req-0001",
  "route": "POST /gateway/requests",
  "user_id_hash": "sha256:...",
  "role": "student",
  "status_code": 200,
  "latency_ms": 142,
  "policy_decision": "review_required",
  "tool_decisions": ["search_it_faq:allow", "create_it_ticket:review_required"],
  "retrieved_source_ids": ["vpn-guide-2026-01"],
  "audit_event_id": "audit-0001"
}
```

Do not log raw access tokens, API keys, full medical records, full customer
profiles, or unnecessary PII. Good logs make the system explainable. Bad logs
become a data leak.

#### Real-World Flow: AI Intake Summary

Suppose a clinic wants a kiosk that collects patient symptoms and prepares a
staff-review summary. The API should not be named `POST /diagnose`, because the
system is not making final clinical decisions. A better API surface is:

```text
POST /v1/intake-sessions
POST /v1/intake-sessions/{session_id}/answers
POST /v1/intake-sessions/{session_id}/summary-jobs
GET  /v1/intake-sessions/{session_id}/staff-review-summary
```

The production-style serverless flow is:

```text
1. Patient mobile app calls POST /v1/intake-sessions.
2. API Gateway invokes a function handler.
3. Handler validates schema and creates a session record.
4. Patient submits answers.
5. Handler checks session ownership and stores answers.
6. Patient or staff requests summary generation.
7. Handler enqueues a summary job and returns 202 Accepted with job_id.
8. Worker function reads the queue.
9. Worker loads allowed session fields, not the whole medical database.
10. Worker calls an LLM gateway to draft a staff-review summary.
11. Guardrail checks unsupported diagnosis or unsafe wording.
12. Worker saves the summary and audit event.
13. Staff dashboard reads the summary after authorization.
```

This design separates user-facing latency from long AI work. It also keeps the
AI output inside a staff-review workflow instead of pretending the model is a
doctor.

#### Real-World Flow: Webhook Receiver

Serverless APIs are also common for webhooks. For example, a payment, GitHub,
LINE, Slack, form, or ticketing system may call your API:

```text
External service
-> POST /v1/webhooks/ticket-system
-> verify signature
-> check idempotency
-> enqueue event
-> return 200 quickly
```

The important idea is:

```text
Webhook received does not mean business processing is complete.
Webhook received means the event was authenticated, deduplicated, stored,
and queued for processing.
```

This prevents external services from retrying because your handler was busy
calling an LLM or waiting for a slow database operation.

#### When Serverless Is A Poor Fit

Serverless API is useful for gateway entrypoints, policy checks, webhook
receivers, audit writes, short RAG calls, and job creation. It is often a poor
fit for:

```text
very long synchronous jobs
large always-warm in-memory models
GPU inference that needs model weights kept resident
heavy local filesystem state
special non-HTTP network protocols
very large dependency packages
workloads where cold start is unacceptable
downstream databases that cannot handle bursty connections
```

For enterprise AI, a mature design is usually hybrid:

```text
Serverless API = entrypoint and control plane
Queue / workflow = long-running coordination
Container / Kubernetes / managed inference endpoint = heavy compute or GPU
Database / object storage = durable state
Observability / audit = evidence and operations
```

#### Cloud Hosting Vs Serverless In Enterprise AI

Enterprise teams usually do not choose only one. They use both.

Cloud hosting usually means VMs, containers, managed container services, or
Kubernetes running long-lived services. Serverless usually means functions,
event handlers, and managed platform invocations.

First-principles comparison:

| Question | Serverless API is usually better when | Cloud hosting / containers are usually better when |
|---|---|---|
| Traffic | Low, spiky, or unpredictable | High, steady, or very high volume |
| Workload | Event-driven, short, stateless | Long-running, stateful, streaming, or always warm |
| Team size | Small team, MVP, PoC, internal automation | Larger team with platform / SRE / DevOps ownership |
| Cost model | Pay-per-use is cheaper at low volume | Reserved capacity is cheaper at sustained high volume |
| Control | Platform defaults are acceptable | CPU, RAM, GPU, network, runtime, and latency need tighter control |
| Portability | Vendor lock-in is acceptable for speed | Multi-cloud, on-prem, private network, or customer deployment matters |
| AI fit | Webhooks, file intake, job triggers, audit events, notifications | AI Gateway core, streaming, memory service, agent runtime, GPU inference |

The cost intuition:

```text
Serverless = like paying per ride.
Cloud hosting = like owning or leasing capacity.

Low request volume:
serverless often wins because idle time costs little or nothing.

High steady volume:
containers or VMs often win because you pay for capacity, not every invocation.
```

This is why large companies still run many core systems on Kubernetes,
containers, or dedicated services. Serverless is not "new equals better."
Serverless is better for a certain class of workload.

For AI systems, the split is especially important. A simple webhook or file
upload trigger is a good serverless job:

```text
PDF upload
-> serverless handler validates request
-> enqueue processing job
-> return 202 Accepted
-> worker / GPU service performs OCR, embedding, RAG indexing, or evaluation
```

But core AI inference usually needs a different shape:

```text
Load balancer / API Gateway
-> containerized AI Gateway
-> agent service / policy service / memory service / tool service
-> GPU inference cluster or managed model endpoint
-> PostgreSQL / Redis / object storage / vector database
```

The mature enterprise pattern is:

```text
Cloud hosting / containers:
- core backend
- AI Gateway core
- agent registry
- tool registry
- policy service
- memory service
- streaming / WebSocket sessions
- GPU inference
- high-volume internal services

Serverless API:
- webhooks
- event processing
- file upload intake
- scheduled jobs
- background job triggers
- notification handlers
- lightweight policy or audit extensions
- internal automation tools
```

For the Day 1 AI Gateway architecture, a practical recommendation is:

```text
Use Kubernetes / containers / managed services for the stable enterprise AI
control plane.

Use serverless functions around the edges for event-driven automation,
webhooks, job triggers, and small internal tools.
```

This is hybrid architecture. It is common because cloud hosting and serverless
solve different workload problems.

A normalized gateway envelope should separate actor, task, actions, resources,
environment, and trace context:

```json
{
  "trace_id": "req-0001",
  "channel": "student_portal",
  "actor": {
    "user_id": "student_001",
    "role": "student",
    "permissions": ["read_public_faq", "request_ticket_creation"]
  },
  "task": {
    "raw_message": "I cannot log in to VPN. If it still fails, create a ticket.",
    "task_type": "helpdesk_question",
    "category": "vpn",
    "risk_class": "medium"
  },
  "requested_actions": [
    {
      "action_type": "retrieve_knowledge",
      "resource": "it_public_faq",
      "tool_name": "search_it_faq",
      "side_effect": false
    },
    {
      "action_type": "create_ticket",
      "resource": "ticket_system",
      "tool_name": "create_it_ticket",
      "side_effect": true
    }
  ],
  "environment": {
    "ip_range": "campus_network"
  }
}
```

The rule is:

```text
Human input may be natural language.
Gateway decisions require structured data.
The LLM may help propose intent, but it must not replace the policy engine.
```

### 2.2.3 How Free Text Becomes Actions

The gateway can use an LLM to help split free text into actions, but the LLM is
only one part of the planner. A reliable production design is usually hybrid:

```text
raw text
-> input validation / PII or prompt-injection checks
-> intent classification
-> slot extraction
-> action proposal
-> canonical action mapping
-> schema validation
-> policy evaluation
-> tool broker enforcement
-> audit log
```

There are five common approaches:

| Method | Good fit | Weakness |
|---|---|---|
| UI controlled fields | stable internal workflows | less flexible for users |
| rule-based parser | phrases such as "open ticket" or "send email" | brittle for varied language |
| traditional classifier | repeated categories such as IT, billing, HR | needs labeled examples |
| LLM structured output | flexible action extraction and slot filling | must be validated and policy-checked |
| workflow planner / graph | multi-step processes and human review | more state and failure handling |

Example:

```text
User:
I cannot log in to VPN. If it still fails, create an IT ticket.
```

Action proposal:

```json
{
  "task_type": "helpdesk_question",
  "category": "vpn",
  "actions": [
    {
      "action_type": "retrieve_knowledge",
      "tool_name": "search_it_faq",
      "resource": "public_it_faq",
      "side_effect": false
    },
    {
      "action_type": "create_ticket",
      "tool_name": "create_it_ticket",
      "resource": "ticket_system",
      "side_effect": true
    }
  ]
}
```

The LLM may generate this JSON through structured output or tool-calling
schemas. The gateway must still validate that the JSON matches the schema,
map tool names to a known tool registry, classify side effects, run policy, and
write audit evidence. Prompt injection is one reason for this separation:
malicious input or retrieved documents can try to make the model bypass safety
controls or trigger unauthorized tools.

### 2.3 Route, Handler, And Log

A backend route maps a method and URL path to a server function:

```text
POST /gateway/requests
GET /gateway/audit/:trace_id
POST /gateway/tool-calls
```

The handler is the code behind the route. A gateway handler usually creates a
trace ID, authenticates the user, checks policy, selects an agent, filters
retrieval, brokers tool calls, checks guardrails, writes audit evidence, and
returns a response.

A log is lifecycle evidence. A useful AI Gateway audit log records fields such
as `trace_id`, `user_id`, `role`, `agent_id`, `policy_decision`,
`requested_tools`, `allowed_tools`, `denied_tools`, `retrieved_source_ids`,
`model_version`, `guardrail_result`, `human_review_status`, and outcome.

### 2.4 Login, Role, Permission

Login answers: "Who are you?" This is authentication.

Authorization answers: "Can you do this action on this resource?"

User identity is the specific person, account, or service making the request.
Role is the category or responsibility assigned to that identity. Permission is
the concrete allowed action.

```json
{
  "user_id": "student_001",
  "email": "student001@example.edu",
  "role": "student"
}
```

Here, `user_id` and `email` identify who is making the request. `role` tells the
gateway what kind of user this identity is.

```text
Identity answers: Who is making this request?
Role answers: What kind of user is this person?
Permission answers: What concrete action can this user perform?
```

Role is a coarse access category such as `student`, `staff`, `admin`, or
`compliance_officer`. Permission is the concrete allowed action, such as
`read_public_faq`, `read_staff_sop`, `create_ticket`, `query_database`, or
`view_audit_log`.

Example:

```text
Jason logs in.
System confirms identity: Jason, user_id = jason_001.

Then the system checks role:
role = student.

Because role = student:
- can read public IT FAQ
- can request ticket creation
- cannot read staff-only SOP
- cannot approve admin actions
```

Enterprise AI policy decisions usually need three outcomes:

```text
allow
deny
review_required
```

This matters because a logged-in student may be allowed to read public VPN FAQ
documents, denied from staff-only SOPs, and routed to review when a ticket
submission would create an external side effect.

The decision pipeline is:

```text
1. Authenticate.
2. Resolve identity, role, and permission server-side.
3. Validate request schema.
4. Normalize user intent into actions, resources, and tools.
5. Classify task and risk.
6. Resolve allowed resources and tools.
7. Evaluate policy.
8. Return allow, deny, or review_required.
9. Execute allowed actions.
10. Queue review_required actions.
11. Write audit log.
```

A practical access-control SOP for a new AI Gateway feature is:

```text
Before launch:
1. List roles: student, staff, admin, reviewer.
2. List data sources and mark access_level, owner, tenant, and document version.
3. List tools and mark read-only or side-effect.
4. Define required input schema for each tool.
5. Define policy table or policy-as-code rules.
6. Define audit fields and retention boundary.
7. Write authorization tests for allow, deny, and review_required.

At runtime:
1. Verify token and resolve identity server-side.
2. Ignore client-provided role, permission, risk_class, and allowed_tools.
3. Normalize requested actions.
4. Evaluate policy per action.
5. Execute allowed actions, block denied actions, queue review_required actions.
6. Write audit event with trace_id, policy_id, source IDs, and tool decisions.

After launch:
1. Review permissions regularly to avoid privilege creep.
2. Version policy changes.
3. Reconstruct incidents from trace_id and audit events.
4. Add regression tests for any authorization bug found in production.
```

Typical decision rules:

| Decision | When it fits | Example |
|---|---|---|
| allow | authenticated user, sufficient permission, allowed data/tool, valid schema, low risk | student searches public VPN FAQ |
| deny | missing login, insufficient role, forbidden resource/tool, attempted privilege bypass | student asks for staff-only SOP |
| review_required | side effect, external communication, sensitive output, high-risk task, low confidence, human approval needed | student requests ticket creation |

Review is not a failure. It is a normal control point for high-risk automation.

The common mistake is thinking "logged in" means "allowed." It does not. A user
can be correctly identified and still be blocked:

```text
Identity check:
Yes, this is student_001.

Permission check:
student_001 has role=student, so staff-only documents are not allowed.

Decision:
deny
```

In enterprise AI systems, audit logs usually record both identity and role:

```json
{
  "trace_id": "req-0001",
  "user_id": "student_001",
  "role": "student",
  "requested_tool": "create_ticket",
  "policy_decision": "review_required"
}
```

For gateway design:

```text
identity tells us who to audit
role helps decide policy
permission decides whether an action is allowed, denied, or sent to review_required
```

Automation should be a state machine, not a model-only judgment:

```text
received
-> authenticated
-> schema_validated
-> intent_normalized
-> policy_checked
-> retrieval_allowed
-> tool_proposed
-> tool_decision_made
-> model_generated
-> guardrail_checked
-> completed / denied / pending_review
-> audit_written
```

The division of labor is:

```text
LLM proposes action.
Gateway validates action.
Policy engine decides allow / deny / review_required.
Tool broker enforces the decision.
Audit log records the evidence.
```

### 2.5 LLM, RAG, API, And Database

An LLM generates or transforms language. It is an inference component, not a
governance layer.

#### 2.5.1 Model Serving: vLLM And SGLang

When students hear "run an LLM", they often imagine one Python script that
loads a model and calls `model.generate()`. That is useful for learning, but it
is not the same as production serving.

For example, a research script may look like this:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct")

inputs = tokenizer("Explain what an API is.", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0]))
```

This is fine for a single user and a small experiment. It is weak for a real
service because real traffic looks more like this:

```text
09:00:00 user A sends a 200-token prompt
09:00:01 user B sends a 5,000-token RAG prompt
09:00:02 user C wants streaming output
09:00:02 user D wants JSON output
09:00:03 user E starts a multi-turn agent workflow
09:00:04 user F sends a long-context document question
```

A serving system must manage:

```text
many concurrent requests
batching so the GPU does not sit idle
KV cache memory
streaming responses
time to first token
time per output token
model loading and versioning
quantization
multi-GPU parallelism
OOM prevention
metrics and logs
Docker / Kubernetes deployment
OpenAI-compatible APIs
```

This is where **vLLM** and **SGLang** fit.

```text
model weights = the learned neural network parameters
vLLM / SGLang = inference serving engines that run the weights efficiently
AI Gateway = control plane for auth, policy, routing, quota, audit, and review
```

So the beginner mental model is:

```text
vLLM / SGLang are usually data-plane serving engines.
AI Gateway is the control plane in front of them.
```

They do not train the model. They do not replace the backend. They do not
replace the AI Gateway. They make model inference fast enough and stable enough
to be called by a backend, RAG system, agent workflow, or gateway.

##### LLM Inference Lifecycle

One request to a model server usually goes through this flow:

```text
user request
-> HTTP API server receives request
-> tokenizer converts text into tokens
-> prefill: model reads the prompt and builds KV cache
-> decode: model generates one token at a time
-> detokenizer converts output tokens back into text
-> server streams or returns the response
```

Two phases matter most:

```text
prefill = process the full input prompt
decode  = generate new tokens one by one
```

Prefill is often compute-intensive. If the prompt contains 8,000 tokens of RAG
context, the model must first process those 8,000 tokens.

Decode is often memory-intensive. The model generates one next token, then
another, then another. Each step uses the previous context through cached
attention data.

This is why long prompts, long answers, streaming, and many concurrent users
stress a model server differently. A good serving engine has to schedule both
prefill and decode well.

##### KV Cache

KV cache is the key concept behind LLM serving performance.

Transformer attention uses Query, Key, and Value vectors. When the model has
already processed previous tokens, it can store their Key and Value vectors
instead of recomputing them every time it generates the next token.

Simplified:

```text
prompt tokens:
[What] [is] [an] [API]

model stores:
K cache = key vectors for previous tokens
V cache = value vectors for previous tokens
```

When the model generates the next token, it reuses the KV cache.

The challenge is that KV cache can become huge:

```text
user A: 200 tokens
user B: 8,000 tokens
user C: 1,500 tokens
user D: 32,000 tokens
```

If GPU memory is managed poorly, the system gets fragmentation, low batch size,
slow throughput, and out-of-memory errors.

##### vLLM

vLLM is a high-performance LLM inference and serving engine. Its most direct
student mental model is:

```text
Hugging Face model weights
-> vLLM engine
-> OpenAI-compatible API server
-> backend / RAG / agent / app
```

vLLM is a strong first tool for learning local or private LLM serving because it
makes the "model as API server" idea concrete.

Typical start command:

```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct
```

Then an app can call the local vLLM server with an OpenAI-compatible client:

```python
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-1.5B-Instruct",
    messages=[
        {"role": "user", "content": "請用大二資工學生能理解的方式解釋 API。"}
    ],
    temperature=0.2,
    max_tokens=512,
)

print(response.choices[0].message.content)
```

The important detail is `base_url`. The code uses the OpenAI Python SDK shape,
but the request goes to the local vLLM server, not necessarily to OpenAI's cloud.

vLLM is known for:

```text
PagedAttention
continuous batching
chunked prefill
prefix caching
OpenAI-compatible API server
streaming output
quantization support
tensor / pipeline / data / expert parallelism
multi-LoRA support
structured outputs and tool-calling support
many Hugging Face model architectures
```

PagedAttention is the classic vLLM idea. It treats KV cache memory more like
operating-system paging: instead of requiring one large continuous memory block
per request, it can manage KV cache in smaller blocks. That helps reduce waste
and fragmentation, which allows more useful batching on the GPU.

Use vLLM first when:

```text
you want to serve Qwen / Llama / Gemma / Mistral / DeepSeek-style models
you need an OpenAI-compatible local API
you are building a RAG backend or internal chatbot
you want streaming
you want a mature general-purpose serving engine
you are learning model serving for the first time
```

##### SGLang

SGLang is also a high-performance serving framework for large language models
and multimodal models. Its beginner mental model is:

```text
vLLM = high-performance general model server
SGLang = high-performance serving runtime that also focuses strongly on
         structured generation, prefix reuse, and complex LLM workflows
```

SGLang is attractive when the workload is not just "ask the model once", but
looks like a language-model program:

```text
1. read a long shared system prompt
2. extract structured fields
3. call or propose tools
4. generate JSON
5. reuse long prompt prefixes across many requests
6. run many similar agent / RAG / extraction workflows
```

SGLang is known for:

```text
RadixAttention and prefix caching
structured outputs with JSON schema / regex / EBNF
OpenAI-compatible APIs
native generation APIs
continuous batching
paged attention
chunked prefill
prefill/decode disaggregation
multi-GPU parallelism
quantization
multi-LoRA batching
Prometheus production metrics
```

Typical start command:

```bash
python3 -m sglang.launch_server \
  --model-path qwen/qwen2.5-0.5b-instruct \
  --host 0.0.0.0 \
  --port 30000
```

Then call it with an OpenAI-compatible API:

```bash
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen/qwen2.5-0.5b-instruct",
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }'
```

SGLang's RadixAttention focuses on reusing common prompt prefixes. That matters
because enterprise prompts often repeat large blocks:

```text
shared system prompt
+ policy rules
+ tool rules
+ response format instructions
+ user-specific message
```

If many requests share the same prefix, reusing the prefix KV cache can reduce
repeated prefill work.

SGLang's structured outputs matter when the backend needs reliable machine-
readable output. For example:

```json
{
  "risk_level": "critical",
  "need_human_review": true,
  "reason": "user reported money transfer and suspected fraud"
}
```

That is easier for a backend to validate with Pydantic or JSON Schema than a
free-form paragraph.

SGLang also documents prefill/decode disaggregation. The idea is that prefill
and decode have different bottlenecks, so large systems may split them into
different workers:

```text
client
-> router
-> prefill workers process long prompts and build KV cache
-> KV transfer
-> decode workers generate tokens
-> response
```

Students do not need to deploy this on Day 1. They only need to understand why
large LLM serving is a scheduling and memory-management problem, not only a
Python API problem.

##### vLLM Vs SGLang

| Question | vLLM | SGLang |
|---|---|---|
| Core identity | General high-performance LLM inference / serving engine | High-performance LLM / multimodal serving framework with strong workflow and structured-generation focus |
| First mental model | Turn Hugging Face model weights into an API server | Execute complex LLM workflows and structured generation efficiently |
| Signature ideas | PagedAttention, continuous batching, OpenAI-compatible serving | RadixAttention, prefix caching, structured outputs, PD disaggregation |
| Good first use | General chatbot, RAG backend, internal model API | JSON extraction, agent workflows, repeated prefixes, long-context workflows |
| Student starting point | Usually easier first | Better after serving basics are understood |
| Gateway replacement? | No | No |

Do not choose by brand. Choose by workload:

```text
If you need general model serving first:
start with vLLM.

If your workload has repeated prefixes, structured output, or complex agent
programs:
benchmark SGLang seriously.

If the system is important:
benchmark both with real prompt distributions.
```

##### Serving Metrics

Do not judge a serving engine by one manual prompt. Measure:

```text
TTFT  = time to first token
TPOT  = time per output token
E2E latency = full request latency
throughput = tokens/sec
request throughput = requests/sec
GPU memory usage
GPU utilization
queue length
cache hit rate
OOM / failed request rate
JSON validity rate for structured output
```

SGLang can expose Prometheus metrics such as prompt tokens, generation tokens,
token usage, cache hit rate, time to first token, running requests, queue
requests, and generation throughput. vLLM also has production metrics and
observability docs. The exact metric names can change by version, so a real
deployment should pin versions and document dashboards.

##### Relationship To AI Gateway

vLLM / SGLang usually sit behind the AI Gateway:

```text
Frontend / internal app
-> backend API
-> AI Gateway
   - auth
   - tenant / user / role
   - rate limit and quota
   - policy and guardrails
   - model routing
   - audit and cost tracking
-> serving layer
   - vLLM server for Qwen
   - vLLM server for Llama
   - SGLang server for structured extraction
   - SGLang server for agent workflow
-> GPU nodes
```

Do not expose vLLM or SGLang directly to a browser in an enterprise system.
They are not the full governance boundary. Put them behind the backend/gateway
and protect them inside a service network.

##### Real-World Example: Internal RAG Assistant

Example requirement:

```text
Employees ask questions about HR rules, IT SOPs, engineering docs, and security
procedures.
The system must cite sources.
The system must not retrieve unauthorized documents.
The system must stream the answer.
The system must record user, role, source IDs, model version, and latency.
```

Possible architecture:

```text
Web UI
-> FastAPI / NestJS backend
-> SSO / OAuth
-> permission filter
-> vector DB: Qdrant / Milvus / pgvector
-> RAG prompt construction
-> AI Gateway: LiteLLM or custom gateway
-> vLLM or SGLang
-> GPU
-> audit log + Prometheus/Grafana
```

vLLM or SGLang handles model inference. The backend and gateway handle identity,
retrieval permissions, policy, audit, quota, and review.

##### Real-World Example: Fraud Call Triage

Example requirement:

```text
ASR transcript enters the system.
LLM extracts fraud type, transferred amount, risk level, and review need.
Output must be JSON.
High-risk cases must go to human review.
```

Expected output shape:

```json
{
  "fraud_type": "fake_investment",
  "has_transferred_money": true,
  "amount_twd": 200000,
  "risk_level": "critical",
  "need_human_review": true,
  "evidence": [
    "caller reported transferring 200000 TWD",
    "caller mentioned an investment group"
  ]
}
```

SGLang is a strong candidate for this kind of structured-output workload. vLLM
can also support structured outputs, so the responsible engineering answer is
to test both with the actual transcripts, JSON schema, concurrency level, and
latency target.

##### Minimal Project Path

A first student project can be:

```text
client -> FastAPI -> vLLM -> model -> response
```

Folder:

```text
local-llm-api/
  app.py
  requirements.txt
  README.md
```

`requirements.txt`:

```text
fastapi
uvicorn
openai
pydantic
```

Start vLLM:

```bash
vllm serve Qwen/Qwen2.5-1.5B-Instruct \
  --host 0.0.0.0 \
  --port 8000
```

FastAPI backend:

```python
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

llm = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    response = llm.chat.completions.create(
        model="Qwen/Qwen2.5-1.5B-Instruct",
        messages=[
            {"role": "system", "content": "你是一位嚴謹的資工教學助理。"},
            {"role": "user", "content": req.message},
        ],
        temperature=0.2,
        max_tokens=512,
    )

    return {
        "answer": response.choices[0].message.content
    }
```

Run:

```bash
uvicorn app:app --reload --port 8080
```

Test:

```bash
curl http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "請解釋什麼是 KV cache"}'
```

Then add, in order:

```text
streaming
RAG
auth
rate limit
structured logs
Prometheus metrics
Docker Compose
Kubernetes deployment
AI Gateway routing
multiple model backends
fallback routing
```

##### Common Misunderstandings

| Misunderstanding | Correction |
|---|---|
| vLLM / SGLang are models | They are serving engines. Qwen, Llama, Gemma, DeepSeek, and Mistral are model families. |
| vLLM / SGLang are AI Gateways | They expose APIs, but they do not replace enterprise gateway governance. |
| If it runs once, it is production-ready | Production needs concurrency, latency, OOM, observability, security, rollback, and versioning tests. |
| Benchmarking one prompt is enough | Benchmark the real prompt distribution: short, long, RAG, streaming, JSON, agent, and multi-turn. |
| You must choose only one | A company may use vLLM for general chat and SGLang for structured extraction or prefix-heavy agent workloads. |

RAG retrieves relevant documents before generation. In an enterprise system,
retrieval must filter by permission and metadata before the model sees context:

```text
correct: role/permission filter -> allowed documents -> model context
weak: all matching documents -> model context -> prompt says "do not leak"
```

An API is a contract between systems. Tool calling is usually a controlled API
action, so the gateway must check tool existence, input schema, permission,
timeout, side effects, approval need, and audit logging.

A database stores evidence and operating state: users, roles, permissions,
documents, chunks, metadata, policies, audit events, review items, chat history,
and evaluation results. If the system must be governed later, the evidence must
be saved somewhere inspectable.

## 3. AI System Formula

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

| Part | Beginner explanation | Engineering evidence |
|---|---|---|
| model | The model that generates or classifies | endpoint, version, config |
| data | Documents, databases, KBs, audio, images | source IDs, metadata, access level |
| infrastructure | Runtime environment | Docker, K8s, VM, GPU, network |
| workflow | How a request becomes an outcome | lifecycle, approval flow |
| governance | Who can do what | RBAC, policy gate, registries |
| security | How the system protects boundaries | auth, masking, guardrails, audit |
| evaluation | How quality and safety are checked | tests, red-team cases, acceptance criteria |
| delivery | How the system is handed off | docs, runbook, review packet |

## 4. Why AI Gateway Exists

The simplest chatbot architecture is:

```text
User -> Web App -> LLM API -> Response
```

This is enough for a demo, but it does not answer enterprise questions:

- Can a student read staff-only documents?
- Can an agent submit a ticket without approval?
- Which source IDs supported the answer?
- Which policy decision allowed or blocked the request?
- Can an operator reconstruct the lifecycle later?

An AI Gateway is the control plane for AI requests:

```text
Client / Channel
-> AI Gateway
-> Auth / Identity
-> RBAC / Policy Gate
-> Agent Registry
-> Tool Broker
-> RAG / KB / SQL / MCP Connector
-> Model Router / Serving
-> Guardrail
-> Audit Log
-> Human Review when required
-> Response
```

Real systems often combine several gateway types:

| Gateway type | Examples | Primary job |
|---|---|---|
| API Gateway | AWS API Gateway, Kong Gateway, Apigee, NGINX, Envoy, Azure API Management | HTTP routing, authentication integration, rate limits, API logs |
| AI / LLM Gateway | Cloudflare AI Gateway, LiteLLM, Portkey, Kong AI Gateway | model routing, retries, fallbacks, caching, token/cost tracking |
| Tool Gateway / Broker | MCP gateway, internal tool broker, function-calling proxy | schema validation, side-effect control, approval workflow |
| Policy Gateway / PDP | OPA, Casbin, Cedar / Amazon Verified Permissions, Cerbos | allow / deny / review_required decisions from structured input |

The hardest practical pain points are making these controls work together:

| Pain point | Why it is hard | Practical control |
|---|---|---|
| Free text is ambiguous | one sentence may contain retrieval, side effect, and restricted data requests | hybrid UI hints + structured output + schema validation |
| RAG permissions drift | source systems, shares, tenants, and document versions change | metadata filtering before retrieval + source permission re-check |
| Side-effect tools are risky | agents can create tickets, send email, update records, or delete data | tool registry + tool broker + idempotency key + human review |
| Policy drift | roles and exceptions grow over time | policy-as-code, versioning, authorization tests, periodic access review |
| Audit gaps | teams log only prompt and answer | trace_id, source IDs, tool decisions, policy ID, guardrail result |
| Cost and latency | every extra check and model call adds delay and spend | risk-tiered automation, caching, fallbacks, smaller classifiers |
| UX friction | users dislike repeated approvals | allow low-risk actions, review only side effects/high-risk outputs |

The mature direction is layered control, not one magic gateway:

```text
API Gateway for HTTP traffic.
AI Gateway for model routing and observability.
Policy Engine for authorization decisions.
Tool Broker for action enforcement.
RAG Connector for source boundaries.
Guardrails for input/output/tool checks.
Human Review for high-risk decisions.
Audit / Observability for evidence.
Evaluation / red-team tests for regression control.
```

## 5. Core Terms

| Term | Beginner definition | Engineering meaning |
|---|---|---|
| AI Gateway | Unified AI request entrypoint | Controls routing, policy, tools, data, audit, guardrails |
| API Gateway | General HTTP/API traffic boundary | Handles routing, auth integration, rate limits, logs |
| AI / LLM Gateway | Model-provider control layer | Handles model routing, caching, fallback, spend, observability |
| Tool Gateway / Broker | Agent action enforcement point | Validates schema, side effects, approval, audit |
| Policy Gateway / Engine | Authorization decision point | Evaluates structured input against policy rules |
| Serverless API | HTTP API whose handler is hosted as a managed function | Changes hosting, not backend responsibility; still needs auth, policy, validation, state, idempotency, logs, and audit |
| Cloud Hosting | Cloud compute running a long-lived app server or container | Better for high-volume, long-running, streaming, or tightly controlled services |
| Local Serverless Emulator | Local tool that simulates serverless invocation | Useful for development, but not the same as the real cloud platform |
| Self-hosted Serverless-like Platform | OpenFaaS, Knative, or similar on infrastructure you operate | Gives serverless-style workflow while keeping platform responsibility local/on-prem |
| Hybrid Architecture | Mix of containers, Kubernetes, serverless, queues, databases, and observability | Common enterprise pattern because workloads differ |
| Auth / Identity | Verifies the caller | Produces trusted user context |
| User Identity | Specific person, account, or service | Determines who is audited |
| Role | Access category assigned to an identity | Helps policy decide user scope |
| Permission | Concrete action the identity can perform | Allows, denies, or routes an action to review_required |
| RBAC | Role-Based Access Control | Uses role to decide permissions |
| Policy Gate | Allows, denies, or routes to review_required | Enforces system rules outside the prompt |
| Agent Registry | Records available agents | Stores owner, scope, tools, data sources, risk class |
| Tool Broker | Mediates tool calls | Checks schema, timeout, permission, side effects, audit |
| RAG Connector | Retrieves allowed data | Filters by metadata and access level before model context |
| Model Router | Selects model endpoint | Manages model choice, version, latency, cost |
| Model Serving Engine | Runs model inference | vLLM/SGLang/hosted provider loads model or calls provider, batches requests, manages KV cache, and streams tokens |
| vLLM | Open-weight model serving engine | Common first tool for exposing Qwen/Llama/Gemma-style models through an OpenAI-compatible API |
| SGLang | Model serving framework for complex LLM workflows | Strong fit for structured output, prefix-heavy prompts, and agent/RAG serving patterns |
| KV Cache | Stored attention keys/values | Reduces repeated computation during token generation but consumes GPU memory |
| TTFT / TPOT | Serving latency metrics | Time to first token and time per output token |
| Guardrail | Checks input/output risk | Detects PII, unsafe output, unsupported claims |
| Audit Log | Request lifecycle evidence | Records user, agent, policy, sources, tools, outcome |
| Human Review | Workflow node for high-risk cases | Creates pending/approve/reject states |
| API Contract | Agreed input/output shape between systems | Method, path, JSON schema, status, errors |
| Authentication | Verifies who the caller is | Token, session, OAuth, SSO, or service identity |
| Authorization | Checks whether the caller may do the action | Role, permission, policy, resource scope |
| Database | Stores durable operating data and evidence | Identity, policy, metadata, audit, evaluation records |

## 6. Main Scenario: Campus IT Helpdesk Assistant

Public-safe scenario:

```text
A student asks:
"I cannot log in to VPN. Please find the setup steps. If it still fails,
help me create an IT ticket."
```

Important design facts:

- `search_it_faq` is read-only.
- `create_it_ticket` is a side-effect tool.
- Student role can read public IT FAQ documents.
- Staff-only SOPs must be filtered before retrieval.
- Ticket submission should require review, rate limit, or explicit workflow
  control.
- The audit event should record trace ID, user role, agent ID, source IDs, tool
  decisions, guardrail result, review state, and outcome.

## 7. Minimum Architecture Diagram

```mermaid
flowchart TD
    C[Client / Channel] --> G[AI Gateway]
    G --> I[Auth / Identity]
    I --> P[RBAC / Policy Gate]
    P --> AR[Agent Registry]
    AR --> TB[Tool Broker]
    AR --> DS[RAG / KB / SQL / MCP Connector]
    AR --> MR[Model Router / Serving]
    TB --> EXT[External Tool / Workflow]
    DS --> MR
    MR --> OG[Output Guardrail]
    OG --> AU[Audit Log]
    OG --> HR[Human Review]
    HR --> OUT[Response]
    AU --> OUT
```

## 8. Request Lifecycle Template

Write a lifecycle with 10-15 steps. A good lifecycle includes:

```text
1. Client sends POST /gateway/requests with a JSON body.
2. Gateway route receives the request and calls the handler.
3. Handler creates trace_id.
4. Gateway authenticates caller.
5. Gateway resolves trusted identity, role, permissions, and agent scope.
6. Gateway validates schema and normalizes free text/form hints into actions.
7. Gateway classifies task risk and evaluates policy.
8. Gateway selects an agent from registry.
9. Connector filters data by permission and metadata.
10. RAG returns allowed source IDs and active document versions.
11. Model generates response from allowed context.
12. Tool broker validates schema, permission, timeout, and side effects.
13. Review-required actions enter human review; denied actions are not executed.
14. Audit log records trace, policy, sources, tools, guardrail, review, outcome.
15. Server returns HTTP status plus JSON response or review status.
```

## 9. Risk-Control Map Template

| Risk | Example | System control | Evidence |
|---|---|---|---|
| Prompt injection | Malicious document asks model to ignore policy | Retrieval filter, instruction hierarchy, output guardrail | red-team test log |
| PII leakage | Phone or ID appears in output/log | PII detector, masking, log minimization | masked audit event |
| Tool abuse | Agent submits ticket automatically | Tool broker, schema validation, approval gate | tool decision log |
| Permission bypass | Student reads staff-only SOP | RBAC, metadata filtering before retrieval | policy decision log |
| Action extraction error | Free text is mapped to the wrong tool | schema validation, confidence threshold, review queue | normalized action record |
| RAG ACL drift | Permission changes in source system are not reflected in vector index | metadata sync, pre-retrieval filter, source re-check | source permission check log |
| Policy drift | roles gain exceptions over time | policy versioning, access review, authorization tests | policy test report |
| Cost / latency blowup | every request calls many models/tools | rate limits, caching, risk-tiered routing | gateway metrics |
| Missing audit trail | No source/tool/policy record | trace_id, source IDs, audit schema | complete audit event |

## 10. Key Rules To Remember

```text
Prompt is not a permission boundary.
Model output is not an audit trail.
Tool calling is not safe without a broker.
RAG is not safe without data and metadata boundaries.
Human review is a workflow node, not a final disclaimer.
```

## 11. Day 1 Submission

Submit one packet with:

1. Architecture diagram.
2. Component responsibility table.
3. Request lifecycle.
4. Risk-control map.
5. One paragraph explaining why prompt-only governance is insufficient.
