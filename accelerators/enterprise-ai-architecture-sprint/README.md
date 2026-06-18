# Enterprise AI Architecture Sprint

This accelerator converts enterprise AI interview and project signals into a
public-safe evidence sprint. It is designed for a learner who already has some
AI implementation experience and needs to produce architecture evidence fast.

The primary 7-day student-facing onboarding tutorial is:

```text
7-day-consulting-onboarding-tutorial.zh-TW.md
```

The expanded 28/30-day spiral bootcamp design is:

```text
30-day-spiral-bootcamp.zh-TW.md
```

Use that file when the learner needs a Traditional Chinese, tutorial-style,
sophomore-friendly path from interview signals to enterprise voice AI system
delivery evidence.

The sprint goal is:

```text
potential
-> architecture evidence
-> deployable system reasoning
-> governance and security proof
-> customer-delivery readiness
```

## What This Accelerator Produces

- AI Gateway architecture diagram and contract.
- Agent governance framework.
- Red teaming framework and test taxonomy.
- K8s inference-service lab plan.
- GPU capacity estimation model.
- PII / guardrail demo plan.
- MCP / tool / memory governance map.
- Real-time voice-agent evidence plan.
- Consolidated 7-day onboarding pack for enterprise voice AI systems.
- Expanded 28-day bootcamp plus 2-day mock review and portfolio packaging
  plan.

## How To Use It

1. Start with `7-day-consulting-onboarding-tutorial.zh-TW.md` when the
   learner needs the complete 7-day overview curriculum.
2. Use `30-day-spiral-bootcamp.zh-TW.md` when the learner needs the
   expanded 28/30-day beginner-to-deliverable bootcamp.
3. Use `00-sprint-map.md` as the evidence map and day-by-day checklist.
4. Use `day-01-ai-gateway/README.md` for the first teaching and
   artifact-production day. The old
   `day-01-ai-gateway-architecture-tutorial.md` path is kept as a compatibility
   entrypoint.
5. Use `day-02-agent-governance/README.md` for the second teaching and
   artifact-production day.
6. Use `../accelerator-day-design-standard.md` and
   `../../templates/accelerator-day-package/` for Day 2 and later course
   packages.
7. Build the artifacts in priority order.
8. Link each sprint output back to the owning module or lab.
9. Treat every numbered sprint file as an evidence-production plan and each
   `day-*` directory as a teachable course package with student, instructor,
   worksheet, reference-answer, rubric, and lab-handoff files.
10. Convert any private source-derived insight into public-safe system
    language.

## Day Course Packages

| Day | Topic | Course package | Evidence plan |
|---|---|---|---|
| 1 | AI Gateway Architecture Evidence | `day-01-ai-gateway/` | `01-ai-gateway-architecture.md` |
| 2 | Agent Governance Framework | `day-02-agent-governance/` | `02-agent-governance-framework.md` |

The full 7-day tutorial covers voice AI, RAG, tool governance, red teaming,
PII guardrails, Docker/K8s, GPU sizing, demo packaging, and first-30 days
onboarding strategy. The 30-day bootcamp revisits the same themes in four
spiral passes: overview, mechanism, lab, and delivery.

## Priority Order

1. Domain map and issue tree.
2. Voice AI pipeline.
3. RAG, tool use, agent governance, and AI Gateway.
4. PII, guardrails, and red teaming.
5. Docker, K8s, GPU sizing, and vLLM serving.
6. Integrated demo and architecture memo.
7. Onboarding pack and first-30-days plan.

## Public-Safe Boundary

This accelerator must not store raw interview transcripts, offer details,
private company claims, contact routes, credentials, customer secrets, or named
customer-specific private facts. Use generalized enterprise AI scenarios such
as bank multi-agent governance, insurance sales coaching, manufacturing audio
monitoring, and customer machine-room deployment.

## Owning Modules

- `modules/03-container-k8s-devops/`
- `modules/04-gpu-inference-infrastructure/`
- `modules/06-rag-data-pipeline/`
- `modules/07-ai-gateway-agent-governance/`
- `modules/08-voice-ai-systems/`
- `modules/09-security-red-teaming/`
- `modules/10-enterprise-delivery-fae/`
- `modules/11-spec-sdd-ai-coding-workflow/`

## Evidence Definition

An artifact counts as evidence only when it includes:

- architecture view
- minimum viable output
- validation checklist
- failure modes
- linked module/lab path
- next implementation gate
