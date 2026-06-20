# RBAC vs ABAC Video Notes

```yaml
artifact_type: ai_agent_readable_video_note
agent_readable: true
accelerator: enterprise-ai-architecture-sprint
day: 1
video_title: "Role-based access control (RBAC) vs. Attribute-based access control (ABAC)"
video_url: "https://www.youtube.com/watch?v=rvZ35YW4t5k"
primary_topic: authorization models for enterprise AI gateway access control
primary_language: zh-TW
recorded_at: 2026-06-21
canonical_note_path: accelerators/enterprise-ai-architecture-sprint/day-01-ai-gateway/rbac-vs-abac-video-notes.md
source_boundary:
  - Public video note
  - Public-safe healthcare-style access-control example
  - Public-safe enterprise AI examples
  - No patient data
  - No customer secrets
  - No credentials
  - No identifiable personal data
agent_use:
  - Use this as Day 1 companion material for authorization and policy gate literacy.
  - Keep the Day 1 required artifacts unchanged.
  - Use the examples to explain identity vs authorization, RBAC, ABAC, hybrid access control, PEP, and PDP.
  - Use the enterprise AI mapping to connect access control to AI Gateway, RAG, tool use, memory, audit, and human review.
downstream_outputs:
  - policy worksheet
  - access-control field list
  - RBAC role-permission table
  - ABAC attribute-rule table
  - PEP/PDP architecture note
  - AI Gateway policy input shape
  - risk-control map for permission bypass
```

## Agent Reading Contract

```yaml
reading_contract:
  purpose: "Record RBAC vs ABAC video notes as reusable Day 1 material for authorization and AI Gateway policy literacy."
  do_not_treat_as:
    - authentication guide
    - full healthcare compliance design
    - final authorization policy
    - new Day 1 grading requirement
  use_as:
    - source for explaining authentication vs authorization
    - source for RBAC and ABAC comparison tables
    - source for PEP/PDP diagrams
    - source for AI Gateway policy-gate examples
    - source for permission-bypass risk-control mapping
  required_student_artifacts_still_owned_by_day_1:
    - AI Gateway architecture diagram
    - Component responsibility table
    - Request lifecycle
    - Risk-control map
  stable_section_ids:
    conclusion: "0"
    two_questions: "1"
    no_roles_problem: "2"
    rbac: "3"
    abac: "4"
    rbac_vs_abac: "5"
    hybrid_model: "6"
    pep_pdp_architecture: "7"
    ai_gateway_mapping: "8"
    campus_it_example: "9"
    policy_input_shape: "10"
    failure_modes: "11"
    interview_answers: "12"
    compressed_summary: "13"
```

## 0. 結論

這支影片真正要教的是 access control 裡最容易被忽略的部分：

```text
Authentication answers: who are you?
Authorization answers: what are you allowed to do?
```

企業系統裡，登入成功不代表可以做任何事。真正難的是 authorization：使用者、服務、agent、tool、資料來源、memory、輸出內容，哪些可以讀、寫、呼叫、分享、審核，必須由可執行的 policy 決定。

影片比較兩種 authorization model：

```text
RBAC = Role-Based Access Control
ABAC = Attribute-Based Access Control
```

最重要結論：

```text
RBAC 用 role 簡化權限管理。
ABAC 用 attributes 提供更細、更動態的決策。
真實企業系統常用 hybrid：RBAC 做高階分組，ABAC 做細節判斷。
PEP 負責執行 allow/deny，PDP 負責做 decision。
```

對 AI Gateway / enterprise AI 來說，這支影片直接對應 Day 1 的身份、角色、權限、policy gate，也會銜接 Day 2 的 agent governance。

## 1. Access Control 的兩個問題

影片用兩個問題開場：

```text
Who are you?
What are you allowed to do?
```

第一個問題是 authentication：

- password
- MFA
- passkey
- token
- SSO
- identity proof

第二個問題是 authorization：

- 可以讀哪份資料？
- 可以寫哪個系統？
- 可以呼叫哪個 tool？
- 可以看哪種 sensitivity level？
- 可以代表誰做事？
- 是否需要 approval？

Day 1 AI Gateway 要讓學生分清楚：

```text
Authenticated does not mean authorized.
```

登入成功的 student 仍然不能讀 staff-only SOP；登入成功的 AI agent 仍然不能任意呼叫 write tool。

## 2. 沒有 Role 時的問題

