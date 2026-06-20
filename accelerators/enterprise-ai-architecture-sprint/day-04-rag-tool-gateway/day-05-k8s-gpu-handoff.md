# Day 5 K8s / GPU Handoff

Day 4 produces Gateway-controlled data and tool contracts. Day 5 turns those
contracts into deployment and capacity evidence.

## Inputs From Day 4

- RAG schema.
- Tool registry.
- Gateway integration note.
- Adapter/evaluation map.

## Day 5 Acceptance Criteria

- Deployment checklist names Gateway, RAG/tool connector, model service, logs,
  secrets, config, and health checks.
- GPU sizing table includes model weights, KV cache, concurrency, runtime
  overhead, safety margin, p50, and p95.
- K8s notes include Deployment, Service, Ingress, ConfigMap, Secret, PVC, and
  GPU resource request.
- Secrets are loaded but not logged.
- Rollback path is documented.
