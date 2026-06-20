# Rubric — Day 5: K8s GPU Serving

## Scoring Summary

| Category | Points |
|---|---:|
| K8s manifest checklist | 25 |
| GPU sizing table | 30 |
| vLLM serving assumptions | 15 |
| Validation plan | 15 |
| Deployment risk-control map | 10 |
| Source boundary | 5 |
| **Total** | **100** |

## Full-Credit Standards

| Category | Standard |
|---|---|
| K8s manifest checklist | Deployment, Service, Ingress, ConfigMap, Secret, PVC, resources, health, logs, rollback. |
| GPU sizing table | Weights, KV cache, context, concurrency, overhead, safety margin, target GPU, fit judgment. |
| vLLM assumptions | Names memory/concurrency/model length/quantization/tensor parallel knobs and separates vLLM from Gateway. |
| Validation plan | Measures actual VRAM, p50/p95, health, route, logs, rollback. |
| Risk-control map | Maps deployment risks to controls and evidence. |
| Source boundary | No private cluster data, secrets, real customer logs, or unpublished claims. |
