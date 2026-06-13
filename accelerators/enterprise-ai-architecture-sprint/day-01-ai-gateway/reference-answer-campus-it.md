# Reference Answer: Campus IT Helpdesk Assistant

Audience: instructor and TA only. Do not give this to students before
submission.

## Scenario

A student asks:

```text
I cannot log in to VPN. Please find the setup steps. If it still fails,
help me create an IT ticket.
```

## Reference Request Contract

```http
POST /gateway/requests
Authorization: Bearer demo-student-session
Content-Type: application/json

{
  "trace_id": "req-0001",
  "channel": "student_portal",
  "raw_message": "I cannot log in to VPN. If it still fails, create an IT ticket.",
  "client_hints": {
    "category": "vpn",
    "requested_actions": ["search_faq", "create_ticket"],
    "urgency": "medium"
  },
  "requested_agent": "campus_it_helpdesk_agent"
}
```

Expected interpretation:

| Field | Reference reading |
|---|---|
| Method and route | `POST /gateway/requests` enters the gateway handler |
| Authentication | bearer/session token identifies the caller |
| User identity | `student_001` is the specific account to audit |
| Role | `student` is the access category used in policy checks |
| Authorization | `student` role can read public FAQ and cannot read staff-only SOP |
| Client hints | category/action/urgency help normalize intent but are not trusted as final policy facts |
| Read-only tool | `search_it_faq` can be allowed for public FAQ search |
| Side-effect tool | `create_it_ticket` should become `review_required` |
| Response status | `200` with `pending_review` is acceptable when the review item is created |
| Audit evidence | trace ID, role, policy decision, source IDs, tool decision, review status, outcome |
| OWASP mapping | client-side hints are UX aids; authorization is enforced server-side with deny-by-default |
| NIST mapping | subject=`student_001`, object=`public_it_faq` or `ticket_system`, operation=`retrieve` or `create`, environment=`student_portal` |
| Action extraction | hybrid UI hints plus structured-output planner propose actions; schema and policy validate them |

Normalized gateway action:

```json
{
  "trace_id": "req-0001",
  "actor": {
    "user_id": "student_001",
    "role": "student",
    "permissions": ["read_public_faq", "request_ticket_creation"]
  },
  "task": {
    "task_type": "helpdesk_question",
    "category": "vpn",
    "risk_class": "medium"
  },
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

Policy table:

| Role | Action | Resource | Decision |
|---|---|---|---|
| student | search_it_faq | public_it_faq | allow |
| student | read_staff_sop | staff_sop | deny |
| student | create_it_ticket | ticket_system | review_required |
| staff | create_it_ticket | ticket_system | allow |
| admin | view_audit_log | audit_db | allow |

Policy decision:

```json
{
  "trace_id": "req-0001",
  "decision": "review_required",
  "allowed_actions": [
    {
      "tool_name": "search_it_faq",
      "reason": "student can read public IT FAQ"
    }
  ],
  "review_actions": [
    {
      "tool_name": "create_it_ticket",
      "reason": "student can request ticket creation, but staff approval is required"
    }
  ],
  "denied_actions": []
}
```

Action extraction evidence:

| Input signal | Reference result |
|---|---|
| raw message mentions VPN | `category = vpn` |
| raw message asks for setup steps | `retrieve_knowledge` with `search_it_faq` |
| raw message asks to create ticket | `create_ticket` with `create_it_ticket` |
| UI hint says `urgency=medium` | accepted as a hint, not as final risk truth |
| tool registry marks `create_it_ticket.side_effect=true` | policy routes it to `review_required` for student |

Serverless implementation variant:

```text
Student portal
-> POST /gateway/requests
-> API Gateway / Vercel Function / Cloudflare Worker
-> token verification
-> permission and policy lookup
-> action normalization
-> tool broker / idempotency check / review queue
-> audit_events table
-> JSON response
```

The serverless function is still trusted backend code. It must not accept
browser-provided `role`, `permission`, `risk_class`, or `allowed_tools` as final
truth. If the student retries the same `create_it_ticket` request, the gateway
should use an idempotency key or review-item lookup so it does not create
duplicate ticket drafts.

Hybrid deployment note:

```text
campus AI Gateway core:
container / Kubernetes / managed service

