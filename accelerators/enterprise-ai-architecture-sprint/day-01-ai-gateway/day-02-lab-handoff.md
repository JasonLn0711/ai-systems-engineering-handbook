# Day 2 Lab Handoff: Minimal AI Gateway Mock

## Purpose

Day 1 produces architecture evidence. Day 2 turns that evidence into a minimal
mock gateway. The lab should preserve the Day 1 contract: identity, policy,
agent selection, RAG boundary, tool broker, guardrail, human review, and audit.

## Recommended Beginner Stack

| Layer | Suggested tool | Day 2 use |
|---|---|---|
| API server | FastAPI | `POST /gateway/requests` |
| Serverless variant | AWS Lambda, Vercel Function, Cloudflare Worker | same trusted handler shape without managing a long-running server |
| Token verification | mock signed token first, OIDC/JWT later | derive trusted identity server-side |
| Schema validation | Pydantic | request/response models |
| Action extraction | rules first, LLM structured output later | raw message and hints become structured actions |
| Model endpoint adapter | Python mock first, OpenAI-compatible client later | keep model calls behind a swappable interface |
| Audit storage | local JSONL first, PostgreSQL later | inspectable audit events |
| Observability | trace ID first, OpenTelemetry later | request path continuity |
| Policy | Python function first, OPA/Cedar/Casbin later | allow/deny/review_required |
| Human review | in-memory queue first, workflow engine later | pending/approved/rejected side-effect actions |
| Idempotency | in-memory key table first, database table later | prevent duplicate tickets or emails after retries |
| Async jobs | in-memory queue first, SQS/Cloudflare Queues/Step Functions later | move long AI work out of synchronous HTTP request |

Day 2 should avoid Kubernetes and GPU serving. vLLM and SGLang are useful later
model-serving engines, but the beginner mock should represent them only as a
future model endpoint behind the gateway.

## API Contract

Route:

```text
POST /gateway/requests
```

The route accepts a JSON body and returns a JSON response. The mock should make
the HTTP outcome visible rather than hiding every result behind `200 OK`.
HTTP is the external client-facing API boundary for this lab. The mock can keep
all internals in Python functions, but the design should still make clear that
future internal layers may use streaming, queues, gRPC, database connections,
model-server protocols, vLLM/SGLang endpoints, or MCP connectors behind the
gateway.

The same handler can later run as a serverless API. Serverless changes the
hosting model, not the trust model:

```text
AWS: API Gateway -> Lambda handler
Vercel: /api/gateway route -> Vercel Function
Cloudflare: Worker route -> gateway handler
```

In every version, the handler still verifies tokens, resolves permission
server-side, validates schema, evaluates policy, brokers tools, and writes
audit evidence.

For local development, be precise about the hosting model:

```text
plain FastAPI on localhost = normal local backend server
SAM local / Vercel dev / Wrangler / LocalStack = local serverless emulation
OpenFaaS / Knative on local Kubernetes = self-hosted serverless-like platform
```

The Day 2 mock can start as a normal local FastAPI server because that is the
lowest-friction way to teach route, handler, schema, policy, tool broker, and
audit. The handler shape should still be portable to a serverless runtime.

For Day 2, keep the first mock synchronous unless the class has time for an
optional queue. Still teach the boundary:

```text
short path:
POST /gateway/requests -> handler -> policy -> mock RAG/model -> response

long path:
POST /gateway/jobs -> handler -> create job_id -> enqueue -> 202 Accepted
worker -> model/evaluation/tool workflow -> result store
```

Any side-effect tool should accept an idempotency key, even if the beginner mock
stores it in memory:

```text
idempotency_key
request_hash
status: processing | completed | failed
response_body
```

If the same key is retried, the mock should not create a second ticket.

| Status | Use in Day 2 mock |
|---:|---|
| 200 | Request completed or a review item was created successfully |
| 400 | JSON body is malformed or missing required schema fields |
| 401 | Session token is missing or invalid |
| 403 | Authenticated user lacks permission for the data, tool, or action |
| 429 | Optional rate-limit path for repeated side-effect requests |
| 500 | Unexpected model, retrieval, tool, or audit failure |

### Request

```json
{
  "session_token": "demo-student-session",
  "channel": "student_portal",
  "raw_message": "我無法登入 VPN，請幫我找設定方式。如果還是不行，幫我建立 IT ticket。",
  "client_hints": {
    "category": "vpn",
    "requested_actions": ["search_faq", "create_ticket"],
    "urgency": "medium"
  },
  "requested_agent": "campus_it_helpdesk_agent"
}
```

### Successful Response

```json
{
  "trace_id": "req-0001",
  "status": "completed",
  "answer": "請先確認 MFA、VPN client 版本與帳號狀態。",
  "source_ids": ["vpn-guide-2026-01"],
  "policy_decision": "allow",
  "guardrail_result": "passed",
  "audit_event_id": "audit-0001"
}
```

### Review Response

```json
{
  "trace_id": "req-0002",
  "status": "pending_review",
  "message": "Ticket submission requires IT staff review.",
  "review_id": "review-1002",
  "policy_decision": "review_required",
  "audit_event_id": "audit-0002"
}
```

### Denied Response

