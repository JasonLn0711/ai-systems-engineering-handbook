# 30 天螺旋式 Enterprise Voice AI Systems Bootcamp

## 設計判斷

你的判斷是對的：7 天課程適合建立戰場地圖，28 天課程才適合把初學者帶到能實作、能解釋、能交付。30 天版本則應該在 28 天主課程後加入 mock review、portfolio、上工第一週計畫與 milestone 對齊。

這份設計採用「螺旋式展開」而不是「把原本 Day 1 擴成 4 天、Day 2 擴成 4 天」的線性展開。

原因很務實：

```text
線性展開:
  先把 Day 1 學很深 -> 再把 Day 2 學很深 -> ...
  風險是前 10 天都在局部主題裡，學生還不知道全局。

螺旋式展開:
  第 1 週先看全局
  第 2 週回到同樣主題但加深機制
  第 3 週把同樣主題做成 lab
  第 4 週整合成可交付作品
  好處是學生每週都回到系統全貌，知識不會散成一堆名詞。
```

正式建議：

```text
7 天版本 = reconnaissance / 戰場偵察
28 天版本 = bootcamp / 可交付訓練
30 天版本 = bootcamp + mock review + portfolio / 上工前封裝
```

## 學習科學與顧問式學習依據

這份課程不是百科式安排，而是顧問式快速學習加上初學者認知負荷控制。

McKinsey 的 structured problem solving 強調先定義問題、拆解問題、排序分析焦點、建立 work plan、分析與綜合建議。搬到本課程，就是先問：

```text
30 天後，初學者需要能交付什麼？
```

而不是先問：

```text
ASR、RAG、Agent、K8s、Red Teaming 每個主題能教多深？
```

National Academies 的學習研究也指出，專家知識圍繞 big ideas / major organizing principles 組織，而不是零散事實。這支持本課程先建立 `data flow / permission flow / responsibility flow / latency flow / cost flow` 這種大框架，再逐步把 ASR、RAG、agent、governance、deployment 放進框架裡。

認知負荷理論提醒我們：初學者的 working memory 有限制。若第一週就把每個主題講到最深，學生會聽到很多名詞，但無法把它們放進同一個系統。這也是為什麼本課程分成三層深度：

| Level | 用途 | 學生要能做到 |
|---|---|---|
| Level 1: 生存理解 | 第 1 週 | 知道這是什麼、在哪一層、失敗會造成什麼後果 |
| Level 2: 工程機制 | 第 2 週 | 知道輸入輸出、核心機制、評估指標、常見 failure modes |
| Level 3: 可交付能力 | 第 3–4 週 | 能做 demo、產 log、寫 README、講限制、提出下一步 |

## 7 天、28 天、30 天的換算

| 版本 | 目的 | 產出 | 適合情境 |
|---|---|---|---|
| 7 天 | 建立全局地圖 | domain map, 50 terms, issue tree, evidence checklist | 面試後快速補強、上工前偵察 |
| 28 天 | 建立可交付能力 | repo, labs, red-team package, GPU sizing, demo, memo | 初學者 bootcamp |
| 30 天 | 上工前封裝 | mock review, portfolio, first-week plan | 準備進公司、準備跟主管對齊 |

換算邏輯：

```text
原 7 天主題:
  1. domain map
  2. voice AI
  3. RAG / agent / tool / gateway
  4. PII / guardrail / red teaming
  5. Docker / K8s / GPU sizing
  6. demo / architecture memo
  7. onboarding pack

28 天螺旋:
  第 1 週: 同樣 7 題，做全局概觀
  第 2 週: 同樣 7 題，加深機制與 schema
  第 3 週: 同樣 7 題，做 lab / repo / logs
  第 4 週: 同樣 7 題，做顧問式交付包

30 天:
  Day 29: mock review
  Day 30: portfolio + first-week work plan
```

## 課程總目標

30 天後，學生要能提交一個 public-safe enterprise voice AI system portfolio：

```text
portfolio/
  01-domain-map.md
  02-50-survival-terms.md
  03-end-to-end-architecture.md
  04-voice-pipeline-report.md
  05-rag-agent-tool-gateway-memo.md
  06-pii-guardrail-redteam-package.md
  07-gpu-sizing-and-k8s-deployment.md
  08-demo-script-and-latency-report.md
  09-customer-workflow-and-acceptance.md
  10-first-30-days-at-work-plan.md
```

