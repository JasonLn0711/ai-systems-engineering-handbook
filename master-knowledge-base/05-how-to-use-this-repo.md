# How To Use This Repo

Use this repository as a tutorial system, not as a quick command dump.

## When Learning A New Topic

1. Start with the Master Knowledge Base map.
2. Choose the owning module.
3. Read the module README and `module-spec.md`.
4. Read chapters in order.
5. Use labs to verify understanding.
6. Add glossary entries when terms become reusable.

## When Adding A New Chapter

1. Confirm the owning module.
2. Copy `templates/chapter-template.md`.
3. Fill frontmatter.
4. Define terms before use.
5. Explain mechanism, workflow, failure modes, and security implications.
6. Add exercises and related chapters.
7. Run the review rubric.

## When Using Codex

Do not ask Codex to write the whole handbook. Give Codex one module, one chapter, one template, and one review target at a time.

Good task shape:

```text
Write modules/07-ai-gateway-agent-governance/chapters/01-why-ai-gateway-exists.md.
Follow templates/chapter-template.md.
Use Traditional Chinese with Taiwan terminology.
Explain mechanism, failure modes, security implications, and exercises.
Do not invent vendor-specific claims.
```

## When Capturing Private Source-Derived Insight

Never copy raw private source material into the handbook. Convert it into public-safe tutorial requirements and keep the original evidence in its canonical private repo.
