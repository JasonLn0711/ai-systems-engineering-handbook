# Glossary Updates: Day 1 AI Gateway

These terms should be merged into the appropriate global glossary files after
review.

| Term | Definition |
|---|---|
| HTTP Request | Client-to-server message with method, path, headers, and body. |
| HTTP Response | Server-to-client result with status code, headers, and body. |
| HTTP API Boundary | Client-facing service boundary that packages an AI task as a routable, authenticatable, observable request/response event. |
| Status Code | Numeric HTTP outcome signal such as `200`, `400`, `401`, `403`, `429`, or `500`. |
| JSON Object | Key-value data structure commonly used in API request and response bodies. |
| JSON Schema | Contract that defines required JSON fields, field types, and validation rules. |
| Route | HTTP method and URL path mapped to a backend handler, such as `POST /gateway/requests`. |
| Handler | Backend function that reads a request, runs business logic, writes logs, and returns a response. |
| API Contract | Agreed interface between systems, including method, path, input schema, output schema, status, and error behavior. |
| Server-side authorization | Authorization performed in trusted backend code, gateway code, or serverless function rather than in browser-only logic. |
| Deny by default | Access-control posture where unknown or unproven requests are denied unless policy explicitly allows them. |
| Least privilege | Security principle that grants only the access needed for the assigned task. |
| OWASP | Open Worldwide Application Security Project; community security guidance, cheat sheets, verification standards, and risk lists, not a law by itself. |
| OWASP ASVS | Application Security Verification Standard; a requirements basis for testing web application technical security controls. |
| NIST SP 800-53 | Security and privacy control catalog; relevant here for access enforcement and least privilege controls. |
| NIST SP 800-162 | Attribute-Based Access Control guidance; useful for subject/object/action/environment policy input. |
| ABAC | Attribute-Based Access Control; authorization based on subject, object, operation, and environment attributes. |
| OIDC ID Token | Security token containing authentication claims about an end user, represented as a JWT in OpenID Connect. |
| JWT | Compact URL-safe token format for transferring signed or integrity-protected claims between parties. |
| Serverless API | HTTP API implemented as functions managed by a platform such as AWS Lambda, Vercel Functions, or Cloudflare Workers; changes hosting, not backend responsibility. |
| Function Invocation | One execution of serverless handler code triggered by an HTTP request, queue message, schedule, or other event. |
| Function Runtime | Language execution environment for a function, such as Python, Node.js, Go, or Java. |
| Cold Start | Extra startup latency when the platform creates a fresh function execution environment. |
| Warm Start | Faster function invocation when the platform can reuse an existing execution environment. |
| Async Job | Long-running task moved out of the immediate HTTP response path and processed through a queue, workflow, or worker. |
| Webhook | HTTP callback sent by an external service to notify the system that an event occurred. |
| Free-text request | Natural-language user input that may contain multiple intents, resources, risks, and side-effect requests. |
| Selected-list request | Controlled UI input where users choose task type, category, action, urgency, or other bounded fields. |
| Hybrid request | Request pattern that combines natural language with controlled fields, then normalizes both into a structured gateway envelope. |
| Client hints | User-interface-provided fields such as category or requested action; useful for normalization but not trusted for final policy. |
| Normalized request envelope | Server-side structured request containing actor, task, requested actions, resources, environment, and trace fields. |
| AI Gateway | Enterprise AI request entrypoint and control plane for identity, policy, agent routing, tool/data boundaries, guardrails, audit, and review. |
| API Gateway | Gateway focused on HTTP/API traffic, routing, authentication integration, rate limits, quotas, and logs. |
| AI / LLM Gateway | Gateway focused on model routing, provider abstraction, fallback, caching, token/cost tracking, and LLM observability. |
| Tool Gateway | Enforcement boundary for agent tool calls, schema validation, side-effect checks, approvals, and tool audit. |
| Policy Gateway | Policy decision point that centralizes authorization logic for applications or services. |
| Control plane | The layer that manages decisions, policy, coordination, and control behavior. |
| Data plane | The layer that executes data movement or request processing, such as retrieval, model serving, and tool execution. |
| User Identity | Specific person, account, or service making a request; answers who should be authenticated and audited. |
| Role | Access category or responsibility assigned to an identity, such as `student`, `staff`, or `admin`. |
| Authentication | Process that verifies who the caller is, usually through session, token, OAuth, SSO, or service identity. |
| Authorization | Process that verifies whether the authenticated caller can perform a specific action on a specific resource. |
| RBAC | Role-Based Access Control; permission model based on user or service role. |
| Permission | Specific allowed action such as `read_public_faq`, `create_ticket`, `query_database`, or `view_audit_log`. |
| Policy Gate | Component that returns allow, deny, or review_required decisions based on identity, task, resource, and risk. |
| Policy Engine | Rules or service that evaluates structured policy input and returns allow, deny, or review_required decisions. |
| Intent Normalization | Process that converts raw text and client hints into structured intent, action, resource, and tool fields. |
| Action Extraction | Process that maps free text and UI hints into canonical actions such as `retrieve_knowledge` or `create_ticket`. |
| LLM Structured Output | Model output constrained to a schema so extracted actions or slots can be validated by code. |
| Workflow Planner | Rule, graph, or agent workflow that decomposes a request into ordered steps with state and review points. |
| Risk Classification | Process that labels an action or task by risk, such as read-only, restricted retrieval, side-effect, external communication, or high-stakes output. |
| Review Required | Policy decision that routes an action to human review instead of direct allow or deny. |
| Review Queue | Workflow store for actions waiting for human approval, editing, rejection, expiration, or continuation. |
| Agent Registry | Inventory of agents, owners, scopes, allowed tools, allowed data sources, and risk class. |
| Tool Broker | Component that mediates tool calls with schema validation, permission checks, timeout, side-effect handling, and audit. |
| Side-effect tool | Tool that changes external state, such as creating a ticket, sending email, or updating a database. |
| RAG Connector | Controlled retrieval component that exposes allowed knowledge sources to the model workflow. |
| LLM | Large language model used as an inference component for language understanding, summarization, extraction, and generation. |
| RAG | Retrieval-Augmented Generation; retrieval of relevant allowed context before language generation. |
| Metadata filtering | Filtering by fields such as `access_level`, `owner`, `document_version`, and `status` before context reaches the model. |
| RAG ACL Drift | Failure mode where a vector index or retrieval cache no longer matches the source system's current permissions. |
| Policy Drift | Failure mode where roles, exceptions, or permissions change over time without tests or review. |
| Privilege Creep | Gradual accumulation of permissions beyond what a user or service needs. |
| Idempotency Key | Unique key used to make retries safe and prevent duplicate side-effect execution such as creating the same ticket twice. |
| Guardrail | Input, retrieval, tool, memory, or output check that routes content to pass, block, or review. |
| Audit Log | Lifecycle evidence record containing user, agent, policy, sources, tools, guardrail result, review state, and outcome. |
| Human Review | Workflow node for high-risk outputs or side-effect actions, usually with pending, approved, and rejected states. |
| Gateway State Machine | Explicit lifecycle states such as received, authenticated, schema_validated, intent_normalized, policy_checked, completed, denied, pending_review, and audit_written. |
| Trace ID | Unique identifier that links events across components for one request. |
| Database | Durable store for identity, role, permission, documents, metadata, policy, audit, review, and evaluation records. |
| Architecture Evidence | Reviewable artifacts such as diagrams, responsibility tables, lifecycles, risk-control maps, and validation checklists. |
