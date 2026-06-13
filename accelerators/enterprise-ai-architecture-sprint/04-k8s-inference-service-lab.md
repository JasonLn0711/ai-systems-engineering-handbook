# K8s Inference Service Lab

## Purpose

Define the minimum Kubernetes knowledge needed to explain how an AI agent or
model service goes online in enterprise infrastructure. This is not a full
Kubernetes course. It is a deployability evidence plan.

## Target Capability

Deploy one inference service with:

```text
Deployment
Service
Ingress
Secret
ConfigMap
PersistentVolume
GPU resource notes
health check
logs
rollback note
```

## System Diagram

```text
Client
  |
Ingress
  |
Service
  |
Deployment
  |
Pod: inference service
  |-- model server
  |-- health endpoint
  |-- logs
  |-- mounted config
  |-- optional persistent model cache
```

## Evidence Output

- One deployment architecture note.
- One manifest inventory.
- One deployment checklist.
- One troubleshooting guide.
- One acceptance test list.

## Minimum Manifest Inventory

| Resource | Purpose |
|---|---|
| Deployment | run model or gateway service pods |
| Service | stable internal endpoint |
| Ingress | external HTTP entrypoint |
| Secret | sensitive runtime values |
| ConfigMap | non-secret configuration |
| PersistentVolume / PersistentVolumeClaim | model cache or durable runtime data |
| Resource request/limit | CPU, memory, and GPU planning |

## Minimum Viable Output

- A documented manifest set for a mock inference endpoint.
- Health endpoint path.
- Example environment variables.
- Resource request notes.
- Log fields required for deployment debugging.

## Debugging Checklist

- [ ] Pod starts.
- [ ] Readiness and liveness checks pass.
- [ ] Service routes to pod.
- [ ] Ingress reaches service.
- [ ] ConfigMap values are visible.
- [ ] Secret values are loaded without being logged.
- [ ] GPU resource request is documented.
- [ ] Logs include request ID, model, latency, and error code.
- [ ] Rollback path is documented.

## Failure Modes

- Image builds but pod cannot start.
- Service exists but selector does not match pods.
- Ingress is reachable but backend returns timeout.
- Secret is missing or accidentally logged.
- Model cache path is not writable.
- GPU driver/runtime mismatch.
- Health check passes while model endpoint fails.

## Linked Modules And Labs

- `modules/03-container-k8s-devops/`
- `modules/04-gpu-inference-infrastructure/`
- `modules/10-enterprise-delivery-fae/`
- `labs/k8s/`
- `labs/vllm/`

## Next Implementation Gate

Create a minimal K8s lab that deploys a mock inference service first, then
extends it to vLLM or Ollama-backed inference when runtime resources are
available.
