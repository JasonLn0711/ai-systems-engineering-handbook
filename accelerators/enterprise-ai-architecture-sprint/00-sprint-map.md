# Sprint Map

## Purpose

This sprint turns enterprise AI architecture knowledge into evidence within
7-14 days. The point is not to learn every topic deeply. The point is to show
that the learner can organize customer-facing AI systems around architecture,
governance, deployment, security, and measurable validation.

## Core Thesis

Enterprise AI delivery is not proven by a working model demo. It is proven by a
system package:

```text
enterprise requirement
-> architecture diagram
-> governed data/tool/model flow
-> deployable service plan
-> capacity estimate
-> security and red-team evidence
-> acceptance criteria
```

## Sprint Flow

```text
Day 1-2: AI Gateway architecture
Day 2-3: Agent governance framework
Day 3-5: Red teaming framework
Day 4-6: GPU capacity model
Day 5-8: K8s inference-service lab
Day 7-10: PII / guardrail demo plan
Day 9-12: MCP / tool / memory governance
Day 10-14: Real-time voice-agent evidence plan
```

## 7-Day Minimum Evidence Pack

- One AI Gateway diagram.
- One Agent Governance Framework table.
- One Red Teaming taxonomy and test-plan outline.
- One GPU capacity estimation table.
- One K8s inference service deployment checklist.

## 14-Day Evidence Pack

- 7-day pack completed.
- PII / guardrail demo plan completed.
- MCP / tool / memory governance map completed.
- Real-time voice-agent evidence plan completed.
- One consolidated architecture memo linking all artifacts.

## 30-Day Evidence Pack

- 14-day pack completed.
- At least one runnable lab result from K8s, vLLM/Ollama, security, or voice AI.
- A written failure-mode review.
- A reusable handoff packet for enterprise AI architecture discussion.

## Deliverable Standard

Each sprint document must answer:

1. What evidence does this artifact produce?
2. Which system risk does it reduce?
3. Which module/lab owns the long-term learning depth?
4. What is the minimum viable implementation?
5. How will the output be validated?

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

## Acceptance Criteria

- The sprint can be explained as an enterprise architecture plan, not a list of
  unrelated tools.
- Each artifact has a concrete output.
- Each output has at least one validation method.
- Private source signals have been rewritten into public-safe system patterns.
