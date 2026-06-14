# Day 1: AI Gateway Architecture Evidence

## Purpose

Day 1 turns a model-centric LLM demo into a system-centric enterprise AI
architecture exercise. The learner does not build the full gateway yet. The
learner produces architecture evidence that can be reviewed before Day 2
implementation.

The core claim is:

```text
Enterprise AI delivery is not proven by a working model demo.
It is proven by a system package with architecture, governance, deployment,
security, validation, and customer-delivery evidence.
```

## Target Learner

This lesson is written for sophomore computer science students who know basic
programming, HTTP/JSON, API handlers, database tables, roles, permissions,
modules, tests, and logs, but have not yet designed an enterprise AI system.

The minimum entry model is intentionally small. Students should be able to read
an HTTP request/response, recognize a JSON object, explain that a backend route
calls a handler and writes logs, distinguish login from authorization, and know
where LLMs, RAG, APIs, and databases sit in a system. They do not need
Kubernetes, GPU serving, red teaming, or enterprise security framework
experience before Day 1. Day 1 introduces GPU/model serving only as an
architecture boundary: students should recognize where vLLM, SGLang, or hosted
model APIs sit, without being asked to operate them yet.

The point of these prerequisites is architectural literacy:

```text
AI Gateway is not only "send the prompt to a model."
AI Gateway turns every AI request into a verifiable, governable, traceable
system lifecycle.
```

## Learning Objectives

By the end of Day 1, the student should be able to:

1. Distinguish a model demo, AI application, AI system, and
   enterprise-deliverable AI system.
2. Read a minimal HTTP/JSON AI request contract and identify method, route,
   headers, body, status, user context, requested action, and trace fields.
3. Explain why AI Gateway commonly exposes HTTP APIs while allowing streaming,
   queue, gRPC, database, model-server, or connector protocols behind the
   gateway.
4. Compare free-text, selected-list/form, and hybrid request entry patterns,
   then normalize a user request into actor, task, action, resource,
   environment, and trace fields.
5. Distinguish user identity, role, permission, authentication, authorization,
   and policy decision.
6. Explain how schema validation, intent normalization, risk classification,
   policy evaluation, tool brokering, human review, and audit produce
   `allow`, `deny`, or `review_required`.
7. Explain why OWASP treats client-side access control as a UX aid rather than
   an authorization decision, and how OWASP/NIST concepts map to AI Gateway
   access-control design.
8. Explain what a serverless API is, where it can host a trusted gateway
   handler, and why it still needs authorization, durable state, idempotency,
   observability, and audit.
9. Distinguish cloud hosting, cloud serverless API, local serverless
   emulation, self-hosted serverless-like platforms, and plain localhost
   backend servers.
10. Explain why enterprise AI systems usually use hybrid hosting: containers,
    Kubernetes, or managed services for core gateway/inference workloads, and
    serverless for event-driven edge automation.
11. Explain that vLLM and SGLang are model-serving engines in the inference
    data plane, while AI Gateway remains the control plane for identity,
    policy, routing, quota, audit, and review.
12. Compare rule-based parsing, classifiers, LLM structured outputs, and
    workflow planners for turning free text into actions.
13. Distinguish API gateways, AI/LLM gateways, model-serving engines, tool
    gateways, and policy gateways, and name the engineering pain each one
    addresses.
14. Explain why an AI Gateway is a control plane rather than only a proxy.
15. Draw an AI Gateway architecture with identity, policy, agent, tool, data,
   model, guardrail, audit, and human-review boundaries.
16. Define the responsibility, input, output, and missing-control failure for
   each component.
17. Write a 10-15 step request lifecycle from user request to audit event.
18. Map prompt injection, PII leakage, tool abuse, permission bypass, action
   extraction failure, RAG ACL drift, cost blowup, and missing audit trail to
   concrete system controls.
19. Produce reviewable architecture evidence without relying on prompt-only
   governance.

## File Map

