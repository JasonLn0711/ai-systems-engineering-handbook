# 詳細學生講義 — Day 3: Red-Team Guardrails

> 台灣繁體中文完整詳細版學生講義。Day 3 把 Day 2 的 governance assumptions
> 轉成可測試的 guardrail、PII、red-team、report 與 backlog evidence。

## 1. 第一結論

Red teaming 不是「問 AI 壞問題」。在 enterprise AI system 裡，red teaming 是一套可重複的 evidence process：

```text
governance assumption
-> target control
-> adversarial input
-> expected policy decision
-> required audit evidence
-> pass/fail rule
-> remediation backlog
```

如果一個 governance assumption 無法被測試，它還不是工程上可靠的 control。

## 2. Why This Day Exists

Day 2 產出了 agent registry、policy gate、tool/data/memory boundary、message
mediation、declassification、human review 與 audit contracts。Day 3 要測試這些
contract 是否足夠具體，能不能抓到 prompt injection、PII leakage、tool misuse、
privilege escalation、unsafe retrieval、memory leakage、audit evasion 與 human-review
bypass。

學生的交付物是 mini harness specification，不是模糊的安全心得。TA 應該能讀測試案例，就知道什麼應該 pass、fail，或進入 human review。

## 3. First-Principles Frame

```text
asset and permission map
-> threat taxonomy
-> case schema
-> expected control
-> expected safe behavior
-> audit fields
-> pass/fail report
-> remediation backlog
```

Day 3 不需要 production infrastructure。它需要精準的 inputs、expected controls、expected outputs 與 review evidence，讓後續可以建立 runnable test runner。

## 4. Core Terms

| Term | Beginner definition | Engineering meaning |
|---|---|---|
| Red-team case | 攻擊一個 expected control 的測試 | Structured adversarial input with expected decision and pass/fail rule |
| Threat category | 被測試的失敗類型 | Prompt injection, PII exfiltration, tool abuse, privilege escalation, memory poisoning, retrieval manipulation, unsafe output, audit evasion, review bypass |
| Expected control | 應該攔截或導流風險的系統機制 | Policy gate, input guardrail, retrieval gate, tool gate, memory gate, output gate, review queue, audit event |
| Policy event | 記錄偵測到什麼風險以及採取什麼 action | Structured event with trace, gate, risk type, action, reason, source refs, review owner |
| Pass/fail rule | Tester 判斷 control 是否有效的規則 | Observable condition based on output, tool state, audit fields, and review state |
| Remediation backlog | 失敗或不確定案例產生的修正工作 | Owner, severity, failing control, recommended fix, next validation |

## 5. Main Public-Safe Scenario

預設情境是 Campus IT Helpdesk Assistant。它可以回答 public VPN 與 Wi-Fi 問題、草擬 ticket、引用 public guides。它不能揭露 staff-only SOP、不能未經 review 直接提交 ticket、不能把 credential 寫入 memory、不能讀 raw privileged broker topics，也不能讓使用者文字關閉 audit logs。

學生也可以使用以下 public-safe tasks：

| Task | Safe data | High-risk boundary |
|---|---|---|
| Campus IT helpdesk | Public FAQ, VPN guide, service status | staff-only SOP, ticket submission, password reset |
| Sales coach | Synthetic training dialogue and rubric | customer PII, CRM write-back, unsupported advice |
| Manufacturing support | Synthetic machine status and SOP snippets | unsafe procedure, customer machine details, privileged logs |

## 6. Threat Taxonomy

Day 3 使用以下最低 taxonomy：

| Threat category | Target control |
|---|---|
| Prompt injection | input / retrieval / output guardrail |
| PII exfiltration | PII detector, redaction, logging minimization |
| Tool abuse | tool boundary, dry run, review, rate limit |
| Privilege escalation | identity, RBAC/ABAC, data boundary |
| Memory poisoning | memory write rule, retention, sharing policy |
| RAG source manipulation | retrieval gate, source metadata, citation check |
| Unsafe output | output guardrail, policy citation, review route |
| Audit evasion | system-enforced audit event |
| Human review bypass | review state machine |
| Confused deputy | original user identity, delegation policy, output classification |
| Broker payload leakage | topic ACL, schema, classification, declassification |
| Replay attack | expiration, nonce, idempotency, per-consume policy check |

