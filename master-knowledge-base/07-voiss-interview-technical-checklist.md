# VOISS Interview Technical Checklist

This checklist converts source-bounded interview-derived learning notes into a
public-safe curriculum artifact. It is based on corrected transcript-derived
notes, not raw audio verification. It records the technical scope that an AI
systems engineer should prepare for when facing VOISS-style enterprise AI work.

Source boundary:

- This file keeps technical terms, system requirements, and learning
  implications.
- It does not store raw transcript text, private contact routes, compensation
  details, customer secrets, or unsupported company claims.
- Company-specific language is treated as a curriculum lens, not as public
  factual representation.

## 1. Seven Technical Mainlines

The practical interview scope is not a single Kubernetes question. It is a
seven-lane AI systems engineering map:

```text
1. On-prem deployment / Docker / Kubernetes / customer machine-room delivery
2. GPU capacity planning / VRAM / KV cache / vLLM / Ollama
3. AI Gateway / agent governance / MCP server / skill / adapter
4. RAG / metadata / reranker / data pipeline
5. Voice AI: ASR / TTS / diarization / VAD / wake word / real-time voice
6. AI security / red teaming / OWASP / NIST / PII / guardrails / prompt injection
7. Spec / SDD / design patterns / Codex / AI-assisted coding control
```

The system model behind the checklist is:

```text
enterprise requirement
-> data pipeline
-> RAG / KB / SQL
-> MCP server
-> skill / adapter
-> AI Gateway
-> agent governance
-> model serving
-> Docker / Kubernetes / GPU
-> audit log / red teaming
-> onsite deployment / customer acceptance
```

## 2. AI Product And System Architecture

- [ ] **AI Coach**: Treat as an enterprise workflow entrypoint, not only a
  chatbot. It can connect sales data, employee workflows, agent tasks, and
  review loops.
- [ ] **AI system**: Model + data + API + permissions + workflow + deployment +
  observability + governance + acceptance criteria.
- [ ] **AI model**: A single model component such as ASR, LLM, TTS, reranker, or
  audio separation model.
- [ ] **AI agent**: A task-executing unit that can use tools, read knowledge,
  call models, and produce governed outputs.
- [ ] **Agentic AI**: Multi-step task execution with tool use, memory,
  decision trace, approval gates, and feedback control.
- [ ] **Agentic pipeline**: A chain of agents, models, tools, and data
  transformations with explicit intermediate outputs.
- [ ] **AI Gateway**: The governance and routing layer for models, agents,
  knowledge bases, tools, policies, logs, and permissions.
- [ ] **Agent governance**: Controls for tool access, data access, memory,
  output format, approval, audit logs, and red-team testing.
- [ ] **System governance**: System-level controls across APIs, network
  boundaries, logs, users, agents, and deployment environments.
- [ ] **Data governance**: Data cleaning, metadata, retention, access control,
  data residency, and source lifecycle control.
- [ ] **Cybersecurity governance**: Security controls for API access, internal
  networks, device access, logs, zero trust, and user-side risks.
- [ ] **Knowledge Base / KB**: A governed source of enterprise knowledge that may
  be shared across agents with different permission boundaries.
- [ ] **SQL source**: A structured source that may be exposed through an MCP
  server, adapter, or task-specific skill.
- [ ] **MCP server**: A standardized server interface for exposing data, tools,
  and workflows to AI applications.
- [ ] **Adapter**: A project-specific translation layer that lets a shared data
  or tool source serve a specific workflow.
- [ ] **Skill**: A task-packaged capability that an agent can invoke, often
  backed by shared KB, SQL, tools, prompts, and policies.
- [ ] **Spec-to-skill workflow**: New requirement -> updated spec -> generated
  or revised skill -> review -> deployment.
- [ ] **Agent harness / orchestration**: A general pattern for controlling agent
  runs, tool choices, traces, tests, and skill lifecycle.
- [ ] **Tool use**: Agent calls to search, APIs, databases, code, workflows, or
  other services.
