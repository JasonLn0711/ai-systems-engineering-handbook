# Student Handout — Day 6: Integrated Demo Memo

This is the summarized Day 6 handout. It preserves the chapter structure of
`student-handout-detailed.md`.

## 1. 第一結論

Day 6 packages the sprint into evidence: demo script, architecture memo, latency
table, known limitations, and acceptance checklist.

## 2. Demo Flow

```text
audio -> VAD/ASR -> PII redaction -> RAG -> agent -> guardrail -> TTS/text -> audit
```

## 3. Demo Script Fields

Name hardware, model names, runtime, input audio condition, ASR latency, LLM
first token latency, TTS first audio latency, end-to-end latency, and known
limits.

## 4. Architecture Memo Thesis

Lead with the capability: the architecture supports enterprise voice-agent tasks
through common audio, model routing, identity, policy, PII, tool, memory, audit,
evaluation, and red-team controls.

## 5. Architecture Layers

Cover audio, knowledge, agent, governance, deployment, and validation layers.

## 6. Validation Dimensions

Include functional, quality, latency, security, and ops evidence.

## 7. Latency Table

Track VAD, ASR, LLM first token, LLM complete, TTS first audio, end-to-end, and
notes for multiple turns.

## 8. Known Limitations As Scope Controls

State current scope and next validation layer instead of pretending the demo is
production-ready.

## 9. Acceptance Checklist

Check repeatability, hardware/runtime/model names, latency, RAG citations,
policy/audit evidence, known limits, and source boundary.

## 10. Required Student Artifacts

1. Demo script.
2. Architecture memo.
3. Latency table.
4. Known limitations.
5. Acceptance checklist.

## 11. Source Boundary

Use synthetic audio and public-safe scenarios.
