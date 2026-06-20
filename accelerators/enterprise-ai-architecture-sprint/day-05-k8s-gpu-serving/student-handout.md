# Student Handout — Day 5: K8s GPU Serving

This is the summarized Day 5 handout. It preserves the chapter structure of
`student-handout-detailed.md`.

## 1. 第一結論

Day 5 is deployability evidence: package the service, name the K8s objects,
estimate GPU memory, validate p50/p95 and VRAM, and document rollback.

## 2. Docker Service Responsibility

List the service responsibilities for Gateway, connector, model service,
database/cache, and observability. You do not need to run all services, but you
must know each service boundary.

## 3. K8s Manifest Inventory

Use Deployment, Service, Ingress, ConfigMap, Secret, PVC, resource limits,
health checks, logs, and rollback notes.

## 4. Minimal Inference Deployment Shape

Your deployment evidence should name image, port, labels/selectors, GPU request,
environment/config, health endpoint, and rollout/rollback path.

## 5. GPU Sizing Formula

```text
required GPU memory = model weights + KV cache + runtime overhead + concurrency overhead + safety margin
```

## 6. vLLM Serving Assumptions

Name `gpu_memory_utilization`, `max_num_seqs`, `max_num_batched_tokens`,
`max_model_len`, `quantization`, and `tensor_parallel_size`.

## 7. Capacity Table

Submit a table with model, params, precision, weights, context, concurrency,
KV cache, overhead, safety margin, target GPU, fit judgment, p50, and p95.

## 8. Validation Plan

Estimate first, then run or define a small load test, measure actual VRAM,
measure p50/p95, compare with estimates, and update safety margin.

## 9. Deployment Checklist

Check pod start, readiness, liveness, service routing, ingress, config, secret
handling, GPU request, logs, and rollback.

## 10. Deployment Risk-Control Map

Map deployment risks to controls and evidence: model readiness, secret handling,
GPU scheduling, VRAM estimate, and rollback.

## 11. Required Student Artifacts

1. K8s manifest checklist.
2. GPU sizing table.
3. vLLM serving assumptions.
4. p50/p95 validation plan.
5. Deployment risk-control map.

## 12. Source Boundary

Use synthetic workloads and no secrets.
