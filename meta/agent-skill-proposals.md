# Agent Skill Proposals For Accelerator Course Authoring

## Purpose

The Day 1 design pattern is reusable enough to become agent skills. This file
tracks proposed and implemented skills. The first implemented skill is installed
locally at:

```text
~/.codex/skills/accelerator-day-architect/
```

That location makes the skill auto-discoverable by local Codex sessions. Keep
repo-local proposals here so the course design rationale remains visible even
when the executable skill lives outside the repo.

Skill design follows these principles:

- Keep each skill concise and action-oriented.
- Put long templates and examples in references or assets, not the main
  `SKILL.md`.
- Trigger skills by concrete authoring tasks, not vague planning language.
- Preserve student/instructor separation.
- Keep source-boundary review as a reusable gate.

## Proposed Skill Set

### 1. `accelerator-day-architect`

Status: implemented locally in `~/.codex/skills/accelerator-day-architect/`.

First applied use: created
`accelerators/enterprise-ai-architecture-sprint/day-02-agent-governance/` from
the Day 2 Agent Governance Framework sprint artifact.

Purpose: turn a sprint-map item into a complete day package plan.

Use when:

- creating Day 2, Day 3, or later accelerator course packages
- mapping a sprint artifact to student deliverables
- deciding required files, learning objectives, and next-day handoff

Inputs:

- accelerator sprint map
- day number and topic
- owning module and supporting lab
- target learner and prerequisites

Outputs:

- day folder plan
- learning objectives
- objective-to-assessment map
- file checklist
- source-boundary note

Resources to bundle:

- `references/accelerator-day-design-standard.md`
- `assets/accelerator-day-package/`

Implemented resources:

- `~/.codex/skills/accelerator-day-architect/SKILL.md`
- `~/.codex/skills/accelerator-day-architect/references/accelerator-day-design-standard.md`
- `~/.codex/skills/accelerator-day-architect/assets/accelerator-day-package/`

### 2. `student-handout-writer`

Purpose: write concise student-facing accelerator handouts without reference
answers or instructor-only grading notes.

Use when:

- drafting `student-handout.md`
- reducing a long source package into readable student material
- checking whether a handout is beginner-readable

Inputs:

- day README
- topic notes
- scenario
- required artifacts

Outputs:

- student handout
- key terms
- diagrams or workflows
- student submission requirements

Guardrails:

- no reference answers
- no detailed rubric answers
- no private source material

### 3. `instructor-guide-builder`

Purpose: create instructor-facing teaching flow, diagnostics, questions, and
failure galleries.

Use when:

- drafting `instructor-guide.md`
- designing 150-minute or 180-minute class flows
- creating common failure galleries
- adding pre-class diagnostics

Outputs:

- teaching flow
- diagnostic questions
- board/slide plan
- instructor prompts
- common failure gallery

### 4. `artifact-rubric-reviewer`

Purpose: build and review rubrics that map learning objectives to artifacts.

Use when:

- drafting `rubric.md`
- checking whether every objective has evidence
- designing TA grading workflow
- auditing if controls are inspectable rather than slogan-level

Outputs:

- 100-point rubric
- objective mapping table
- TA grading workflow
- quality-gate checklist

### 5. `lab-handoff-contract-designer`

Purpose: convert a day artifact into the next implementation or evidence gate.

Use when:

- drafting `day-<NN+1>-lab-handoff.md`
- turning architecture evidence into API/schema/test contracts
- defining acceptance criteria for the next lab

Outputs:

- next-day purpose
- API or workflow contract
- model/schema shapes
- pseudo-code or procedure
- acceptance criteria

### 6. `source-boundary-course-reviewer`

Purpose: review accelerator course material for public-safe source boundaries
and positive scope language.

Use when:

- checking scenarios, examples, references, and notes before publication
- converting sensitive source-derived ideas into generalized tutorial language
- reviewing medical, financial, customer, or company-facing examples

Outputs:

- source-boundary findings
- rewrite suggestions
- public-safe scenario replacements
- positive scope-control phrasing