- [ ] **Approval gate / human review**: A required control when output has
  business, safety, privacy, or customer impact.
- [ ] **Ground truth**: Reference data or evaluation labels used to judge agent
  decisions.
- [ ] **Output format**: A contract for agent/model output that downstream
  tasks can parse and audit.
- [ ] **User flow**: The end-to-end path a user takes through an agent system;
  it shapes governance and red-team scenarios.

## 3. Deployment, Containers, Kubernetes, And Delivery

- [ ] **Local model / on-prem model**: A model deployed inside customer,
  enterprise, lab, or controlled infrastructure instead of only through public
  API calls.
- [ ] **On-prem deployment**: Delivery into customer-owned infrastructure with
  local network, security, GPU, data residency, and operational constraints.
- [ ] **Docker**: Container packaging for application code, runtime,
  dependencies, and settings.
- [ ] **Container**: A repeatable runtime unit that reduces environment drift
  between development, staging, and customer infrastructure.
- [ ] **Docker image**: The build artifact that can be deployed by Docker,
  Docker Compose, Kubernetes, or customer deployment tooling.
- [ ] **Kubernetes / K8s**: Container orchestration for deployment, scaling, and
  management of containerized workloads.
- [ ] **Pod / Deployment / Service / Ingress**: The minimum Kubernetes concepts
  needed to run and expose AI services.
- [ ] **ConfigMap / Secret**: Kubernetes mechanisms for configuration and
  sensitive runtime values; credentials still require strict secret handling.
- [ ] **FAE workflow**: Requirement check, package, deploy, troubleshoot,
  document, hand off, and escalate.
- [ ] **Machine-room delivery**: Onsite or controlled-environment deployment
  where networking, firewall, GPU drivers, storage, and monitoring matter.
- [ ] **Deployment troubleshooting**: Isolate failures across process, port,
  DNS, TLS, container, GPU, model server, API contract, and logs.
- [ ] **Internal network**: Customer-side network boundary that affects data
  residency, API access, device trust, and logging.
- [ ] **API architecture**: Explicit request/response, auth, policy, logging,
  retry, timeout, and error contracts.
- [ ] **Port**: Runtime service exposure and a common source of deployment and
  security failures.
- [ ] **Token usage / hosted inference budget**: A fallback path when local
  capacity is unavailable, expensive, or still being provisioned.
- [ ] **OpenRouter / Together AI**: Hosted inference options to understand as
  cloud-service comparators, not replacements for on-prem discipline.

## 4. GPU, VRAM, And Model Serving

- [ ] **GPU**: The primary accelerator for local AI inference and many training
  or fine-tuning tasks.
- [ ] **NVIDIA / CUDA**: Common GPU and software stack for model serving.
- [ ] **AMD / ROCm**: AMD GPU software stack that may matter for customer
  hardware diversity.
- [ ] **VRAM**: GPU memory; capacity planning must include weights, KV cache,
  runtime overhead, batch, concurrency, and buffers.
- [ ] **RAM**: Host memory; relevant for loading, preprocessing, offload,
  service processes, and retrieval components.
- [ ] **KV cache**: Runtime memory for transformer attention keys/values; it
  grows with sequence length and active requests.
- [ ] **Buffer**: Safety margin for runtime overhead, fragmentation, spikes, and
  multi-service contention.
- [ ] **vLLM**: LLM inference and serving engine with memory-management features
  such as paged KV cache handling.
- [ ] **Ollama**: Local model management and serving tool useful for development
  and small local deployments.
- [ ] **Model serving**: Turning a model into a reliable API service with
  startup, health, timeout, batching, logging, and capacity controls.
- [ ] **Multi-model serving**: Operating several models under finite GPU memory,
  throughput, and latency constraints.
- [ ] **Batch size**: A throughput and memory control for inference or training.
- [ ] **Concurrency**: Number of simultaneous requests or sessions that the
  serving stack must support.
