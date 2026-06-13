# GPU Capacity Estimation Model

## Purpose

Create a repeatable capacity-estimation model for local or on-prem AI
inference. The goal is to explain why a workload needs a given GPU class,
memory size, concurrency limit, and safety buffer.

## Core Formula

```text
required GPU memory
= model weights
+ KV cache
+ runtime overhead
+ batch / concurrency overhead
+ safety margin
```

## Evidence Output

- Capacity-estimation table.
- Assumption list.
- Scenario comparison.
- Validation plan.

## Estimation Inputs

| Input | Meaning | Example question |
|---|---|---|
| model family | dense, MoE, ASR, TTS, reranker | What model is loaded? |
| parameter count | model size | How large are the weights? |
| precision | FP16, BF16, INT8, INT4 | What quantization is used? |
| context length | prompt + generated tokens | How long can a request be? |
| concurrency | active requests or sessions | How many users at once? |
| KV cache per request | transformer runtime memory | How much memory grows at runtime? |
| runtime overhead | serving framework, tokenizer, buffers | What does the server itself need? |
| safety margin | headroom for spikes and fragmentation | How much unused VRAM is reserved? |

## Scenario Table

| Scenario | GPU target | Workload | Main constraint |
|---|---|---|---|
| developer workstation | RTX-class GPU | local demo and small tests | VRAM and thermal headroom |
| lab server | A6000-class GPU | prototype multi-model serving | memory sharing and concurrency |
| enterprise server | H200-class GPU | customer inference capacity | concurrency, reliability, isolation |
| edge box | compact accelerator | local agent and low latency | power, memory, and portability |

## Minimum Viable Output

- One spreadsheet or CSV with at least three hardware scenarios.
- Model-weight estimate.
- KV-cache assumption.
- Concurrency assumption.
- Runtime buffer.
- Safety margin.
- Pass/fail capacity judgment.

## Validation Method

1. Estimate memory before deployment.
2. Run a small load test.
3. Measure actual VRAM.
4. Measure p50/p95 latency.
5. Compare estimate vs observed usage.
6. Update safety margin.

## Failure Modes

- Model weights are estimated but KV cache is ignored.
- Single-user latency is measured but concurrency is ignored.
- Quantization reduces memory but quality or compatibility is not tested.
- Runtime buffer is too small and service crashes under spike.
- Hosted inference fallback is used without data-boundary review.

## Linked Modules And Labs

- `modules/04-gpu-inference-infrastructure/`
- `modules/05-llm-application-architecture/`
- `labs/vllm/`
- `review/checklists/gpu-sizing-sop.md`

## Next Implementation Gate

Fill `assets/gpu-capacity-estimation-template.csv` for three scenarios:
workstation, lab server, and enterprise server.