最終能力不是「我知道很多模型名字」，而是：

```text
我能把語音、RAG、agent、tool、governance、deployment、security、
customer workflow 串成可交付、可驗證、可維運的 enterprise AI system。
```

## 每日固定顧問式學習模板

每天都用同一個模板，避免課程變成讀書心得。

```text
1. 今天的 business problem 是什麼？
2. 這個問題在整體系統哪一層？
3. 初學者最常誤解什麼？
4. 核心概念是哪 5 個？
5. 真實世界 failure mode 是什麼？
6. 今天要讀哪 2-3 份高密度資料？
7. 今天要做哪個小 lab 或 artifact？
8. 今天要更新哪一張 issue tree？
9. 今天有哪個假設被推翻或修正？
10. 明天要交接什麼 evidence？
```

一般讀書法：

```text
今天讀 ASR。
```

顧問式學習法：

```text
今天我要回答：
企業語音 AI 系統中，ASR 錯誤如何影響後續 agent decision、
PII gate、RAG retrieval 與客戶驗收？
```

這樣學到的知識才會長在系統上。

---

# 第 1 週：建立全局地圖

第 1 週不追求精通。目標是讓初學者知道「這份工作到底在幹嘛」，並建立可以被修正的初版 mental model。

## Day 1: 角色定位與問題定義

### Business problem

學生要回答：

```text
我正在進入的領域是什麼？
Enterprise AI Coach / voice agent 跟一般 chatbot 差在哪裡？
公司真正交付的是模型、產品、流程，還是可驗收系統？
```

### 必懂概念

- Enterprise voice AI system
- AI Coach
- system boundary
- customer workflow
- acceptance criteria
- public-safe source boundary

### 初學者常見誤解

```text
誤解: AI Coach 就是會聊天的 AI。
修正: AI Coach 是訓練、評估、回饋、追蹤與企業系統整合的一組工作流。
```

### 今日 artifact

建立 `01-problem-statement.md`：

```text
Problem:
  30 天內建立 enterprise voice AI agent system 的基本交付能力。

Target capability:
  能說明 end-to-end architecture、voice pipeline、RAG/agent/tool use、
  governance/red teaming、K8s/GPU sizing、demo and acceptance evidence。

Boundary:
  只保存 public-safe learning signals，不保存私人逐字稿、客戶秘密、
  薪資條件、私人聯絡方式或可識別個資。
```

### 今日完成標準

- 能用 3 分鐘說明本課程不是模型課，而是 AI systems engineering bootcamp。
- 能畫出粗略總流程：

```text
audio -> ASR -> PII gate -> RAG -> agent -> tool -> output -> audit -> deployment
```

## Day 2: Voice AI pipeline 概觀

### Business problem

企業要把真實語音變成可分析、可評分、可追溯的資料。

### 必懂概念

- ASR
- VAD
- diarization
- overlap speech
- hotwords / contextual biasing
- TTS latency

### 初學者常見誤解

```text
誤解: ASR 準就代表 voice AI 系統準。
修正: Enterprise voice AI 還需要 speaker attribution、hotword accuracy、
latency、audio condition、TTS quality、logs 和 failure analysis。
```

### 今日 artifact

建立 `02-audio-module-inventory-v0.md`：

| Module | 解決問題 | Input | Output | Failure if missing |
|---|---|---|---|---|
| VAD | 判斷何時有人說話 | audio stream | speech segments | 切掉句首句尾或等待太久 |
| ASR | 語音轉文字 | speech segment | transcript | 下游 RAG/agent 吃錯資料 |
| Diarization | 誰在何時說話 | audio | speaker turns | AI Coach 評分對象錯 |
| Hotword correction | 修專有名詞 | transcript + lexicon | corrected transcript | 公司名/產品名/金額錯 |
| TTS | 回覆成語音 | text | audio | 對話體驗延遲或口音不符 |

## Day 3: RAG / Agent / Tool Use 概觀

### Business problem

企業 AI 必須能查公司知識、使用工具、產生可追溯輸出，而不是只靠模型記憶。

### 必懂概念

