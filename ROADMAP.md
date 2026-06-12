# Roadmap

## Phase 1: Skeleton

- Establish README, SPEC, SDD, ROADMAP, CONTRIBUTING.
- Establish `master-knowledge-base/`.
- Establish all numbered module directories.
- Add templates, prompts, review rubrics, source-boundary rules, references, and script placeholders.

## Phase 2: Core Path

Write first stable chapters:

1. What is AI Systems Engineering?
2. VOISS-style enterprise AI system map.
3. Local deployment basics.
4. Docker for AI services.
5. GPU/VRAM inference basics.
6. RAG data pipeline basics.
7. AI Gateway and agent governance basics.
8. Voice AI pipeline basics.
9. AI security and red teaming basics.
10. Spec + SDD + AI coding workflow.

## Phase 3: Labs

Add:

1. Deploy FastAPI AI service with Docker.
2. Run local LLM with vLLM or Ollama.
3. Build a mini RAG pipeline.
4. Build metadata + reranker retrieval flow.
5. Build simple AI Gateway mock.
6. Build VAD + ASR demo.
7. Add audit log and policy gate.

## Phase 4: Case Studies

Add:

1. Enterprise AI Coach.
2. Bank multi-agent governance.
3. Voice AI sales agent.
4. Hospital pre-consultation ASR/RAG.
5. Semiconductor sound anomaly detection.
6. Private cloud AI appliance.

## Phase 5: Validation Scripts

Implement:

- `scripts/validate-frontmatter.py`
- `scripts/validate-links.py`
- `scripts/validate-glossary-coverage.py`
- `scripts/generate-module-index.py`
- `scripts/generate-reading-paths.py`

## First Content Gate

Write:

```text
modules/00-ai-systems-foundations/chapters/01-what-is-ai-systems-engineering.md
```

Acceptance target: a reader can explain why AI systems engineering is model + data + infrastructure + workflow + governance + security + evaluation + delivery, not only model API usage.
