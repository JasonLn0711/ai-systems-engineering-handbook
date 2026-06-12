# VOISS Interview Terms Glossary

This glossary stores reusable public-safe terms extracted from
interview-derived learning notes. It is not a transcript archive. It groups
terms by owning system layer and links them to handbook modules for deeper
chapter work.

## AI Gateway

Definition: A control layer that routes and governs access to models, agents,
tools, knowledge bases, policies, and logs.

Why it matters: Enterprise AI needs one place to enforce permissions, tool
boundaries, model routing, approval gates, and auditability.

Common confusion: An AI Gateway is not only an API proxy. It owns governance
behavior.

Related terms: agent governance, policy gate, tool registry, audit log.

Related chapters: `modules/07-ai-gateway-agent-governance/`.

## Agent Governance

Definition: The operating rules for agent tool use, data access, memory,
outputs, approvals, traces, and red-team tests.

Why it matters: Multi-agent systems fail when agents can pass data, call tools,
or make decisions without explicit boundaries.

Common confusion: Governance is broader than prompt instructions.

Related terms: permission boundary, memory governance, approval gate.

Related chapters: `modules/07-ai-gateway-agent-governance/`,
`modules/09-security-red-teaming/`.

## MCP Server

Definition: A Model Context Protocol server that exposes data, tools, or
workflows to AI applications through a standardized interface.

Why it matters: Shared KB, SQL, file, or workflow access can be packaged once
and reused across agents with task-specific controls.

Common confusion: MCP does not remove the need for authentication, policy,
logging, and source-boundary design.

Related terms: adapter, skill, tool registry, AI Gateway.

Related chapters: `modules/07-ai-gateway-agent-governance/`.

## Skill

Definition: A packaged task capability that an agent can invoke, usually with a
prompt contract, tool access, input/output schema, and review rules.

Why it matters: Skills turn shared infrastructure into task-specific behavior.

Common confusion: A skill is not just a prompt; it is an operational contract.

Related terms: adapter, spec-to-skill, structured output.

Related chapters: `modules/07-ai-gateway-agent-governance/`,
`modules/11-spec-sdd-ai-coding-workflow/`.

## Adapter

Definition: A translation layer that maps shared data, tools, or services into
a project-specific or agent-specific interface.

Why it matters: Adapters let different agents reuse the same KB, SQL, model, or
tool source without collapsing into one overcoupled implementation.

Common confusion: An adapter should not become the hidden owner of business
policy.

Related terms: skill, MCP server, module boundary.

Related chapters: `modules/07-ai-gateway-agent-governance/`.

## On-Prem Deployment

Definition: Deployment into customer-controlled infrastructure such as a
machine room, private network, local GPU server, or private cloud.

Why it matters: On-prem work changes data residency, network, security,
observability, driver, GPU, and support responsibilities.

Common confusion: On-prem is not simply "run Docker locally."

Related terms: Docker, Kubernetes, FAE, data residency.

Related chapters: `modules/02-cloud-onprem-private-cloud/`,
`modules/03-container-k8s-devops/`,
`modules/10-enterprise-delivery-fae/`.

## Kubernetes

Definition: A container orchestration platform for deploying and managing
containerized workloads and services.

Why it matters: Enterprise AI services often need repeatable deployment,
service exposure, configuration, scaling, health checks, and operational
handoff.

Common confusion: Knowing Kubernetes commands is weaker than understanding
workload, network, secret, and troubleshooting behavior.

Related terms: Pod, Deployment, Service, Ingress, ConfigMap, Secret.

Related chapters: `modules/03-container-k8s-devops/`.

## GPU Capacity Planning

Definition: Estimating whether available GPU and host resources can support
model weights, KV cache, runtime overhead, batch, concurrency, latency, and
buffer.

Why it matters: Local model delivery fails when memory and throughput are
estimated only from parameter count.

Common confusion: VRAM planning is not only model-size planning.