| File | Audience | Purpose |
|---|---|---|
| `student-handout.md` | Students | Summarized first-principle lecture handout without reference answers. |
| `student-handout-detailed.md` | Students / instructor | Detailed companion handout with extended explanations, examples, and comparisons. |
| `student-handout-detailed.zh-TW.md` | Students / instructor | Complete Taiwan Traditional Chinese version of the detailed handout. |
| `worksheet.md` | Students | Printable in-class artifact templates. |
| `instructor-guide.md` | Instructor | Teaching flow, diagnostic, prompts, failure gallery. |
| `reference-answer-campus-it.md` | Instructor / TA | Campus IT Helpdesk reference answer. |
| `rubric.md` | Instructor / TA | 100-point rubric, objective mapping, grading workflow. |
| `day-02-lab-handoff.md` | Instructor / TA / implementer | Contract for the next minimal gateway mock lab. |
| `glossary-updates.md` | Maintainers | Terms to merge into global glossary files later. |
| `source-package.md` | Maintainers | Original full package preserved as source material. |

## Recommended Use Order

For a class session:

1. Send `student-handout.md` sections 1-6 as pre-class reading.
2. Start class with the pre-class diagnostic in `instructor-guide.md`.
3. Teach the main concept using `student-handout.md`, then use
   `student-handout-detailed.md` when students need deeper examples.
4. Use `student-handout-detailed.zh-TW.md` when students need the complete
   Taiwan Traditional Chinese detailed version.
5. Run the workshop using `worksheet.md`.
6. Grade using `rubric.md`.
7. Compare instructor/TA review against `reference-answer-campus-it.md`.
8. Move implementation work into `day-02-lab-handoff.md`.

## Learning Objective To Assessment Map

| Objective | Evidence artifact | Rubric category |
|---|---|---|
| Model demo vs AI system | Short explanation in worksheet | Beginner clarity |
| HTTP/JSON request contract | Request contract warm-up | Beginner clarity |
| HTTP as gateway boundary | Short explanation and lifecycle status paths | Beginner clarity, Request lifecycle |
| Free text / form / hybrid input | Input-mode and normalization worksheet | Beginner clarity, Component responsibility |
| Identity vs role vs permission | Policy worksheet and audit fields | Beginner clarity, Component responsibility |
| Allow/deny/review pipeline | Policy decision worksheet and lifecycle | Request lifecycle, Risk-control map |
| OWASP/NIST access-control basis | Standards mapping in short explanation and risk-control map | Beginner clarity, Risk-control map |
| Serverless API boundary | Student handout serverless lifecycle, request-contract bridge, worksheet, and Day 2 handoff note | Beginner clarity, Request lifecycle |
| Cloud hosting vs serverless vs local emulation | Serverless boundary worksheet and architecture hosting notes | Beginner clarity, Component responsibility |
| Enterprise hybrid hosting | Gateway comparison, pain-point map, and risk-control map | Risk-control map, Component responsibility |
| vLLM/SGLang model-serving boundary | Student handout model serving section, diagram, component table, and gateway comparison | Beginner clarity, Component responsibility |
| Action extraction strategies | Normalization worksheet with multi-label action candidates, slots, risk, confidence, fallback, and lifecycle | Component responsibility, Request lifecycle |
| Natural-language-first UX with policy-first execution | Action preview / smart hints worksheet and risk-confidence behavior table | Beginner clarity, Risk-control map |
| Gateway types and pain points | Gateway comparison and risk-control map | Risk-control map, Beginner clarity |
| AI Gateway as control plane | Architecture diagram | Architecture diagram |
| Component responsibility | Component responsibility table | Component responsibility |
| Request lifecycle | 10-15 step lifecycle | Request lifecycle |
| Risk-control reasoning | Risk-control map | Risk-control map |
| Prompt-only governance boundary | Failure gallery critique | Risk-control map, beginner clarity |
| Public-safe design | Scenario and source-boundary check | Source boundary |

## Student / Instructor Separation

Students should receive:

- `student-handout.md`
- `worksheet.md`
- public-safe scenario options

Students should not receive before submission:

- `reference-answer-campus-it.md`
- detailed grading notes in `rubric.md`
- instructor-only failure diagnosis notes

This separation keeps the activity diagnostic. Students should construct the
architecture rather than copy the reference answer.

## Minimum Day 1 Deliverables

Every student or group submits:

1. AI Gateway architecture diagram.
2. Component responsibility table.
3. Request lifecycle.
4. Risk-control map.

The worksheet also includes a short request-contract warm-up. It verifies that
the student can read one JSON request, one JSON response, one policy decision,
and one audit event before drawing the larger architecture.

## Minimum Passing Contract

Before moving into Day 2 implementation, the student should be able to:

1. Read one JSON request and one JSON response.
2. Explain why HTTP is a practical gateway boundary for clients, routing,
   authentication, status codes, observability, and enterprise network controls.
3. Explain why client-provided fields are hints and server-side identity,
   role, permission, agent scope, and policy data must be resolved by the
   gateway, using the OWASP server-side authorization and deny-by-default
   mental model.
4. Normalize free text and selected fields into structured action/resource
   inputs and explain when rules, classifiers, LLM structured outputs, or
   workflow planners are appropriate.
5. Explain what a serverless API is and why serverless still requires trusted
   token validation, authorization, schema validation, durable state, secret
   handling, idempotency for side effects, observability, and audit logging.
6. Distinguish serverless API from cloud hosting, local emulation, self-hosted
   serverless-like platforms, and plain localhost backend servers.
7. Explain why enterprise AI Gateway designs often use containers/Kubernetes
   for core gateway/inference services and serverless for webhooks, triggers,
   scheduled jobs, notifications, and lightweight automation.
8. Explain that vLLM/SGLang load model weights and serve inference requests,
   while the AI Gateway performs identity, policy, quota, audit, routing, and
   review controls before calling those serving engines.
9. Explain that a route maps a URL and method to a handler.
10. Explain why logs can reconstruct a request lifecycle.
11. Distinguish user identity from role.
12. Distinguish authentication from authorization.
13. Explain how role and permission affect data and tool access.
14. Explain why a logged-in user can still receive `deny` or `review_required`.
15. Explain why RAG must filter by permission before model context construction.
16. Explain why a tool call is a controlled API action.
17. Identify the database evidence needed for policy, metadata, and audit.
18. Name at least three practical AI Gateway pain points and the control layer
    that reduces each one.

## Source Boundary

All scenarios must be public-safe. Use generalized examples such as campus IT
helpdesk, bank internal knowledge assistant, medical intake support, and
manufacturing audio monitoring. Do not use private transcripts, customer
secrets, credentials, personal contact routes, salary or offer details,
unpublished company claims, or identifiable personal data.

## Background References

These are background references for the instructor and maintainer. Day 1 does
not require students to master these tools or frameworks.

- FastAPI documentation: <https://fastapi.tiangolo.com/>
- Pydantic documentation: <https://docs.pydantic.dev/latest/>
- JSON Schema documentation: <https://json-schema.org/learn/getting-started-step-by-step>
- OpenAI Structured Outputs guide:
  <https://platform.openai.com/docs/guides/structured-outputs>
- Pydantic JSON Schema:
  <https://docs.pydantic.dev/latest/concepts/json_schema/>
- scikit-learn text feature extraction:
  <https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction>
- scikit-learn text classification example:
  <https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html>
- Hugging Face Transformers text classification:
  <https://huggingface.co/docs/transformers/tasks/sequence_classification>
- Hugging Face Transformers pipelines:
  <https://huggingface.co/docs/transformers/main_classes/pipelines>
- People + AI Guidebook, Explainability and Trust:
  <https://pair.withgoogle.com/chapter/explainability-trust/>
- Microsoft Guidelines for Human-AI Interaction:
  <https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/>