- [ ] **Latency**: Response time, especially critical in real-time voice loops.
- [ ] **Throughput**: Sustained request or token rate under load.
- [ ] **Quantization / INT4 / INT8**: Lower-precision model representation that
  can reduce memory cost with quality and compatibility trade-offs.
- [ ] **H200 / A6000 / RTX-class GPUs**: Hardware examples for contrasting
  enterprise, lab, and personal capacity planning.
- [ ] **Edge AI / NPU / ARM**: Local inference on smaller or specialized
  devices, often with stricter latency, power, and portability constraints.

## 5. LLM, Fine-Tuning, And Inference

- [ ] **LLM**: A language model used for summarization, reasoning, extraction,
  structured output, and agent planning.
- [ ] **LLMOps**: Deployment, monitoring, evaluation, cost, versioning, and
  governance practices for LLM systems.
- [ ] **System prompt**: Stable instruction layer; it must not replace policy,
  permission, or audit controls.
- [ ] **Prompt**: Input instructions and context; needs structure and testing.
- [ ] **Decision trace instead of hidden reasoning**: Design observable
  intermediate outputs, tool calls, and rationales without relying on private
  chain-of-thought text.
- [ ] **Fine-tuning**: Model adaptation using task data; useful but expensive
  and not a substitute for data quality or evaluation.
- [ ] **LoRA / PEFT**: Parameter-efficient fine-tuning methods that reduce
  trainable parameter count and memory cost.
- [ ] **Hugging Face / Transformers**: Common model, dataset, and tooling
  ecosystem.
- [ ] **Encoder / decoder**: Model architecture components that matter for ASR,
  TTS, and transformer systems.
- [ ] **Model weights**: Stored learned parameters and the first part of memory
  sizing.
- [ ] **Dense model / MoE model**: Model architecture choices with different
  serving, routing, and capacity behavior.

## 6. Voice AI And Audio Systems

- [ ] **ASR**: Speech-to-text, including model selection, sampling rate,
  language/domain adaptation, timestamps, and error analysis.
- [ ] **Breeze-ASR / Whisper**: Public model families worth studying for
  Taiwanese Mandarin, Mandarin-English code switching, and ASR baselines.
- [ ] **8 kHz telephone audio / 16 kHz speech audio**: Sampling-rate constraints
  that affect speech information and recognition quality.
- [ ] **CER / WER**: Error metrics for ASR.
- [ ] **VAD**: Voice activity detection for segmenting speech from silence or
  noise.
- [ ] **Diarization**: Speaker segmentation and labeling: "who spoke when."
- [ ] **Real-time diarization**: Diarization under streaming and latency
  constraints.
- [ ] **Speaker embedding**: Vector representation for speaker similarity.
- [ ] **Overlapping speech**: A difficult case where multiple speakers or sounds
  occur at the same time.
- [ ] **Synthetic data**: Generated or augmented audio used to strengthen
  training or evaluation when real labeled data is limited.
- [ ] **BreezyVoice / CosyVoice**: TTS and voice-cloning systems to understand
  for Taiwanese Mandarin and voice AI pipelines.
- [ ] **TTS**: Text-to-speech generation for voice-agent response.
- [ ] **Voice cloning**: Speaker-style adaptation with quality, consent, safety,
  and data requirements.
- [ ] **Prosody / tone / emotion control**: Speech style dimensions that affect
  usability and realism.
- [ ] **Hotwords**: Domain vocabulary support for ASR.
- [ ] **Waveform / acoustic feature**: Audio representations used in analysis,
  enhancement, and model input.
- [ ] **Noise reduction / far-field audio**: Necessary for production voice
  systems outside clean microphone conditions.
- [ ] **Environmental sound detection**: Detecting alarms, abnormal machine
  sounds, anger, or other non-speech events.
- [ ] **Audio source separation / SAM Audio**: Separating target sounds from
  mixed audio with text, visual, or temporal prompts.
- [ ] **Wake word**: Trigger detection for physical AI or always-listening voice
  systems.
