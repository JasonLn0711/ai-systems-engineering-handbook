# First 30 Days Learning Checklist

This checklist turns the VOISS-style interview technical map into a first-month
learning path. It is a readiness plan, not a promise that every topic becomes
production-deep within one month.

The month wins when the learner can explain, deploy, debug, and review a small
enterprise AI system across deployment, model serving, RAG, governance, voice
AI, security, and AI-assisted coding controls.

For a shorter evidence sprint, use:

```text
accelerators/enterprise-ai-architecture-sprint/
```

The accelerator converts this 30-day learning map into a 7-14 day public-safe
architecture evidence packet.

## P0: First Month Must Reach Working Competence

Outcome: build and explain a small governed local AI service with deployment,
model serving, retrieval, policy, logs, and tests.

- [ ] **Docker**: Package a FastAPI/backend/model service with pinned runtime,
  health check, env vars, and reproducible startup.
- [ ] **Kubernetes basics**: Explain and use Pod, Deployment, Service, Ingress,
  ConfigMap, Secret, resource request/limit, and basic GPU workload concepts.
- [ ] **Linux server debugging**: Check process, port, log, disk, memory,
  network, GPU process, driver, and service status.
- [ ] **GPU / VRAM estimation**: Estimate model weights, quantization, KV
  cache, batch, concurrency, runtime overhead, and buffer.
- [ ] **vLLM**: Start a local serving endpoint, run health checks, measure
  latency/throughput, and explain KV cache impact.
- [ ] **Ollama**: Run and manage local models for small experiments and compare
  where it fits relative to vLLM.
- [ ] **RAG**: Implement or trace embedding, metadata, reranker, top-k,
  threshold, evaluation, and citation behavior.
- [ ] **Data pipeline**: Define cleaning, metadata, intermediate outputs, and
  format contracts before generation.
- [ ] **AI Gateway baseline**: Design an agent/model/tool registry with policy
  gate, approval gate, and audit log.
- [ ] **MCP server baseline**: Explain how KB, SQL, file, or tool access can be
  exposed to agents through MCP-style boundaries.
- [ ] **Skill / adapter baseline**: Convert one shared source into two
  task-specific capabilities without duplicating the whole pipeline.
- [ ] **Prompt injection defense**: Add pre-gate, retrieval gate, tool gate,
  output gate, and sensitive-info checks.
- [ ] **Red-team baseline**: Test prompt injection, tool abuse, data
  exfiltration, unsafe output, and permission-boundary failures.
- [ ] **Spec / SDD discipline**: Write the spec, SDD, interface contracts, and
  acceptance criteria before asking Codex to implement.
- [ ] **AI-assisted coding control**: Use small Codex tasks, module boundaries,
  linter/type/test gates, and source-boundary checks.

## P1: Voice AI Line To Deepen

Outcome: demonstrate a small voice loop and explain where audio quality,
speaker handling, TTS, latency, and governance fail.

- [ ] **ASR**: Understand Whisper/Breeze-ASR-style deployment, evaluation, and
  domain adaptation.
- [ ] **Telephone and Taiwanese Mandarin context**: Compare 8 kHz telephone
  audio, 16 kHz speech audio, code-switching, and domain vocabulary.
- [ ] **VAD**: Segment speech and avoid sending silence/noise into ASR.
- [ ] **Diarization**: Explain speaker segmentation, speaker embeddings,
  overlapping speech, and real-time trade-offs.
- [ ] **TTS**: Run or inspect a BreezyVoice/CosyVoice-style TTS path.
- [ ] **Voice cloning**: Explain consent, data amount, quality limits, and
  speaker-style controls.
- [ ] **Prosody / tone**: Identify where emotion, rhythm, accent, and style are
  controlled or limited.
- [ ] **Hotwords**: Explain domain vocabulary enhancement and its evaluation.
- [ ] **Real-time voice loop**: Measure ASR -> LLM -> TTS latency, plus
  interruption and session-state behavior.
- [ ] **Wake word**: Explain activation design for physical AI or
  always-listening systems.
- [ ] **Environmental audio**: Study noise reduction, far-field capture,
  abnormal-sound detection, and evaluation.
- [ ] **SAM Audio / source separation**: Understand text, visual, or temporal
  prompt-based sound separation as an advanced audio capability.

## P2: Advanced Strengthening Topics

Outcome: strengthen breadth for hardware diversity, structured context,
security frameworks, and multi-agent governance.

- [ ] **AMD ROCm**: Understand how AMD GPU deployment differs from CUDA-first
  assumptions.
- [ ] **Edge AI**: Learn NPU, ARM, local autonomous agent box, and low-power
  deployment constraints.
- [ ] **TOON**: Evaluate compact structured-data notation for prompt payloads.
- [ ] **XML tags / context engineering**: Structure instructions, context,
  examples, source blocks, and outputs.
- [ ] **Microsoft AI Red Teaming**: Study scalable AI red-team workflow design.
- [ ] **OWASP LLM Top 10**: Use as a baseline for LLM application risk review.
- [ ] **NIST AI RMF**: Use as a governance and risk-management reference.
- [ ] **PII detection / masking**: Apply to prompts, retrieval chunks, logs,
  exports, and memory.
- [ ] **Guardrail framework**: Separate input, retrieval, tool, memory, output,
  and workflow policy.
- [ ] **Cross-agent memory governance**: Design high/low permission agents,
  memory-sharing rules, and escalation controls.
- [ ] **Agent harness / spec-to-skill lifecycle**: Control skill creation,
  review, testing, deployment, and rollback.

## Weekly Execution Shape

- Week 1: Docker, Linux debugging, local model serving, and VRAM estimation.
- Week 2: RAG pipeline, metadata, reranker, and intermediate-output contracts.
- Week 3: AI Gateway, MCP-style tool/data access, skills, adapters, and audit
  logs.
- Week 4: Voice AI loop, AI security/red teaming, and Spec/SDD/Codex control.

## Acceptance Evidence

- A small service runs locally in Docker and exposes a health endpoint.
- A model server runs through vLLM or Ollama and reports basic latency.
- A mini RAG flow returns source-backed answers with metadata.
- A gateway mock records tool/model calls and policy decisions.
- A red-team checklist catches at least prompt injection, unsafe retrieval,
  tool misuse, and PII leakage paths.
- A Spec + SDD + README explains the architecture before code changes.

## Accelerator Bridge

The first evidence packet should prioritize:

1. AI Gateway architecture.
2. Agent Governance Framework.
3. Red Teaming Framework.
4. GPU capacity estimation model.
5. K8s inference deployment lab.
6. PII / Guardrail demo.
7. MCP / Tool / Memory governance.
8. Real-time voice-agent evidence plan.
