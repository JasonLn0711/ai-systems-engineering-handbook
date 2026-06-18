# Sprint Map

## Purpose

This sprint turns enterprise voice AI architecture knowledge into reviewable
evidence within 7 days. The point is not to learn every tool deeply. The point
is to show that the learner can organize customer-facing AI systems around
architecture, governance, deployment, security, voice quality, and measurable
validation.

The detailed Traditional Chinese tutorial for students is:

```text
7-day-consulting-onboarding-tutorial.zh-TW.md
```

The expanded 28/30-day spiral bootcamp is:

```text
30-day-spiral-bootcamp.zh-TW.md
```

## Core Thesis

Enterprise AI delivery is not proven by a working model demo. It is proven by a
system package:

```text
enterprise requirement
-> architecture diagram
-> governed audio/data/tool/model flow
-> deployable service plan
-> capacity estimate
-> guardrail and red-team evidence
-> latency and quality metrics
-> customer acceptance criteria
```

## 7-Day Consulting Sprint Flow

| Day | Focus | Main evidence |
|---|---|---|
| 1 | Domain map and interview-signal issue tree | one-page domain brief, 50 survival terms, issue tree |
| 2 | Voice AI pipeline | voice pipeline diagram, module inventory, latency table |
| 3 | RAG, tool use, agent governance, AI Gateway | RAG schema, tool registry, gateway architecture |
| 4 | PII, guardrails, red teaming | PII policy event schema, 30-case red-team mini harness |
| 5 | Docker, K8s, GPU sizing, vLLM | K8s checklist, GPU sizing spreadsheet, deployment notes |
| 6 | Integrated demo and architecture memo | demo script, architecture memo, known limitations |
| 7 | Onboarding pack and first 30 days | reusable onboarding pack, first-week questions, 30-day plan |

## 28/30-Day Spiral Bootcamp Flow

The 7-day sprint is the reconnaissance pass. The 28-day bootcamp keeps the
same core topics but revisits them four times with increasing depth:

| Week | Depth | Purpose | Evidence |
|---|---|---|---|
| 1 | Map | Build the full battlefield map without overloading the beginner | domain map, 50 terms, issue tree, weakness map |
| 2 | Mechanism | Turn names into inputs, outputs, schemas, metrics, and failure modes | model cards, schemas, architecture memo v1, source claim matrix |
| 3 | Lab | Turn concepts into repo evidence, configs, tests, logs, and reports | audio lab, RAG/tool lab, red-team lab, K8s/GPU lab, demo v1 |
| 4 | Delivery | Package the work for architecture review, customer sizing, and onboarding | demo video, governance proposal, red-team report, sizing pack, onboarding pack |

The 30-day version adds:

| Day | Purpose | Evidence |
|---|---|---|
| 29 | Mock technical review | mock review Q&A and weak-answer rewrites |
| 30 | Portfolio and first-week work plan | portfolio index, first-week plan, milestone alignment questions |

## 7-Day Minimum Evidence Pack

- One end-to-end enterprise voice agent architecture diagram.
- One 50-term glossary with layer, decision impact, and common misconception.
- One AI Gateway / agent governance memo.
- One tool registry schema with permission, idempotency, dry-run, approval, and
  audit fields.
- One RAG schema with metadata, ACL, retrieval, reranking, citation, and
  abstain behavior.
- One PII / guardrail policy event schema.
- One red-team taxonomy and at least 30 test cases.
- One GPU capacity estimation table covering weights, KV cache, concurrency,
  overhead, safety margin, and p50/p95 validation plan.
- One K8s inference-service deployment checklist.
- One voice demo plan with component-level latency measurement.
- One onboarding pack and first-30-days plan.

## Optional 14-Day Evidence Pack

- 7-day pack completed.
- Runnable PII / guardrail demo.
- Runnable mock gateway with registry-driven tool calls.
- Runnable K8s mock inference endpoint.
- Recorded ASR -> agent -> TTS demo with timing overlay.
- Consolidated architecture memo linking all artifacts.

## 30-Day Evidence Pack

- 14-day pack completed.
- At least one runnable lab result from K8s, vLLM/Ollama/SGLang, security, or
  voice AI.
- A written failure-mode review.
- A reusable handoff packet for enterprise AI architecture discussion.

## Deliverable Standard

Each sprint document must answer:

1. What evidence does this artifact produce?
2. Which system risk does it reduce?
3. Which module/lab owns the long-term learning depth?
4. What is the minimum viable implementation?
5. How will the output be validated?
6. Which weakness does this artifact repair?

## Weakness Routing

| Weakness | Sprint artifact | Owning module | Supporting lab |
|---|---|---|---|
| Gateway governance is abstract | AI Gateway architecture | `07-ai-gateway-agent-governance` | `labs/ai-gateway` |
| Tool use is shallow | Tool registry and lifecycle | `07-ai-gateway-agent-governance` | `labs/ai-gateway` |
| Cross-agent memory is underspecified | MCP / tool / memory governance | `07-ai-gateway-agent-governance` | `labs/ai-gateway` |
| Red teaming is new | Red teaming framework | `09-security-red-teaming` | `labs/security` |
| PII / guardrail is new | PII / guardrail demo | `09-security-red-teaming` | `labs/security` |
| GPU sizing relies on experience | GPU capacity model | `04-gpu-inference-infrastructure` | `labs/vllm` |
| K8s is weak | K8s inference service | `03-container-k8s-devops` | `labs/k8s` |
| Voice system latency is anecdotal | Real-time voice evidence | `08-voice-ai-systems` | `labs/voice-ai` |
| RAG metrics are incomplete | RAG schema and eval plan | `06-rag-data-pipeline` | `labs/rag` |
| Delivery questions are vague | Onboarding and acceptance pack | `10-enterprise-delivery-fae` | `labs/local-dev` |

## Module Routing

| Sprint artifact | Owning module | Supporting lab |
|---|---|---|
| AI Gateway architecture | `07-ai-gateway-agent-governance` | `labs/ai-gateway` |
| Agent governance framework | `07-ai-gateway-agent-governance` | `labs/ai-gateway` |
| Red teaming framework | `09-security-red-teaming` | `labs/security` |
| GPU capacity model | `04-gpu-inference-infrastructure` | `labs/vllm` |
| K8s inference service | `03-container-k8s-devops` | `labs/k8s` |
| PII / guardrail demo | `09-security-red-teaming` | `labs/security` |
| MCP / tool / memory governance | `07-ai-gateway-agent-governance` | `labs/ai-gateway` |
| Real-time voice evidence | `08-voice-ai-systems` | `labs/voice-ai` |

## Consulting Learning Loop

The sprint uses a hypothesis-driven expert learning loop:

```text
define output
-> build survival terms
-> draw initial maps
-> write hypotheses
-> read public source dossier or interview experts
-> code claims into a comparable table
-> identify consensus, dissent, and evidence-backed minority views
-> convert findings into artifacts
```

When expert interviews are not available, use the public source dossier in
`7-day-consulting-onboarding-tutorial.zh-TW.md` as the substitute research
set.

## Acceptance Criteria

- The sprint can be explained as an enterprise architecture plan, not a list of
  unrelated tools.
- Each artifact has a concrete output.
- Each output has at least one validation method.
- Private source signals have been rewritten into public-safe system patterns.
- Student materials are understandable to a sophomore computer science learner.
- Technical claims are linked to public references when they name standards,
  frameworks, packages, or serving/deployment tools.
- Scope controls are stated as operating boundaries and next validation gates.