- RAG
- metadata
- reranker
- citation
- agent
- tool registry
- schema validation
- audit log

### 初學者常見誤解

```text
誤解: RAG 就是 vector DB。
修正: Enterprise RAG 是 parsing、chunking、metadata、ACL、retrieval、
reranking、citation、abstain、evaluation 的完整 pipeline。
```

```text
誤解: Tool use 最大問題是格式錯。
修正: Tool use 的核心風險是權限、副作用、idempotency、prompt injection、
PII、audit 和 human approval。
```

### 今日 artifact

建立：

```text
03-rag-pipeline-v0.md
03-tool-registry-v0.yaml
```

## Day 4: Governance / PII / Guardrail / Red Teaming 概觀

### Business problem

企業不只問 AI 好不好用，還會問：

```text
會不會洩漏資料？
會不會越權？
出錯能不能追？
高風險行為誰核准？
攻擊測過沒有？
```

### 必懂概念

- AI Gateway
- PII
- DLP
- guardrail
- prompt injection
- red teaming
- NIST AI RMF
- OWASP LLM Top 10

### 初學者常見誤解

```text
誤解: 在 system prompt 寫「不要洩漏資料」就夠。
修正: 企業系統需要 input gate、retrieval gate、tool gate、memory gate、
output gate、human review route 和 audit log。
```

### 今日 artifact

建立：

```text
04-risk-map-v0.md
04-owasp-nist-glossary-v0.md
```

## Day 5: Docker / K8s / GPU / vLLM 概觀

### Business problem

模型 demo 要變成企業服務，必須能部署、監控、估算資源、處理故障。

### 必懂概念

- Docker
- Docker Compose
- Kubernetes
- Deployment / Service / Ingress
- GPU device plugin
- vLLM / SGLang / Ollama
- KV cache
- p50 / p95 latency

### 初學者常見誤解

```text
誤解: 模型能在本機跑，就可以交付。
修正: 交付需要 service boundary、health check、logs、resource limits、
rollback、capacity estimate、customer data boundary。
```

### 今日 artifact

建立：

```text
05-deployment-map-v0.md
05-vram-formula-card-v0.md
```

## Day 6: Demo / Memo / Repo 概觀

### Business problem

能跑一次的 demo 不等於可信。可信 demo 必須可重現、可量測、可說明限制。

### 必懂概念

- demo script
- architecture memo
- README
- model inventory
- latency overlay
- known limitations
- acceptance criteria

### 今日 artifact

建立：

```text
06-demo-script-v0.md
06-architecture-memo-outline.md
```

## Day 7: 第一輪綜合

### Business problem

把前 6 天整理成 domain onboarding pack v0。

### 今日 artifact

```text
07-domain-onboarding-pack-v0/
  one-page-domain-map.md
  50-survival-terms.md
  end-to-end-workflow.md
  capability-gap-map.md
  top-10-open-questions.md
  week-2-learning-hypotheses.md
```

### 第 1 週完成標準

學生不是專家，但已經能說清楚：

```text
這個領域的核心不是模型，而是 enterprise voice AI system delivery。
```

---

# 第 2 週：回到同樣主題，加深工程機制

第 2 週把第 1 週的名詞變成機制、schema、metric、failure mode。

## Day 8: Interview-signal issue tree

### Business problem

從面試問題反推實際工作需求。

### 任務

把 public-safe interview signals 分成：

```text
1. voice AI
2. RAG / metadata
3. agent / tool use
4. gateway / governance
5. red teaming / PII
6. K8s / GPU deployment
7. customer onsite workflow
8. milestone / acceptance
```

### 今日 artifact

```text
08-capability-issue-tree.md
08-weakness-priority-matrix.md
```

### 完成標準

學生能回答：

```text
面試官問這題，不只是想知道我會不會名詞，而是在測哪個交付風險？
```

## Day 9: Voice AI 機制深挖

### 必懂機制

```text
VAD = voice probability + energy threshold + smoothing
ASR = acoustic representation + decoder / CTC / transducer / seq2seq
Diarization = speaker embedding + clustering + timestamp attribution
Overlap = overlap detection + source separation + multi-label attribution
TTS = text normalization + acoustic model + vocoder + prosody control
```

### 今日 artifact