```json
{
  "trace_id": "req-0003",
  "status": "denied",
  "message": "This role cannot access staff-only documents.",
  "policy_decision": "deny",
  "audit_event_id": "audit-0003"
}
```

## Required Pydantic Model Shapes

The implementation can rename fields if needed, but it must preserve the
contract concepts:

```text
AIRequest:
  session_token
  channel
  raw_message
  client_hints
  requested_agent

IdentityContext:
  user_id
  email
  role
  permissions
  token_issuer
  token_audience

ActionExtractionResult:
  method: rules | classifier | llm_structured_output | workflow_planner
  confidence
  normalized_actions
  validation_errors

NormalizedAction:
  action_type
  tool_name
  resource
  side_effect
  required_slots

PolicyDecision:
  decision: allow | deny | review_required
  allowed_actions
  denied_actions
  review_actions
  allowed_access_levels
  denied_access_levels
  reason

RAGResult:
  source_id
  title
  access_level
  document_version
  excerpt

ModelCallResult:
  model_backend: mock | hosted_api | vllm | sglang
  model_name
  model_version
  latency_ms
  token_count
  output_text

ToolDecision:
  tool_name
  decision: allow | deny | review_required
  reason

AuditEvent:
  audit_event_id
  trace_id
  user_id
  role
  token_subject
  policy_id
  agent_id
  action_extraction_method
  model_backend
  model_version
  model_latency_ms
  policy_decision
  retrieved_source_ids
  tool_decisions
  guardrail_result
  human_review_status
  outcome
```

Minimum policy table:

| Role | Tool | Decision |
|---|---|---|
| student | search_it_faq | allow |
| student | create_it_ticket | review_required |
| student | read_staff_sop | deny |
| staff | search_it_faq | allow |
| staff | create_it_ticket | allow |
| staff | read_staff_sop | allow |

## Minimal Pseudo-Code

```python
@app.post("/gateway/requests")
def handle_ai_request(request: AIRequest):
    trace_id = create_trace_id()
    validate_request_schema(request)

    token_claims = verify_token(request.session_token)
    identity = resolve_identity_and_permissions(token_claims)

    extraction = normalize_intent(
        raw_message=request.raw_message,
        client_hints=request.client_hints,
        method="rules_first_then_structured_output",
    )
    actions = validate_action_schema(extraction.normalized_actions)
    classified_actions = classify_risk(actions)
    policy = check_policy(identity, classified_actions)

    if policy.decision == "deny":
        audit_event = write_audit(trace_id, identity, policy, outcome="denied")
        return denied_response(trace_id, policy, audit_event)

    agent = select_agent(request.requested_agent)
    input_guardrail = check_input(request.raw_message)

    sources = search_it_faq(
        query=request.raw_message,
        allowed_access_levels=policy.allowed_access_levels,
    )

    answer = generate_mock_answer(request.raw_message, sources)
    output_guardrail = check_output(answer)

    tool_decisions = []
    review_status = "not_required"
    for action in classified_actions:
        if action.tool_name == "create_it_ticket":
            tool_decision = broker_tool_call(action, identity, policy)
            tool_decisions.append(tool_decision)
            if tool_decision.decision == "review_required":
                create_review_item(trace_id, action, reviewer_role="it_staff")
                review_status = "pending_review"

    audit_event = write_audit(
        trace_id=trace_id,
        identity=identity,
        agent=agent,
        policy=policy,
        sources=sources,
        action_extraction_method=extraction.method,
        tool_decisions=tool_decisions,
        guardrail=output_guardrail,
        human_review_status=review_status,
    )

    return build_response(trace_id, answer, sources, policy, output_guardrail, audit_event)
```

## Day 2 Acceptance Criteria

- [ ] `POST /gateway/requests` accepts a JSON request.
- [ ] Request schema validation rejects malformed input.
- [ ] Invalid session returns an authentication failure path.
- [ ] Authenticated but unauthorized access returns a permission failure path.
- [ ] Gateway creates a `trace_id`.
- [ ] Token verification checks issuer, audience, expiration, and subject in
      the mock or documents how the real OIDC/JWT check will work.
- [ ] Gateway treats `client_hints` as hints and resolves identity, role,
      permissions, and policy server-side.
- [ ] Free text is normalized into structured actions with a named method:
      rules, classifier, LLM structured output, or workflow planner.
- [ ] Action extraction output is schema-validated before policy evaluation.
- [ ] Risk classifier marks `create_it_ticket` as side-effecting.
- [ ] Policy function returns `allow`, `deny`, or `review_required`.
- [ ] RAG mock returns only allowed source IDs.
- [ ] Model call goes through a model endpoint adapter rather than being
      hard-coded into the handler.
- [ ] The mock records model backend/version/latency fields even if the backend
      is only `mock`.
- [ ] Tool broker routes `create_it_ticket` to `review_required` for `student`.
- [ ] Review item is created with `pending_review` state.
- [ ] Guardrail mock returns `passed`, `blocked`, or `review_required`.
- [ ] Audit event is written to JSONL or PostgreSQL.
- [ ] Response includes `trace_id`, `source_ids`, policy decision, and
      `audit_event_id`.
- [ ] Optional serverless note identifies where the same handler would run on
      AWS Lambda, Vercel Functions, or Cloudflare Workers, and what operational
      risk must be handled there.
