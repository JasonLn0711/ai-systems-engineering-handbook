---
id: sop.gpu-sizing
status: draft
owner: TBD
last_updated: 2026-06-12
type: sop
domain: model-serving
confidentiality: internal
---

# SOP — GPU / VRAM Capacity Planning

## Inputs

- Model name / parameter count
- Quantization level
- Context length
- Expected concurrency
- Batch size
- KV cache policy
- Latency target
- Number of models loaded concurrently

## Procedure

1. Estimate model weight memory.
2. Estimate KV cache memory.
3. Estimate runtime overhead.
4. Estimate embedding / reranker / ASR / TTS companion models.
5. Add operational buffer.
6. Test with realistic traffic.
7. Produce recommendation: feasible / marginal / infeasible.

## Output

```yaml
recommended_gpu:
  model_set: []
  quantization: []
  max_concurrency: TBD
  expected_latency_p50: TBD
  expected_latency_p95: TBD
  risk: TBD
  fallback_plan: TBD
```
