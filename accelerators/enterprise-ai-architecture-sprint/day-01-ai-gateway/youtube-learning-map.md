# Day 1 YouTube Learning Map

```yaml
artifact_type: ai_agent_readable_learning_map
accelerator: enterprise-ai-architecture-sprint
day: 1
day_topic: AI Gateway Architecture Evidence
primary_language: zh-TW
created_for: Day 1 video-based learning support
retrieved_at: 2026-06-20
source_scope:
  - Existing Day 1 course package concepts
  - Public YouTube instructional videos
source_boundary:
  - No private transcripts
  - No customer secrets
  - No credentials
  - No identifiable personal data
agent_use:
  - Use top_10_priority_videos for the first viewing assignment
  - Use learning_sequence for the complete Day 1 coverage path
  - Use coverage_index to check whether every Day 1 concept has video support
```

## Reading Contract For Agents

This file maps existing Day 1 concepts to public YouTube videos. It does not
introduce new Day 1 requirements. The target Day 1 evidence remains:

1. `domain-brief.md`
2. AI Gateway architecture diagram
3. component responsibility table
4. 10-15 step request lifecycle
5. risk-control map

Each sequence item uses this shape:

```yaml
sequence_id: stable order key
concepts: Day 1 concepts covered
recommended_videos: YouTube links
required_output: artifact evidence after watching
coverage_notes: why this belongs in Day 1
```

## Top 10 Priority Videos

These are the first ten videos to watch before the full sequence. They cover the
minimum mental model for Day 1: problem framing, architecture, request contract,
identity/policy, gateway control plane, RAG/tool boundaries, security controls,
audit, and deployment/inference awareness.

