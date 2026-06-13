# Instructor Guide: Agent Governance Framework

## Teaching Goal

Students should leave Day 2 able to turn one enterprise agent into a governed
contract: registry entry, policy gate, tool and memory boundaries, audit event,
and red-team seeds.

## Pre-Class Diagnostic

Use these questions before lecture:

1. In Day 1, where did the Gateway decide whether a request was allowed?
2. What is the difference between a read-only tool and a side-effect tool?
3. What fields would identify an agent in an audit event?
4. Why might memory shared across agents create a security risk?
5. What does `allow | deny | review` mean in a policy decision?

If students struggle with 1-2, review Day 1 architecture. If students struggle
with 3-5, slow down during agent registration and audit sections.

## 180-Minute Flow

| Time | Activity | Goal | Instructor emphasis |
|---:|---|---|---|
| 0-15 min | Diagnostic and Day 1 recap | Reconnect Gateway to governance | Gateway needs contracts, not guesses |
| 15-35 min | Governance layers | Introduce identity, registry, tool, data, memory, policy, audit | Agent safety is system design |
| 35-60 min | Common vs adapter | Separate reusable controls from scenario behavior | Avoid rebuilding governance per customer |
| 60-85 min | Agent registration | Fill registry fields | Blank fields become unenforced boundaries |
| 85-110 min | Policy gate and audit | allow/deny/review plus evidence | Policy decisions must be logged |
| 110-145 min | Workshop | Students fill all Day 2 artifacts | Push for concrete fields |
| 145-170 min | Peer review | Find missing tool/memory/audit controls | Convert gaps into red-team seeds |
| 170-180 min | Handoff | Day 3 red-team tests | Governance assumptions become attack cases |

## 150-Minute Flow

| Time | Activity | Goal |
|---:|---|---|
| 0-10 min | Diagnostic | Confirm Day 1 concepts |
| 10-30 min | Governance layers | Map the agent control surface |
| 30-55 min | Registration and common-vs-adapter | Create reusable governance structure |
| 55-75 min | Policy and audit | Turn rules into decisions and evidence |
| 75-115 min | Workshop | Complete artifacts |
| 115-140 min | Peer review | Identify failure modes |
| 140-150 min | Handoff | Write red-team seeds |

## Common Failure Gallery

### Failure 1: Agent Without Owner Or Scope

```text
agent_id: helpdesk_agent
allowed_tools: all
allowed_data_sources: all
```

Missing controls:

- no owner
- no task scope
- no risk class
- no data boundary
- no tool boundary

Student critique prompt: "Who is responsible when this agent misuses a tool?"

### Failure 2: Tool Approval Only In Prompt

```text
system prompt: Ask a human before submitting a ticket.
tool: submit_ticket
```

Missing controls:

- no policy gate
- no tool broker decision
- no review state
- no audit field proving approval

Student critique prompt: "What prevents the tool call from executing anyway?"

### Failure 3: Shared Memory Without Scope

```text
memory: shared_agent_notes
retention: forever
sharing: all_agents
```

Missing controls:

- no retention limit
- no deletion rule
- no PII handling
- no role boundary
- no cross-agent leakage test

Student critique prompt: "Could another agent read student-private context?"

## Instructor Questions

1. Which fields must be in the agent registry before the Gateway can route to it?
2. Which governance controls are common across agents?
3. Which behavior belongs in the campus IT adapter?
4. What makes a tool side-effecting?
5. Which memory fields are sensitive?
6. What should audit record beyond final text?
7. Which policy assumptions should become Day 3 red-team cases?

## Teaching Notes

- When students say "allowed tools: all," ask for the minimum necessary tool set.
- When students create a policy but no audit event, ask how a TA can verify it.
- When students write "human approval" in prose, ask for the review state field.
- When students ignore memory, ask whether the agent can retain or share PII.
- Treat weak governance fields as Day 3 red-team seeds.