- Open Policy Agent documentation: <https://www.openpolicyagent.org/docs/>
- Casbin documentation: <https://casbin.apache.org/docs/overview/>
- LangGraph interrupts documentation:
  <https://docs.langchain.com/oss/python/langgraph/interrupts>
- OpenTelemetry documentation: <https://opentelemetry.io/docs/>
- PostgreSQL documentation: <https://www.postgresql.org/docs/>
- OWASP Broken Access Control:
  <https://owasp.org/Top10/2021/A01_2021-Broken_Access_Control/>
- OWASP Authorization Cheat Sheet:
  <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
- OWASP ASVS:
  <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP LLM Prompt Injection Prevention:
  <https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html>
- OWASP Top 10 for Large Language Model Applications:
  <https://owasp.org/www-project-top-10-for-large-language-model-applications/>
- OpenID Connect Core:
  <https://openid.net/specs/openid-connect-core-1_0.html>
- JSON Web Token RFC 7519:
  <https://datatracker.ietf.org/doc/html/rfc7519>
- NIST SP 800-53:
  <https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final>
- NIST SP 800-162 ABAC:
  <https://csrc.nist.gov/pubs/sp/800/162/upd2/final>
- NIST AI Risk Management Framework:
  <https://www.nist.gov/itl/ai-risk-management-framework>
- NIST AI RMF Generative AI Profile:
  <https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence>
- ISO/IEC 42001 overview:
  <https://www.iso.org/standard/42001>
- EU AI Act overview:
  <https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai>
- AWS API Gateway documentation:
  <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>
- AWS Lambda + API Gateway:
  <https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html>
- AWS Lambda execution environment lifecycle:
  <https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html>
- AWS Lambda best practices:
  <https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html>
- AWS Serverless Application Model:
  <https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html>
- OpenAPI Specification:
  <https://swagger.io/specification/>
- Vercel Functions:
  <https://vercel.com/docs/functions>
- Cloudflare Workers:
  <https://developers.cloudflare.com/workers/>
- Hono:
  <https://hono.dev/>
- OpenFaaS:
  <https://www.openfaas.com/>
- Knative:
  <https://knative.dev/docs/>
- AWS Step Functions:
  <https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html>
- AWS Lambda with SQS:
  <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html>
- AWS Lambda Powertools idempotency:
  <https://docs.aws.amazon.com/powertools/python/latest/utilities/idempotency/>
- OWASP API Security: Broken Object Level Authorization:
  <https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/>
- OWASP Serverless Top 10:
  <https://owasp.org/www-project-serverless-top-10/>
- OpenAI Function Calling:
  <https://platform.openai.com/docs/guides/function-calling>
- OpenAI Guardrails and Human Review:
  <https://platform.openai.com/docs/guides/agents/guardrails-approvals>
- LangChain Human-in-the-loop:
  <https://docs.langchain.com/oss/python/langchain/human-in-the-loop>
- vLLM documentation:
  <https://docs.vllm.ai/>
- vLLM quickstart:
  <https://docs.vllm.ai/en/latest/getting_started/quickstart/>
- PagedAttention paper:
  <https://arxiv.org/abs/2309.06180>
- SGLang documentation:
  <https://docs.sglang.ai/>
- SGLang quickstart:
  <https://docs.sglang.io/docs/get-started/quickstart>
- SGLang structured outputs:
  <https://docs.sglang.ai/advanced_features/structured_outputs.html>
- SGLang PD disaggregation:
  <https://docs.sglang.ai/advanced_features/pd_disaggregation.html>
- SGLang production metrics:
  <https://docs.sglang.io/docs/references/production_metrics>
- Cloudflare AI Gateway:
  <https://developers.cloudflare.com/ai-gateway/>
- LiteLLM:
  <https://docs.litellm.ai/docs/>
- Kong AI Gateway:
  <https://developer.konghq.com/ai-gateway/>
- Model Context Protocol:
  <https://modelcontextprotocol.io/docs/getting-started/intro>
