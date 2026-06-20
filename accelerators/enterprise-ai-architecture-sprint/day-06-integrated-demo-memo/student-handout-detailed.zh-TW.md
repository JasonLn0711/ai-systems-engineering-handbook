# Detailed Student Handout zh-TW — Day 6: Integrated Demo Memo

## 1. 第一結論

Day 6 把前五天的 artifacts 變成可以展示、可以量測、可以驗收的 evidence pack。Demo 可以是 semi-real-time，不必假裝 production-ready；重點是 scope、metrics、known limits 與可重現。

## 2. Demo Flow

```text
audio file or microphone
-> VAD / ASR
-> optional diarization label
-> PII redaction
-> RAG retrieve
-> agent feedback
-> output guardrail
-> TTS or text response
-> audit log
```

每一步都要能回答：輸入是什麼、輸出是什麼、控制在哪裡、evidence 存在哪裡。

## 3. Demo Script Fields

Demo script 必須列：

```text
hardware
model names
runtime
input audio condition
ASR latency
LLM first token latency
TTS first audio latency
end-to-end latency
known limitations
```

## 4. Architecture Memo Thesis

建議標題：

```text
Enterprise Voice Agent Gateway v0 Architecture Proposal
```

第一段先寫 capability：

```text
本架構支援多種企業 AI Coach 任務。共同層負責 audio intake、model routing、
identity、policy、PII、tool permission、memory scope、audit、evaluation、
red teaming；adapter 層負責不同任務的 taxonomy、RAG corpus、output schema、
policy rules、tool permissions、evaluator。
```

## 5. Architecture Layers

```text
Audio layer:
  VAD / ASR / diarization / hotword correction / TTS

Knowledge layer:
  parsing / metadata / embedding / vector DB / reranker / citation

Agent layer:
  orchestrator / tool registry / memory / approval queue

Governance layer:
  identity / RBAC / ABAC / PII / policy / audit / red teaming

Deployment layer:
  Docker / K8s / vLLM / observability / rollback
```

## 6. Validation Dimensions

| Dimension | Evidence |
|---|---|
| Functional | 完成指定 coaching / retrieval / report task |
| Quality | ASR WER/CER, keyword accuracy, RAG hit@k/MRR, faithfulness |
| Latency | p50/p95 by component and end-to-end |
| Security | red-team pass rate, PII leakage tests |
| Ops | health checks, logs, GPU memory, rollback |

## 7. Latency Table

| Turn | VAD ms | ASR ms | LLM first token ms | LLM complete ms | TTS first audio ms | End-to-end ms | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 |  |  |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |

## 8. Known Limitations As Scope Controls

Use positive scope-control language:

```text
Current scope:
  The demo supports controlled audio-file or short-turn microphone input.

Validation layer:
  Real-time barge-in, overlap-heavy audio, and noisy far-field audio require
  separate latency and accuracy validation before production deployment.
```

## 9. Acceptance Checklist

```text
demo can be repeated
hardware and runtime are named
models are named
component latency is measured or planned
RAG citations are inspectable
policy/audit events are inspectable
known limits are stated as validation layers
```

## 10. Required Student Artifacts

1. `demo-script.md`
2. `architecture-memo.md`
3. `latency-table.csv` or markdown table
4. `known-limitations.md`
5. `acceptance-checklist.md`

## 11. Source Boundary

Use synthetic audio and public-safe scenarios. Do not use private recordings,
real customer calls, private transcripts, credentials, or identifiable personal
data.
