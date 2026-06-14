# Day <DAY_NUMBER>: <TOPIC>

## Purpose

<One paragraph explaining what this day turns into reviewable evidence.>

## Day Metadata

```text
Day number: <DAY_NUMBER>
Topic: <TOPIC>
Sprint artifact: <ARTIFACT>
Owning module: <MODULE_PATH>
Supporting lab: <LAB_PATH>
Target learner: sophomore CS students / junior engineers
Prerequisites: <PREREQUISITES>
Expected student deliverables: <DELIVERABLES>
Next gate: <NEXT_DAY_OR_LAB_GATE>
```

## Target Learner

<Describe what the learner already knows and what they do not need yet.>

## Learning Objectives

By the end of this day, the student should be able to:

1. <Observable objective>
2. <Observable objective>
3. <Observable objective>
4. <Observable objective>
5. <Observable objective>

## File Map

| File | Audience | Purpose |
|---|---|---|
| `student-handout.md` | Students | Normal first-principle summary derived from `student-handout-detailed.md`, without reference answers. |
| `student-handout-detailed.md` | Students / instructor | Canonical long-form student explanation; add new student-facing material here first. |
| `student-handout-detailed.zh-TW.md` | Students / instructor | Complete Taiwan Traditional Chinese version of `student-handout-detailed.md`; preserve every detail. |
| `worksheet.md` | Students | Printable in-class artifact templates. |
| `instructor-guide.md` | Instructor | Teaching flow, diagnostic, prompts, failure gallery. |
| `reference-answer-<scenario>.md` | Instructor / TA | Filled reference answer. |
| `rubric.md` | Instructor / TA | 100-point rubric, objective mapping, grading workflow. |
| `day-<NEXT_DAY_NUMBER>-lab-handoff.md` | Instructor / implementer | Next-day contract and acceptance criteria. |
| `glossary-updates.md` | Maintainers | Terms to merge into global glossary later. |
| `source-package.md` | Maintainers | Optional original full package, not a student handout. |

## Recommended Use Order

1. Send `student-handout.md` sections <X-Y> as pre-class reading.
2. Start class with the diagnostic in `instructor-guide.md`.
3. Teach the main concept using `student-handout.md`; use
   `student-handout-detailed.md` for deeper examples or follow-up reading.
4. Use `student-handout-detailed.zh-TW.md` when students need the complete
   Taiwan Traditional Chinese detailed version.
5. Run the workshop using `worksheet.md`.
6. Grade using `rubric.md`.
7. Compare instructor/TA review against `reference-answer-<scenario>.md`.
8. Move implementation work into `day-<NEXT_DAY_NUMBER>-lab-handoff.md`.

## Learning Objective To Assessment Map

| Objective | Evidence artifact | Rubric category |
|---|---|---|
| <Objective> | <Artifact> | <Rubric category> |
| <Objective> | <Artifact> | <Rubric category> |
| <Objective> | <Artifact> | <Rubric category> |

## Student / Instructor Separation

Students should receive:

- `student-handout.md`
- `student-handout-detailed.md` when deeper reading is appropriate
- `student-handout-detailed.zh-TW.md` when students need the complete Taiwan
  Traditional Chinese detailed version
- `worksheet.md`
- public-safe scenario options

Students should not receive before submission:

- `reference-answer-<scenario>.md`
- detailed grading notes in `rubric.md`
- instructor-only failure diagnosis notes

## Student Handout Maintenance Rule

When new student-facing source material is added to this day, integrate it into
`student-handout-detailed.md` first. Then update
`student-handout-detailed.zh-TW.md` as the complete Taiwan Traditional Chinese
version, and update `student-handout.md` as a first-principle summary of the
detailed version.

The normal handout must preserve every chapter and subchapter from the detailed
version while shortening each section to the core claim, mechanism, boundary,
student action, and review evidence.

The Taiwan Traditional Chinese detailed handout must preserve every heading,
subheading, paragraph, table, diagram, code block, command, schema, list,
example, source-boundary note, and reference from the detailed source. It is not
a summary or selected excerpt.

## Minimum Day Deliverables

Every student or group submits:

1. <Artifact 1>
2. <Artifact 2>
3. <Artifact 3>
4. <Artifact 4>

## Source Boundary

All scenarios must be public-safe. Do not use private transcripts, customer
secrets, credentials, personal contact routes, salary or offer details,
unpublished company claims, or identifiable personal data.

## Background References

- <Reference 1>
- <Reference 2>
- <Reference 3>