edge automation:
serverless webhook handler, file-intake function, notification function,
scheduled audit-export trigger
```

This keeps the core gateway stable while using serverless for short event-driven
edges.

## Reference Architecture Diagram

```mermaid
flowchart TD
    C[Student Web App] --> G[AI Gateway]
    G --> T[Trace Context\ntrace_id=req-0001]
    T --> I[Auth / Identity\nstudent_001 role=student]
    I --> P[Policy Gate\nstudent policy]

    P -->|public docs allowed| AR[Agent Registry\ncampus_it_helpdesk_agent]
    P -->|staff-only docs denied| DENY[Denied Data Access]

    AR --> IG[Input Guardrail\nscope + injection + PII]
    IG --> RAG[RAG Connector\nfilter access_level=public]
    RAG --> FAQ[IT FAQ / VPN Guide\nsource_ids]
    FAQ --> MR[Model Router]
    MR --> MS[Model Serving Engine / Hosted Model API\nvLLM / SGLang / provider]

    IG --> TB[Tool Broker]
    TB -->|allow| SEARCH[search_it_faq]
    TB -->|review_required| REVIEW[create_it_ticket approval gate]

    MS --> OG[Output Guardrail\nPII + citation check]
    OG --> RB[Response Builder]
    REVIEW --> RB

    DENY --> AU[Audit Log]
    SEARCH --> AU
    REVIEW --> AU
    RB --> AU
    AU --> OUT[Student receives answer\n+ ticket pending status]
