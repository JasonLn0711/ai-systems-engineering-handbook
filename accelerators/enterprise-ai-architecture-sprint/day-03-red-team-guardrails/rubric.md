# Rubric — Day 3: Red-Team Guardrails

> 100-point grading rubric. Grade submitted artifacts, not oral confidence.

## 1. Scoring Summary

| Category | Points |
|---|---:|
| Threat taxonomy | 15 |
| PII / guardrail policy event schema | 20 |
| Test-case quality | 25 |
| 30-case harness coverage | 15 |
| Pass/fail report and remediation backlog | 15 |
| Source boundary | 10 |
| **Total** | **100** |

## 2. Threat Taxonomy — 15

| Points | Standard |
|---:|---|
| 13-15 | Covers at least 9 categories and maps each to a concrete target control. |
| 10-12 | Covers most categories but a few controls are vague. |
| 6-9 | Has a list of risks but weak mapping to controls. |
| 0-5 | Random attack ideas without taxonomy. |

## 3. PII / Guardrail Policy Event Schema — 20

| Subcategory | Points | Standard |
|---|---:|---|
| Gate coverage | 5 | Covers input, retrieval, tool, memory, output, review, audit. |
| Risk/action fields | 5 | Records risk type, detected pattern, action, reason. |
| Review and ownership | 4 | Includes review owner/status when needed. |
| Audit evidence | 4 | Includes trace, case ID, policy/control, outcome. |
| PII minimization | 2 | Avoids raw secrets and unnecessary PII. |

## 4. Test-Case Quality — 25

| Points | Standard |
|---:|---|
| 22-25 | Every inspected case has attacker goal, target control, expected decision, safe behavior, required audit fields, pass/fail rule, severity, owner. |
| 17-21 | Cases are mostly executable; some audit or safe-behavior fields need detail. |
| 10-16 | Cases are understandable but weakly testable. |
| 0-9 | Cases are prompt lists without expected controls or pass/fail rules. |

## 5. 30-Case Harness Coverage — 15

| Points | Standard |
|---:|---|
| 13-15 | 30 cases, 3 tasks, at least 9 categories, balanced risk coverage. |
| 10-12 | 30 cases exist but task/category distribution is uneven. |
| 6-9 | Fewer than 30 cases or only 1-2 tasks. |
| 0-5 | Harness matrix is missing or too sparse. |

## 6. Pass/Fail Report And Backlog — 15

| Points | Standard |
|---:|---|
| 13-15 | Report distinguishes pass/fail/review and backlog has owner, severity, control change, next validation. |
| 10-12 | Report and backlog exist but owner or next validation is incomplete. |
| 6-9 | Report is mostly status labels without evidence. |
| 0-5 | No usable report or remediation backlog. |

## 7. Source Boundary — 10

| Points | Standard |
|---:|---|
| 10 | Fully public-safe synthetic scenario. |
| 7-9 | Mostly public-safe with minor unnecessary detail. |
| 4-6 | Too close to a real private scenario; needs generalization. |
| 0-3 | Contains credentials, identifiable personal data, real tickets, private transcripts, customer secrets, or unpublished company claims. |

## 8. TA Workflow

1. Count case total and task distribution.
2. Check taxonomy coverage.
3. Inspect policy event schema.
4. Deep-grade five random cases.
5. Check report/backlog.
6. Apply source-boundary score last.
