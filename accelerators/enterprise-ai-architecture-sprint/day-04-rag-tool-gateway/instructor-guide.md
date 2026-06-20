# Instructor Guide — Day 4: RAG Tool Gateway

## 1. Teaching Goal

Students learn that RAG and tool calls are enterprise contracts controlled by
Gateway policy, not model conveniences.

## 2. Pre-Class Diagnostic

1. What is the difference between retrieval top-k and generation top-p?
2. Which metadata field controls document access?
3. Why does a write tool need idempotency?
4. What audit fields prove a tool call was allowed?
5. Where should memory scope be enforced?

## 3. 150-Minute Flow

| Time | Activity | Output |
|---:|---|---|
| 0-10 | Diagnostic | Misconception list |
| 10-35 | RAG metadata and ACL | RAG schema draft |
| 35-60 | Tool registry | Two tool records |
| 60-85 | Agent-tool lifecycle | Lifecycle table |
| 85-110 | Connector map | Connector boundaries |
| 110-135 | Gateway integration note | Route/policy/audit note |
| 135-150 | Peer review | Fix list |

## 4. Failure Gallery

### Failure 1: Vector DB as magic

Metadata exists but policy never reads it. Require metadata in policy input.

### Failure 2: Tool schema without permission

Input schema validates shape but not caller authority. Add allowed roles,
allowed agents, side effect, and approval.

### Failure 3: Write retry duplicates action

Retry has no idempotency key. Require stable idempotency for side-effect tools.

### Failure 4: Citation leaks restricted source

Answer cites a source the user cannot access. Filter before retrieval and audit
source IDs.

## 5. TA Workflow

1. Check RAG metadata fields.
2. Check two tool records.
3. Inspect lifecycle for policy and audit.
4. Verify adapter map has policy and evaluator.
5. Apply source-boundary penalty if needed.