```

## Filled Component Table

| Component | Responsibility | Input | Output | Failure if missing |
|---|---|---|---|---|
| Student Web App | Sends the student request | message, session | gateway request | user source and channel risk are unclear |
| AI Gateway | Controls request lifecycle | request | routed calls, trace context | policy, tool, RAG, audit scatter across apps |
| Trace Context | Creates `trace_id` | request | `req-0001` | lifecycle cannot be reconstructed |
| Auth / Identity | Verifies student identity | session token | trusted user context | anonymous or spoofed requests enter |
| Policy Gate | Checks what student can do | identity, task, tool request | allow/deny/review_required | student may read staff-only SOP or create tickets directly |
| Agent Registry | Selects scoped IT agent | task type | `campus_it_helpdesk_agent` | owner and allowed tools are unclear |
| Input Guardrail | Checks input risk | user message | pass/block/review | prompt injection or PII can proceed |
| RAG Connector | Retrieves allowed documents | query, role, metadata | public VPN guide chunks | staff-only docs can enter model context |
| Tool Broker | Mediates tool calls | tool request | allow/deny/review_required | agent can create many tickets directly |
| Model Router | Selects endpoint | allowed context, task | model endpoint and config | model choice, cost, version, latency are unmanaged |
| Model Serving Engine / Hosted Model API | Runs inference through hosted API or engines such as vLLM/SGLang | allowed prompt/context, model config | model response and serving metrics | model server becomes confused with policy/audit boundary; latency, OOM, queue, and cache failures are invisible |
| Output Guardrail | Checks answer | model output | pass/review/block | PII or unsupported content can return |
| Human Review | Reviews `create_it_ticket` | review item | approve/edit/reject/pending | side effects depend only on model judgment |
| Audit Log | Records evidence | lifecycle events | audit record | no debug, audit, or acceptance evidence |

## Reference Lifecycle

1. Student Web App receives the VPN request.
2. Web App sends `POST /gateway/requests` with raw message, client hints,
   session token, and requested agent to AI Gateway.
3. AI Gateway creates `trace_id = req-0001`.
4. Auth / Identity validates session and emits trusted user context:
   identity=`student_001`, role=`student`.
5. Gateway validates request schema and treats client hints as hints, not
   final authority.
6. Intent normalizer converts the raw message into `retrieve_knowledge` and
   `create_ticket`; risk classifier marks ticket creation as side-effecting.
7. Policy Gate allows public IT docs, denies staff-only SOPs, and requires
   review for ticket submission.
8. Agent Registry selects `campus_it_helpdesk_agent`.
9. Input Guardrail checks injection, PII, and task scope.
10. RAG Connector filters by `role=student` and `access_level=public`.
11. RAG Connector returns source IDs such as `vpn-guide-2026-01`.
12. Model Router sends allowed context and question to a hosted model API or
    serving engine such as vLLM/SGLang, and records model/version/latency
    context for audit and operations.
13. Model drafts VPN troubleshooting steps and a ticket draft.
14. Tool Broker classifies `create_it_ticket` as side-effecting and creates a
    human-review item.
15. Output Guardrail checks PII, staff-only content, unsafe claims, and source
    references; Audit Log records identity, policy decision, sources, tools,
    guardrail, review, and outcome; Response returns VPN steps plus ticket
    pending status as JSON.

Review queue item:

```json
{
  "review_id": "review-0001",
  "trace_id": "req-0001",
  "action": "create_it_ticket",
  "proposed_args": {
    "title": "VPN login failure",
    "description": "Student reports inability to login to VPN",
    "priority": "medium"
  },
  "reviewer_role": "it_staff",
  "status": "pending_review",
  "available_actions": ["approve", "edit", "reject"]
}
```

## Reference Risk-Control Map

| Risk | Example | Control | Evidence |
|---|---|---|---|
| Permission bypass | student accesses staff-only account-lock SOP | RBAC + metadata filtering before retrieval | policy log denies staff-only; RAG result only public |
| Tool abuse | agent creates ticket automatically | Tool Broker + approval gate + rate limit | tool decision log: `create_it_ticket = review_required` |
| Action extraction error | planner maps "find setup steps" to ticket creation only | schema validation + action preview + confidence threshold | normalized action record reviewed |
| RAG ACL drift | staff-only document remains in vector index after permission change | metadata sync + pre-retrieval permission filter + source re-check | retrieval filter log |
| Policy drift | student role gradually gains exception rules | policy versioning + regression tests + periodic access review | policy test report |
| Cost / latency blowup | each request calls classifier, planner, retriever, and large model | risk-tiered routing + caching + rate limits | gateway metrics |
| UX friction | every ticket request asks for repeated approval | only side effects enter review; read-only answers return immediately | review queue metrics |
| Missing audit trail | no record of cited documents | trace_id + source IDs + audit event | audit event contains source IDs |
| Prompt injection | FAQ chunk asks model to ignore policy | document treated as data, instruction hierarchy, output guardrail | malicious chunk test blocked or ignored |
| PII leakage | ticket content contains phone or private email | PII detector + masking + log minimization | masked audit record |
| Stale document | outdated VPN settings cited | version metadata + active filter | source version checked in RAG result |
| Wrong review path | ticket should be reviewed but is sent | side-effect policy requires review | human review item created |
| Model serving overload | long VPN troubleshooting context and many users increase TTFT or OOM risk | model routing, prompt budget, queue limits, serving metrics | latency, token, queue, cache, GPU memory, and failure metrics |
| Serving engine mistaken for gateway | vLLM/SGLang endpoint exposed directly to the app | place serving behind gateway; enforce auth, policy, quota, and audit before model call | audit event ties identity, policy, sources, and model endpoint |

## Instructor Notes

Passing answers show:

- Gateway is more than a proxy.
- OWASP/NIST ideas are translated into concrete server-side authorization,
  deny-by-default, least privilege, and ABAC-style policy inputs.
- Data filtering occurs before model context construction.
- Tool Broker separates read-only and side-effect tools.
- Action extraction is a proposal step, not an execution decision.
- Serverless API is treated as trusted backend code, not as "no backend"; long
  jobs and retry-prone side effects still need queue/state/idempotency design.
- vLLM/SGLang or any hosted model endpoint is treated as model-serving data
  plane behind the gateway, not as the policy/audit control plane.
- Human Review is represented as workflow state.
- Free text and client hints are normalized into structured actions before
  policy.
- Client-provided role, permission, risk class, and allowed tools are not
  trusted as final authority.
- Audit Log records lifecycle evidence, not only final text.

Common errors:

- Treating "please do not leak data" as access control.
- Drawing only model and data, with no policy or audit boundary.
- Letting RAG retrieve staff-only documents before permission filtering.
- Calling `create_it_ticket` directly from the agent.
- Letting the LLM decide final allow/deny/review_required without a policy engine.
- Trusting client-provided role, permission, risk class, or tool scope.
- Treating OWASP as a legal rule rather than a security guideline that informs
  implementation.
- Saying "serverless" removes the need for backend authorization.
- Exposing vLLM/SGLang directly to the browser and calling it the gateway.
- Letting LLM action extraction bypass schema validation or policy.
- Logging only final output instead of source IDs, tool decisions, and policy.
