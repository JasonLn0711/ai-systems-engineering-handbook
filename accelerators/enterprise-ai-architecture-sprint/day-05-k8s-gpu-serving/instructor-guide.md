# Instructor Guide — Day 5: K8s GPU Serving

## 1. Teaching Goal

Students learn to produce deployability and capacity evidence without pretending
they have a full production cluster.

## 2. Pre-Class Diagnostic

1. What is the difference between Deployment and Service?
2. Why is `Secret` different from `ConfigMap`?
3. Why is vLLM not the AI Gateway?
4. What memory terms belong in a GPU estimate?
5. What proves rollback is possible?

## 3. 150-Minute Flow

| Time | Activity | Output |
|---:|---|---|
| 0-10 | Diagnostic | Weakness list |
| 10-35 | K8s object map | Manifest inventory |
| 35-60 | Minimal inference manifest | Checklist |
| 60-90 | GPU sizing formula | Capacity table |
| 90-115 | vLLM assumptions | Serving config notes |
| 115-140 | Validation and risk map | p50/p95 plan |
| 140-150 | Handoff | Demo inputs |

## 4. Failure Gallery

### Failure 1: Health check lies

The pod is healthy but model endpoint fails. Make readiness hit the model route.

### Failure 2: GPU request missing

Manifest runs on CPU or fails scheduling. Document device plugin and GPU limit.

### Failure 3: KV cache ignored

Weights fit but concurrency fails. Include context and concurrency assumptions.

### Failure 4: Secret appears in logs

Config works but leaks credential. Check log redaction and source boundary.

## 5. TA Workflow

1. Check manifest inventory.
2. Inspect GPU sizing table assumptions.
3. Confirm p50/p95 and VRAM validation plan.
4. Check risk-control map.
5. Apply source-boundary score last.
