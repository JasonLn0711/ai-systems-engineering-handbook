# Glossary Updates: Agent Governance Framework

These terms should be merged into the appropriate global glossary files after
review.

| Term | Definition |
|---|---|
| Agent Registry | Inventory of agents with owner, task scope, risk class, allowed users, tools, data sources, memory scope, evaluation set, red-team suite, and audit events. |
| Task Scope | Explicit boundary describing what an agent is allowed to do. |
| Common Governance | Reusable control layer shared across agents, such as identity, policy, tool boundary, audit, and evaluation. |
| Adapter-Specific Behavior | Scenario-specific mapping from common governance into a customer, domain, or workflow context. |
| Memory Scope | Rule describing memory storage, retention, sharing, deletion, and sensitive-data handling. |
| Tool Boundary | Governance rule for which tools an agent can call and under what decision path. |
| Policy Decision | Enforced result from a policy gate, commonly `allow`, `deny`, or `review`. |
| Human Review Trigger | Condition that routes a request, output, or side-effect tool action to a person for approval. |
| Red-Team Seed | A policy assumption or risk scenario that should become a formal red-team test case. |
| Evaluation Hook | A measurable checkpoint for correctness, safety, latency, coverage, or regression. |