```text
09-audio-model-card-template.md
09-asr-case-study-v1.md
09-latency-table-template.csv
```

### 完成標準

學生能對每個 voice module 說：

```text
input / output / model choices / metric / failure mode / log field
```

## Day 10: RAG / Metadata / Agent 機制深挖

### 必懂機制

```text
document parsing
chunking
metadata schema
embedding
hybrid search
reranking
thresholding
abstain
citation
faithfulness evaluation
```

Tool use 要能說：

```text
typed schema
permission scope
idempotency
retry
dry-run
human approval
output validation
audit log
```

### 今日 artifact

```text
10-rag-schema-v1.md
10-tool-registry-v1.yaml
10-agent-registration-template.yaml
```

## Day 11: PII / Guardrail / Red Teaming 機制深挖

### 必懂機制

```text
PII detection
redaction
DLP
prompt injection
tool injection
data exfiltration
policy engine
threat taxonomy
attack case generation
pass/fail scoring
```

### 今日 artifact

```text
11-red-teaming-architecture-v1.md
11-pii-guardrail-design-v1.md
11-policy-event-schema.yaml
```

## Day 12: GPU / K8s / vLLM 機制深挖

### 必懂機制

```text
model weights memory
quantization memory
KV cache memory
runtime overhead
concurrency
p50 / p95 latency
vLLM serving parameters
Docker Compose
K8s Deployment / Service / Ingress
GPU resource request
health check
logs
```

### 今日 artifact

```text
12-vram-spreadsheet-v1.csv
12-k8s-vocabulary-map.md
12-serving-parameter-cheatsheet.md
```

## Day 13: Architecture Memo v1

### Memo 結構

```text
Problem
Architecture
Common governance layer
Task adapter layer
Deployment layer
Risk controls
Evaluation metrics
Next validation gates
```

### 今日 artifact

```text
13-ai-gateway-governance-memo-v1.md
```

## Day 14: Expert-proxy synthesis

### Business problem

如果沒有 5-10 位專家可以訪談，就用 20 份高密度公開資料建立 expert-proxy matrix。

### 每份資料只抽 5 件事

```text
1. 它主要解決什麼問題？
2. 核心概念是什麼？
3. 它提到哪些 failure modes？
4. 它對我們的架構有什麼影響？
5. 哪些地方需要驗證？
```

### 今日 artifact

```text
14-source-claim-matrix.md
14-top-10-consensus.md
14-top-10-disagreements.md
14-top-10-unknowns.md
```

### 完成標準

學生能區分：

```text
共識
有證據的少數意見
漂亮但無例子的話術
需要下一輪驗證的假設
```

---

# 第 3 週：開始實作

第 3 週每一天都要有 repo、code、config、test、log 或 report。不再只讀。

## Day 15: Repo scaffold / Spec / Schema

### Repo skeleton

```text
enterprise-voice-agent-bootcamp/
  apps/
    gateway-api/
    audio-service/
    rag-service/
    agent-service/
  packages/
    schemas/
    policy/
    logging/
  infra/
    docker/
    k8s/
  tests/
    redteam/
    rag_eval/
    audio_eval/
  docs/
    architecture.md
    model_inventory.md
    deployment.md
```

### 今日 artifact

```text
repo skeleton
system schema v1
README v0
```

### 完成標準

學生能解釋每個資料夾負責什麼，不是亂放 code。

## Day 16: Audio mini-lab

### Pipeline

```text
input audio
-> VAD segment
-> ASR transcript
-> timestamp
-> optional diarization
-> JSON output
-> latency log
```

### 今日 artifact

```text
audio_output.json
latency_log.csv
audio_model_inventory.md
```

### 評估欄位

```text
audio length
audio condition
VAD segment time
ASR latency
diarization latency
model name
hardware
known errors
```

## Day 17: RAG / Agent / Tool mini-lab

### Pipeline

```text
query
-> retrieval top-k
-> rerank
-> agent decides
-> tool call
-> output with citation
-> audit log
```

### 今日 artifact

```text
rag_eval.csv
tool_call_log.jsonl
agent_trace.md
```

### 完成標準

學生能指出：

```text
哪個 tool 被 call？
為什麼允許？
輸入 schema 是什麼？
output 有沒有 citation？
audit log 能不能重建流程？
```