- [ ] **Real-time voice agent**: ASR -> LLM -> TTS loop with strict latency,
  barge-in, interruption, and session-state concerns.

## 7. RAG, Metadata, Retrieval, And Data Pipeline

- [ ] **RAG**: Retrieval-augmented generation that uses external knowledge
  during generation.
- [ ] **Embedding / vector search**: Semantic retrieval foundation.
- [ ] **Reranker**: Second-stage relevance model that reorders retrieved
  candidates.
- [ ] **Metadata**: Structured evidence about source, topic, date, permissions,
  document type, customer boundary, and retrieval use.
- [ ] **JSON**: Common format for metadata and intermediate outputs.
- [ ] **Top-k**: Number of retrieval candidates selected before or after
  reranking.
- [ ] **Top-p**: Primarily a generation sampling control; do not confuse it with
  retrieval top-k.
- [ ] **Threshold**: Confidence or margin rule for deciding whether retrieval is
  strong enough.
- [ ] **Query**: User or agent information need; enterprise queries are often
  ambiguous and unevenly phrased.
- [ ] **PDF parsing / OCR**: Document ingestion methods for scanned or
  semi-structured enterprise files.
- [ ] **Bag of Words / TF-IDF / keyword extraction**: Classical NLP tools that
  can support metadata, search, and explainability.
- [ ] **Summary**: Condensed representation of source content; must preserve
  source boundary and uncertainty.
- [ ] **Data cleaning / filtering / selection**: Controls that determine whether
  downstream AI behavior is usable.
- [ ] **Intermediate output**: Stored task output used for later tasks,
  debugging, audit, and reproducibility.
- [ ] **Data pipeline**: The governed flow from source data to parsed text,
  metadata, embedding, retrieval, generation, output, logs, and review.
- [ ] **Context pollution**: Loss of control when unrelated context accumulates
  inside prompts, memory, or agent state.
- [ ] **Audit conflict**: Inconsistent review mechanisms caused by unclear
  contracts, overlapping agents, or bloated tasks.

## 8. AI Security, Red Teaming, And Governance

- [ ] **Cybersecurity**: Protection of systems, APIs, networks, users, data, and
  operational workflows.
- [ ] **Zero trust**: Design assumption that access must be verified and
  minimized across layers.
- [ ] **Log / audit log / decision trace**: Evidence trail for who did what,
  which agent acted, what tool was used, and which policy applied.
- [ ] **OWASP LLM Top 10**: Baseline risk taxonomy for LLM applications.
- [ ] **NIST AI RMF**: Risk-management framework for AI systems.
- [ ] **PII**: Personally identifiable information that requires detection,
  minimization, masking, access control, and retention rules.
- [ ] **Guardrail**: Input, retrieval, tool, output, memory, and workflow policy
  controls.
- [ ] **Prompt injection**: User or retrieved content attempts to override
  instructions or safety controls.
- [ ] **Pre-gate / post-gate**: Controls before model/tool execution and after
  generated output.
- [ ] **Red teaming**: Structured adversarial testing of end-to-end AI systems.
- [ ] **User-side red teaming**: Testing realistic user flows, device behaviors,
  phishing risks, and misuse paths.
- [ ] **Penetration testing / port scanning / CVE**: Conventional security
  testing that still matters for AI systems.
- [ ] **Social engineering / phishing / URL/domain signals**: User-side attack
  surfaces around AI-assisted workflows.
- [ ] **Agent poisoning**: A compromised or manipulated lower-level agent
  affects higher-level decisions or data flow.
- [ ] **Cross-agent privilege escalation**: Unauthorized data or tool access
  through agent-to-agent communication.
- [ ] **Permission boundary**: Explicit rule for which user, agent, tool, and
  memory can access which data.
- [ ] **Memory governance**: Control over what is stored, shared, retrieved,
  deleted, and audited.

## 9. Prompt, Context, And Structured Input

- [ ] **Prompt engineering**: Clear instructions, examples, constraints, and
  output contracts.
