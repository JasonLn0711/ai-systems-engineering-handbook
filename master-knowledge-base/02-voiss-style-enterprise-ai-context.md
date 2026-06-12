# VOISS-Style Enterprise AI Context

This file records the general enterprise-AI context that shapes the curriculum. It does not record private interview details or treat interview statements as public company facts.

The relevant learning context is:

- enterprise AI is a workflow, data, deployment, governance, and evaluation problem
- local and controlled-environment deployment require Linux, Docker, Kubernetes, GPU, networking, and observability knowledge
- AI Gateway and agent governance matter when many agents, knowledge bases, SQL sources, and tools must share controlled access
- RAG quality depends on ingestion, metadata, reranking, context construction, and evaluation
- voice AI systems require ASR, VAD, diarization, TTS, wake word, latency budgeting, and noisy-environment testing
- customer delivery requires requirement interviews, site surveys, deployment plans, rollback plans, acceptance criteria, and incident handling
- AI-assisted coding needs spec-first and SDD-first discipline so generated systems remain modular, reviewable, and testable

## Curriculum Implication

The handbook should teach from real system pressure:

```text
enterprise workflow
→ data flow
→ model/tool orchestration
→ deployment environment
→ governance boundary
→ security review
→ acceptance test
→ maintenance loop
```

This makes cloud/on-prem knowledge one major module inside a larger AI systems curriculum, not the whole curriculum by itself.