## Day 18: PII / Guardrail / Red Team mini-lab

### Pipeline

```text
input text
-> PII detection
-> redaction
-> prompt injection detection
-> policy decision
-> safe output
-> guardrail log
```

### Red-team cases

最低 30 題：

```text
10 prompt injection
10 PII exfiltration
10 tool misuse
```

### 今日 artifact

```text
redteam_cases.jsonl
redteam_report.md
guardrail_log.jsonl
```

## Day 19: Docker / K8s / VRAM mini-lab

### Minimum implementation

```text
Dockerfile
docker-compose.yml
k8s/deployment.yaml
k8s/service.yaml
k8s/ingress.yaml
vram_sizing.csv
deployment_notes.md
```

### 完成標準

即使本機沒有 GPU K8s，也要能說清楚：

```text
這個 service 怎麼被包裝？
K8s resource 是什麼？
GPU request 寫在哪裡？
health check 怎麼做？
logs 要有哪些欄位？
rollback 怎麼做？
VRAM 如何估算？
```

## Day 20: End-to-end demo v1

### Flow

```text
audio input
-> ASR
-> PII gate
-> RAG
-> agent
-> tool call
-> output
-> TTS or text response
-> audit log
```

### 今日 artifact

```text
demo_recording.mp4
demo_script.md
latency_breakdown.csv
known_limitations.md
```

## Day 21: Testing / Documentation Day

### 今天不加新功能

只做：

```text
README
architecture diagram
known limitations
run instructions
test instructions
model inventory
dependency list
```

### 今日 artifact

```text
public-facing demo repo v1
```

### 完成標準

另一個工程師照 README 能知道：

```text
這是什麼
怎麼跑
怎麼測
限制在哪
下一步要做什麼
```

---

# 第 4 週：顧問式交付與上工準備

第 4 週把學生從「做出小 demo」推到「能跟公司、主管、客戶討論」。

## Day 22: Customer workflow map

### Business problem

企業導入不是模型問題，而是工作流、責任、資料、採購、驗收問題。

### 要畫的圖

```text
stakeholder map
responsibility flow
money flow
data flow
risk flow
```

### 今日 artifact

```text
22-stakeholder-map.md
22-responsibility-flow.md
22-money-data-risk-flow.md
```

## Day 23: Audio benchmark report

### 報告欄位

```text
ASR model
VAD model
TTS model
hardware
audio length
audio condition
ASR latency
LLM first token latency
TTS first audio latency
total latency
known failure modes
next benchmark plan
```

### 今日 artifact

```text
23-audio-benchmark-report.md
```

## Day 24: AI Gateway / Governance proposal

### Proposal structure

```text
Common layer:
  identity
  policy registry
  tool permission
  memory scope
  PII gate
  audit log
  eval harness
  red-team harness

Adapter layer:
  sales coach
  fraud call analyzer
  HR coach
  medical intake support
  manufacturing audio monitoring
```

### 今日 artifact

```text
24-gateway-governance-proposal-v2.md
```

## Day 25: Security / Red Team package

### Package contents

```text
threat taxonomy
attack case library
test runner contract
pass/fail scoring
risk report
mitigation plan
regression backlog
```

### 今日 artifact

```text
25-redteam-package-v1/
```

## Day 26: Deployment / Customer sizing package

### Scenarios

```text
developer workstation
single GPU lab server
A6000-class customer box
H100/H200 enterprise server
edge or on-prem appliance
```

### 每個 scenario 要回答

```text
model size
precision
context length
concurrency
KV cache estimate
runtime overhead
safety buffer
expected p50/p95 latency
data boundary
deployment risk
```

### 今日 artifact

```text
26-customer-sizing-pack.md
26-vram-spreadsheet-v2.csv
```

## Day 27: Final demo video / README / memo

### Demo 影片必須包含

```text
input
models
hardware
pipeline
latency
logs
known limitations
next validation layer
```

### 今日 artifact

```text
27-final-demo.mp4
27-readme-final.md
27-architecture-memo-final.md
```

## Day 28: Onboarding pack / Mock review prep

### Final pack

```text
1. 30 天學習摘要
2. 系統理解一頁紙
3. 架構圖
4. demo repo
5. red-team report
6. PII / guardrail demo
7. GPU sizing spreadsheet
8. K8s deployment notes
9. first 30 days at work plan
10. 要問公司的 20 個問題
```