- [ ] **Context engineering**: Selecting and organizing what the model sees at
  runtime.
- [ ] **XML-structured prompting / HTML-like tags**: A way to separate
  instructions, context, examples, input, and output requirements.
- [ ] **TOON**: A compact structured-data notation worth understanding as a
  prompt-format option.
- [ ] **Markdown skill format**: Skills can be packaged as readable,
  reviewable Markdown contracts.
- [ ] **Structured output / schema**: Output contracts for parsability,
  downstream workflow, and auditability.

## 10. Software Engineering And AI-Assisted Coding

- [ ] **Python / JavaScript / Node.js / Rust**: Practical languages that appear
  across model services, backend control, CLI tools, and systems work.
- [ ] **Backend / API**: Service layer where auth, routing, policy, logging, and
  model/tool integration happen.
- [ ] **Codex / GPT workflow**: Use AI agents for drafting and implementation
  only after the spec, SDD, contracts, and review gates are clear.
- [ ] **AI-assisted coding control**: Prevent architecture drift, overcoupling,
  context pollution, and unreviewable changes.
- [ ] **Hand coding**: Ability to implement and debug critical pipeline pieces
  manually.
- [ ] **Spec**: Requirement contract before implementation.
- [ ] **SDD**: Architecture, module, interface, and data-flow design before
  coding.
- [ ] **README**: Public orientation and runnable contract for a repo or module.
- [ ] **Design pattern**: Repeatable structure that keeps code and agent tasks
  understandable.
- [ ] **Module boundary**: Clear ownership between core, domain, discovery,
  clinical, gateway, and delivery components.
- [ ] **Overcoupling**: Failure mode where one change triggers unexpected
  changes across unrelated modules.
- [ ] **Shared module / event-style boundary**: A shared data or event layer can
  reduce duplication when many modules need the same facts.
- [ ] **Linter / type checker / test suite**: Guardrails for AI-generated and
  human-written code.

## 11. Data Formats And Enterprise Knowledge

- [ ] **PDF / OCR**: Enterprise knowledge ingestion often starts from messy
  document formats.
- [ ] **JSON / Markdown / HTML / XML**: Practical formats for metadata,
  documentation, prompts, and structured exchange.
- [ ] **Knowledge ingestion**: Source collection, parsing, metadata, chunking,
  embedding, indexing, retrieval, and review.
- [ ] **Data residency**: Requirement that data may need to stay inside customer
  or controlled infrastructure.

## 12. Application Scenarios

- [ ] **Enterprise AI Coach**: Workflow assistant and enterprise behavior/data
  analysis entrypoint.
- [ ] **Bank multi-agent governance**: Multiple agents, shared data, vendor
  boundaries, policy, and audit.
- [ ] **AI sales agent / sales opportunity mining**: Voice or text analysis for
  follow-up prioritization and coaching.
- [ ] **Call-recording analysis agent**: ASR + diarization + summary + evidence
  extraction + governance.
- [ ] **Report-writing agent**: Structured drafting with source boundaries and
  approval gates.
- [ ] **Anti-fraud classification**: Speech/text analysis with safety,
  uncertainty, and review controls.
- [ ] **Healthcare ASR + LLM intake**: Clinical support context requiring strict
  scope controls and human review.
- [ ] **Internal-network device workflow**: Enterprise device, API, and logging
  governance.
- [ ] **Semiconductor audio anomaly detection**: Far-field audio, noise
  reduction, event detection, and source separation.
- [ ] **Physical AI coach**: Robot or device-based assistant with wake word,
  ASR, voice loop, and local control.

## 13. What To Learn As A System

Do not memorize these terms as isolated trivia. Build a working system map:

```text
customer workflow
-> deployment environment
-> data and knowledge boundary
-> model/tool orchestration
-> agent governance
-> security and red-team testing
-> acceptance evidence
```

The practical goal is to explain, design, deploy, debug, and review the whole
system under enterprise constraints.
