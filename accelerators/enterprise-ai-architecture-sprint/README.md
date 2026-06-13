# Enterprise AI Architecture Sprint

This accelerator converts enterprise AI interview and project signals into a
public-safe evidence sprint. It is designed for a learner who already has some
AI implementation experience and needs to produce architecture evidence fast.

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

## How To Use It

1. Start with `00-sprint-map.md`.
2. Use `day-01-ai-gateway/README.md` for the first teaching and
   artifact-production day. The old
   `day-01-ai-gateway-architecture-tutorial.md` path is kept as a compatibility
   entrypoint.
3. Use `day-02-agent-governance/README.md` for the second teaching and
   artifact-production day.
4. Use `../accelerator-day-design-standard.md` and
   `../../templates/accelerator-day-package/` for Day 2 and later course
   packages.
5. Build the artifacts in priority order.
6. Link each sprint output back to the owning module or lab.
7. Treat every numbered sprint file as an evidence-production plan and each
   `day-*` directory as a teachable course package with student, instructor,
   worksheet, reference-answer, rubric, and lab-handoff files.
8. Convert any private source-derived insight into public-safe system language.

## Day Course Packages

| Day | Topic | Course package | Evidence plan |
|---|---|---|---|
| 1 | AI Gateway Architecture Evidence | `day-01-ai-gateway/` | `01-ai-gateway-architecture.md` |
| 2 | Agent Governance Framework | `day-02-agent-governance/` | `02-agent-governance-framework.md` |

## Priority Order

1. AI Gateway architecture.
2. Agent Governance Framework.
3. Red Teaming Framework.
4. GPU capacity estimation model.
5. K8s inference deployment lab.
6. PII / Guardrail demo.
7. MCP / Tool / Memory governance.
8. Physical / real-time voice pipeline.

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
