# Reference Answer — Voice Agent Demo Memo

> Instructor / TA only.

## Demo Script Example

```text
Scenario: synthetic sales coach role-play review
Hardware: local workstation or documented lab machine
Models: ASR model, LLM/runtime, optional TTS model
Runtime: local script or demo service
Input audio condition: 2-minute synthetic clean audio file
Flow: audio -> ASR -> PII redaction -> RAG -> agent feedback -> text/TTS -> audit
```

## Architecture Memo Thesis

The v0 architecture supports controlled enterprise coaching demos by separating
audio intake, retrieval, agent reasoning, governance controls, deployment
evidence, and validation metrics.

## Known Limitations Example

```text
Current scope:
  Controlled short-turn audio-file input with synthetic transcript and public-safe
  knowledge snippets.

Validation layer:
  Real-time interruption, overlap-heavy audio, noisy far-field input, and
  production customer data require separate latency, accuracy, and governance
  validation before deployment.
```

## Common Mistakes

- No hardware/runtime/model names.
- Latency table only has end-to-end time.
- Memo does not mention governance.
- Limitations are written as apologies instead of scope controls.