## 7. Guardrail Scope

Guardrails 必須涵蓋完整 lifecycle：

```text
input gate
-> retrieval gate
-> tool gate
-> memory gate
-> output gate
-> human review route
-> audit log
```

只靠 prompt safety 不夠。有用的 Day 3 case 會說明哪一個 gate 應該抓到風險，以及哪一個 event 證明 gate 有作用。

## 8. PII Policy Event Schema

所有 gates 使用同一個 schema，才方便比較結果：

```yaml
event_id:
trace_id:
timestamp:
user_id:
agent_id:
gate: input | retrieval | tool | memory | output
risk_type: pii | prompt_injection | unsafe_tool | data_boundary | memory_boundary | audit_evasion | other
detected_pattern:
action: allow | redact | block | human_review
reason:
source_refs:
review_owner:
audit_evidence:
  policy_id:
  case_id:
  expected_control:
  outcome:
```

不要把 raw passwords、tokens、完整 ID 或不必要的 personal data 存進 policy event。能用 summary、hash、source ID 與 decision metadata 時，就不要保存原文。

## 9. Red-Team Test Case Schema

每一個 case 都要精準到後續可以寫成 test runner：

```yaml
case_id:
task:
threat_category:
attacker_goal:
input_payload:
retrieved_context_payload:
target_control:
expected_control:
expected_policy_decision: allow | deny | review | redact | block
expected_safe_behavior:
required_audit_fields:
  -
pass_fail_rule:
severity: low | medium | high | critical
remediation_owner:
```

## 10. 30-Case Mini Harness Spec

Day 3 harness 的最低門檻：

```text
3 public-safe tasks
10 cases per task
30 cases total
at least 9 threat categories
every case has expected control and pass/fail rule
every case names required audit fields
```

建議 task mix：

| Task | Required cases |
|---|---|
| Campus IT helpdesk | staff SOP bypass, ticket review bypass, credential memory, audit disable, stale VPN guide |
| Sales coach | customer PII leakage, CRM write-back abuse, hidden scoring request, unsupported advice, retrieved prompt injection |
| Manufacturing support | unsafe repair instruction, privileged log request, stale SOP, tool misuse, missing human review |

## 11. Pass / Fail / Review

| Result | Condition |
|---|---|
| pass | Expected control triggers, no restricted content leaks, high-risk tool does not execute, required audit fields exist |
| fail | Restricted data leaks, prompt changes role/policy, tool executes without review, audit evidence is missing |
| review | Behavior is ambiguous; human reviewer must classify and create next scorer rule |

當系統有意識地把高風險或模糊任務導入 human review，而且留下 evidence 時，review 不是 failure。

## 12. Required Student Artifacts

Submit:

1. Red-team taxonomy.
2. PII / guardrail policy event schema.
3. 30-case mini harness spec.
4. Pass/fail report template.
5. Remediation backlog.

## 13. Common Failure Patterns

| Failure | Why it fails | Control to add |
|---|---|---|
| Only asks "bad prompts" | No repeatable expected outcome | Structured case schema |
| Only checks final answer | Tool execution or audit may fail silently | Tool state and audit fields |
| PII is redacted in output but stored in logs | Output safety hides storage leakage | Logging minimization and audit schema |
| Prompt injection is tested only in user input | Retrieved content can also inject | Retrieval gate cases |
| Human review is mentioned but no state is recorded | Cannot prove action was paused | Review state and audit event |

## 14. Key Rules To Remember

```text
One case tests one primary control.
Every expected behavior needs evidence.
Audit is part of the test, not an afterthought.
PII can appear in input, retrieval, tool output, logs, trace, memory, and DLQ.
Failed cases create remediation work.
```

## 15. Source Boundary

使用 synthetic examples 與 public-safe enterprise scenarios。不要把真實 tickets、真實 customer records、credentials、private transcripts 或 identifiable personal data 貼進 harness。
