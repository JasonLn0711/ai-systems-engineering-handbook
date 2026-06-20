# Source Package — Day 5: K8s GPU Serving

## Source Boundary

Allowed: public-safe deployment patterns, synthetic workloads, public model
serving examples, public Kubernetes and vLLM documentation concepts.

Not allowed: credentials, private cluster names, customer deployment details,
real logs with secrets, unpublished company claims, or identifiable data.

## Repo Sources Used

- `04-k8s-inference-service-lab.md`
- `05-gpu-capacity-estimation-model.md`
- `assets/gpu-capacity-estimation-template.csv`
- `7-day-consulting-onboarding-tutorial.zh-TW.md`
- `modules/03-container-k8s-devops/`
- `modules/04-gpu-inference-infrastructure/`
- `labs/k8s/`
- `labs/vllm/`

## Technical Language

Day 5 uses Deployment, Service, Ingress, ConfigMap, Secret, PVC, readiness,
liveness, GPU resource request, model weights, KV cache, runtime overhead,
safety margin, p50/p95, vLLM serving assumptions, and rollback.
