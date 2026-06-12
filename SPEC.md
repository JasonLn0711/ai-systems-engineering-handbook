# SPEC: AI Systems Engineering Handbook

## 1. Project Name

Repository name: `ai-systems-engineering-handbook`

Display title: `AI Systems Engineering Handbook`

Subtitle: `A Master Knowledge Base and Modular Tutorial System for AI System Engineering`

中文名稱：`AI 系統工程完整教程`

## 2. Product Type

This repository is a tutorial-oriented knowledge system.

It is not merely:

- a company engineering handbook
- an SOP wiki
- a random notes collection
- a cloud deployment tutorial
- a prompt engineering cookbook

It is a Master Knowledge Base + Knowledge Modules system for learning, organizing, and operationalizing the knowledge required to design, deploy, evaluate, secure, and maintain AI systems in enterprise environments.

## 3. Primary Goal

Build a structured, extensible, AI-agent-maintainable tutorial repository that teaches the knowledge required for an AI systems engineer working in VOISS-like enterprise AI environments.

The tutorial must cover:

1. AI system foundations.
2. Enterprise AI product context.
3. On-prem, private cloud, and public cloud deployment.
4. GPU inference infrastructure.
5. Docker, K8s, Linux, networking, and storage.
6. AI Gateway and AI agent governance.
7. RAG, MCP server, skill, adapter, and agentic pipeline.
8. Data pipeline engineering.
9. Voice AI systems: ASR, TTS, diarization, VAD, wake word, voice cloning, real-time voice.
10. Security, red teaming, prompt injection, PII, guardrails, audit logging.
11. Customer deployment, FAE workflow, onsite debugging.
12. Spec, SDD, design pattern, and AI-assisted coding discipline.

## 4. Non-Goals

This repository should not become:

1. A collection of disconnected tutorials.
2. A company policy handbook.
3. A list of commands without explanation.
4. A shallow AI tools index.
5. A pure academic ML textbook.
6. A vendor-specific cloud certification guide.
7. A prompt-only guide.
8. A place to dump meeting notes without structure.

## 5. Target Learners

Primary learner: an AI systems engineer who needs to work on enterprise AI projects involving local model deployment, AI agent systems, RAG pipelines, AI Gateway, governance, voice AI, customer-side deployment, GPU infrastructure, security, and auditability.

Secondary learners:

- Junior FAE engineers who need deployment and troubleshooting depth.
- Backend engineers moving into AI systems.
- ML engineers moving from model training to production systems.
- Product and PM people who need enough technical depth to understand AI system constraints.
- Technical founders or architects designing enterprise AI products.

## 6. Expected Learning Outcome

After completing the core path, the learner should be able to answer and implement:

1. What is the difference between cloud, private cloud, on-prem, and hybrid deployment?
2. How do Linux, Docker, K8s, GPU, networking, storage, and security combine into an AI deployment environment?
3. How do you estimate VRAM, RAM, GPU scheduling, model loading, KV cache, concurrency, and inference cost?
4. How do you design a local AI service that can be deployed in an enterprise machine room?
5. How do you design an AI Gateway that manages multiple agents, tools, knowledge bases, and user permissions?
6. How do you design RAG with ingestion, metadata, chunking, embedding, reranking, evaluation, and monitoring?
7. How do you design voice AI pipelines involving ASR, TTS, VAD, diarization, wake word, and real-time latency?
8. How do you secure AI systems against prompt injection, data leakage, PII exposure, bad tool use, and cross-agent privilege escalation?
9. How do you write specs and SDDs before using Codex or AI agents for implementation?
10. How do you prevent AI-generated systems from becoming over-coupled, context-polluted, and unmaintainable?

## 7. Repository Philosophy

Every chapter must answer five questions:

1. What is it?
2. Why does it exist?
3. How does it work underneath?
4. How is it used in real AI systems?
5. What fails when it is misunderstood?

Each chapter must connect concepts to operating systems, networking, software engineering, system engineering, security, AI model behavior, and enterprise deployment constraints.

