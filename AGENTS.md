# Codex Local Agent Defaults

## Accelerator Student Handout Rule

For accelerator day packages, maintain a two-layer student handout structure:

- `student-handout-detailed.md` is the canonical long-form student explanation.
  When Jason provides new day-specific source material, transcript-derived
  notes, examples, technical expansions, or teaching details, integrate them
  into the detailed version first after applying the repo source-boundary rules.
- `student-handout-detailed.zh-TW.md` is the Taiwan Traditional Chinese
  companion to the detailed handout. It must be a complete, section-preserving
  translation of `student-handout-detailed.md`, not a summary, adaptation, or
  selected excerpt. Preserve every heading, table, code block, diagram, list,
  example, and source-boundary note. Keep technical identifiers, commands,
  filenames, API names, status codes, schemas, and code in their original form
  unless a translation note is needed for student comprehension.
- `student-handout.md` is the normal class handout. It must be derived from
  `student-handout-detailed.md` by first-principle summarization.
- The normal handout must preserve every chapter and subchapter from the
  detailed version, while shortening explanations to the core claim, mechanism,
  boundary, student action, and review evidence.
- Do not add new concepts only to the normal handout. If a concept belongs in
  student-facing material, add it to the detailed handout first, then regenerate
  or update the normal handout from that source.
- When the detailed handout changes, update the Taiwan Traditional Chinese
  detailed version before treating the day package as ready.
- Keep reference answers, grading notes, and instructor-only diagnosis out of
  all student handouts.

Use `accelerators/accelerator-day-design-standard.md` as the repo-level source
of truth for accelerator package structure.
