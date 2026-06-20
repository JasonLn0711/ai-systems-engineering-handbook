# Enterprise AI Architecture Sprint — Day 5: K8s GPU Serving

Day 5 turns deployability and capacity planning into evidence. The goal is not
to teach all Kubernetes or all GPU inference. The goal is to let students answer
how an enterprise AI service would be packaged, exposed, sized, checked,
debugged, and rolled back.

## Day Metadata

```text
Day number: Day 5
Topic: Docker / K8s / GPU Sizing / vLLM
Sprint artifact: 04-k8s-inference-service-lab.md + 05-gpu-capacity-estimation-model.md
Owning module: modules/03-container-k8s-devops/
Supporting lab: labs/k8s/ and labs/vllm/
Target learner: sophomore CS students / junior engineers
Prerequisites: Day 4 Gateway integration, basic HTTP service concepts
Expected student deliverables: K8s manifest checklist, GPU sizing table, deployment risk-control map, validation plan
Next gate: day-06-demo-memo-handoff.md
```

## Learning Objectives

1. Explain how Deployment, Service, Ingress, ConfigMap, Secret, PVC, resource
   limits, health checks, logs, and rollback support an inference service.
2. Estimate GPU memory using model weights, KV cache, runtime overhead,
   concurrency overhead, and safety margin.
3. Distinguish AI Gateway control plane from vLLM/model-serving data plane.
4. Define p50/p95 validation for latency and actual VRAM usage.
5. Produce a deployment risk-control map.

## File Map

| File | Audience | Purpose |
|---|---|---|
| `README.md` | Everyone | Day 5 scope and completion definition. |
| `student-handout-detailed.md` | Students / instructor | Canonical long-form explanation. |
| `student-handout-detailed.zh-TW.md` | Students / instructor | Complete Taiwan Traditional Chinese detailed version. |
| `student-handout.md` | Students | Summary handout. |
| `worksheet.md` | Students | Templates for checklist, sizing, validation, risk map. |
| `instructor-guide.md` | Instructor / TA | Teaching flow and failure gallery. |
| `reference-answer-vllm-mock-serving.md` | Instructor / TA | Filled public-safe example. |
| `rubric.md` | Instructor / TA | 100-point rubric. |
| `day-06-demo-memo-handoff.md` | Instructor / implementer | Next integrated demo gate. |
| `glossary-updates.md` | Maintainers | Candidate terms. |
| `source-package.md` | Maintainers | Source boundary and references. |

## Minimum Deliverables

1. K8s manifest inventory and deployment checklist.
2. GPU sizing table for at least three model/hardware scenarios.
3. vLLM serving assumptions.
4. p50/p95 and VRAM validation plan.
5. Deployment risk-control map.

## Source Boundary

Use synthetic workloads and public-safe model/hardware examples. Do not store
customer deployment details, credentials, private cluster names, real logs with
secrets, or unpublished company claims.