影片用 hospital example 說明，如果不用 role，而是直接把每個 user 接到每個 capability，權限圖會快速變成 spaghetti。

簡化例子：

```text
Doctor:
- write orders
- read orders
- read lab reports
- cannot write lab reports

Nurse:
- read orders
- read lab reports
- cannot write orders
- cannot write lab reports

Lab technician:
- write lab reports
- read lab reports
- probably does not need order-writing permissions
```

如果只有幾個 user 和幾個 capability，還能手動管理。當組織擴大到 thousands / tens of thousands / hundreds of thousands users，直接 user-to-permission mapping 會很難維護。

問題：

- 權限設定重複。
- 新增 capability 要改很多 user。
- 新增 employee 要手動補很多 permission。
- 離職或轉職容易留下過期權限。
- audit 很難回答「這類人為什麼有這些權限」。

## 3. RBAC: Role-Based Access Control

RBAC 的方法：

```text
把 permission 掛在 role 上。
再把 user 掛到 role。
```

影片中的 hospital RBAC 範例：

```text
Doctor role:
- write orders
- read orders
- read labs

Nurse role:
- read orders
- read labs

Lab technician role:
- write labs
- read labs
```

然後個別 user 只需要被分配到 role：

```text
Alice -> Doctor
Bob -> Nurse
Carol -> Nurse
Dave -> Lab technician
```

RBAC 的價值：

- 權限更乾淨。
- 新 employee 只要 map 到 role。
- 新 capability 可以加到 role，不用逐一修改 user。
- 容易對組織階層建模。
- 容易向管理者和 auditor 解釋。

RBAC 的缺點：

- role explosion：角色越切越細，最後變得難管理。
- 動態條件不容易表達，例如地區、時間、資料 sensitivity、employment status。
- 無法單靠 role 表達「finance manager 且 clearance high 才能看特定 report」。
- 跨部門、矩陣式、臨時任務、multi-tenant 系統會更複雜。

工程判斷：

```text
RBAC 適合組織階層清楚、權限分組穩定的系統。
```

## 4. ABAC: Attribute-Based Access Control

ABAC 使用 attributes 做 authorization decision。

影片列出的 attribute 類型：

- geography：US、Europe、Latin America。
- position：組織中的職位。
- department：部門。
- employment status：full-time、contractor、part-time。
- manager status：是否 manager。
- clearance level：high、medium、low、secret、top secret。

ABAC rule 範例：

```text
Allow access to sensitive financial report if:
- clearance = high
- manager = true
- department = finance
```

ABAC 的價值：

- 比 RBAC 更細。
- 可表達動態條件。
- 適合跨地區、跨部門、矩陣式組織。
- 適合資料 sensitivity、環境條件、resource metadata。
- 適合 AI Gateway 的 structured policy input。

ABAC 的挑戰：

- attribute quality 很重要。
- attribute 來源要可信。
- policy 可能變複雜。
- debug authorization decision 需要好的 audit reason。
- 如果 attribute 名稱與語意不一致，會造成 policy drift。

工程判斷：

```text
ABAC 適合需要彈性、動態、多條件 authorization 的系統。
```

## 5. RBAC vs ABAC

| Dimension | RBAC | ABAC |
|---|---|---|
| Decision basis | user role | subject/resource/action/environment attributes |
| Simple mental model | 高 | 中 |
| Dynamic conditions | 弱 | 強 |
| Good for hierarchy | 強 | 可支援但較抽象 |
| Good for fine-grained policies | 中 | 強 |
| Risk | role explosion | policy/attribute complexity |
| Example | doctor can write orders | finance manager with high clearance can view sensitive report |
| AI Gateway fit | coarse role gating | fine-grained policy gate |

影片結論不是誰比較好，而是：

```text
It depends.
```

如果組織階層清楚，RBAC 很自然。如果組織需要更動態、更多條件，ABAC 可能更合適。兩者都可能被過度設計，也都可以設計得很清楚。

## 6. Hybrid Model: Both / And

影片強調不必二選一。真實系統常用 hybrid：

```text
Role gives the high-level permission bundle.
Attributes refine the actual decision.
```

例子：

```text
Role:
finance_manager

Attributes:
department=finance
clearance=high
region=US
employment_status=full_time
resource.sensitivity=high
environment.network=corp_vpn
```

Hybrid policy：

```text
Allow if:
- role includes finance_manager
- department = finance
- clearance >= high
- resource.type = financial_report
- resource.region = user.region
- request comes from trusted device/network
```

