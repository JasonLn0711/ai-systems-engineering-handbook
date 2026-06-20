# Enterprise AI Architecture Sprint — Day 3: Red-Team Guardrails

Day 3 turns the Day 2 governance assumptions into executable red-team and
guardrail evidence. The day is acceptable when a TA can inspect the taxonomy,
test-case schema, PII policy event schema, pass/fail rules, and remediation
backlog without relying on student explanation.

## Day Metadata

```text
Day number: Day 3
Topic: Red-Team Guardrails
Sprint artifact: 03-red-teaming-framework.md + 06-pii-guardrail-demo-plan.md
Owning module: modules/09-security-red-teaming/
Supporting lab: labs/security/
Target learner: sophomore CS students / junior engineers
Prerequisites: Day 1 AI Gateway lifecycle, Day 2 agent governance artifacts
Expected student deliverables: taxonomy, 30-case mini harness spec, PII policy event schema, pass/fail report template, remediation backlog
Next gate: day-04-deployment-handoff.md
```

## Learning Objectives

By the end of Day 3, the student should be able to:

1. Convert a governance assumption into a red-team test case with expected
   control, pass/fail rule, and audit evidence.
2. Classify AI-agent risks across prompt injection, PII leakage, tool abuse,
   privilege escalation, memory, retrieval, output, audit, and review bypass.
3. Design a PII / guardrail policy event schema for input, retrieval, tool,
   memory, output, human-review, and audit gates.
4. Build a 30-case mini harness specification across three public-safe tasks.
5. Produce a pass/fail report and remediation backlog that can feed the next
   implementation or deployment gate.

## File Map

| File | Audience | Purpose |
|---|---|---|
| `README.md` | Everyone | Day 3 scope, objectives, file map, completion definition. |
| `student-handout-detailed.md` | Students / instructor | Canonical long-form explanation. |
| `student-handout-detailed.zh-TW.md` | Students / instructor | Complete Taiwan Traditional Chinese detailed version. |
| `student-handout.md` | Students | Short first-principle summary derived from the detailed handout. |
| `worksheet.md` | Students | Templates for taxonomy, 30 cases, policy event schema, report, backlog. |
| `instructor-guide.md` | Instructor / TA | Teaching flow, diagnostic, failure gallery, review prompts. |
| `reference-answer-campus-it-red-team.md` | Instructor / TA | Filled public-safe Campus IT examples and common mistakes. |
| `rubric.md` | Instructor / TA | 100-point rubric and grading workflow. |
| `day-04-rag-tool-gateway-handoff.md` | Instructor / implementer | Next gate for turning red-team evidence into RAG/tool gateway controls. |
| `glossary-updates.md` | Maintainers | Terms to merge later. |
| `source-package.md` | Maintainers | Source boundary and reference routes. |

## Recommended Use Order

1. Students read `student-handout.md`.
2. Students use `student-handout-detailed.md` or
   `student-handout-detailed.zh-TW.md` when they need full examples.
3. Instructor opens with the diagnostic in `instructor-guide.md`.
4. Students fill `worksheet.md` sections 1-4 during the workshop.
5. Students complete the 30-case harness spec and report template after class.
6. TA grades with `rubric.md`.
7. Instructor uses `day-04-deployment-handoff.md` to start the runnable harness
   or deployment evidence gate.

## Objective To Assessment Map

| Objective | Evidence artifact | Rubric category |
|---|---|---|
| Convert governance assumptions to tests | Policy-to-test map and test cases | Test-case quality |
| Classify agent risks | Red-team taxonomy | Threat taxonomy |
| Design policy event schema | PII / guardrail event schema | Guardrail event schema |
| Build 30-case harness spec | 30 test cases across 3 tasks | Harness coverage |
| Produce reviewable outcome evidence | Pass/fail report and backlog | Report and remediation |

## Minimum Deliverables

Every student or group submits:

1. Red-team taxonomy with at least 9 threat categories.
2. PII / guardrail policy event schema.
3. 30-case mini harness spec across 3 public-safe tasks.
4. Pass/fail report template with required audit fields.
5. Remediation backlog with owner, severity, and next control change.

## Student / Instructor Separation

Students receive the handouts, worksheet, and scenario options. Students should
not receive `reference-answer-campus-it-red-team.md` or detailed grading notes
before submission.

## Source Boundary

All examples must be public-safe. Use synthetic Campus IT, sales coach,
manufacturing support, banking knowledge assistant, or healthcare staff-review
intake support scenarios. Do not use private transcripts, customer secrets,
credentials, personal contact routes, salary or offer details, unpublished
company claims, real tickets, or identifiable personal data.

## Background References

- `03-red-teaming-framework.md`
- `06-pii-guardrail-demo-plan.md`
- `day-02-agent-governance/day-03-red-team-handoff.md`
- `modules/09-security-red-teaming/`
- `labs/security/`
- `review/security-review-checklist.md`

## Completion Definition

Day 3 is ready when:

- required files exist;
- student handouts do not contain the reference answer;
- worksheet can be completed without extra context;
- rubric totals 100 points;
- 30-case harness expectations are explicit;
- PII / guardrail event schema includes gates, action, reason, review owner,
  and audit evidence;
- next handoff has acceptance criteria;
- source boundary is explicit.
