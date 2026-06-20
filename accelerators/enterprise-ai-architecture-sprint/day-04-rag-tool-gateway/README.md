# Enterprise AI Architecture Sprint — Day 4: RAG Tool Gateway

Day 4 turns RAG, tool use, MCP-style connector access, and AI Gateway routing
into reviewable integration evidence. The day is acceptable when students can
submit a RAG schema, typed tool registry, gateway integration note, adapter map,
and evaluation plan that a TA can inspect without oral explanation.

## Day Metadata

```text
Day number: Day 4
Topic: RAG + Tool Registry + Gateway Integration
Sprint artifact: 07-mcp-tool-memory-governance.md + 02-agent-governance-framework.md
Owning module: modules/07-ai-gateway-agent-governance/
Supporting lab: labs/ai-gateway/
Target learner: sophomore CS students / junior engineers
Prerequisites: Day 1 gateway lifecycle, Day 2 governance contracts, Day 3 guardrail test cases
Expected student deliverables: RAG schema, tool registry, agent-tool lifecycle, gateway integration note, adapter/eval map
Next gate: day-05-k8s-gpu-handoff.md
```

## Learning Objectives

1. Design a RAG metadata schema that supports ACL, freshness, citation, rerank,
   and abstain behavior.
2. Write a typed tool registry with permissions, side effects, approval,
   idempotency, timeout, retry, and audit fields.
3. Explain the agent-tool lifecycle from proposed action to policy decision,
   execution, redaction, audit, and bounded result.
4. Connect RAG, tools, memory, and MCP-style connectors to the AI Gateway rather
   than letting agents access them directly.
5. Define three task adapters with taxonomy, tools, policy, and evaluator.

## File Map

| File | Audience | Purpose |
|---|---|---|
| `README.md` | Everyone | Day 4 scope, objectives, file map, completion definition. |
| `student-handout-detailed.md` | Students / instructor | Canonical long-form explanation. |
| `student-handout-detailed.zh-TW.md` | Students / instructor | Complete Taiwan Traditional Chinese detailed version. |
| `student-handout.md` | Students | First-principle summary. |
| `worksheet.md` | Students | Templates for all Day 4 artifacts. |
| `instructor-guide.md` | Instructor / TA | Teaching flow, diagnostic, failure gallery. |
| `reference-answer-sales-coach-gateway.md` | Instructor / TA | Filled public-safe answer. |
| `rubric.md` | Instructor / TA | 100-point rubric. |
| `day-05-k8s-gpu-handoff.md` | Instructor / implementer | Next deployment and sizing gate. |
| `glossary-updates.md` | Maintainers | Candidate terms to merge. |
| `source-package.md` | Maintainers | Source boundary and reference routes. |

## Minimum Deliverables

1. RAG schema with metadata, ACL, freshness, citation, reranker, threshold, and
   abstain fields.
2. Tool registry with one read-only tool and one approval-gated side-effect tool.
3. Agent-tool lifecycle diagram or step list.
4. Gateway integration note showing identity, policy, tool/data/memory boundary,
   audit, and HTTP outcome.
5. Adapter/evaluation map for three public-safe tasks.

## Objective To Assessment Map

| Objective | Evidence artifact | Rubric category |
|---|---|---|
| Design RAG metadata schema | RAG schema | RAG schema quality |
| Write typed tool registry | Tool registry | Tool governance |
| Explain lifecycle | Agent-tool lifecycle | Lifecycle and audit |
| Connect to gateway | Gateway integration note | Gateway integration |
| Define adapters/evals | Adapter/evaluation map | Adapter and evaluation |

## Source Boundary

Use synthetic sales coach, fraud-call analyzer, HR coach, Campus IT, banking
knowledge assistant, or manufacturing support scenarios. Do not use private
transcripts, real customer data, credentials, unpublished company claims, or
identifiable personal data.
