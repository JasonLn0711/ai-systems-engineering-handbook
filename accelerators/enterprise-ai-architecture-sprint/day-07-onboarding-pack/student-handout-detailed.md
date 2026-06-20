# Detailed Student Handout — Day 7: Onboarding Pack

## 1. 第一結論

Day 7 的任務是把 7 天產出整理成可上工、可展示、可討論的 onboarding pack。7 天版本是 primary deliverable；30 天版本是後續 spiral bootcamp，不是今天要補完的全部深度。

## 2. Onboarding Pack File Map

| File | 用途 |
|---|---|
| `one-page-domain-brief.md` | 10 分鐘講清楚領域與系統邊界 |
| `50-survival-terms.md` | 讓學生不再像外行 |
| `end-to-end-workflow.md` | 從 audio 到 audit |
| `gateway-governance-memo.md` | 架構與治理主張 |
| `rag-tool-gateway.md` | RAG schema、tool registry、gateway integration |
| `red-team-cases.jsonl` | 可測試安全風險 |
| `pii-guardrail-demo.md` | PII / guardrail 控制 |
| `gpu-sizing.csv` | 算力估算 |
| `k8s-checklist.md` | 部署可行性 |
| `demo-script.md` | 可展示流程 |
| `architecture-memo.md` | 2-page architecture memo |
| `first-30-days-plan.md` | 上工節奏 |

## 3. Evidence Index

Evidence index 把 Day 1-6 連成一個故事：

| Sprint day | Evidence | What it proves |
|---|---|---|
| Day 1 | AI Gateway architecture | Request lifecycle and control-plane thinking |
| Day 2 | Agent governance | Registry, policy, memory, review, audit contracts |
| Day 3 | Red-team guardrails | Testable security and PII controls |
| Day 4 | RAG/tool gateway | Data/tool access governed by schema and policy |
| Day 5 | K8s/GPU serving | Deployability and capacity evidence |
| Day 6 | Demo/memo | Integrated, measurable, scoped demonstration |

## 4. First-Week Fact-Finding Questions

```text
目前 production stack 是 Python、Node.js、Go、Rust，還是混合？
模型服務用 vLLM、SGLang、Ollama、Triton、TGI、hosted API，還是自架？
客戶部署是 cloud、on-prem、edge、hybrid，比例如何？
資料是否可以離開客戶環境？
目前有沒有 AI Gateway 或統一 model router？
有沒有統一 audit log schema？
RAG 用哪個 vector DB？metadata schema 是什麼？
有沒有 retrieval eval set？
ASR/TTS 用哪些模型？授權條件與限制？
客戶最常抱怨的是 latency、準確率、資料安全、整合速度還是驗收不清？
milestone 驗收標準是功能、準確率、latency、安全、部署、文件還是客戶 demo？
```

## 5. First 30 Days Plan

### Week 1: 盤點，不急著重寫

```text
repo structure
deployment method
model inventory
customer workflows
current logs
current eval method
security / PII policy
demo script
milestone and acceptance criteria
```

### Week 2: 補最小治理層

```text
request_id
audit log schema
PII gate
tool registry
latency measurement
model inventory
```

### Week 3: 補 evaluation / red-team harness

```text
RAG eval set
ASR eval set
prompt injection tests
PII leakage tests
tool misuse tests
```

### Week 4: 補部署與客戶交付文件

```text
Docker / K8s notes
GPU sizing spreadsheet
customer architecture diagram
known limitations
acceptance criteria
```

## 6. Mock Review Checklist

每個 mock answer 都要包含：

```text
architecture
metric
control
limitation
next validation
```

Example questions:

```text
你的 demo latency 是多少？
如果 50 個人同時用，VRAM 怎麼估？
如果客戶資料不能出內網，怎麼設計？
如果 transcript 裡有 prompt injection，怎麼擋？
如果 agent 要寫 CRM，怎麼做 approval？
如果 TTS 口音不符合需求，怎麼改善？
如果 K8s pod 掛了，怎麼追？
```

## 7. Weakness-To-Evidence Map

| Weakness | One-week evidence | Next validation |
|---|---|---|
| AI red teaming new | 30-case mini harness | runnable test runner |
| PII / guardrail weak | policy event schema | command-line demo |
| K8s weak | mock inference checklist | local or lab deployment |
| GPU sizing experience-based | weights + KV cache table | observed VRAM and p95 |
| Tool use thin | typed tool registry | policy-driven tool call |
| RAG metrics incomplete | hit@k / MRR / citation / abstain plan | eval set |

## 8. Next Validation Path

The 7-day sprint is complete when the learner can explain and submit the evidence
packet. The next validation path can be:

1. Runnable mock Gateway.
2. Runnable PII / guardrail CLI.
3. YAML/JSONL red-team runner.
4. Local K8s mock inference endpoint.
5. Recorded ASR -> agent -> TTS demo.

## 9. Source Boundary

Keep the onboarding pack public-safe. Do not include private interview text,
customer secrets, credentials, identifiable personal data, salary/offer details,
or unpublished company claims.
