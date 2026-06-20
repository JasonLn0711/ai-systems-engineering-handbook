# Worksheet — Day 5: K8s GPU Serving

## 1. Manifest Inventory

| Resource | Purpose | Required fields | Evidence |
|---|---|---|---|
| Deployment |  |  |  |
| Service |  |  |  |
| Ingress |  |  |  |
| ConfigMap |  |  |  |
| Secret |  |  |  |
| PVC |  |  |  |
| Resource request/limit |  |  |  |

## 2. GPU Sizing Table

| model | params_B | precision | weight_GB | context | concurrency | kv_cache_GB | overhead_GB | safety_GB | total_GB | GPU | fits | p50 | p95 |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## 3. vLLM Assumptions

```text
gpu_memory_utilization:
max_num_seqs:
max_num_batched_tokens:
max_model_len:
quantization:
tensor_parallel_size:
```

## 4. Validation Plan

| Check | Command/evidence | Pass condition |
|---|---|---|
| Pod starts |  |  |
| Readiness passes |  |  |
| Service routes |  |  |
| GPU visible |  |  |
| VRAM observed |  |  |
| p50/p95 measured |  |  |
| Rollback documented |  |  |

## 5. Risk-Control Map

| Risk | Control | Evidence |
|---|---|---|
|  |  |  |

## 6. Final Checklist

- [ ] K8s objects are named.
- [ ] Secret values are not logged.
- [ ] GPU request is documented.
- [ ] Sizing formula includes KV cache and safety margin.
- [ ] p50/p95 validation exists.
- [ ] Rollback path exists.