| Rank | Video | Why Watch First | Day 1 Output |
|---:|---|---|---|
| 1 | [HOW TO SOLVE PROBLEMS - hypothesis-based problem solving explained](https://www.youtube.com/watch?v=TBvJzXxRuxs) | Frames Day 1 as output-driven, hypothesis-driven learning instead of passive study. | One-sentence job/system map and issue tree. |
| 2 | [Visualising software architecture with the C4 model](https://www.youtube.com/watch?v=x2-rSnhpw0g) | Gives a clean way to draw system context, containers, components, and boundaries. | First AI Gateway architecture sketch. |
| 3 | [Web Application Architecture: Full Request-Response Lifecycle](https://www.youtube.com/watch?v=xv0Be4QfkH0) | Connects HTTP request, backend handling, response, and logs. | Request lifecycle baseline. |
| 4 | [RBAC vs ABAC](https://www.youtube.com/watch?v=rvZ35YW4t5k) | Establishes identity, role, permission, and attribute-based policy thinking. | Policy worksheet and access-control fields. |
| 5 | [What is API Gateway?](https://www.youtube.com/watch?v=6ULyxuHKxg8) | Explains gateway as a control boundary before AI-specific gateway work. | API Gateway vs AI Gateway distinction. |
| 6 | [What is an LLM Gateway?](https://www.youtube.com/watch?v=NXS3N9JY9dY) | Introduces AI/LLM gateway concerns: routing, provider abstraction, cost, observability. | Gateway type and pain-point map. |
| 7 | [What is Tool Calling? Connecting LLMs to Your Data](https://www.youtube.com/watch?v=h8gMhXYAv1k) | Shows why tool calls must be structured API actions, not prompt magic. | Tool broker and tool registry fields. |
| 8 | [RAG Explained For Beginners](https://www.youtube.com/watch?v=_HQ2H_0Ayy0) | Covers the basic retrieval path before RAG ACL and citation controls. | RAG/data boundary. |
| 9 | [Explained: OWASP Top 10 for LLM Applications](https://www.youtube.com/watch?v=cYuesqIKf9A) | Gives AI security risk vocabulary for prompt injection, leakage, and tool abuse. | Risk-control map seed. |
| 10 | [OpenTelemetry: Simplifying Hybrid Cloud Monitoring](https://www.youtube.com/watch?v=hLvwoow3XTk) | Connects trace IDs, logs, metrics, and lifecycle evidence. | Audit event and observability fields. |

## Learning Sequence

| Seq | Concept IDs | Concepts | Recommended Videos | Required Output | Coverage Notes |
|---:|---|---|---|---|---|
| 1 | `consulting.output`, `issue_tree`, `hypothesis_learning` | Define output, build issue tree, write weakness repair goals. | [Hypothesis-based problem solving](https://www.youtube.com/watch?v=TBvJzXxRuxs); [McKinsey Issue Tree Explained](https://www.youtube.com/watch?v=aEQ90SjYOlo) | One-sentence role/system map; issue tree. | Day 1 begins by turning vague AI terms into reviewable system questions. |
| 2 | `source_coding`, `claim_table`, `evidence_rating` | Code public sources into comparable claims. | [Qualitative Coding Tutorial](https://www.youtube.com/watch?v=8MHkVtE_sVw); [Thematic Analysis Step by Step](https://www.youtube.com/watch?v=rvMf1cbctYM) | Source claim table with confidence and next validation. | Supports the Day 1 consulting learning loop. |
| 3 | `domain_map`, `stakeholder_map`, `workflow_map` | Map data flow, permission flow, responsibility flow, latency flow, and cost flow. | [Business Process Mapping 101](https://www.youtube.com/watch?v=zGB9SScvoQU); [Stakeholder Management](https://www.youtube.com/watch?v=-tNHplQ_-hw) | Five-flow domain map. | Keeps Day 1 grounded in enterprise delivery, not only model behavior. |
| 4 | `architecture_map`, `interface_map`, `c4_model` | Draw architecture as system boundary and interface map. | [C4 model architecture diagrams](https://www.youtube.com/watch?v=x2-rSnhpw0g); [First Architecture Diagram](https://www.youtube.com/watch?v=FS_M3s2BL8M) | Initial AI Gateway architecture diagram. | Diagram must expose boundaries, not decorate a slide. |
| 5 | `http_request`, `http_response`, `route`, `headers`, `body` | Read an HTTP request and response as an API contract. | [Parts of an HTTP Request](https://www.youtube.com/watch?v=pHFWGN-upGM); [What Is REST API?](https://www.youtube.com/watch?v=-mN3VyJuCjM) | Filled request-contract warm-up. | Required before drawing the AI Gateway. |
| 6 | `status_code`, `200`, `400`, `401`, `403`, `404`, `429`, `500` | Interpret gateway status paths. | [HTTP Status Codes Explained](https://www.youtube.com/watch?v=qmpUfWN7hh4) | Status-code mapping for allow, deny, malformed, rate-limit, and failure paths. | Day 2 mock gateway must expose meaningful HTTP outcomes. |
| 7 | `json_object`, `json_schema`, `pydantic`, `schema_validation` | Validate request/response shapes. | [What is JSON Schema](https://www.youtube.com/watch?v=kK-_gL7Vsc0); [Pydantic Tutorial](https://www.youtube.com/watch?v=M81pfi64eeM) | Request schema and response schema draft. | Schema validation is a system control before model/tool execution. |
| 8 | `request_lifecycle`, `handler`, `log` | Trace route -> handler -> controlled work -> log -> response. | [Full Request-Response Lifecycle](https://www.youtube.com/watch?v=xv0Be4QfkH0); [FastAPI Handles Requests](https://www.youtube.com/watch?v=tGD3653BrZ8) | 10-15 step request lifecycle baseline. | The lifecycle is more important than a static diagram. |
| 9 | `authentication`, `session`, `token`, `jwt`, `oauth2`, `oidc`, `bearer_token` | Verify who the caller is. | [OAuth and OpenID Connect](https://www.youtube.com/watch?v=t18YB3xDfXI); [JWT, OAuth2, and More](https://www.youtube.com/watch?v=xJA8tP74KD0) | Trusted identity fields. | Client-provided identity cannot be final authority. |
| 10 | `authorization`, `identity`, `role`, `permission`, `rbac`, `abac` | Decide what the caller may do. | [RBAC vs ABAC](https://www.youtube.com/watch?v=rvZ35YW4t5k); [Authorization Explained](https://www.youtube.com/watch?v=DT6Zy1X3ytM) | Policy worksheet. | Distinguishes logged-in from allowed. |
| 11 | `owasp`, `asvs`, `least_privilege`, `deny_by_default`, `server_side_authorization` | Map standards to concrete access-control behavior. | [OWASP Top Ten to ASVS](https://www.youtube.com/watch?v=nvzMN5Z8DJI); [API Security Tips](https://www.youtube.com/watch?v=6WZ6S-qmtqY) | OWASP/NIST mapping note. | Standards are used as control vocabulary, not decorative citations. |
| 12 | `policy_engine`, `policy_gate`, `allow`, `deny`, `review_required`, `policy_drift` | Evaluate structured policy decisions. | [OPA Quickstart](https://www.youtube.com/watch?v=M7IwpC9WpIg); [OPA Intro and Deep Dive](https://www.youtube.com/watch?v=hENwFyrtm1g) | Minimum policy table. | Day 1 requires allow/deny/review paths. |
| 13 | `api_gateway`, `traffic_routing`, `rate_limit`, `quota`, `api_logs` | Understand API Gateway as HTTP/API boundary. | [What is API Gateway?](https://www.youtube.com/watch?v=6ULyxuHKxg8) | API Gateway row in gateway type map. | API Gateway is not the same as AI Gateway, but it is the practical external boundary. |
| 14 | `serverless_api`, `lambda`, `vercel_function`, `cloudflare_worker`, `cloud_hosting` | Separate serverless hosting from backend trust responsibility. | [Lambda + API Gateway Tutorial](https://www.youtube.com/watch?v=C0S01rnN-Os); [AWS Serverless Full Course](https://www.youtube.com/watch?v=5rG-YgTHMC8) | Serverless API boundary worksheet. | Serverless changes hosting, not authorization/audit duties. |
| 15 | `localhost`, `emulator`, `self_hosted_serverless_like`, `plain_backend` | Distinguish local development models. | [Create REST API with API Gateway and Lambda](https://www.youtube.com/watch?v=jgpRAiar2LQ) | Localhost vs emulator note. | Prevents confusing local FastAPI with serverless. |
| 16 | `sync_api`, `async_api`, `queue`, `worker`, `webhook` | Route long-running work outside synchronous request paths. | [Asynchronous Architecture Explained](https://www.youtube.com/watch?v=TyRhDxjVn3k); [How WebHook works](https://www.youtube.com/watch?v=oQaJn6RdA3g) | Short path / long path gateway design. | Needed for audio, batch, review, and side-effect workflows. |
| 17 | `idempotency`, `retry`, `side_effect`, `duplicate_prevention` | Make retries safe for side-effect tools. | [Idempotency](https://www.youtube.com/watch?v=XAccGbtl3Z8); [Idempotency Keys](https://www.youtube.com/watch?v=vlJtT3zkBMw) | Idempotency-key design note. | Required for ticket/email/write-back actions. |
| 18 | `llm_gateway`, `ai_gateway`, `model_routing`, `fallback`, `cost_tracking` | Understand AI/LLM Gateway concerns. | [What is an LLM Gateway?](https://www.youtube.com/watch?v=NXS3N9JY9dY); [LiteLLM Gateway](https://www.youtube.com/watch?v=mwP4sdp7gW0) | AI/LLM Gateway row in gateway type map. | Establishes gateway concerns before agent governance. |
| 19 | `control_plane`, `ai_gateway_boundary`, `agent_gateway` | Treat AI Gateway as identity/policy/tool/data/audit/review control plane. | [Introducing Agent Gateway](https://www.youtube.com/watch?v=SomP92JWPmE); [Top 5 AI Gateway Use Cases](https://www.youtube.com/watch?v=A1xIBCE0mcA) | Control-plane architecture diagram. | Central Day 1 claim. |
| 20 | `agent_orchestrator`, `agent_workflow`, `bounded_task`, `multi_agent` | Place agents inside governed workflows. | [Building AI Agent Systems](https://www.youtube.com/watch?v=fCHe_fOqlYA); [Multi Agent Systems Explained](https://www.youtube.com/watch?v=sWH0T4Zez6I) | Agent boundary in component table. | Agent is not a synonym for chatbot. |
| 21 | `tool_use`, `function_calling`, `tool_registry`, `tool_broker`, `tool_schema` | Treat tool calls as controlled API actions. | [What is Tool Calling?](https://www.youtube.com/watch?v=h8gMhXYAv1k); [Function Calling Tutorial](https://www.youtube.com/watch?v=aqdWSYWC_LI) | Tool worksheet. | Covers read-only vs side-effect tool distinction. |
| 22 | `structured_output`, `llm_proposes_gateway_enforces`, `action_schema` | Use LLM output as proposal, not authority. | [Structured Outputs, Function Calling, MCP](https://www.youtube.com/watch?v=HmneQx1maCI); [Structured Outputs with Pydantic](https://www.youtube.com/watch?v=3Z03fwH1I7s) | Action extraction schema. | Supports policy-first execution. |
| 23 | `free_text`, `selected_list`, `hybrid_request`, `client_hints`, `action_decomposition`, `slot_filling`, `confidence`, `fallback` | Convert natural language into structured actions. | [LLM Function Calling Explained](https://www.youtube.com/watch?v=9DThnOIue4I) | Normalized action plan. | Complex prompts need multiple candidates, not one label. |
| 24 | `mcp`, `memory_scope`, `provenance`, `agent_memory`, `connector_boundary` | Govern external tools, shared memory, and provenance. | [What is MCP?](https://www.youtube.com/watch?v=eur8dUO9mvE); [Memory in AI agents](https://www.youtube.com/watch?v=UF230UuclZM) | Memory/connector boundary note. | Prevents ad hoc integrations and memory leakage. |
| 25 | `rag`, `embedding`, `vector_db`, `retrieval`, `generation` | Understand the basic RAG path. | [RAG Explained For Beginners](https://www.youtube.com/watch?v=_HQ2H_0Ayy0) | RAG data path. | RAG is allowed knowledge retrieval, not generic context stuffing. |
| 26 | `chunking`, `metadata`, `hybrid_search`, `reranker`, `top_k`, `threshold` | Improve retrieval precision and filterability. | [Advanced RAG Techniques](https://www.youtube.com/watch?v=sGvXO7CVwc0); [Chunking Strategies in RAG](https://www.youtube.com/watch?v=pIGRwMjhMaQ) | RAG schema notes. | Covers retrieval fields used later in Day 4. |
| 27 | `faithfulness`, `citation`, `abstain`, `ragas`, `source_id`, `rag_acl_drift` | Evaluate source-grounded answers. | [RAG Evaluation](https://www.youtube.com/watch?v=7_LTU0LA374); [Why LLMs Hallucinate](https://www.youtube.com/watch?v=cfqtFvWOfg0) | Source/citation evidence note. | Missing source evidence becomes audit risk. |
| 28 | `guardrail`, `prompt_injection`, `data_exfiltration`, `owasp_llm_top_10` | Map LLM risks to system controls. | [OWASP Top 10 for LLM Applications](https://www.youtube.com/watch?v=cYuesqIKf9A); [Prompt Injection Attack](https://www.youtube.com/watch?v=jrHRe9lSqqA) | Risk-control map seeds. | Prompt-only governance is insufficient. |
| 29 | `pii`, `dlp`, `redaction`, `data_classification` | Detect and reduce sensitive-data exposure. | [Data Loss Prevention](https://www.youtube.com/watch?v=OjMnlizubTU); [Microsoft Presidio Anonymization](https://www.youtube.com/watch?v=4GuK9sPUvus) | PII/redaction controls. | PII can appear in input, retrieval, output, logs, or memory. |
| 30 | `human_in_the_loop`, `review_queue`, `approval_workflow` | Treat review as workflow state. | [Human In The Loop with AI](https://www.youtube.com/watch?v=9iS-YYLIXiw); [Human-in-the-Loop](https://www.youtube.com/watch?v=qeuRQAityB8) | `review_required` path. | Review is a control point, not a failure. |
| 31 | `nist_ai_rmf`, `ai_governance`, `risk_vocabulary` | Use governance language for risk framing. | [NIST RMF Explained](https://www.youtube.com/watch?v=0oeD2Wf25wY) | NIST mapping note. | Keeps boundaries as operating controls. |
| 32 | `red_teaming`, `eval_harness`, `regression_test` | Build repeatable security/eval tests. | [Promptfoo Red Teaming](https://www.youtube.com/watch?v=y6Dlsz5P8s8); [What is LLM Red Teaming?](https://www.youtube.com/watch?v=-OUmHDuaPPA) | Red-team seed list. | Prepares for Day 3 and Day 4. |
| 33 | `audit_log`, `trace_id`, `logs`, `metrics`, `traces`, `opentelemetry` | Record lifecycle evidence. | [Logging Best Practices](https://www.youtube.com/watch?v=I2mWnh66Bkg); [OpenTelemetry](https://www.youtube.com/watch?v=hLvwoow3XTk) | Audit event fields. | TA should reconstruct a request after failure. |
| 34 | `p50`, `p95`, `p99`, `tail_latency` | Measure average and tail latency. | [P50, P95, P99](https://www.youtube.com/watch?v=9rlGSahksLQ); [Latency Metrics](https://www.youtube.com/watch?v=lJ4NEMNBeS4) | Latency field list. | Needed for voice and inference survival terms. |
| 35A | `audio_signal`, `waveform`, `sample_rate`, `pcm`, `spectrogram`, `mel_spectrogram`, `mfcc` | Turn raw audio into model-readable and deployable data. | [Audio Signal Processing for Machine Learning](https://www.youtube.com/watch?v=iCwMQJnKk2c) | `modules/08-voice-ai-systems/audio-signal-processing-for-machine-learning-video-notes.md` | Prerequisite bridge before ASR, VAD, diarization, and realtime voice labs. |
| 35 | `asr`, `speech_to_text`, `speech_synthesis` | Understand voice pipeline entry and exit. | [Automatic Speech Recognition Overview](https://www.youtube.com/watch?v=q67z7PTGRi8); [What is Speech Recognition?](https://www.youtube.com/watch?v=uSNUmJffK4c) | Voice pipeline terms. | Day 1 survival terms include voice even if implementation starts later. |
| 36 | `vad`, `speech_segment`, `silero_vad`, `webrtcvad` | Detect speech activity and segment audio. | [Voice Activity Detection](https://www.youtube.com/watch?v=yADlHILxlDw); [Silero VAD](https://www.youtube.com/watch?v=HUbYXGeR8_c) | VAD boundary note. | VAD influences latency and ASR cost. |
| 37 | `diarization`, `speaker_attribution`, `speaker_embedding`, `overlap_speech` | Identify who spoke when. | [pyannote speaker diarization](https://www.youtube.com/watch?v=37R_R82lfwA); [Whisper Speaker Diarization](https://www.youtube.com/watch?v=MVW746z8y_I) | Diarization risk notes. | Speaker errors change responsibility and audit meaning. |
| 38 | `tts`, `voice_clone`, `first_audio_latency`, `mos` | Generate speech response and measure user experience. | [Text-to-Speech and Voice Cloning](https://www.youtube.com/watch?v=4Lbox-d0UcE); [Introduction to TTS](https://www.youtube.com/watch?v=TZIBQ24UCgA) | TTS latency notes. | TTS is part of end-to-end customer acceptance. |
| 39 | `wer`, `cer`, `der`, `jer`, `voice_eval` | Evaluate speech recognition and diarization. | [Word Error Rate Explained](https://www.youtube.com/watch?v=hoEWRdHi7dI); [Evaluation of Speaker Diarization Systems](https://www.youtube.com/watch?v=9Fdlj3zZIkM) | Voice eval metric table. | Average WER is not enough for enterprise keywords and speakers. |
| 40 | `docker`, `containerization`, `deployment_boundary` | Package services for repeatable deployment. | [Docker Crash Course](https://www.youtube.com/watch?v=pg19Z8LL06w); [Containerization Explained](https://www.youtube.com/watch?v=0qotVMX-J5s) | Docker survival note. | Docker is packaging, not production readiness by itself. |
| 41 | `kubernetes`, `pod`, `service`, `deployment`, `orchestration` | Understand K8s deployment primitives. | [Kubernetes Explained](https://www.youtube.com/watch?v=TlHvYWVUZyc); [Kubernetes YAML Deployment and Service](https://www.youtube.com/watch?v=qmDzcu5uY1I) | K8s survival note. | K8s appears as deployment boundary, not Day 1 lab requirement. |
| 42 | `gpu_device_plugin`, `gpu_scheduling`, `ai_cluster` | See how K8s schedules GPU workloads. | [GPU Management in Kubernetes](https://www.youtube.com/watch?v=jbpIFCkEEng); [GPUs in Kubernetes for AI Workloads](https://www.youtube.com/watch?v=zuRKdveFuZ4) | GPU plugin note. | Prevents assuming GPUs are automatically schedulable. |
| 43 | `vllm`, `sglang`, `model_router`, `inference_data_plane` | Place model serving behind the gateway. | [What is vLLM?](https://www.youtube.com/watch?v=McLdlg5Gc9s); [SGLang Deep Dive](https://www.youtube.com/watch?v=TWbrz5rSfFI) | Model serving boundary note. | vLLM/SGLang do not replace AI Gateway. |
| 44 | `kv_cache`, `paged_attention`, `prefix_caching`, `ttft`, `tpot` | Understand inference memory and latency drivers. | [KV Cache](https://www.youtube.com/watch?v=80bIUggRJf4); [vLLM and PagedAttention](https://www.youtube.com/watch?v=5ZlavKF_98U) | Inference metric notes. | Connects context length, concurrency, latency, and GPU memory. |
| 45 | `quantization`, `vram`, `quality_tradeoff` | Estimate model memory and accuracy tradeoffs. | [Quantizing LLMs](https://www.youtube.com/watch?v=3EDI4akymhA); [How Much VRAM My LLM Needs](https://www.youtube.com/watch?v=IJufykNYGRs) | VRAM/quantization note. | Required by Day 1 survival terms and Day 5 handoff. |
| 46 | `final_submission`, `architecture_diagram`, `component_table`, `request_lifecycle`, `risk_control_map` | Assemble Day 1 evidence. | Reuse sequence 4, 8, 12, 19, 21, 28, and 33. | Complete Day 1 submission. | The outcome is reviewable evidence, not watched-video completion. |

## Coverage Index

```yaml
consulting_learning_method:
  covered_by: [1, 2, 3]
  concepts:
    - define_output
    - fifty_survival_terms
    - draw_first_then_correct
    - eight_initial_hypotheses
    - public_source_dossier
    - claim_coding
    - consensus_and_dissent

domain_and_architecture:
  covered_by: [3, 4]
  concepts:
    - data_flow
    - permission_flow
    - responsibility_flow
    - latency_flow
    - cost_flow
    - value_chain
    - stakeholder_map
    - workflow
    - technical_architecture
    - risk_map

api_contract:
  covered_by: [5, 6, 7, 8]
  concepts:
    - http_method
    - route
    - headers
    - json_body
    - request
    - response
    - status_code
    - json_object
    - json_schema
    - pydantic
    - route_handler_log

identity_policy_access_control:
  covered_by: [9, 10, 11, 12]
  concepts:
    - authentication
    - authorization
    - identity
    - role
    - permission
    - session
    - jwt
    - oauth2
    - oidc
    - rbac
    - abac
    - least_privilege
    - deny_by_default
    - server_side_authorization
    - allow
    - deny
    - review_required

serverless_and_runtime_boundaries:
  covered_by: [13, 14, 15, 16, 17]
  concepts:
    - api_gateway
    - serverless_api
    - cloud_hosting
    - localhost
    - emulator
    - self_hosted_serverless_like_platform
    - synchronous_api
    - asynchronous_api
    - queue
    - worker
    - webhook
    - idempotency

ai_gateway_agent_tool:
  covered_by: [18, 19, 20, 21, 22, 23, 24]
  concepts:
    - llm_gateway
    - ai_gateway
    - control_plane
    - data_plane
    - agent_orchestrator
    - tool_use
    - tool_registry
    - tool_broker
    - schema_validation
    - structured_output
    - free_text_request
    - selected_list_request
    - hybrid_request
    - client_hints
    - normalized_request_envelope
    - action_decomposition
    - slot_filling
    - confidence_threshold
    - safe_default
    - mcp
    - memory_scope
    - provenance

rag_and_evaluation:
  covered_by: [25, 26, 27]
  concepts:
    - rag
    - embedding
    - vector_db
    - chunking
    - metadata
    - hybrid_search
    - reranker
    - top_k
    - top_p
    - threshold
    - abstain
    - faithfulness
    - citation
    - source_id
    - rag_acl_drift

security_governance_review:
  covered_by: [28, 29, 30, 31, 32]
  concepts:
    - guardrail
    - prompt_injection
    - data_exfiltration
    - owasp_llm_top_10
    - pii_detection
    - dlp
    - redaction
    - data_classification
    - human_in_the_loop
    - review_queue
    - nist_ai_rmf
    - red_teaming
    - eval_harness
    - regression_test

observability_and_audit:
  covered_by: [33, 34]
  concepts:
    - audit_log
    - trace_id
    - logs
    - metrics
    - traces
    - opentelemetry
    - p50_latency
    - p95_latency
    - p99_latency
    - tail_latency

voice_ai_survival_terms:
  covered_by: [35, 36, 37, 38, 39]
  concepts:
    - asr
    - tts
    - vad
    - diarization
    - speaker_embedding
    - speaker_attribution
    - overlap_speech
    - hotword
    - contextual_biasing
    - wer
    - cer
    - der
    - jer
    - mos
    - first_audio_latency

deployment_inference_survival_terms:
  covered_by: [40, 41, 42, 43, 44, 45]
  concepts:
    - docker
    - containerization
    - kubernetes
    - pod
    - service
    - deployment
    - gpu_device_plugin
    - vllm
    - sglang
    - model_serving
    - model_router
    - kv_cache
    - paged_attention
    - prefix_caching
    - ttft
    - tpot
    - quantization
    - vram

day_1_artifacts:
  covered_by: [46]
  artifacts:
    - domain_brief_md
    - ai_gateway_architecture_diagram
    - component_responsibility_table
    - request_lifecycle
    - risk_control_map
```

## Agent Selection Rules

Use these rules when generating a shorter assignment from this map:

1. Always include sequences 1, 4, 5, 10, 13, 18, 19, 21, 25, 28, 33, and 46
   for any Day 1 compressed path.
2. If time is limited to ten videos, use the Top 10 Priority Videos section.
3. If the learner already knows web APIs, sequences 5-8 can be skimmed, but the
   request-contract warm-up must still be completed.
4. If the learner already knows Docker/K8s, sequences 40-42 can be treated as
   survival-term review, not implementation practice.
5. Do not skip sequences 9-12 or 28-33; identity, policy, security, review, and
   audit are the main difference between an AI demo and enterprise AI system.
6. Watching videos is not completion evidence. Completion evidence is the Day 1
   artifact set listed in the reading contract.
