# ADR-0001: Use Master Knowledge Base Plus Knowledge Modules

## Status

Accepted

## Context

AI systems engineering knowledge is graph-shaped. Deployment, data pipeline, RAG, agent governance, voice AI, security, and customer delivery depend on one another.

A single linear tutorial would hide cross-module dependencies. Many separate repos would duplicate concepts and make learning paths harder to maintain.

## Decision

Use one repository with:

- `master-knowledge-base/` for the global map and learning paths
- `modules/` for domain-specific tutorial systems
- `labs/`, `case-studies/`, `glossary/`, `review/`, and `prompts/` as shared support layers

## Consequences

- Cross-links are first-class.
- AI agents can route work by module.
- SOPs remain supporting artifacts rather than the organizing layer.
- Sensitive source material must stay outside the tutorial layer.
