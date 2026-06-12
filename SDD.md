# SDD: AI Systems Engineering Handbook

## 1. System Overview

This repository is a structured tutorial knowledge system. It contains a Master Knowledge Base, Knowledge Modules, chapter-level tutorials, labs, case studies, glossary, diagrams, review rubrics, AI authoring prompts, and content validation rules.

The repository is designed so human authors and AI agents can collaborate without turning the repo into unstructured notes.

## 2. Design Goals

### 2.1 Modularity

Each knowledge domain is isolated into a module. A module should be understandable independently and connected through cross-links to the Master Knowledge Base.

### 2.2 Progressive Learning

Each module should support beginner mental model, engineering mechanism, and production system design.

### 2.3 Traceability

Each chapter should explain sources of concepts, related modules, assumptions, failure modes, and downstream implications.

### 2.4 AI-Agent Maintainability

AI agents should be able to locate the correct template, generate a draft, update glossary, add cross-links, run consistency checks, and produce review comments. AI agents must work inside a strict content schema.

### 2.5 VOISS-Style Relevance

Every major module should eventually connect back to AI Coach, enterprise AI deployment, local/private/on-prem infrastructure, AI Gateway, agent governance, voice AI, customer-side delivery, security, and red teaming.

## 3. Repository Tree

```text
ai-systems-engineering-handbook/
├── README.md
├── SPEC.md
├── SDD.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── master-knowledge-base/
├── modules/
├── glossary/
├── labs/
├── case-studies/
├── diagrams/
├── templates/
├── prompts/
├── review/
├── references/
├── scripts/
├── meta/
└── decisions/
```

## 4. Module Internal Structure

Every module follows this structure:

```text
modules/<module-name>/
├── README.md
├── module-spec.md
├── chapters/
├── labs/
├── diagrams/
├── exercises/
├── glossary.md
├── failure-modes.md
├── checklists.md
└── references.md
```

## 5. Module Index

### 5.1 Module 00: AI Systems Foundations

Purpose: explain what an AI system is.

Topics: AI model vs AI application vs AI system, inference vs training, request lifecycle, data lifecycle, model lifecycle, system boundary, latency, throughput, cost, reliability, human-in-the-loop, agentic workflow, enterprise integration.

### 5.2 Module 01: Linux, OS, And Networking

Purpose: build the system foundation required for deployment.

Topics: Linux filesystem, process, service, daemon, systemd, port, socket, DNS, TLS, SSH, firewall, users and permissions, logs, resource monitoring, package management.

### 5.3 Module 02: Cloud, On-Prem, And Private Cloud

Purpose: teach deployment environments.

Topics: public cloud, private cloud, on-prem, hybrid cloud, IaaS, PaaS, SaaS, bare metal, VM, VPC, VPN, subnet, load balancer, enterprise machine room, compliance boundary, data residency, deployment trade-offs.

### 5.4 Module 03: Container, K8s, And DevOps

Purpose: teach deployment packaging and orchestration.

Topics: Docker image, container runtime, volume, network, Docker Compose, Kubernetes pod, deployment, service, ingress, configmap, secret, health check, rolling update, GPU scheduling in K8s, debugging deployment failures.

### 5.5 Module 04: GPU And AI Inference Infrastructure

Purpose: teach AI compute planning.

Topics: GPU architecture basics, CUDA, ROCm, VRAM, model weights, quantization, KV cache, batch size, sequence length, concurrency, vLLM, Ollama, model serving, GPU sharing, multi-model scheduling, capacity planning, token cost vs local inference cost.

### 5.6 Module 05: LLM Application Architecture

Purpose: teach how LLM apps become systems.

Topics: API gateway, backend service, model router, prompt template, tool calling, structured output, retry, timeout, fallback, streaming, logging, evaluation, observability.

### 5.7 Module 06: RAG And Data Pipeline

Purpose: teach enterprise knowledge ingestion and retrieval.

Topics: ingestion, OCR, parsing, chunking, metadata generation, embedding, vector database, reranker, hybrid search, SQL + KB integration, query rewriting, context construction, citation, evaluation, hallucination control, stale knowledge detection.

### 5.8 Module 07: AI Gateway And Agent Governance

Purpose: teach scalable control of multiple AI agents.

Topics: AI Gateway, policy engine, MCP server, skill, adapter, agent registry, tool registry, permission boundary, memory governance, cross-agent communication, audit log, approval gate, task-specific vs general governance, human review bottleneck, agent red teaming, governance evaluation.

### 5.9 Module 08: Voice AI Systems

Purpose: teach VOISS-relevant voice AI systems.

Topics: audio basics, sampling rate, 8 kHz vs 16 kHz, VAD, ASR, diarization, speaker embedding, overlapping speech, hotwords, TTS, voice cloning, emotion and prosody, wake word, real-time audio pipeline, far-field audio, noise reduction, environmental sound detection, voice sales agent, voice AI latency budget.

### 5.10 Module 09: Security, Red Teaming, And AI Risk

Purpose: teach security from system and AI perspectives.

