# Day 4 RAG / Tool Gateway Handoff

Day 3 produces red-team and guardrail evidence. Day 4 uses that evidence to
design RAG metadata, tool registry, connector boundaries, and Gateway
integration rules that are testable.

## Inputs From Day 3

- Red-team taxonomy.
- PII / guardrail policy event schema.
- 30-case mini harness spec.
- Pass/fail report template.
- Remediation backlog.

## Day 4 Design Questions

Use the failed or high-risk Day 3 cases to ask:

1. Which RAG metadata fields must exist to enforce ACL, freshness, and citation?
2. Which tool registry fields prevent unauthorized side effects?
3. Which connector boundaries prevent KB, SQL, file, workflow, or memory leaks?
4. Which Gateway policy decisions should return allow, deny, review, redact, or
   block?
5. Which audit fields prove that data and tool access stayed inside boundary?

## Acceptance Criteria

- RAG schema includes ACL, source version, owner, approved_by, citation, rerank,
  and abstain fields.
- Tool registry includes side_effect, approval, idempotency, allowed roles,
  allowed agents, timeout, retry, and audit fields.
- Gateway integration note maps Day 3 threat categories to Day 4 controls.
- Adapter/evaluation map names at least three public-safe tasks.
- No real private data enters examples or fixtures.

## Source Boundary

Use synthetic records only. Do not turn real tickets, transcripts, credentials,
or identifiable personal data into fixtures.