Enterprise AI 通常需要 hybrid：

```text
RBAC:
student, staff, it_reviewer, admin, service_account

ABAC:
tenant_id, department, data_access_level, tool_risk, action_type, request_channel, risk_score, output_classification, review_state
```

## 7. PEP / PDP Architecture

影片最後用架構圖解釋真實世界怎麼實作 authorization。

```text
User
-> Policy Enforcement Point (PEP)
-> Policy Decision Point (PDP)
-> allow / deny
-> Resource
```

### 7.1 Policy Enforcement Point (PEP)

PEP 是 enforcement component。它站在 user 和 resource 中間，負責執行 decision。

PEP 問 PDP：

```text
Should I grant access to this user for this resource?
```

PEP 的工作要簡單：

```text
If allow -> let request pass.
If deny -> block request.
If review_required -> route to review workflow.
```

### 7.2 Policy Decision Point (PDP)

PDP 是 decision component。它負責評估 policy。

PDP 可以使用：

- RBAC
- ABAC
- hybrid RBAC + ABAC
- policy-as-code
- custom policy table

PDP 的工作比較難：

- 收集 trusted identity。
- 讀取 role / attributes。
- 讀取 resource attributes。
- 檢查 action。
- 檢查 environment。
- 回傳 decision 與 reason。

設計原則：

```text
Decision separate from enforcement.
```

這對 AI Gateway 很重要，因為 gateway 可以是 PEP，而 policy service / OPA / Cedar / custom PDP 可以做 decision。

## 8. AI Gateway 對應

AI Gateway 的 access-control 不是只問使用者能否登入，而是問：

```text
這個 subject 能不能對這個 object 做這個 operation，在目前 environment 下？
```

對應：

| Access-control term | AI Gateway example |
|---|---|
| Subject | user、service account、agent identity、tool caller |
| Role | student、staff、it_reviewer、admin、support_agent |
| Attributes | tenant、department、region、clearance、employment status、risk tier |
| Object / Resource | document、tool、model、memory namespace、conversation、ticket |
| Operation / Action | retrieve、summarize、write_memory、call_tool、submit_ticket、reset_password |
| Environment | channel、network、device trust、time、request risk、data residency |
| PEP | API Gateway、AI Gateway、Tool Broker、RAG Connector |
| PDP | Policy Engine、OPA、Cedar、Casbin、custom policy service |
| Decision | allow、deny、review_required |
| Evidence | policy decision log、audit event、trace_id |

Day 1 AI Gateway example：

```text
student asks campus_it_helpdesk_agent for VPN setup
-> subject.role = student
-> resource = vpn_setup_guide
-> action = retrieve
-> resource.access_level = public
-> decision = allow
```

Restricted example：

```text
student asks for staff_account_lock_sop
-> subject.role = student
-> resource.access_level = staff_only
-> action = retrieve
-> decision = deny
```

Review example:

```text
student asks agent to submit ticket
-> action = submit_ticket
-> tool.risk = side_effect
-> subject.role = student
-> decision = review_required
```

## 9. Campus IT Helpdesk Example

RBAC table:

| Role | Allowed actions |
|---|---|
| student | read public FAQ, read VPN guide, check service status, draft ticket |
| staff | read public docs, read staff helpdesk docs, draft ticket |
| it_reviewer | approve ticket submission, review high-risk actions |
| admin | manage policy, manage registry, review audit |

ABAC attributes:

| Attribute | Example |
|---|---|
| `tenant_id` | `campus_demo` |
| `department` | `it`, `student_affairs` |
| `resource.access_level` | `public`, `staff_only`, `restricted` |
| `tool.type` | `read_only`, `side_effect`, `high_risk_side_effect` |
| `channel` | `student_portal`, `admin_console`, `api` |
| `risk_score` | `low`, `medium`, `high` |
| `output_classification` | `student_support_safe`, `staff_only` |
| `review_state` | `none`, `pending`, `approved`, `rejected` |

Hybrid rule examples:

```yaml
rules:
  - id: allow_public_vpn_guide
    if:
      role: student
      action: retrieve
      resource.access_level: public
      resource.topic: vpn
    decision: allow

  - id: deny_staff_sop_to_student
    if:
      role: student
      action: retrieve
      resource.access_level: staff_only
    decision: deny

  - id: review_student_submit_ticket
    if:
      role: student
      action: submit_ticket
      tool.type: side_effect
    decision: review_required
```