Related terms: VRAM, KV cache, vLLM, quantization.

Related chapters: `modules/04-gpu-inference-infrastructure/`.

## KV Cache

Definition: Runtime key/value attention memory used during transformer
inference.

Why it matters: It grows with sequence length and active requests, so it is a
major part of serving capacity.

Common confusion: KV cache is separate from model weights.

Related terms: vLLM, PagedAttention, concurrency, latency.

Related chapters: `modules/04-gpu-inference-infrastructure/`.

## vLLM

Definition: An LLM inference and serving engine designed for efficient,
high-throughput model serving.

Why it matters: It is a practical tool for serving local LLMs with attention to
KV cache and batching behavior.

Common confusion: vLLM still requires explicit capacity, model, networking, and
API design.

Related terms: model serving, KV cache, throughput.

Related chapters: `modules/04-gpu-inference-infrastructure/`,
`modules/05-llm-application-architecture/`.

## Ollama

Definition: A local model management and serving tool for running LLMs on
developer or workstation environments.

Why it matters: It provides a fast path for local testing and small deployment
experiments.

Common confusion: A convenient local model runner is not a full enterprise
serving platform by itself.

Related terms: model serving, local model, quantization.

Related chapters: `modules/04-gpu-inference-infrastructure/`.

## RAG

Definition: Retrieval-augmented generation: using external retrieved evidence
to support model generation.

Why it matters: Enterprise AI often needs current, permissioned, source-backed
answers instead of model memory alone.

Common confusion: RAG quality depends on ingestion, metadata, retrieval,
reranking, context construction, and evaluation, not only vector search.

Related terms: embedding, metadata, reranker, query, context construction.

Related chapters: `modules/06-rag-data-pipeline/`.

## Metadata

Definition: Structured data about source content, such as source, date, topic,
permission, document type, owner, and retrieval role.

Why it matters: Metadata makes retrieval governable, filterable, explainable,
and auditable.

Common confusion: Metadata is not decorative; it shapes search and policy.

Related terms: JSON, retrieval, data governance.

Related chapters: `modules/06-rag-data-pipeline/`.

## Reranker

Definition: A second-stage model or scoring method that reorders retrieval
candidates after initial search.

Why it matters: Reranking improves relevance when raw embedding search returns
semantically close but task-wrong chunks.

Common confusion: Retrieval `top-k` and generation `top-p` are different
controls.

Related terms: embedding, top-k, threshold, evaluation.

Related chapters: `modules/06-rag-data-pipeline/`.

## Data Pipeline

Definition: The full governed flow from source data to parsing, cleaning,
metadata, embedding, retrieval, generation, output, logs, and review.

Why it matters: AI system quality usually follows pipeline quality.

Common confusion: A data pipeline is not just an ETL script; it is an evidence,
format, and governance contract.

Related terms: intermediate output, context pollution, data governance.

Related chapters: `modules/06-rag-data-pipeline/`,
`modules/11-spec-sdd-ai-coding-workflow/`.

## ASR

Definition: Automatic speech recognition: converting speech audio into text.

Why it matters: Voice AI systems depend on accurate transcription before LLM,
RAG, analytics, or workflow steps.

Common confusion: ASR accuracy depends on audio quality, domain vocabulary,
sampling rate, speaker overlap, and evaluation metric.

Related terms: Whisper, Breeze-ASR, CER, VAD.

Related chapters: `modules/08-voice-ai-systems/`.

## VAD

Definition: Voice activity detection: identifying which audio segments contain
speech.

Why it matters: VAD reduces empty input, improves segmentation, and supports
real-time voice-agent flow.

Common confusion: VAD detects speech activity; it does not identify speakers.

Related terms: ASR, diarization, real-time voice.

Related chapters: `modules/08-voice-ai-systems/`.

## Diarization

Definition: Segmenting audio by speaker: "who spoke when."