Topics: IAM, zero trust, audit log, OWASP, NIST, PII, guardrail, prompt injection, data exfiltration, tool abuse, malicious document, user-side attack, agent privilege escalation, red teaming framework, security acceptance test.

### 5.11 Module 10: Enterprise Delivery And FAE Workflow

Purpose: teach customer-facing deployment.

Topics: requirement interview, site survey, machine room checklist, network constraints, GPU inventory, deployment plan, rollback plan, customer acceptance criteria, incident handling, onsite debugging, handover document, FAE escalation path.

### 5.12 Module 11: Spec, SDD, And AI-Assisted Coding Workflow

Purpose: teach how to use Codex and AI agents without losing architecture.

Topics: requirement decomposition, spec writing, SDD writing, design pattern, module boundary, interface contract, anti-overcoupling, context hygiene, AI-generated code review, prompt discipline, architecture guardrails, regression testing.

### 5.13 Module 12: Integrated Case Studies

Purpose: connect modules into realistic projects.

Case studies: Enterprise AI Coach, bank multi-agent governance, on-prem voice AI sales agent, hospital ASR + RAG workflow, semiconductor audio anomaly detection, private cloud AI appliance, multi-GPU local model serving, MCP + skill + adapter enterprise agent platform.

## 6. Content Metadata Schema

Every chapter must include frontmatter:

```yaml
---
title:
module:
chapter_id:
level: beginner | intermediate | advanced
status: draft | review | stable
last_updated:
prerequisites:
learning_objectives:
related_terms:
related_chapters:
voiss_style_relevance:
security_relevance:
estimated_reading_time:
confidentiality: public-safe | internal | restricted
---
```

## 7. Cross-Linking Rules

Every chapter must link to at least one glossary entry, one related chapter, one failure mode, one lab or exercise when applicable, and one system-level implication.

## 8. AI Authoring Workflow

```text
User idea
↓
Curriculum Architect Agent
↓
Module Spec
↓
Chapter Outline
↓
Chapter Writer Agent
↓
Technical Reviewer Agent
↓
Security Reviewer Agent
↓
Style Editor Agent
↓
Human Review
↓
Stable Chapter
```

## 9. Agent Roles

- Curriculum Architect Agent: chooses module placement, chapter outline, prerequisites, learning objectives, and related chapters.
- Chapter Writer Agent: writes drafts from templates and must define terms, explain mechanisms, include failure modes, include exercises, and avoid unsupported claims.
- Technical Reviewer Agent: checks correctness, prerequisites, abstractions, workflow, production realism, and hidden coupling.
- Security Reviewer Agent: checks IAM, PII, prompt injection, audit logs, red-team tests, and data retention controls.
- Style Editor Agent: checks Traditional Chinese, Taiwan terminology, no marketing tone, no vague filler, and precise sentences.
- Consistency Auditor Agent: checks duplicated definitions, inconsistent terminology, broken cross-links, module boundary violations, and glossary mismatch.

## 10. Validation Scripts

The repo should eventually include scripts for frontmatter validation, internal link validation, glossary coverage validation, module index generation, and beginner/intermediate/advanced learning path generation.

## 11. Review Gates

A chapter can move from draft to stable only if it passes:

```text
Q0: frontmatter valid
Q1: terminology defined
Q2: mechanism explained
Q3: workflow included
Q4: security implications included
Q5: failure modes included
Q6: VOISS-style relevance included
Q7: examples included
Q8: exercises included
Q9: cross-links valid
Q10: human approved
```

## 12. Design Trade-Offs

Use one repo because AI systems knowledge is highly interconnected. Use Master KB + modules because the Master KB gives the global map and modules provide depth. Use tutorials as primary content and SOP/checklists only as supporting artifacts. AI agents may draft, but humans own architecture, claim boundaries, and final judgment.

## 13. Failure Modes Of This Repository

- It becomes a dumping ground: mitigate with module placement and templates.
- It becomes too broad: mitigate with VOISS-style relevance and learning paths.
- It becomes too shallow: require mechanism, workflow, and failure modes.
- It becomes outdated: use `last_updated`, status tags, and review cadence.
- AI agents generate inconsistent terms: use glossary-first writing and consistency audit.
- It becomes company SOP instead of tutorial: keep SOP files supporting-only.

## 14. MVP Implementation Plan

Phase 1 creates skeleton docs, templates, master maps, and module directories.

Phase 2 writes the first core chapters across foundations, deployment, Docker, GPU, RAG, AI Gateway, voice AI, security, and Spec/SDD workflow.

Phase 3 adds labs for Docker deployment, local LLM serving, mini RAG, reranking, simple AI Gateway, VAD + ASR, audit log, and policy gates.

Phase 4 adds case studies for Enterprise AI Coach, bank governance, voice sales agent, hospital ASR/RAG, and semiconductor sound anomaly detection.

## 15. Done Definition

The first stable version is done when a new engineer can read the Master KB and understand the whole map, each module has at least one stable introductory chapter, core glossary entries exist, at least three labs are runnable, at least three case studies connect multiple modules, Codex prompts can generate chapters without breaking structure, and review rubrics catch shallow or over-coupled writing.