## 10. AI Gateway Policy Input Shape

```json
{
  "subject": {
    "user_id": "student_001",
    "role": "student",
    "tenant_id": "campus_demo",
    "department": "computer_science",
    "employment_status": "student",
    "clearance": "low"
  },
  "agent": {
    "agent_id": "campus_it_helpdesk_agent",
    "risk_class": "medium"
  },
  "resource": {
    "type": "document",
    "source_id": "staff_account_lock_sop",
    "access_level": "staff_only",
    "department": "it"
  },
  "action": {
    "name": "retrieve",
    "type": "read"
  },
  "environment": {
    "channel": "student_portal",
    "network": "campus_network",
    "request_risk": "medium",
    "time": "2026-06-21T10:00:00+08:00"
  }
}
```

Expected policy output:

```json
{
  "decision": "deny",
  "reason": "student role cannot retrieve staff_only resource",
  "safe_user_message": "這份資料僅限授權 IT staff 使用。",
  "audit_fields": [
    "subject.user_id",
    "subject.role",
    "resource.source_id",
    "resource.access_level",
    "action.name",
    "decision",
    "reason"
  ]
}
```

## 11. Failure Modes

| Failure | Symptom | Control |
|---|---|---|
| Authentication confused with authorization | Logged-in user gets broad access | Separate identity verification from policy decision |
| User-to-permission spaghetti | Permissions hard to audit | Use RBAC role-permission groups |
| Role explosion | Too many tiny roles | Add ABAC attributes for dynamic conditions |
| Untrusted attributes | User self-claims department/clearance | Resolve attributes server-side |
| Missing resource attributes | Policy cannot classify data | Add metadata: access_level, owner, tenant, sensitivity |
| PEP bypass | Service calls resource directly | Force access through gateway/tool broker/RAG connector |
| PDP no audit reason | Denials hard to debug | Return decision reason and audit fields |
| Prompt-based authorization | Model decides permissions | Use system-enforced PEP/PDP policy gate |
| Tool over-permission | Agent can call write tools freely | Tool allowlist, side-effect classification, review gate |
| Memory leakage | Agent reads/writes wrong namespace | Memory scope attributes and tenant/user policy |

## 12. 面試回答模板

### 12.1 Authentication vs Authorization

```text
Authentication answers who the user or service is. Authorization answers what that identity is allowed to do. In an enterprise AI Gateway, a user can be successfully authenticated and still be denied access to a document, model, memory namespace, or tool because the policy decision depends on role, resource sensitivity, action type, tenant, and risk context.
```

### 12.2 RBAC vs ABAC

```text
RBAC assigns permissions through roles, so it is simple and easy to manage in hierarchical organizations. ABAC makes decisions from attributes such as department, geography, clearance, resource sensitivity, action type, and environment, so it supports more dynamic and fine-grained control. In real systems I would often use both: RBAC for coarse role groups and ABAC for fine-grained policy decisions.
```

### 12.3 PEP vs PDP

```text
The Policy Enforcement Point sits in the request path and enforces the decision. The Policy Decision Point evaluates the policy and returns allow, deny, or review_required. For an AI Gateway, the gateway, tool broker, or RAG connector can act as PEP, while OPA, Cedar, Casbin, or a custom policy service can act as PDP.
```

### 12.4 AI Agent Authorization

```text
I would not let the model decide authorization. The model can propose an action, but the gateway must check a structured policy input: subject, role, agent, resource, action, tool risk, memory scope, tenant, and environment. The policy service returns allow, deny, or review_required, and the audit log records the decision and reason.
```

## 13. 最終濃縮版

```text
Authentication: who are you?
Authorization: what are you allowed to do?

RBAC:
role -> permissions
simple, explainable, good for stable organizational roles

ABAC:
attributes -> policy decision
fine-grained, dynamic, good for context-sensitive access

Hybrid:
roles give broad access groups
attributes refine exact decisions

PEP:
enforces the decision

PDP:
makes the decision

AI Gateway:
must use system-enforced authorization for models, tools, data, memory, output, and review.
Prompt is not an authorization boundary.
```

## References

- Day 1 YouTube learning map: `accelerators/enterprise-ai-architecture-sprint/day-01-ai-gateway/youtube-learning-map.md`
- Video: <https://www.youtube.com/watch?v=rvZ35YW4t5k>
