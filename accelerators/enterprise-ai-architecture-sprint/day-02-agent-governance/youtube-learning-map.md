# Day 2 YouTube Learning Map

```yaml
artifact_type: ai_agent_readable_learning_map
accelerator: enterprise-ai-architecture-sprint
day: 2
day_topic: Agent Governance Framework
primary_language: zh-TW
created_for: Day 2 video-based learning support
retrieved_at: 2026-06-20
source_scope:
  - Existing Day 2 course package concepts
  - Public YouTube instructional videos
source_boundary:
  - No private transcripts
  - No customer secrets
  - No credentials
  - No identifiable personal data
agent_use:
  - Use top_10_priority_videos for the first viewing assignment
  - Use learning_sequence for complete Day 2 coverage
  - Use coverage_index to verify that every Day 2 concept has video support
  - Use agent-governance-framework-video-notes.md as the companion note for the first priority video
```

## Reading Contract For Agents

This file maps existing Day 2 concepts to public YouTube videos. It does not
introduce new Day 2 requirements. The target Day 2 evidence remains:

1. Day 1-to-Day 2 gateway alignment and message mediation note.
2. Governance layer map.
3. Common-vs-adapter table.
4. Agent registration record.
5. Tool boundary table.
6. Memory scope rule.
7. Policy gate record.
8. Message mediation contract.
9. Audit event schema.
10. Risk-control map.
11. Day 3 red-team seed list.

Each sequence item uses this shape:

```yaml
sequence_id: stable order key
concepts: Day 2 concepts covered
recommended_videos: YouTube links
required_output: artifact evidence after watching
coverage_notes: why this belongs in Day 2
```

## Top 10 Priority Videos

These are the first videos to watch before the full sequence. They establish
the first-pass Day 2 mental model: prompt is not a boundary, gateway contract,
identity, control plane, policy decision, tool boundary, human review, RAG
access control, risk vocabulary, and audit evidence. The complete learning
sequence below covers the remaining message mediation, declassification,
confused deputy, replay, and Day 3 red-team details.

