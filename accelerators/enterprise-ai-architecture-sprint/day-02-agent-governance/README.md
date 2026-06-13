# Day 2: Agent Governance Framework

## Purpose

Day 2 turns the Day 1 AI Gateway architecture into a reusable governance
framework for enterprise agents. The learner does not build every runtime
component yet. The learner produces agent, tool, memory, policy, audit, and
review contracts that can drive a minimal gateway mock and later red-team tests.

The core claim is:

```text
An enterprise agent is not governed by intention.
It is governed by registry, policy, tool boundaries, memory scope, audit events,
evaluation hooks, and review states.
```

## Day Metadata

```text
Day number: 2
Topic: Agent Governance Framework
Sprint artifact: Agent governance framework
Owning module: modules/07-ai-gateway-agent-governance/
Supporting lab: labs/ai-gateway/
Target learner: sophomore CS students / junior engineers
Prerequisites: Day 1 AI Gateway architecture, HTTP/JSON, roles, logs, basic API concepts
Expected student deliverables: governance layer map, common-vs-adapter table, agent registration, policy gate, audit event schema, risk-control map
Next gate: Day 3 red-team handoff for prompt injection, tool abuse, memory leakage, and policy bypass tests
```

## Target Learner

This lesson is written for students who can already draw the Day 1 AI Gateway
request lifecycle. They should understand identity, policy, tool broker, RAG
connector, guardrail, audit log, and human review at a beginner level. They do
not need to know production IAM, OPA, Cedar, or full red-team methodology yet.

## Learning Objectives

By the end of Day 2, the student should be able to:

1. Explain why agents need registration, ownership, task scope, allowed tools,
   allowed data sources, memory scope, policy gates, audit events, and review
   states.
2. Separate common governance rules from adapter-specific behavior.
3. Write an agent registration record for one public-safe enterprise agent.
4. Write a policy gate that returns `allow`, `deny`, or `review`.
5. Design an audit event schema that records identity, agent, tool, source,
   memory, policy, guardrail, review, and outcome.
6. Map tool abuse, memory leakage, permission bypass, prompt-only approval, and
   missing audit detail to concrete governance controls.
7. Produce governance evidence that can become Day 3 red-team test cases.

## File Map

| File | Audience | Purpose |
|---|---|---|
| `student-handout.md` | Students | Main lecture handout without reference answers. |
| `worksheet.md` | Students | Printable in-class governance templates. |
| `instructor-guide.md` | Instructor | Teaching flow, diagnostic, questions, failure gallery. |
| `reference-answer-campus-it-agent.md` | Instructor / TA | Campus IT agent governance reference answer. |
| `rubric.md` | Instructor / TA | 100-point rubric, objective mapping, grading workflow. |
| `day-03-red-team-handoff.md` | Instructor / implementer | Contract for turning governance rules into red-team cases. |
| `glossary-updates.md` | Maintainers | Terms to merge into global glossary later. |
| `source-package.md` | Maintainers | Source notes and routing references for this day. |

## Recommended Use Order

1. Send `student-handout.md` sections 1-5 as pre-class reading.
2. Start class with the diagnostic in `instructor-guide.md`.
3. Review Day 1 AI Gateway lifecycle.
4. Teach governance layers using `student-handout.md`.
5. Run the workshop using `worksheet.md`.
6. Grade using `rubric.md`.
7. Compare instructor/TA review against `reference-answer-campus-it-agent.md`.
8. Move red-team work into `day-03-red-team-handoff.md`.

## Learning Objective To Assessment Map

| Objective | Evidence artifact | Rubric category |
|---|---|---|
| Agent governance purpose | short explanation in worksheet | Beginner clarity |
| Common vs adapter separation | common-vs-adapter table | Governance separation |
| Agent registration | YAML/JSON registration record | Agent registration |
| Policy gate | policy gate template | Policy gate |
| Audit event schema | audit event schema | Auditability |
| Risk-control reasoning | risk-control map | Risk-control map |
| Day 3 readiness | red-team seed cases | Next-gate readiness |

## Student / Instructor Separation

Students should receive:

- `student-handout.md`
- `worksheet.md`
- public-safe scenario options

Students should not receive before submission:

- `reference-answer-campus-it-agent.md`
- detailed grading notes in `rubric.md`
- instructor-only failure diagnosis notes

## Minimum Day 2 Deliverables

Every student or group submits:

1. Governance layer map.
2. Common-vs-adapter table.
3. Agent registration record.
4. Policy gate record.
5. Audit event schema.
6. Risk-control map.
7. Day 3 red-team seed list.

## Source Boundary

All scenarios must be public-safe. Use generalized examples such as campus IT
helpdesk, bank internal knowledge assistant, medical intake support, and
manufacturing audio monitoring. Do not use private transcripts, customer
secrets, credentials, personal contact routes, salary or offer details,
unpublished company claims, or identifiable personal data.

## Background References

These references are for instructor and maintainer context. Day 2 does not
require students to master them.

- OWASP Top 10 for Large Language Model Applications:
  <https://owasp.org/www-project-top-10-for-large-language-model-applications/>
- NIST AI Risk Management Framework:
  <https://www.nist.gov/itl/ai-risk-management-framework>
- Open Policy Agent documentation: <https://www.openpolicyagent.org/docs/latest/>
- Cedar policy language documentation: <https://docs.cedarpolicy.com/>
- OpenTelemetry documentation: <https://opentelemetry.io/docs/>
