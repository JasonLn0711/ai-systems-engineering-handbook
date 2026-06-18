# Rubric: Day 1 AI Gateway Architecture Evidence

Total: 100 points.

## Score Summary

| Category | Points | Requirement |
|---|---:|---|
| Architecture diagram | 25 | Complete components and clear data/control flow |
| Component responsibility | 20 | Responsibility, input, output, missing-control failure, and gateway type separation |
| Request lifecycle | 20 | HTTP request to audit event with standards-aware auth, normalization, risk, policy, retrieval, tool, guardrail |
| Risk-control map | 20 | At least seven concrete risks mapped to system controls |
| Beginner clarity | 10 | Sophomore-readable explanation, HTTP/serverless boundary, OWASP/NIST mental model, identity/role/permission, and readable HTTP/JSON contracts |
| Source boundary | 5 | Public-safe scenario, no private source material |

## Learning Objective Mapping

| Learning objective | Evidence | Rubric category |
|---|---|---|
| Distinguish demo/app/system/deliverable system | short written explanation | Beginner clarity |
| Read HTTP/JSON request contract | request contract warm-up and lifecycle | Beginner clarity, Request lifecycle |
| Explain HTTP as gateway API boundary | request contract warm-up and lifecycle status paths | Beginner clarity, Request lifecycle |
| Normalize free text/form input | request envelope and policy worksheet | Component responsibility, Request lifecycle |
| Explain OWASP/NIST access-control basis | standards mapping worksheet | Beginner clarity, Risk-control map |
| Explain serverless API boundary | serverless worksheet and lifecycle | Beginner clarity, Request lifecycle |
| Compare action extraction methods | action extraction worksheet with multi-intent decomposition, slots, confidence, and fallback | Component responsibility, Request lifecycle |
| Separate gateway types | gateway type map | Component responsibility, Risk-control map |
| Separate identity, role, and permission | policy worksheet, component table, audit fields | Beginner clarity, Component responsibility |
| Decide allow/deny/review | policy worksheet, lifecycle, risk-control map | Request lifecycle, Risk-control map |
| Explain AI Gateway as control plane | architecture diagram and explanation | Architecture diagram |
| Define component boundaries | component table | Component responsibility |
| Write request lifecycle | lifecycle list | Request lifecycle |
| Map risks to controls | risk-control map | Risk-control map |
| Avoid prompt-only governance | risk-control map and explanation | Risk-control map |
| Keep scenario public-safe | scenario description | Source boundary |

## Architecture Diagram: 25 Points

| Score | Standard |
|---:|---|
| 23-25 | Includes all required components; data flow and control flow are clear; deny/review/pass paths are visible |
| 18-22 | Components mostly complete, but some review/audit/data path is unclear |
| 12-17 | Has gateway and model, but misses several governance components |
| 0-11 | Mostly `User -> LLM -> Response`; no enterprise architecture |

## Component Responsibility: 20 Points

| Score | Standard |
|---:|---|
| 18-20 | Every component has clear responsibility, input, output, and failure if missing; separates API gateway, AI/LLM gateway, tool broker, and policy engine |
| 14-17 | Most components are clear; some input/output fields are vague |
| 8-13 | Concept descriptions exist, but interface contracts are weak |
| 0-7 | Responsibilities are merged into the model or prompt |

## Request Lifecycle: 20 Points

| Score | Standard |
|---:|---|
| 18-20 | 10-15 steps; includes HTTP route, JSON body, trace ID, token verification, server-side identity/role/permission lookup, schema validation, action extraction, risk classification, policy evaluation, RAG, tool broker enforcement, human review queue, audit, response status; action extraction treats complex prompts as multiple action proposals rather than one label |
| 14-17 | Mostly complete but missing one or two critical steps |
| 8-13 | Basic flow exists, but governance or audit is incomplete |
| 0-7 | Only describes a model call |

## Risk-Control Map: 20 Points

| Score | Standard |
|---:|---|
| 18-20 | At least seven concrete risks; includes free-text ambiguity, action extraction error, client-hint tampering, RAG ACL drift, side-effect tool risk, policy drift, cost/latency, UX friction, or audit gaps; controls are system-enforced; evidence is inspectable |
| 14-17 | Risks are concrete, but evidence or controls are partly vague |
| 8-13 | Risks are generic; controls are mostly slogans or prompt instructions |
| 0-7 | Risks are not mapped to system controls |

## Beginner Clarity: 10 Points

| Score | Standard |
|---:|---|
| 9-10 | Sophomore-readable; defines why HTTP/serverless APIs are gateway boundaries; explains OWASP as guidance, NIST as control/risk vocabulary; separates free text, client hints, normalized request, user identity, role, permission, authentication, authorization, JSON object/schema, route/handler/log, RAG/API/database in concrete examples; explains natural-language-first UI and policy-first execution without forcing users into long forms |
| 6-8 | Mostly readable, but some request-contract, HTTP/serverless boundary, standards mapping, or identity/role terms are unexplained |
| 3-5 | Reads like an industry slide deck; hard for beginners |
| 0-2 | Mostly abstract nouns |

## Source Boundary: 5 Points

| Score | Standard |
|---:|---|
| 5 | Fully public-safe, no private data or identifiable facts |
| 3-4 | Mostly safe, but some scenario detail is too specific |
| 1-2 | Possibly exposes private context or sensitive detail |
| 0 | Uses private transcript, customer secret, credential, or identifiable personal data |

## TA Grading Workflow

1. **Source boundary check first**: reject or return for revision if the answer
   contains private data, credentials, identifiable people, or private customer
   facts.
2. **Request-contract check**: confirm that the student can identify method,
   route, JSON body, user context, client hints, normalized actions, policy
   decision, response status, and audit fields in the warm-up.
3. **Standards mapping check**: confirm that OWASP/NIST concepts are translated
   into server-side authorization, deny-by-default, least privilege, ABAC-style
   attributes, or audit controls rather than cited as vague authority.
4. **Action extraction check**: confirm that rules/classifier/LLM structured
   output/workflow planner is named; complex prompts are decomposed into
   action candidates; slots, confidence, risk, ambiguity, and fallback are
   present; model output is validated before policy or tool execution.
5. **Artifact completeness check**: confirm that all four artifacts are present.
6. **Architecture pass**: inspect required components and flow direction.
7. **Lifecycle pass**: verify ordering from identity to schema validation to
   intent normalization to risk classification to policy to data/tool/model to
   guardrail to audit.
8. **Risk-control pass**: reject controls that are only prompt instructions when
   system enforcement is required.
9. **Evidence pass**: look for trace IDs, source IDs, tool decisions, policy
   decisions, review state, and audit event.
10. **Feedback pass**: give one next implementation gate, usually tied to Day 2
   minimal gateway mock.

## Minimum Pass Gate

The student is ready for Day 2 when they can read one JSON request, one JSON
response, one policy decision, and one audit event; explain why HTTP is used as
the external gateway API boundary; explain `401` vs `403`; separate user
identity from role and permission; separate authentication from authorization;
normalize free text/client hints into structured actions; show that RAG filters
permissions before model context; describe tool calling as a controlled API
action; explain why serverless API still needs trusted authorization logic;
map at least one OWASP and one NIST idea to the gateway design; name an action
extraction method; explain why classifier output should include multi-label
intents, action candidates, slots, risk, confidence, and fallback; and explain
why review is a normal control point rather than a failure.
