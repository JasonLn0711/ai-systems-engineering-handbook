# Accelerator Day Design Standard

## Purpose

This standard turns one accelerator day into a repeatable course package. Use it
for Day 2, Day 3, and every later accelerator day so the repo stays teachable,
reviewable, and maintainable.

The fixed unit is:

```text
accelerators/<accelerator-name>/day-<NN>-<short-topic>/
├── README.md
├── student-handout.md
├── instructor-guide.md
├── worksheet.md
├── reference-answer-<scenario>.md
├── rubric.md
├── day-<NN+1>-lab-handoff.md
├── glossary-updates.md
└── source-package.md              optional
```

If a day has no lab handoff, still include the handoff file and explain the next
evidence gate.

## Design Thesis

Each day must convert knowledge into evidence.

```text
concept
-> mechanism
-> system boundary
-> artifact template
-> student production
-> review evidence
-> next implementation or evidence gate
```

The day is acceptable only when a TA can grade it from artifacts rather than
from vibes.

## Required Files

| File | Audience | Required contents |
|---|---|---|
| `README.md` | everyone | purpose, target learner, learning objectives, file map, use order, objective-to-assessment map, source boundary, references |
| `student-handout.md` | students | concise concept explanation, core terms, scenario, diagrams, artifact expectations, no reference answer |
| `instructor-guide.md` | instructor | teaching flow, pre-class diagnostic, board/slide plan, questions, common failure gallery |
| `worksheet.md` | students | printable templates for all student artifacts |
| `reference-answer-<scenario>.md` | instructor / TA | filled answer for one public-safe scenario, common mistakes |
| `rubric.md` | instructor / TA | 100-point rubric, objective mapping, TA grading workflow |
| `day-<NN+1>-lab-handoff.md` | instructor / implementer | next-day contract, API/schema/lab acceptance criteria when applicable |
| `glossary-updates.md` | maintainer | terms to merge into global glossary |
| `source-package.md` | maintainer | optional full source package, explicitly not assigned as default student handout |

## Required Day Metadata

Every `README.md` should state:

```text
Day number:
Topic:
Sprint artifact:
Owning module:
Supporting lab:
Target learner:
Prerequisites:
Expected student deliverables:
Next gate:
```

## Learning Objective Rules

Learning objectives must be observable. Avoid:

```text
Understand AI Gateway.
```

Prefer:

```text
Draw an AI Gateway architecture that includes identity, policy, agent, tool,
data, model, guardrail, audit, and human-review boundaries.
```

Each objective must map to:

- one student artifact
- one rubric category
- one validation method

## Student / Instructor Separation

Students receive:

- `student-handout.md`
- `worksheet.md`
- public-safe scenario options

Students do not receive before submission:

- reference answers
- detailed grading notes
- instructor-only failure diagnosis

This keeps the lesson diagnostic and prevents answer-copying.

## Required Artifact Pattern

Every day should produce 3-5 artifacts. A good day usually includes:

1. Architecture or workflow diagram.
2. Responsibility / contract / schema table.
3. Lifecycle / procedure / evaluation path.
4. Risk-control / failure-mode map.
5. Next-gate handoff note.

For implementation days, artifacts may include code, commands, logs, test
output, and screenshots, but they still need review evidence.

## Required Pedagogical Controls

Each day must include:

- pre-class diagnostic with 3-5 questions
- common failure gallery with at least 3 flawed examples
- public-safe real-world scenario
- source-boundary reminder
- TA grading workflow
- one-page summary or completion checklist
- next-day handoff

## Engineering Design Principles

Use these principles in every accelerator day:

- Capability first, scope controls immediately after.
- Mechanism before tool names.
- Interface contracts before implementation.
- Evidence before claims.
- System-enforced controls before prompt instructions.
- Failure modes before grading.
- Day-to-day handoff before closure.

## Source Boundary Rules

Allowed:

- generalized architecture patterns
- public-safe scenarios
- public standards and documentation
- synthetic examples

Not allowed:

- private transcripts
- customer secrets
- credentials
- personal contact routes
- salary or offer details
- unpublished company claims
- identifiable personal data

## Quality Gate

Before marking a day ready:

- [ ] Required files exist.
- [ ] Student handout does not contain reference answer or detailed rubric.
- [ ] Instructor guide has diagnostic and failure gallery.
- [ ] Worksheet can be completed without extra context.
- [ ] Rubric maps objectives to artifacts.
- [ ] Next handoff has explicit acceptance criteria.
- [ ] References are listed when technical tools, standards, or frameworks are named.
- [ ] Source boundary is explicit.

## Recommended Creation Workflow

1. Copy `templates/accelerator-day-package/` into the accelerator directory.
2. Rename the folder to `day-<NN>-<short-topic>/`.
3. Fill `README.md` first.
4. Draft `student-handout.md` without answers.
5. Draft `worksheet.md` from required deliverables.
6. Draft `reference-answer-<scenario>.md`.
7. Draft `rubric.md` and objective mapping.
8. Draft `instructor-guide.md` with diagnostic and failure gallery.
9. Draft `day-<NN+1>-lab-handoff.md`.
10. Add `glossary-updates.md`.
11. Run repo checks and review links.
