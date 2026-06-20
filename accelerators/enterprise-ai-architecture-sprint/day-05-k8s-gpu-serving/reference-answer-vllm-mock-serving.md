# Reference Answer — vLLM Mock Serving

> Instructor / TA only.

## Manifest Checklist Example

| Resource | Purpose | Evidence |
|---|---|---|
| Deployment | run `vllm-service` pod | replica, labels, image, port |
| Service | stable internal endpoint | selector matches pod labels |
| Ingress | demo HTTP route | path maps to service |
| ConfigMap | model name and feature flags | non-secret values only |
| Secret | API key or DB password | loaded but not logged |
| PVC | model cache | writable cache path |
| Resource limit | GPU request | `nvidia.com/gpu: 1` |

## GPU Sizing Example

| model | params_B | precision | weight_GB | context | concurrency | kv_cache_GB | overhead_GB | safety_GB | total_GB | GPU | fits |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 7B | 7 | INT4 | 4 | 4096 | 4 | 4 | 4 | 4 | 16 | 24GB | yes |
| 31B | 31 | INT4 | 18 | 8192 | 2 | 8 | 8 | 8 | 42 | 48GB | likely |
| 70B | 70 | INT4 | 40 | 8192 | 4 | 20 | 12 | 12 | 84 | H100/H200 | depends |

These are teaching estimates, not vendor guarantees. The validation plan must
measure actual VRAM and p50/p95 latency.

## Common Mistakes

- Health check only checks `/`, not model readiness.
- No rollback note.
- Secret appears in example logs.
- GPU sizing omits KV cache.
- vLLM config is treated as governance.
