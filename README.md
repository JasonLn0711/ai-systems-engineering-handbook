# AI Systems Engineering Handbook

A Master Knowledge Base and Modular Tutorial System for AI System Engineering.

中文定位：

`AI 系統工程完整教程：從地端部署、AI Gateway、Agent Governance、RAG、語音 AI 到企業交付`

This repository is a structured tutorial system for learning how to design, deploy, secure, evaluate, and operate enterprise AI systems.

It is not a company engineering handbook and not a collection of random tutorials. The goal is to build deep operational understanding, not shallow tool familiarity.

## Core Coverage

- AI system foundations
- on-prem, private cloud, and public cloud deployment
- Linux, Docker, K8s, networking, storage, and GPU infrastructure
- LLM application architecture
- RAG and enterprise data pipelines
- AI Gateway and agent governance
- MCP servers, skills, and adapters
- voice AI systems: ASR, TTS, diarization, VAD, wake word, real-time voice
- AI security, PII, guardrails, prompt injection, red teaming
- enterprise delivery, FAE workflow, spec, SDD, and AI-assisted coding discipline

## Repository Model

The repository is built as one master knowledge base plus many knowledge modules.

```text
ai-systems-engineering-handbook/
├── master-knowledge-base/
├── modules/
├── labs/
├── case-studies/
├── glossary/
├── diagrams/
├── templates/
├── prompts/
├── review/
├── references/
└── scripts/
```

The key distinction:

- Master Knowledge Base explains the full map.
- Knowledge Modules teach one domain deeply.
- Tutorials teach concepts progressively.
- Labs force implementation.
- Case Studies connect domains into realistic enterprise AI projects.
- Checklists are memory aids, not substitutes for tutorials.

## Module Set

- `00-ai-systems-foundations`
- `01-linux-os-networking`
- `02-cloud-onprem-private-cloud`
- `03-container-k8s-devops`
- `04-gpu-inference-infrastructure`
- `05-llm-application-architecture`
- `06-rag-data-pipeline`
- `07-ai-gateway-agent-governance`
- `08-voice-ai-systems`
- `09-security-red-teaming`
- `10-enterprise-delivery-fae`
- `11-spec-sdd-ai-coding-workflow`
- `12-case-study-integrations`

## First Path

Start here:

1. `master-knowledge-base/00-overview.md`
2. `master-knowledge-base/01-ai-systems-engineering-map.md`
3. `master-knowledge-base/02-voiss-style-enterprise-ai-context.md`
4. `master-knowledge-base/03-learning-paths.md`
5. `master-knowledge-base/05-how-to-use-this-repo.md`

Then choose a module by current work:

- Deployment work: modules `01` to `04`
- RAG and agent work: modules `06` to `07`
- Voice AI work: module `08`
- Security review: module `09`
- Customer delivery: module `10`
- Codex workflow: module `11`

## Chapter Standard

Every chapter must answer:

1. What is it?
2. Why does it exist?
3. How does it work underneath?
4. How is it used in real AI systems?
5. What fails when it is misunderstood?
6. What are the security and governance implications?
7. How should the learner practice or verify it?

Use `templates/chapter-template.md` for all new chapters.

## Source Boundary

This repo may be informed by private learning context, interviews, demos, and project notes, but it must not store raw private transcripts, salary details, customer secrets, credentials, personal contact routes, or unverified company claims.

Rewrite source-derived insight as general tutorial requirements. Keep sensitive evidence in its canonical private repo.
