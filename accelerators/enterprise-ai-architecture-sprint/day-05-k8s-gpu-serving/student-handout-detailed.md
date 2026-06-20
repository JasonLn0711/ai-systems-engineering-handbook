# Detailed Student Handout — Day 5: K8s GPU Serving

## 1. 第一結論

Day 5 的能力是用初階但正確的方式回答：

```text
這個 AI system 怎麼部署？
需要多少 GPU / VRAM？
怎麼知道它真的能跑？
出了問題怎麼查？
怎麼 rollback？
```

這一天不是完整 K8s 課，也不是 GPU 硬體課。它是 deployability evidence。

## 2. Docker Service Responsibility

Docker 把服務、依賴與 runtime 包起來。最小服務拆法：

```text
api-gateway
rag-tool-connector
model-service
postgres
redis
observability
```

學生不一定要把全部服務跑起來，但 README 或 architecture note 必須說清楚每個 service 的責任、輸入、輸出、health check 與 logs。

## 3. K8s Manifest Inventory

| Resource | 用途 | AI system example |
|---|---|---|
| Pod | 跑 container 的最小單位 | inference service pod |
| Deployment | 管理 replica 與 rolling update | model server rollout |
| Service | 穩定內部入口 | gateway 呼叫 model service |
| Ingress | 對外 HTTP/HTTPS | demo 或 customer entrypoint |
| ConfigMap | 非敏感設定 | model name, feature flags |
| Secret | 敏感設定 | API key, DB password |
| PVC | 持久化儲存 | model cache, logs |
| Resource limits | CPU/memory/GPU 要求 | `nvidia.com/gpu: 1` |

GPU 在 K8s 不是自動出現。通常需要 device plugin 讓 kubelet 知道節點有哪些 GPU resources 可以排程。

## 4. Minimal Inference Deployment Shape

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-service
spec:
  replicas: 1
  selector:
    matchLabels:
      app: vllm-service
  template:
    metadata:
      labels:
        app: vllm-service
    spec:
      containers:
        - name: vllm
          image: vllm/vllm-openai:latest
          ports:
            - containerPort: 8000
          resources:
            limits:
              nvidia.com/gpu: 1
          env:
            - name: MODEL_NAME
              value: "replace-with-model-name"
```

這只是 manifest evidence，不代表 production-ready。學生要補 health endpoint、secret/config policy、logs、resource notes 與 rollback path。

## 5. GPU Sizing Formula

不要只說「A6000 應該可以」。先拆公式：

```text
required GPU memory
= model weights
+ KV cache
+ runtime overhead
+ batch / concurrency overhead
+ safety margin
```

模型權重粗估：

```text
FP16 / BF16: params * 2 bytes
INT8: params * 1 byte + overhead
INT4: params * 0.5 byte + overhead
```

KV cache depends on layers, KV heads, head dimension, context length,
concurrency, and bytes per element. Students can use a simplified estimate if
they name the assumption and leave a validation plan.

## 6. vLLM Serving Assumptions

Students should name these knobs:

```text
gpu_memory_utilization
max_num_seqs
max_num_batched_tokens
max_model_len
quantization
tensor_parallel_size
```

vLLM is model-serving data plane. It is not the AI Gateway. Gateway owns
identity, policy, tool permission, audit, review, routing, and source boundary.

## 7. Capacity Table

| model | params_B | precision | weight_GB | context | concurrency | kv_cache_GB | overhead_GB | safety_GB | total_GB | GPU | fits | p50 | p95 |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---:|---:|
| 7B | 7 | INT4 |  | 4096 | 4 |  |  |  |  | 24GB |  |  |  |
| 31B | 31 | INT4 |  | 8192 | 2 |  |  |  |  | 48GB |  |  |  |
| 70B | 70 | INT4 |  | 8192 | 4 |  |  |  |  | H100/H200 |  |  |  |

## 8. Validation Plan

```text
estimate memory before deployment
-> run small load test
-> measure actual VRAM
-> measure p50/p95 latency
-> compare estimate vs observed usage
-> update safety margin
```

## 9. Deployment Checklist

```text
pod starts
readiness passes
liveness passes
service routes
ingress reaches service
secret loaded but not logged
config visible
GPU resource request documented
logs include request_id, model, latency, error_code
rollback path documented
```

## 10. Deployment Risk-Control Map

| Risk | Control | Evidence |
|---|---|---|
| Pod starts but model endpoint fails | Readiness check hits model route | readiness log |
| Secret is logged | Secret handling and log scrub | log review |
| GPU unavailable | Resource request and node/device plugin check | scheduling event |
| VRAM underestimation | Capacity table + observed VRAM | validation report |
| Rollout breaks service | Deployment strategy and rollback note | rollback command |

## 11. Required Student Artifacts

1. K8s manifest checklist.
2. GPU sizing table.
3. vLLM serving assumptions.
4. p50/p95 validation plan.
5. Deployment risk-control map.

## 12. Source Boundary

Use synthetic workloads. Do not include private cluster names, credentials,
customer deployment data, or logs containing secrets.