| Rank | Video | Why Watch First | Day 2 Output |
|---:|---|---|---|
| 1 | [Building an AI Agent Governance Framework: 5 Essential Pillars](https://www.youtube.com/watch?v=5hK7pQsvpy0) ([notes](agent-governance-framework-video-notes.md)) | Frames agent governance as runtime control, not policy prose or prompt wording. | One-paragraph Day 2 thesis. |
| 2 | [What is an AI Gateway?](https://www.youtube.com/watch?v=88q_RAHJFlo) | Establishes the AI Gateway as the entry/control boundary for model and agent traffic. | Gateway alignment note baseline. |
| 3 | [Authorization EXPLAINED! RBAC vs ABAC vs ACL](https://www.youtube.com/watch?v=7CG5VQafaTI) | Separates identity, role, permission, and attribute-based decisions. | Trusted identity and allowed-user fields. |
| 4 | [Data Plane vs. Control Plane](https://www.youtube.com/watch?v=Ep1QW-wOmgc) | Explains why policy/audit/review belong in the control plane, not model output. | Control-plane vs data-plane section. |
| 5 | [Open Policy Agent Intro & Deep Dive](https://www.youtube.com/watch?v=hENwFyrtm1g) | Shows policy as a structured decision point. | Policy gate record. |
| 6 | [Build a Tool Calling Agent](https://www.youtube.com/watch?v=eKmj_xXPX0A) | Shows tool calls as structured actions, not free-form model authority. | Tool boundary table. |
| 7 | [How to Build Human-in-the-Loop for AI Agents](https://www.youtube.com/watch?v=7GOxUgVTz3s) | Shows review as a workflow state around risky tool calls. | Review path and `pending_review` behavior. |
| 8 | [Building a permissions system for RAG applications](https://www.youtube.com/watch?v=cK9RrbcyfBs) | Connects retrieval to access control and metadata. | Data boundary and source filter rows. |
| 9 | [OWASP Top 10 for LLMs](https://www.youtube.com/watch?v=de9UPN7yD5U) | Gives prompt injection, data leakage, excessive agency, and tool-risk vocabulary. | Risk-control map. |
| 10 | [OpenTelemetry Fundamentals: Traces, Metrics & Logs Explained](https://www.youtube.com/watch?v=ItZouStG_nk) | Explains trace/log/metric vocabulary used by audit evidence. | Audit event schema fields. |

## Learning Sequence

| Seq | Concept IDs | Concepts | Recommended Videos | Required Output | Coverage Notes |
|---:|---|---|---|---|---|
| 1 | `governance.thesis`, `prompt_not_boundary`, `system_contract` | Enterprise agent 不是靠 prompt 治理；真正的邊界是 registry、policy、tool/data/memory/message boundary、declassification、audit、review、evaluation feedback。 | [Building an AI Agent Governance Framework](https://www.youtube.com/watch?v=5hK7pQsvpy0) ([notes](agent-governance-framework-video-notes.md)); [OWASP Top 10 for LLMs](https://www.youtube.com/watch?v=de9UPN7yD5U) | Day 2 thesis sentence. | 對應 handout 第 0-1 章。 |
| 2 | `campus_it`, `staff_only`, `ticket_spam`, `pii_memory` | Campus IT Helpdesk 情境：public FAQ/VPN/status 可查；staff-only SOP 不可查；ticket submit 要 review；PII 不進 shared memory。 | [Guide to Architect Secure AI Agents](https://www.youtube.com/watch?v=UMYtqHptYvA); [Presidio in Action](https://www.youtube.com/watch?v=_dAzcCk-3U4) | Scenario boundary note. | 先建立公共安全案例，再進 artifacts。 |
| 3 | `ai_gateway`, `post_gateway_requests`, `gateway_contract` | Day 1 的 `POST /gateway/requests` 接到 Day 2 的 schema validation、identity、action extraction、registry、policy、tool/data/memory/message check、review、audit、HTTP outcome。 | [What is an AI Gateway?](https://www.youtube.com/watch?v=88q_RAHJFlo); [Workshop 101: Enterprise-Grade AI Platform with Kong AI Gateway](https://www.youtube.com/watch?v=P8hNtNW3I4s) | Gateway alignment outline. | Day 2 必須接回 Day 1 route，而不是獨立治理表格。 |
| 4 | `request_schema`, `json_schema`, `pydantic`, `http_outcomes` | Request fields：`session_token`、`channel`、`raw_message`、`client_hints`、`requested_agent`；outcomes：`200`、`202`、`400`、`401`、`403`。 | [API Request Validation with JSON Schema](https://www.youtube.com/watch?v=PvGidZovN4c); [FastAPI in 15 Minutes](https://www.youtube.com/watch?v=BPRKBQwEHe0); [Learn HTTP Status Codes In 10 Minutes](https://www.youtube.com/watch?v=wJa5CTIFj7U) | Request/response contract table. | Schema failure and auth failure must be visible system outcomes. |
| 5 | `trusted_identity`, `rbac`, `abac`, `client_hints_untrusted` | `client_hints.role`、requested department、requested agent 都不是可信權限來源；可信 identity 由 server-side token/session 解析。 | [Authorization EXPLAINED! RBAC vs ABAC vs ACL](https://www.youtube.com/watch?v=7CG5VQafaTI); [Get started with OAuth 2.0 On-Behalf-Of flow](https://www.youtube.com/watch?v=S2uYPgxBbMw) | Trusted identity source row. | 支撐 deny/review 決策與 confused deputy 防護。 |
| 6 | `control_plane`, `data_plane`, `enforcement`, `evidence` | Control plane 決定是否可做、誰可做、是否 review、留下什麼 evidence；data plane 查資料、呼叫工具、產生回答。 | [Data Plane vs. Control Plane](https://www.youtube.com/watch?v=Ep1QW-wOmgc) | Control/data plane comparison. | 防止把權限決策交給 model。 |
| 7 | `governance_layer_map`, `identity`, `registry`, `policy`, `audit` | 畫出 User/Channel -> Auth/RBAC -> AI Gateway -> Agent Registry -> Policy Gate -> Tool Broker -> RAG Connector -> Memory Store -> Message Mediation -> Declassifier -> Model Runtime -> Guardrail -> Audit -> Review -> Evaluation/Red Team。 | [Building an AI Agent Governance Framework](https://www.youtube.com/watch?v=5hK7pQsvpy0); [AI Gateway for Enterprise Agentic Traffic Flows](https://www.youtube.com/watch?v=emwIyhXhMtU) | Governance layer map. | 每層都要有 responsibility、enforcement、evidence。 |
| 8 | `agent_registry`, `owner`, `task_scope`, `risk_class`, `allowed_users` | Agent registration 是 Gateway 可讀的 configuration contract：owner、task_scope、risk_class、allowed users/tools/data、memory、message channels、output classification、approval、eval、red-team、audit。 | [Entra Agent Registry: The Corporate Yellow Pages for AI Agents](https://www.youtube.com/watch?v=yiTT7Etl4OY); [MCP Server & Agent Security at Scale](https://www.youtube.com/watch?v=78sgXVNf808) | Agent registration YAML. | Registration 不是自然語言 agent inventory。 |
| 9 | `tool_calling`, `tool_schema`, `tool_permission`, `side_effect` | Tool schema 管呼叫格式；tool permission 管誰能呼叫、是否 side effect、timeout、retry、rate limit、idempotency、audit、review。 | [Build a Tool Calling Agent](https://www.youtube.com/watch?v=eKmj_xXPX0A); [How to Build Human-in-the-Loop for AI Agents](https://www.youtube.com/watch?v=7GOxUgVTz3s) | Tool boundary table. | 對應 read-only、side-effect、high-risk side-effect。 |
| 10 | `human_review`, `review_state`, `pending_review`, `safe_user_message` | High-risk 或 side-effect action 建立 pending review item；模型說 approved 不算批准；review 需要 reviewer role、review ID、status、safe user message。 | [Add Human in the Loop Control Directly to Tools in AI Agent Workflows](https://www.youtube.com/watch?v=snI7BvB4Qxg); [Complete Guide to Human Approval in AI Agents](https://www.youtube.com/watch?v=-mbPPno8OWE) | Review path in policy output. | `submit_ticket` 應回 pending review，不直接執行。 |
| 11 | `data_boundary`, `rag_acl`, `metadata_filter`, `source_id`, `freshness` | Data boundary 用 source allowlist、metadata filter、access_level、document version、freshness、source citation 控制 retrieval。 | [Building a permissions system for RAG applications](https://www.youtube.com/watch?v=cK9RrbcyfBs); [How to Get LLM Answers With Sources](https://www.youtube.com/watch?v=69gUQ4XHg0o) | Data source table and retrieval rule. | Staff-only 文件不應先進 model context 再叫模型不要說。 |
| 12 | `memory_scope`, `retention`, `sharing`, `pii_rule`, `deletion_rule` | Memory scope 定義 read/write/retention/shared_memory/PII/deletion/audit；memory 是資料保留與洩漏邊界。 | [Approaches for Managing Agent Memory](https://www.youtube.com/watch?v=3aS1A-0775s); [Protect User Data in AI Agents with PII Redaction Middleware](https://www.youtube.com/watch?v=2HZ9c089jM8) | Memory scope YAML. | 防止學號、密碼、ticket details 進入 shared memory。 |
| 13 | `pii_redaction`, `declassification`, `output_classification`, `safe_release` | Declassification 是 redaction、summarization、field removal、policy check、human review、output classification、audit 的 controlled release。 | [Presidio in Action](https://www.youtube.com/watch?v=_dAzcCk-3U4); [How to Scrub Sensitive Data Before it Reaches Your LLM](https://www.youtube.com/watch?v=Ql2gLHWuX7M) | Declassification/redaction rule. | LLM reviewer 可輔助，但不能取代 deterministic checks。 |
| 14 | `policy_gate`, `decision_api`, `opa`, `allow_deny_review` | Policy gate 是 decision API；input 包含 request、user、agent、action、tool/data/memory/message/output context；output 包含 decision、reason、reviewer、safe message、audit fields。 | [Open Policy Agent Intro & Deep Dive](https://www.youtube.com/watch?v=hENwFyrtm1g); [OPA Quickstart Guide with Simple Rego Rules](https://www.youtube.com/watch?v=M7IwpC9WpIg) | Policy gate YAML and examples. | 必須能回 `allow`、`deny`、`review`。 |
| 15 | `cedar`, `principal_action_resource_context`, `authorization_vocabulary` | Cedar / Verified Permissions 用 principal、action、resource、context 幫學生理解 structured authorization request。 | [Amazon Verified Permissions - Policy Creation and Testing Primer](https://www.youtube.com/watch?v=Gi3joEySMPQ); [Write and enforce fine grained application permissions using Policy as Code](https://www.youtube.com/watch?v=41t3PZNsSpk) | Policy input shape note. | Cedar 是概念校準工具，不是 Day 2 必修實作。 |
| 16 | `message_mediation`, `broker_acl`, `producer_consumer_identity`, `schema_registry` | 跨 agent/process/tool/retrieval service 不能直連；要走 gateway、broker、queue 或 tool gateway，具備 identity、ACL、schema、classification、retention、audit。 | [Kafka Security: Authorization with Default and Custom Authorizers](https://www.youtube.com/watch?v=Jb7XTUFhUHY); [How to Write, Manage, and Register Schemas](https://www.youtube.com/watch?v=ovIsHhIrie8) | Message mediation contract. | Broker 不是完整安全邊界，只是 mediation layer 的一部分。 |
| 17 | `raw_payload`, `dlq`, `retention`, `replay`, `idempotency` | Raw privileged payload 不進 shared topic/log/cache/trace/DLQ；message 要有 classification、purpose、expires_at、trace_id；consume 前重新 policy check。 | [Messaging, Event-Driven Architecture, and Backpressure Explained](https://www.youtube.com/watch?v=XWX8jOqtPpk); [The RIGHT Way to Handle Retries & Dead Letter Queue](https://www.youtube.com/watch?v=2fXWjv1lsAA) | Replay/DLQ rows in message contract. | 支撐 broker payload leakage 與 replay attack 防護。 |
| 18 | `confused_deputy`, `original_user`, `delegation`, `capability_token` | 低權限 agent 不能誘使高權限 agent/tool 代讀；policy 檢查 original user、requesting agent、resource、purpose、output classification。 | [Understand the Confused Deputy Problem](https://www.youtube.com/watch?v=viVoZBc-33s); [Capability-Based Authorization for AI Agents](https://www.youtube.com/watch?v=bw928cFShK4) | Confused-deputy risk-control row. | 高權限 service 有讀取權，不代表可把結果交給任何 requester。 |
| 19 | `audit_event`, `trace_id`, `append_only`, `structured_logging`, `otel` | Audit event 要重建 lifecycle：identity、agent、policy、source、tool、memory、message channel、output classification、review、HTTP outcome；避免存 password/token/full PII/raw sensitive prompt。 | [OpenTelemetry Fundamentals](https://www.youtube.com/watch?v=ItZouStG_nk); [12 Logging BEST Practices in 12 minutes](https://www.youtube.com/watch?v=I2mWnh66Bkg); [Event Sourcing Microservice Design Pattern](https://www.youtube.com/watch?v=5fFFlIdCBiw) | Audit event schema. | Audit evidence 不等於 debug log。 |
| 20 | `common_vs_adapter`, `platform_governance`, `scenario_mapping` | Common governance 可跨 Campus IT、Bank、Healthcare、Manufacturing 重用；adapter-specific behavior 只映射特定角色、工具、資料、流程。 | [Building an AI Agent Governance Framework](https://www.youtube.com/watch?v=5hK7pQsvpy0); [NIST AI RMF Playbook Explained](https://www.youtube.com/watch?v=-v2zEkKQv2Y) | Common-vs-adapter table. | 避免每個客戶都重寫治理邏輯。 |
| 21 | `owasp_genai`, `prompt_injection`, `excessive_agency`, `sensitive_disclosure` | 將 OWASP GenAI / LLM Top 10 風險映射到 controls：prompt injection、permission bypass、tool abuse、memory leakage、excessive agency、data leakage。 | [OWASP Top 10 for LLMs](https://www.youtube.com/watch?v=de9UPN7yD5U); [Deep Dive into the OWASP Top 10 for Agentic AI Applications](https://www.youtube.com/watch?v=-vXoC0UvpjY) | Risk taxonomy note. | OWASP 是風險語言，不是背誦清單。 |
| 22 | `risk_control_map`, `required_risks`, `evidence` | Risk-control map 至少包含 tool abuse、memory leakage、permission bypass、confused deputy、broker payload leakage、replay、missing schema field、prompt-only approval、missing audit detail、HTTP outcome mismatch、stale retrieval、prompt injection、excessive agency。 | [AI Model Penetration: Testing LLMs for Prompt Injection & Jailbreaks](https://www.youtube.com/watch?v=xOQW_qMZdlc); [OWASP Top 10 for LLMs](https://www.youtube.com/watch?v=de9UPN7yD5U) | Risk-control map. | 每個 risk 都要有 example、required control、evidence。 |
| 23 | `red_team_seed`, `day3_handoff`, `pass_condition`, `failure_signal` | Red-team seed 必須可執行、可判斷 pass/fail：test_id、threat_category、target_control、input、expected policy/HTTP/audit、pass_condition、failure_signal。 | [Red Teaming of LLM Applications](https://www.youtube.com/watch?v=yalj9BbWqoI); [Test Your AI Like a Hacker, Promptfoo Tutorial](https://www.youtube.com/watch?v=KghDstjwwNA) | Day 3 seed list. | Day 2 每個治理假設都應能轉成 Day 3 測試。 |
| 24 | `nist_ai_rmf`, `govern_map_measure_manage`, `lifecycle` | NIST AI RMF 對應：Govern/Map -> governance artifacts；Measure -> audit/evaluation；Manage -> policy updates/red-team feedback。 | [Mastering AI Risk: NIST's Risk Management Framework Explained](https://www.youtube.com/watch?v=0oeD2Wf25wY); [NIST AI RMF Playbook Explained](https://www.youtube.com/watch?v=-v2zEkKQv2Y) | NIST mapping note. | 大二學生只需理解 risk management 是 lifecycle。 |
| 25 | `implementation_examples`, `fastapi`, `redis`, `postgres`, `opentelemetry`, `presidio`, `kafka` | 技術落地例子：FastAPI/Pydantic、OPA/Cedar、PostgreSQL audit store、Redis session/rate limit、OpenTelemetry、Kafka/Redpanda/RabbitMQ/NATS、Presidio。 | [FastAPI in 15 Minutes](https://www.youtube.com/watch?v=BPRKBQwEHe0); [OpenTelemetry FastAPI Tutorial](https://www.youtube.com/watch?v=m28TTogdcbk); [Confluent Kafka Schema Registry in Python](https://www.youtube.com/watch?v=4wkrEog1AUk) | Implementation mapping note. | 工具名稱只是實作例子；評分重點仍是 artifact quality。 |
| 26 | `real_world_flow`, `step_1_to_11`, `request_to_audit` | 從 request 到 audit 的 11 步：client request、schema validation、identity resolution、action extraction、registry lookup、boundary check、policy decision、message mediation/declassification、human review、audit event、HTTP response。 | Reuse sequence 3, 4, 5, 8, 14, 16, 19. | 11-step lifecycle note. | 這是 Day 2 artifacts 能否實作的主線。 |
| 27 | `common_mistakes`, `prompt_only`, `schema_without_permission`, `final_answer_audit`, `empty_memory_scope`, `broker_as_boundary`, `privileged_agent_reader` | 初學者常見錯誤：只靠 prompt、tool schema 無 permission、audit 只記 final answer、memory 空白、把 broker 當安全邊界、高權限 agent 變代讀器。 | Reuse sequence 9, 12, 16, 18, 19, 21. | Mistake-to-fix table. | 對應 instructor/TA 診斷與 rubric 扣分點。 |
| 28 | `source_boundary`, `public_safe`, `no_credentials`, `no_private_sop` | 案例保持 public-safe：不使用私人逐字稿、客戶秘密、credentials、personal contact routes、salary/offer detail、未公開公司主張、可識別個資、真實 ticket 或真實內部 SOP。 | [Presidio in Action](https://www.youtube.com/watch?v=_dAzcCk-3U4); [NIST AI RMF Playbook Explained](https://www.youtube.com/watch?v=-v2zEkKQv2Y) | Source boundary checklist. | Source boundary 是 Day 2 rubric 的 5 分。 |

## Coverage Index

```yaml
core_thesis_and_case:
  covered_by: [1, 2, 21, 28]
  concepts:
    - prompt_is_not_permission_boundary
    - governance_contract
    - Campus_IT_Helpdesk_Assistant
    - public_it_faq
    - vpn_setup_guide
    - service_status_page
    - staff_account_lock_sop
    - ticket_spam
    - submit_ticket_requires_review
    - reset_password_deny_by_default
    - shared_memory_pii_block
    - public_safe_source_boundary

gateway_alignment:
  covered_by: [3, 4, 5, 26]
  concepts:
    - POST_gateway_requests
    - session_token
    - channel
    - raw_message
    - client_hints
    - requested_agent
    - schema_validation
    - token_identity_resolution
    - server_side_identity
    - action_extraction
    - intent_labels
    - action_candidates
    - risk_labels
    - missing_slots
    - ambiguity
    - confidence
    - recommended_next_step
    - safe_default_low_risk_high_confidence
    - safe_default_high_risk_or_low_confidence
    - registry_lookup
    - policy_decision
    - audited_execution
    - 200_completed
    - 202_pending_review
    - 400_malformed_input
    - 401_invalid_token
    - 403_denied

governance_layers:
  covered_by: [6, 7, 20]
  concepts:
    - control_plane
    - data_plane
    - identity
    - agent_registry
    - tool_boundary
    - data_boundary
    - memory_boundary
    - mediated_message_boundary
    - policy_gate
    - declassifier
    - model_runtime
    - guardrail
    - audit_event_store
    - human_review_queue
    - evaluation_hook
    - red_team_seed
    - responsibility
    - enforcement
    - evidence

agent_registration:
  covered_by: [8]
  concepts:
    - agent_id
    - owner
    - task_scope
    - risk_class
    - allowed_users
    - allowed_tools
    - allowed_data_sources
    - memory_scope
    - allowed_message_channels
    - output_classification
    - approval_required_for
    - evaluation_set
    - red_team_suite
    - audit_events

tool_and_review:
  covered_by: [9, 10]
  concepts:
    - tool_schema
    - tool_permission
    - read_only_tool
    - side_effect_tool
    - high_risk_side_effect_tool
    - timeout
    - retry
    - rate_limit
    - idempotency
    - user_confirmation
    - human_review
    - review_id
    - reviewer_role
    - pending
    - approved
    - rejected
    - safe_user_message

data_memory_declassification:
  covered_by: [11, 12, 13]
  concepts:
    - source_allowlist
    - access_level_metadata
    - metadata_filter
    - document_version
    - freshness
    - source_id
    - citation
    - retrieval_before_context_assembly
    - memory_read
    - memory_write
    - retention
    - sharing
    - deletion_rule
    - pii_rule
    - pii_detection
    - anonymization
    - redaction
    - summarization
    - field_removal
    - output_classification
    - declassification_review

policy_gate:
  covered_by: [14, 15]
  concepts:
    - policy_id
    - applies_to
    - preconditions
    - allowed_actions
    - blocked_actions
    - pii_rule
    - retrieval_rule
    - tool_rule
    - memory_rule
    - message_rule
    - declassification_rule
    - human_review_trigger
    - failure_response
    - audit_fields
    - allow
    - deny
    - review
    - decision_api
    - principal
    - action
    - resource
    - context

message_mediation:
  covered_by: [16, 17, 18]
  concepts:
    - gateway_path
    - broker
    - queue
    - tool_gateway
    - producer_identity
    - consumer_identity
    - topic_acl
    - schema_validation
    - schema_registry
    - classification
    - purpose
    - expires_at
    - trace_id
    - resource_reference
    - retention
    - replay_protection
    - nonce
    - idempotency_key
    - dead_letter_queue
    - raw_payload_block
    - raw_privileged_payload
    - broker_payload_leakage
    - confused_deputy
    - capability_based_delegation

audit_and_observability:
  covered_by: [19]
  concepts:
    - trace_id
    - timestamp
    - user_id_or_hash
    - user_role
    - tenant
    - agent_id
    - request_summary
    - policy_decision
    - policy_reason
    - retrieved_source_ids
    - tool_decisions
    - executed_status
    - memory_decision
    - message_channel
    - output_classification
    - human_review_status
    - review_id
    - http_status
    - outcome
    - declassification_reason
    - rejection_reason
    - pii_minimization
    - no_password_token_full_pii_private_content_raw_sensitive_prompt

risk_control_and_red_team:
  covered_by: [21, 22, 23]
  concepts:
    - tool_abuse
    - memory_leakage
    - permission_bypass
    - confused_deputy
    - broker_payload_leakage
    - replay_of_privileged_result
    - missing_schema_field
    - prompt_only_approval
    - missing_audit_detail
    - http_outcome_mismatch
    - stale_retrieval
    - prompt_injection
    - excessive_agency
    - audit_evasion
    - schema_bypass
    - target_control
    - expected_policy_decision
    - expected_message_channel
    - expected_output_classification
    - expected_http_outcome
    - expected_audit_fields
    - pass_condition
    - failure_signal

risk_framework_and_implementation_examples:
  covered_by: [24, 25]
  concepts:
    - NIST_AI_RMF
    - govern
    - map
    - measure
    - manage
    - FastAPI
    - Pydantic
    - zod
    - OPA
    - Rego
    - Cedar
    - PostgreSQL
    - Redis
    - OpenTelemetry
    - structlog
    - Kafka
    - Redpanda
    - RabbitMQ
    - NATS_JetStream
    - Presidio
```