## Recommended First Skill To Build

Build `accelerator-day-architect` first. It can route work to the other skills
and enforce the file structure. The other skills can be created after two or
three more days reveal which repeated tasks are most painful.

## Why Not One Giant Skill

One giant skill would mirror the original problem: one artifact containing too
many roles. Separate skills preserve role boundaries:

- architect decides structure
- handout writer writes student material
- instructor builder writes teacher material
- rubric reviewer grades evidence
- handoff designer connects days
- source-boundary reviewer protects publication scope

## Skill Scope Decision

The first executable skill is installed as a local-global Codex skill at:

```text
~/.codex/skills/accelerator-day-architect/
```

This location was chosen for the first implementation because the skill captures
the reusable authoring method, not only one repo-specific lesson. Its job is to
turn any accelerator day into a reviewable course package with student,
instructor, worksheet, reference-answer, rubric, glossary, and next-day handoff
files. That pattern can support Day 2, Day 3, and later AI systems engineering
curricula without requiring each session to rediscover the structure.

The skill also copies the repo's day-package standard and template assets into
the skill folder:

```text
~/.codex/skills/accelerator-day-architect/references/accelerator-day-design-standard.md
~/.codex/skills/accelerator-day-architect/assets/accelerator-day-package/
```

The repo remains the source of record for course content, while the skill is the
local execution helper that applies the course-design method.

## Why The First Skill Is Local-Global

Local-global means "available to this machine's Codex sessions," not "published
to every user" or "committed into every repo." The practical benefits are:

- Auto-discovery: future prompts such as "設計 Day 3 accelerator 教程" can trigger
  the skill without re-explaining the file structure.
- Reuse: the same method can help this repo, a future course repo, or a
  professor-facing teaching packet.
- Separation of concerns: repo files hold the course artifacts; the skill holds
  the repeated authoring behavior.
- Faster iteration: Day 2 and Day 3 can test whether the method is useful before
  creating a full family of smaller skills.

This decision is reversible. If the skill should travel with the repo or be
reviewed by collaborators, copy the folder into a repo-local path such as:

```text
agent-skills/accelerator-day-architect/
```

Then update this file to mark the repo-local version as the canonical skill
draft and decide whether to remove the local-global copy.

## When Repo-Local Is Better

Use a repo-local skill when the skill:

- encodes paths, policies, or assumptions that apply only to this handbook;
- needs to be version-reviewed with pull requests;
- should be shared with a professor, TA, or collaborator through the repo;
- contains course-specific grading policy or unpublished curriculum decisions;
- should not trigger in other repos.

For this first skill, the current `SKILL.md` deliberately stays narrow and
method-focused. It does not include credentials, private source material, or
unpublished external claims. The repo-specific evidence and examples stay in the
repo day packages.

## Remaining Skill Decisions

1. After Day 3, decide whether `accelerator-day-architect` should remain the
   only skill or be split into smaller skills.
2. Decide whether to create a repo-local copy for professor collaboration.
3. Decide whether skills should write directly into the repo or produce
   patch-ready drafts for instructor review.
4. Keep final human review for source boundary and course quality with the repo
   maintainer or course owner.

## Important Additional Recommendations

### Maintain Day-Level Traceability

Every day should state which previous day it consumes and which next day it
enables. This prevents isolated lessons.

### Add A Course Release Gate

Before publishing a week of accelerator content, run a week-level review:

- all days have required files
- all handoffs connect
- no reference answers leak into student material
- glossary terms are reconciled
- source boundaries are clean
- rubrics use comparable scoring scales

### Keep A Student Work Sample Library

After running the course, collect anonymized examples:

- strong answer
- passing answer
- common failure answer

Use these only after removing personal or private details.

### Add Versioning To Course Days

Each day should eventually carry:

```text
status: draft | pilot | stable
last_reviewed:
review_owner:
tested_with_students: yes | no
```

### Build A Consistency Checker Later

A future script can check whether every `day-*` directory contains required
files and whether student handouts accidentally contain `reference answer`,
`rubric`, or instructor-only text.
