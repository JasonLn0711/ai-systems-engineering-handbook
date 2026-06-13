# Rubric: Agent Governance Framework

Total: 100 points.

## Score Summary

| Category | Points | Requirement |
|---|---:|---|
| Governance layer map | 15 | Identity, registry, tool, data, memory, policy, audit, eval, red-team layers |
| Common-vs-adapter separation | 15 | Reusable controls separated from scenario behavior |
| Agent registration | 20 | Complete owner, scope, risk, users, tools, data, memory, approval, eval, red-team fields |
| Policy gate | 20 | allow/deny/review rules for actions, retrieval, tools, memory, PII, review |
| Auditability | 15 | Audit schema records decisions, sources, tools, memory, review, outcome |
| Risk-control and Day 3 readiness | 10 | Risks map to controls and testable red-team seeds |
| Source boundary | 5 | Public-safe scenario, no private source material |

## Learning Objective Mapping

| Learning objective | Evidence | Rubric category |
|---|---|---|
| Explain agent governance purpose | short explanation | Governance layer map |
| Separate common and adapter behavior | common-vs-adapter table | Common-vs-adapter separation |
| Write an agent registration | registration record | Agent registration |
| Write a policy gate | policy record | Policy gate |
| Design an audit event | schema | Auditability |
| Map governance risks | risk-control map | Risk-control and Day 3 readiness |
| Prepare red-team seeds | seed list | Risk-control and Day 3 readiness |

## Governance Layer Map: 15 Points

| Score | Standard |
|---:|---|
| 14-15 | Includes all major layers and shows how they connect |
| 11-13 | Mostly complete, but one or two layers are vague |
| 6-10 | Has registry and policy but misses memory, audit, or red-team |
| 0-5 | Treats agent as a prompt/model only |

## Common-Vs-Adapter Separation: 15 Points

| Score | Standard |
|---:|---|
| 14-15 | Clearly separates reusable governance from scenario-specific behavior |
| 11-13 | Separation is mostly clear, with some mixed fields |
| 6-10 | Table exists but common controls and adapter behavior are confused |
| 0-5 | Rebuilds governance as one-off scenario prose |

## Agent Registration: 20 Points

| Score | Standard |
|---:|---|
| 18-20 | All required fields complete and enforceable |
| 14-17 | Most fields complete, but memory/eval/red-team or risk class is weak |
| 8-13 | Basic agent ID and tools exist, but owner/scope/boundaries are vague |
| 0-7 | Agent is unregistered or allowed broad access |

## Policy Gate: 20 Points

| Score | Standard |
|---:|---|
| 18-20 | Clear allow/deny/review rules for user, data, tools, memory, PII, review |
| 14-17 | Good policy shape but one control area is weak |
| 8-13 | Policy is mostly prose or prompt instruction |
| 0-7 | No enforceable policy decision |

## Auditability: 15 Points

| Score | Standard |
|---:|---|
| 14-15 | Audit schema records identity, agent, policy, sources, tools, memory, review, outcome |
| 11-13 | Audit schema mostly complete but misses one decision field |
| 6-10 | Audit records final text but not enough decisions |
| 0-5 | No meaningful audit event |

## Risk-Control And Day 3 Readiness: 10 Points

| Score | Standard |
|---:|---|
| 9-10 | At least five risks and three testable red-team seeds |
| 6-8 | Risks are useful, but seeds or evidence are vague |
| 3-5 | Risks are generic and not tied to controls |
| 0-2 | No usable risk-control reasoning |

## Source Boundary: 5 Points

| Score | Standard |
|---:|---|
| 5 | Fully public-safe |
| 3-4 | Mostly safe but too specific in minor places |
| 1-2 | Potentially sensitive context |
| 0 | Private transcript, customer secret, credential, or identifiable personal data |

## TA Grading Workflow

1. Check source boundary first.
2. Confirm all seven deliverables are present.
3. Verify the agent registration fields are enforceable.
4. Check policy returns `allow`, `deny`, or `review`.
5. Reject prompt-only approval where system policy is required.
6. Inspect audit schema for decision evidence, not only final output.
7. Confirm memory scope includes retention and sharing.
8. Confirm at least three red-team seeds can become Day 3 tests.
9. Give one next-gate comment for red-team implementation.
