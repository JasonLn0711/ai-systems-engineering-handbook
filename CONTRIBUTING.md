# Contributing

This repo is maintained as a tutorial knowledge system.

## Add A Chapter

1. Pick the correct module.
2. Copy `templates/chapter-template.md`.
3. Add frontmatter.
4. Define terms before using them.
5. Explain mechanism, workflow, failure modes, security implications, and verification.
6. Add related chapters and glossary links.
7. Run the review checklist in `review/rubric.md`.

## Add A Module

Do not add a module for a single topic. Add one only when the topic needs its own learning path, glossary, labs, failure modes, and case studies.

New modules must include:

- `README.md`
- `module-spec.md`
- `chapters/`
- `labs/`
- `diagrams/`
- `exercises/`
- `glossary.md`
- `failure-modes.md`
- `checklists.md`
- `references.md`

## AI Agent Rules

Codex or another AI agent may draft content only after reading:

- `README.md`
- `SPEC.md`
- `SDD.md`
- `templates/chapter-template.md`
- `review/rubric.md`
- relevant module `README.md`

AI-generated content must not invent company facts, copy raw private source material, or skip security and failure-mode sections.

## Source Boundary

Private interviews, demos, project notes, customer conversations, salary discussions, credentials, and unpublished business information must not be copied into this repo. Convert source-derived insight into general tutorial requirements and cite only public-safe references.

## Style

Use Traditional Chinese for tutorial prose unless a file is clearly English-facing. Keep technical terms in English when that is the common engineering term. Write with positive scope: capability, evidence, boundary, and next validation layer.