Why it matters: Meetings, calls, sales analysis, and clinical conversations
need speaker-specific transcripts and evidence.

Common confusion: Diarization is different from ASR and speaker identity
verification.

Related terms: speaker embedding, overlapping speech, ASR.

Related chapters: `modules/08-voice-ai-systems/`.

## TTS

Definition: Text-to-speech generation.

Why it matters: Real-time voice agents need generated audio responses with
latency, style, safety, and interruption controls.

Common confusion: Good TTS output is not enough; the system also needs consent,
voice policy, caching, and runtime latency planning.

Related terms: BreezyVoice, CosyVoice, voice cloning, prosody.

Related chapters: `modules/08-voice-ai-systems/`.

## Wake Word

Definition: A trigger phrase or sound pattern that starts a voice interaction.

Why it matters: Physical AI and always-listening systems need controlled
activation.

Common confusion: Wake word detection is not the same as full ASR.

Related terms: VAD, real-time voice, physical AI.

Related chapters: `modules/08-voice-ai-systems/`.

## Prompt Injection

Definition: An attack where input or retrieved content manipulates model
behavior, instructions, or safety controls.

Why it matters: Prompt injection can bypass intended workflow, leak data,
misuse tools, or corrupt downstream decisions.

Common confusion: Prompt injection cannot be solved by prompt wording alone.

Related terms: OWASP LLM Top 10, guardrail, red teaming, tool abuse.

Related chapters: `modules/09-security-red-teaming/`.

## Guardrail

Definition: A policy control applied to input, retrieval, tool use, output,
memory, or workflow.

Why it matters: Enterprise AI systems need enforceable boundaries beyond model
instructions.

Common confusion: A guardrail is a system control, not just a safety sentence
inside the prompt.

Related terms: policy gate, PII, permission boundary.

Related chapters: `modules/09-security-red-teaming/`,
`modules/07-ai-gateway-agent-governance/`.

## PII

Definition: Personally identifiable information.

Why it matters: PII requires detection, minimization, masking, access control,
retention policy, and auditability.

Common confusion: PII risk appears in logs, prompts, retrieval chunks, tool
results, exports, and memory.

Related terms: data governance, guardrail, audit log.

Related chapters: `modules/09-security-red-teaming/`.

## Red Teaming

Definition: Structured adversarial testing of an AI system across prompts,
retrieval, tools, memory, permissions, APIs, and user flows.

Why it matters: It reveals system failures before customer or attacker use.

Common confusion: AI red teaming is broader than jailbreak prompts.

Related terms: OWASP LLM Top 10, NIST AI RMF, prompt injection, tool abuse.

Related chapters: `modules/09-security-red-teaming/`.

## Spec

Definition: A requirement contract describing what the system must do, for
whom, under which constraints, and how success is judged.

Why it matters: Spec-first work keeps AI-assisted coding aligned with user and
customer needs.

Common confusion: A spec is not a vague feature description.

Related terms: SDD, acceptance criteria, source boundary.

Related chapters: `modules/11-spec-sdd-ai-coding-workflow/`.

## SDD

Definition: Software Design Document: architecture, module, interface, data
flow, and review plan before implementation.

Why it matters: SDD-first work prevents generated systems from drifting into
overcoupled, untestable code.

Common confusion: SDD should constrain Codex tasks; it should not be written
after the code as decoration.

Related terms: design pattern, module boundary, test suite.

Related chapters: `modules/11-spec-sdd-ai-coding-workflow/`.

## Context Pollution

Definition: Loss of task control when unrelated or stale context enters prompts,
memory, docs, or agent state.

Why it matters: It causes bloated tasks, contradictory audit rules, and
unreliable generated changes.

Common confusion: More context is not always better context.

Related terms: context engineering, intermediate output, Codex control.

Related chapters: `modules/11-spec-sdd-ai-coding-workflow/`,
`modules/06-rag-data-pipeline/`.