## 8. Content Architecture

The repository uses:

1. Master Knowledge Base.
2. Knowledge Modules.
3. Tutorials.
4. Labs.
5. Case Studies.
6. Glossary.
7. Diagrams.
8. SOP-like Checklists.
9. Design Documents.
10. Agent Prompts.
11. Review Rubrics.

Master Knowledge Base explains the full map. Knowledge Modules teach one domain deeply. Tutorials teach progressively. Labs force implementation. Case Studies connect everything to enterprise projects. Checklists support memory but do not replace tutorials.

## 9. Content Unit Types

- Concept Chapter: explains foundational knowledge.
- System Chapter: explains how several concepts compose into a working system.
- Workflow Chapter: explains a process.
- Lab: hands-on implementation or debugging.
- Case Study: business + technical system design.
- Design Note: trade-off or decision explanation.
- Glossary Entry: short but precise definition.

## 10. Required Chapter Template

Every chapter must follow `templates/chapter-template.md` and include:

- why this chapter exists
- mental model
- core terms
- mechanism
- system context
- engineering workflow
- VOISS-style relevance
- security and governance implications
- failure modes
- minimal example
- production-grade example
- checklist
- exercises
- related chapters

## 11. Required Lab Template

Every lab must follow `templates/lab-template.md` and include objective, prerequisites, system diagram, environment, steps, expected output, debugging guide, failure modes, extension tasks, and cleanup.

## 12. Required Case Study Template

Every case study must follow `templates/case-study-template.md` and include scenario, business goal, user workflow, system requirements, data flow, model flow, infrastructure architecture, governance architecture, deployment architecture, security risks, failure modes, trade-offs, recommended design, and monitoring.

## 13. Quality Bar

A chapter is acceptable only if it:

1. Defines all key terms.
2. Explains the underlying mechanism.
3. Connects to real AI system design.
4. Includes at least one failure mode.
5. Includes a practical workflow.
6. Includes a VOISS-style relevance section.
7. Avoids marketing language.
8. Avoids vague claims.
9. Distinguishes toy example from production reality.
10. Tells the learner what to do next.

## 14. AI Agent Usage Policy

AI agents may be used for outlining, drafting, summarizing, generating diagrams, generating examples, writing labs, checking consistency, producing glossary entries, and reviewing for missing failure modes.

AI agents must not invent unsupported facts, write chapters without templates, merge unrelated modules, introduce hidden dependencies, skip security implications, produce tutorial prose without exercises, or generate code that violates the intended architecture.

Every AI-generated chapter must pass curriculum review, technical review, security review, style review, and link/reference review.

## 15. MVP Scope

The first version should contain:

1. `README.md`
2. `SPEC.md`
3. `SDD.md`
4. `ROADMAP.md`
5. `master-knowledge-base/00-overview.md`
6. `master-knowledge-base/01-ai-systems-engineering-map.md`
7. `master-knowledge-base/02-voiss-style-enterprise-ai-context.md`
8. `master-knowledge-base/03-learning-paths.md`
9. `master-knowledge-base/04-core-mental-models.md`
10. `master-knowledge-base/05-how-to-use-this-repo.md`
11. `master-knowledge-base/06-cross-module-dependency-map.md`
12. all numbered module folders
13. `glossary/`
14. `prompts/`
15. `templates/`
16. `review/`
17. `references/`
18. `scripts/`

## 16. Success Criteria

The repository succeeds if a learner can:

1. Explain VOISS-style AI system architecture.
2. Deploy a local AI service with Docker.
3. Understand what K8s adds beyond Docker.
4. Estimate basic GPU and VRAM needs.
5. Design a simple RAG pipeline.
6. Explain why metadata and intermediate outputs matter.
7. Design a basic AI Gateway with policy checks.
8. Explain agent skill/adapter/MCP architecture.
9. Explain voice AI pipeline components.
10. Identify AI system security risks.
11. Write a spec and SDD before implementation.
12. Use Codex without letting architecture collapse.
