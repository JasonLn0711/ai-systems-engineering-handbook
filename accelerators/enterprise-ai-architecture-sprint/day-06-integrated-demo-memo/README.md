# Enterprise AI Architecture Sprint — Day 6: Integrated Demo Memo

Day 6 packages the previous five days into demonstration evidence: a demo
script, architecture memo, latency table, known limitations, and acceptance
checklist. The demo may be semi-real-time; the evidence must be measurable,
bounded, and repeatable.

## Day Metadata

```text
Day number: Day 6
Topic: Integrated Demo + Architecture Memo
Sprint artifact: 08-voice-agent-evidence-plan.md + 01-ai-gateway-architecture.md
Owning module: modules/08-voice-ai-systems/
Supporting lab: labs/voice-ai/
Target learner: sophomore CS students / junior engineers
Prerequisites: Day 1-5 artifacts
Expected student deliverables: demo script, architecture memo, latency table, known limitations, acceptance checklist
Next gate: day-07-onboarding-handoff.md
```

## Learning Objectives

1. Scope a semi-real-time enterprise voice agent demo without overstating
   production readiness.
2. Write a demo script that names hardware, models, runtime, input condition,
   component latency, and known limits.
3. Write a two-page architecture memo connecting audio, RAG, agent, governance,
   deployment, and validation layers.
4. Measure or specify p50/p95 latency by component.
5. Express limitations as scope controls and next validation layers.

## File Map

| File | Audience | Purpose |
|---|---|---|
| `README.md` | Everyone | Day 6 scope and completion definition. |
| `student-handout-detailed.md` | Students / instructor | Canonical long-form explanation. |
| `student-handout-detailed.zh-TW.md` | Students / instructor | Complete Taiwan Traditional Chinese detailed version. |
| `student-handout.md` | Students | Summary handout. |
| `worksheet.md` | Students | Templates for demo script, memo, latency, acceptance. |
| `instructor-guide.md` | Instructor / TA | Teaching flow and failure gallery. |
| `reference-answer-voice-agent-demo.md` | Instructor / TA | Filled public-safe example. |
| `rubric.md` | Instructor / TA | 100-point rubric. |
| `day-07-onboarding-handoff.md` | Instructor / implementer | Next onboarding pack gate. |
| `glossary-updates.md` | Maintainers | Candidate terms. |
| `source-package.md` | Maintainers | Source boundary and reference routes. |

## Minimum Deliverables

1. Demo script.
2. Two-page architecture memo.
3. Latency table with component-level p50/p95 plan.
4. Known limitations in positive scope-control language.
5. Acceptance checklist.

## Source Boundary

Use synthetic audio, synthetic transcripts, and public-safe architecture
examples. Do not use private call recordings, customer data, credentials,
private transcripts, or identifiable personal data.