### 今日 artifact

```text
28-onboarding-pack/
```

---

# Day 29–30: 上工前封裝

## Day 29: Mock technical review

### 模擬問題

```text
你的 demo latency 是多少？
如果 50 個人同時用，VRAM 怎麼估？
如果客戶資料不能出內網，怎麼設計？
如果 transcript 裡有 prompt injection，怎麼擋？
如果 agent 要寫 CRM，怎麼做 approval？
如果 TTS 口音不符合需求，怎麼改善？
如果 K8s pod 掛了，怎麼追？
如果客戶問為什麼要 AI Coach，你怎麼答？
```

### 今日 artifact

```text
29-mock-review-qa.md
29-weak-answer-rewrites.md
```

### 完成標準

每個答案都要包含：

```text
architecture
metric
control
limitation
next validation
```

## Day 30: Final portfolio and first-week work plan

### 今日 artifact

```text
30-portfolio-index.md
30-first-week-work-plan.md
30-milestone-alignment-questions.md
```

### 最終定位

```text
我不是只會模型，而是能把語音、RAG、agent、governance、部署與客戶現場
整合成可交付系統的人。
```

---

# 每週產出總結

## Week 1: 地圖

```text
domain map
50 terms
workflow
issue tree
weakness map
```

## Week 2: 機制

```text
architecture memo v1
model cards
schemas
risk map
VRAM formula
source claim matrix
```

## Week 3: 實作

```text
repo skeleton
audio lab
RAG lab
tool-use lab
PII / red-team lab
Docker / K8s lab
end-to-end demo v1
```

## Week 4: 交付

```text
demo video
customer sizing pack
governance proposal
red-team report
onboarding pack
mock review prep
```

## Day 29–30: 封裝

```text
mock review Q&A
portfolio index
first-week work plan
milestone alignment questions
```

---

# 課程深度拿捏規則

## Rule 1: 先位置，後機制，最後工具

錯誤教法：

```text
今天我們從 vLLM 的所有參數開始。
```

正確教法：

```text
先知道 vLLM 在系統裡是 model-serving data plane，
再知道它管理 KV cache / batching / streaming，
最後才學 gpu_memory_utilization / max_num_seqs / max_num_batched_tokens。
```

## Rule 2: 每個深概念都要接回 failure mode

例子：

```text
KV cache 不是抽象名詞。
如果 context length 和 concurrency 增加，KV cache 會吃掉 VRAM，
造成 OOM 或 p95 latency 變差。
```

## Rule 3: 每天只允許 3–5 個核心概念

初學者一日容量有限。每一天有很多名詞沒關係，但真正要掌握的核心概念最多 5 個。

## Rule 4: 每天必須產出 artifact

沒有 artifact 的學習很難被檢查。

Artifact 可以是：

```text
diagram
schema
table
checklist
test cases
logs
README
memo
demo script
```

## Rule 5: 每週都要回到全局

每週最後一天都要回答：

```text
這週學到的東西如何改變我的 end-to-end architecture？
哪個假設被修正？
哪個風險變得更清楚？
下週的 evidence gate 是什麼？
```

---

# 28 天與 30 天的正式定案

建議採用：

```text
正式教學: 28 天
上工封裝: 2 天
總計: 30 天
```

7 天版本仍然保留，因為它適合快速建立全局。

28 天版本是正式 bootcamp。

30 天版本是職前封裝。

一句話：

```text
7 天版本讓你知道戰場在哪；
28 天版本讓你能拿武器上場；
30 天版本讓你帶著作品、架構圖、demo、試算表與上工問題清單走進公司。
```

## References

- McKinsey, How to master the seven-step problem-solving process:
  <https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-to-master-the-seven-step-problem-solving-process>
- McKinsey, Six problem-solving mindsets for very uncertain times:
  <https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/six-problem-solving-mindsets-for-very-uncertain-times>
- National Academies, How People Learn, Chapter 2: How Experts Differ from
  Novices: <https://www.nationalacademies.org/read/9853/chapter/5>
- Cognitive Load Theory, educational research, and instructional design:
  <https://link.springer.com/article/10.1007/s11251-009-9110-0>
