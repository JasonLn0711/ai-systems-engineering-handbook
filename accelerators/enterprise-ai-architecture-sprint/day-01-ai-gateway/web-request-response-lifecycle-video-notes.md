# Web Request-Response Lifecycle Video Notes

```yaml
artifact_type: ai_agent_readable_video_note
agent_readable: true
accelerator: enterprise-ai-architecture-sprint
day: 1
video_title: "Web Application Architecture: Full Request-Response Lifecycle"
video_url: "https://www.youtube.com/watch?v=xv0Be4QfkH0"
primary_topic: full web request-response lifecycle for enterprise AI systems
primary_language: zh-TW
recorded_at: 2026-06-21
canonical_note_path: accelerators/enterprise-ai-architecture-sprint/day-01-ai-gateway/web-request-response-lifecycle-video-notes.md
source_boundary:
  - Public video note
  - Public technical documentation
  - Public-safe enterprise AI examples
  - Synthetic system scenarios
  - No customer secrets
  - No credentials
  - No identifiable personal data
agent_use:
  - Use this as Day 1 companion material for request lifecycle literacy.
  - Keep the Day 1 required artifacts unchanged.
  - Use the method to explain HTTP/API Gateway/backend/cache/database/queue/observability paths.
  - Use the enterprise AI mapping to connect web request lifecycles to AI Gateway, voice AI, and agent governance.
downstream_outputs:
  - request lifecycle baseline
  - web architecture responsibility table
  - production debugging cheat sheet
  - AI Gateway lifecycle mapping
  - Docker Compose request lifecycle lab
  - observability checklist
  - Kubernetes deployment mental model
```

## Agent Reading Contract

```yaml
reading_contract:
  purpose: "Record the full web request-response lifecycle video as reusable Day 1 material for architecture and production debugging literacy."
  do_not_treat_as:
    - AWS certification guide
    - mandatory cloud architecture
    - final AI Gateway implementation
    - new Day 1 grading requirement
  use_as:
    - source for request lifecycle explanations
    - source for web/cloud responsibility tables
    - source for debugging status codes and layer symptoms
    - source for AI Gateway request-path analogies
    - source for one-week request lifecycle lab design
  required_student_artifacts_still_owned_by_day_1:
    - AI Gateway architecture diagram
    - Component responsibility table
    - Request lifecycle
    - Risk-control map
  stable_section_ids:
    conclusion: "0"
    transcript_corrections: "1"
    canonical_path: "2"
    browser_request: "3"
    dns: "4"
    cdn: "5"
    waf: "6"
    load_balancer: "7"
    reverse_proxy_nginx: "8"
    kubernetes_mapping: "9"
    api_gateway: "10"
    backend_services: "11"
    databases: "12"
    cache: "13"
    queue_stream: "14"
    auth: "15"
    observability: "16"
    response_path: "17"
    corrections_to_video_simplifications: "18"
    ecommerce_example: "19"
    ai_gateway_mapping: "20"
    one_week_lab: "21"
    debugging_cheat_sheet: "22"
    interview_answer: "23"
    tools: "24"
    learning_strategy: "25"
```

## 0. 結論

這支影片的核心不是 AWS 名詞介紹，而是現代 web / cloud system 的完整 request lifecycle。

一週內要上手 enterprise AI / voice AI / agent gateway 工作，重點不是背 Route 53、CloudFront、WAF、ALB、Nginx、API Gateway、PostgreSQL、DynamoDB、Kafka 這些名詞，而是能回答三件事：

```text
1. 使用者點按鈕後，一個 request 經過哪些層。
2. 每一層負責什麼、不負責什麼、壞掉時會出現什麼症狀。
3. 在 enterprise AI / voice AI / agent gateway 場景中，怎麼把同一套概念用在 API Gateway、agent governance、tool registry、memory、PII、guardrail、logging、approval flow、K8s deployment 上。
```

最重要的工程判斷：

```text
每一層都要有清楚責任。
每一層都可能產生不同錯誤症狀。
每一層都需要可觀測證據。
AI workload 也是 production request lifecycle，不是單純 model call。
```

## 1. 逐字稿 ASR 錯字校正

| 逐字稿錯字 | 正確詞 | 中文意思 |
|---|---|---|
| `vaav` / `VAV` | `WAF` | Web Application Firewall，網頁應用程式防火牆 |
| `cross-siiz scripting` | Cross-site scripting, `XSS` | 跨站腳本攻擊 |
| `enginex` | Nginx | reverse proxy / web server / load balancer |
| `cash static assets` | cache static assets | 快取靜態資源 |
| `easy to instance` | EC2 instance | AWS 虛擬機器 |
| `Dynamo TV` / `Dynamo DV` | DynamoDB | AWS serverless NoSQL database |
| `HQ` | queue | 佇列，例如 SQS、Kafka、RabbitMQ |
| `STS` | tasks | 背景任務 |
| `mcast` | Memcached | 記憶體快取系統 |
| `promas` | Prometheus | metrics monitoring system |

## 2. 典型 Request Path

一個典型 request 的路徑可簡化成：

```text
User Browser / Mobile App
        |
        v
DNS: Route 53 / Cloudflare DNS
        |
        v
CDN / Edge: CloudFront / Cloudflare CDN
        |
        v
WAF / DDoS Protection
        |
        v
Load Balancer: ALB / NLB
        |
        v
Reverse Proxy / Ingress: Nginx / Kubernetes Ingress / Gateway API
        |
        v
API Gateway
        |
        v
Backend Services: FastAPI / Node.js / Go / Java / Lambda / K8s Pods
        |
        +--> Cache: Redis / Memcached
        |
        +--> Database: PostgreSQL / MySQL / DynamoDB
        |
        +--> Queue / Event Stream: SQS / Kafka / RabbitMQ
        |
        +--> Worker Services / Background Jobs
        |
        v
Observability: Logs + Metrics + Traces
        |
        v
Response back to user
```

這不是死板固定路徑。真實系統會刪減、合併或替換某些層。

範例：

```text
Small SaaS:
Cloudflare -> Vercel -> Postgres

Enterprise on-prem:
DNS -> F5 / Nginx -> Keycloak -> K8s Ingress -> microservices

AI gateway:
Nginx / ALB -> gateway -> model router -> policy engine -> LLM provider / self-hosted GPU inference
```

## 3. Browser Request: 從使用者按下按鈕開始

假設使用者輸入：

```text
https://example.com/api/products?id=123
```

瀏覽器不是直接找到網站。它通常經過：

1. DNS 解析 `example.com` 到可連線 endpoint。
2. 建立 TCP connection。
3. HTTPS 場景進行 TLS handshake。
4. 送出 HTTP request。

範例 HTTP request：

```http
GET /api/products?id=123 HTTP/1.1
Host: example.com
Authorization: Bearer <access_token>
Cookie: session_id=...
User-Agent: Chrome/...
Accept: application/json
```

工程師看 request 時，不能只看 URL。要看：

- method
- path
- query string
- headers
- cookies
- body
- client IP
- user agent
- trace ID / request ID
- authorization token

很多 production bug 都藏在 header、cookie、proxy forwarding、CORS、timeout、body size limit 裡。

## 4. DNS: 名字解析層

DNS 的責任：

```text
把 domain name 轉成可連線 endpoint。
```

DNS 也牽涉 availability、routing、failover、TTL。

常見 DNS record：

| Record | 用途 |
|---|---|
| A | domain -> IPv4 |
| AAAA | domain -> IPv6 |
| CNAME | domain -> another domain |
| TXT | 驗證、SPF、DKIM、其他 metadata |
| MX | email server |
| Alias / ANAME | root domain 指向 cloud resource |

工程重點：

1. TTL 會影響切換速度。TTL 太長，使用者可能一直連舊 IP；TTL 太短，DNS 查詢成本與負載上升。
2. DNS 不是 request-level load balancing。Client 可能快取 DNS 結果，不是每個 HTTP request 都重新決定。
3. DNS 壞掉時，CDN、WAF、backend 都還沒機會工作。

常見錯誤：

- `NXDOMAIN`
- `SERVFAIL`
- 解析到錯誤 IP
- split-horizon DNS 設定錯誤
- 內外網 DNS 不一致

面試回答：

```text
DNS 是 request lifecycle 的入口。它不處理 HTTP 內容，只負責把 domain name 解析到可連線 endpoint，並可透過 health check、latency routing 或 weighted routing 支援 failover 與流量切分。
```

## 5. CDN: 把內容推到離使用者更近的地方

CDN 目的：

- 降低 latency。
- 減少 origin server 負載。
- 提高全球使用者存取速度。

常被 CDN 快取：

```text
/static/app.js
/static/style.css
/images/logo.png
/videos/intro.mp4
```

也可快取 API response，但要小心 user-specific data。不能把 A 使用者的個資 response 快取後給 B 使用者。

關鍵概念：

| 概念 | 說明 |
|---|---|
| Edge location | 靠近使用者的節點 |
| Origin | 真正來源伺服器，例如 S3、ALB、Nginx、API server |
| Cache hit | Edge 已有內容，直接回應 |
| Cache miss | Edge 沒有內容，回 origin 抓 |
| TTL | 快取多久 |
| Cache key | 用 path、query、header、cookie 等判斷同一份內容 |
| Invalidation | 主動清除 CDN cache |

工程陷阱：

```text
Backend 修好了，使用者仍看到舊內容。
```

常見原因是 CDN cache 沒清或 cache key 設錯。

前端資源通常用 hash filename：

```text
app.91f3a7.js
style.aa12bb.css
```

新版檔名不同，CDN 不會誤用舊 cache。

## 6. WAF: 第一層應用層防線

WAF 是 Web Application Firewall，處理 application-layer 惡意 HTTP request。

WAF 可擋：

```text
/api/users?id=1 OR 1=1
/search?q=<script>alert(1)</script>
/login with suspicious bot traffic
大量異常 request 觸發 rate-based rule
```

但 WAF 不是萬能盾牌。正確安全是多層防禦：

```text
WAF
+ input validation
+ parameterized SQL
+ output encoding
+ CSRF protection
+ secure cookies
+ auth / authorization
+ rate limiting
+ logging / alerting
```

WAF 常見問題：

| 問題 | 現象 |
|---|---|
| false positive | 正常使用者被擋，HTTP `403` |
| false negative | 攻擊繞過 WAF |
| rule 太寬 | 攻擊仍進 backend |
| rule 太嚴 | API 被大量誤擋 |
| 只擋外部 | 內部 lateral movement 沒防住 |

對 enterprise AI：

```text
WAF 只能擋 HTTP 層攻擊。
擋不了 prompt injection、tool misuse、PII leakage、agent 越權執行。
AI Gateway 仍需要 policy engine、tool allowlist、approval gate、audit log、output guardrail。
```

## 7. Load Balancer: 把流量分配到健康服務

Load balancer 核心責任：

```text
把 incoming traffic 分配到多個 backend targets。
透過 health check 避免把流量送到壞掉的 instance / container。
```

### 7.1 ALB: Application Load Balancer, Layer 7

ALB 工作在 OSI Layer 7，看得懂 HTTP / HTTPS request，可依 host、path、header、method、query string routing。

例子：

```text
api.example.com/users    -> user-service
api.example.com/payments -> payment-service
static.example.com       -> static-service
```

ALB 適合：

- REST API
- Web app
- Microservices
- Path-based routing
- Host-based routing
- HTTP/HTTPS traffic

### 7.2 NLB: Network Load Balancer, Layer 4

NLB 工作在 OSI Layer 4，不理解 HTTP path/header，主要看 IP、port、protocol。

NLB 適合：

- 極低延遲需求
- TCP / UDP service
- WebSocket / streaming / gaming / financial trading
- static IP
- 非 HTTP service

比較：

| 項目 | ALB | NLB |
|---|---|---|
| OSI layer | L7 | L4 |
| 看 HTTP path/header | 看 | 不看 |
| 適合 | Web API、microservices | TCP/UDP、高吞吐、低延遲 |
| routing 能力 | 強 | 較低階 |
| static IP | 通常不是重點 | 常見需求 |
| 例子 | `/api/users` -> user service | TCP 443 -> backend pool |

不要說「NLB 比 ALB 高級」或「ALB 比 NLB 高級」。它們是不同層級、不同用途。

## 8. Nginx: Reverse Proxy

Nginx 可做：

- HTTP web server
- reverse proxy
- content cache
- load balancer
- TCP/UDP proxy server

Reverse proxy：

```text
Client -> Nginx -> FastAPI / Node.js / Go service
```

Nginx 常做：

```text
SSL/TLS termination
path-based routing
host-based routing
gzip / brotli compression
static file serving
reverse proxy
request body size limit
timeout control
rate limiting
access log
upstream load balancing
```

範例設定概念：

```nginx
server {
    listen 80;
    server_name example.com;

    location /api/ {
        proxy_pass http://backend:8000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Request-ID $request_id;
    }

    location /static/ {
        root /var/www/app;
        expires 1h;
    }
}
```

重要 headers：

- `X-Forwarded-For`
- `X-Real-IP`
- `X-Request-ID`

如果 backend 只看到 Nginx IP，看不到真正 client IP，通常是 proxy header 沒處理好。這會影響資安、rate limiting、audit log。

## 9. Kubernetes 對應概念

如果公司用 Kubernetes，要把影片架構翻譯成 K8s 語言。

| Cloud / Web 名詞 | Kubernetes 對應 |
|---|---|
| backend server | Pod |
| backend pool | Deployment / ReplicaSet |
| service discovery | Service |
| reverse proxy | Ingress Controller / Gateway |
| load balancer | Service type LoadBalancer / cloud LB |
| health check | readinessProbe / livenessProbe |
| scaling | HPA / replicas |
| config | ConfigMap |
| secret | Secret |
| logs | `kubectl logs` / centralized logging |
| metrics | Prometheus / metrics-server |

先會看：

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl describe pod <pod>
kubectl logs <pod> -f
kubectl port-forward svc/api 8000:80
```

## 10. API Gateway: 流量入口、權限、限流、版本管理

API Gateway 是 backend API 前門。

常做：

```text
request validation
authentication
authorization
rate limiting
quota
API key management
routing
request / response transformation
CORS
versioning
canary release
logging
```

要分清楚：

| Concept | Meaning |
|---|---|
| Authentication | 你是誰？ |
| Authorization | 你可以做什麼？ |
| Rate limit | 多久可以做幾次？ |
| Quota | 這個月最多用多少？ |
| Validation | request 格式正不正確？ |

AI Gateway 對應：

```text
Authentication: 使用者 / tenant / service account 是誰？
Authorization: 能不能呼叫某個 model / tool / memory？
Rate limit: 每分鐘 token / request / cost 限制
Quota: 每月模型預算
Validation: prompt / tool call / JSON schema 是否合格
Policy: 是否含 PII、是否越權、是否需要人工 approval
Audit: 每次模型呼叫、工具呼叫、輸出結果是否可追溯
```

這是 AI Gateway、Agent Governance、Registry、Memory、PII、Guardrail 的底層系統設計核心。

## 11. Backend Services: 執行商業邏輯

一般 web backend：

```text
user-service: 註冊、登入、權限
product-service: 商品查詢
payment-service: 付款
notification-service: 通知
order-service: 訂單
```

AI voice / enterprise AI backend：

```text
audio-ingest-service: 接收音訊
vad-service: voice activity detection
asr-service: speech-to-text
orchestrator-service: agent workflow
model-router-service: 選模型
policy-service: guardrail / PII / approval
memory-service: conversation memory / vector retrieval
tts-service: text-to-speech
audit-service: trace / log / evidence packet
```

Backend 執行環境判準：

| 選項 | 適合 |
|---|---|
| EC2 / VM | 完整控制 OS / GPU / driver / network |
| Lambda / serverless | 短任務、事件觸發、無狀態 |
| Kubernetes | containerized microservices、on-prem、hybrid cloud、GPU inference、企業環境 |
| ECS/Fargate | AWS container service，操作比 K8s 簡化 |
| Bare metal / on-prem GPU | 資料不能出企業內網、需本地 GPU inference |

基本判準：

```text
需要完整控制 OS / GPU / driver / network -> EC2 / bare metal / K8s
短任務、事件觸發、無狀態 -> Lambda
多服務、可移植、企業 on-prem -> Kubernetes
快速 SaaS web app -> managed platform / container service
```

## 12. Database: PostgreSQL vs DynamoDB

不要簡化成「structured 用 PostgreSQL，unstructured 用 DynamoDB」。真正選 database 要看 access pattern、consistency、transaction、query flexibility、scale、operational burden。

PostgreSQL 適合：

```text
資料關聯清楚
需要 JOIN
需要複雜查詢
需要 transaction
需要 schema constraint
需要報表分析
```

範例：

```sql
SELECT u.email, o.total_amount
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE o.created_at >= now() - interval '7 days';
```

DynamoDB 適合：

```text
key-value lookup
高流量低延遲
access pattern 明確
不需要複雜 JOIN
serverless / global scale
```

範例：

```text
PK = USER#123
SK = SESSION#2026-06-21T10:00:00
```

最重要的一句：

```text
PostgreSQL 是先設計關係與一致性，再查詢。
DynamoDB 是先知道查詢模式，再設計 key。
NoSQL 一樣要設計，只是設計重點不同。
```

## 13. Cache: Redis / Memcached

Cache 目的：

```text
把常被讀取、計算成本高、可以短時間容忍舊資料的結果放在快取層。
```

常見使用：

```text
user profile
product detail
session
rate limit counter
JWT blacklist
feature flags
LLM response cache
embedding retrieval cache
temporary job status
```

典型流程：

```text
1. backend 收到 GET /products/123
2. 先查 Redis: product:123
3. cache hit -> 直接回傳
4. cache miss -> 查 PostgreSQL
5. 把結果寫入 Redis，TTL 60 秒
6. 回傳使用者
```

Python pseudo-code：

```python
cache_key = "product:123"

cached = redis.get(cache_key)
if cached:
    return json.loads(cached)

product = db.query(Product).filter(Product.id == 123).first()
redis.setex(cache_key, 60, json.dumps(product.to_dict()))

return product
```

Cache 陷阱：

| 問題 | 說明 |
|---|---|
| stale cache | DB 更新了，但 cache 還是舊資料 |
| cache stampede | cache 同時失效，大量 request 同時打 DB |
| cache penetration | 查不存在資料，每次都打 DB |
| cache avalanche | 大量 key 同時過期 |
| inconsistent data | 多層 cache 導致資料版本混亂 |
| sensitive data leakage | cache key 設計錯，把 A 使用者資料給 B |

AI 系統也常用 Redis 做：

```text
conversation state
short-term memory
rate limit
distributed lock
job queue
streaming buffer
tool execution state
```

但長期記憶、audit log、法規稽核資料，不應只放 Redis。

## 14. Queue / Kafka / SQS

不是所有事情都要在使用者等待時完成。適合 queue：

```text
寄 email
產生報表
轉檔
跑模型評估
寫 audit pipeline
更新 search index
ASR / TTS / embedding / reranking / eval / PII scan
```

SQS vs Kafka：

| 項目 | SQS | Kafka |
|---|---|---|
| 模型 | Queue | Distributed event log / stream |
| 使用方式 | producer -> queue -> consumer | producer -> topic -> consumers |
| 適合 | 背景任務、解耦服務 | event streaming、log pipeline、多 consumer replay |
| 操作複雜度 | 較低 | 較高 |
| 是否保留事件歷史 | 有限制 | 核心特色之一 |
| 常見場景 | email、job、async API | clickstream、交易流、audit event、ML feature pipeline |

Async API pattern：

```text
POST /reports
-> API Gateway 驗證
-> backend 建立 job_id
-> message 放入 queue
-> 回傳 202 Accepted + job_id
-> worker 背景處理
-> client 用 GET /reports/{job_id} 查狀態
```

關鍵工程概念：

```text
idempotency key
retry policy
dead-letter queue
visibility timeout
backoff
poison message
at-least-once delivery
duplicate processing
job status table
```

Voice AI / agent 系統尤其需要 async：ASR、LLM、TTS、embedding、reranking、eval、PII scan 都可能很慢，不應全部卡在 synchronous HTTP request 裡。

## 15. Authentication: OAuth 2.0、OIDC、JWT

不要混在一起：

| Term | Meaning |
|---|---|
| OAuth 2.0 | 授權框架，重點是 access delegation |
| OpenID Connect | OAuth 2.0 上的 identity layer，重點是登入與身分 |
| JWT | token format，裡面放 claims |
| Access Token | 用來呼叫 API |
| ID Token | 用來表示使用者身分 |
| Refresh Token | 用來換新的 access token |

JWT 範例：

```json
{
  "iss": "https://auth.example.com",
  "sub": "user_123",
  "aud": "api.example.com",
  "exp": 1780000000,
  "iat": 1779990000,
  "scope": "read:products write:orders",
  "tenant_id": "tenant_a"
}
```

後端驗證 JWT 不是只 decode，要檢查：

```text
signature 是否有效
iss 是否正確
aud 是否正確
exp 是否過期
nbf / iat 是否合理
scope / role / permission 是否足夠
token 是否被撤銷
演算法是否符合允許清單
```

Enterprise 常見：

- Keycloak
- Auth0
- Okta
- Cognito
- OIDC
- SAML
- service account
- realm / client / role

## 16. Observability: Logs + Metrics + Traces

不是有 log 就叫可觀測。

三個核心信號：

| Signal | 問題 |
|---|---|
| Logs | 發生了什麼事件？ |
| Metrics | 系統整體狀態如何？ |
| Traces | 一個 request 經過哪些服務、每段花多久？ |

Production request 應有 correlation ID：

```text
x-request-id: 9f2a4a9e-...
```

每層都帶著它：

```text
CloudFront log
WAF log
ALB access log
Nginx access log
API Gateway log
Backend app log
DB query log
Queue message metadata
Worker log
Trace span
```

這樣才能回答：

```text
這個 request 是誰發的？
走到哪一層失敗？
花最多時間的是哪一段？
是 WAF 擋掉、Gateway 429、ALB 502、backend 500、DB timeout，還是 queue backlog？
```

進公司後很有價值的能力：

```text
不是只會寫 API，而是會追 request。
```

## 17. Response Path

HTTP response 通常沿著原本 connection / proxy chain 回去：

```text
Backend
-> API Gateway / Nginx / ALB
-> CDN / Edge
-> Browser
```

Response 範例：

```http
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: max-age=60
Set-Cookie: session_id=...
X-Request-ID: 9f2a4a9e-...

{
  "id": 123,
  "name": "Keyboard"
}
```

注意：

- 不要 cache private user data。
- 要設定正確 `Cache-Control`。
- 錯誤 response 不一定該 cache。
- `Set-Cookie` 與 CDN cache 要小心。
- CORS header 要正確。
- 壓縮與 streaming response 會影響 latency。

## 18. 影片簡化說法的修正

1. Nginx 不一定在 WAF 後、Load Balancer 前。真實架構可能是：

```text
CloudFront -> WAF -> ALB -> ECS/K8s
Cloudflare -> Nginx -> App
F5 -> Nginx Ingress -> K8s Services
ALB -> Nginx Ingress -> Pods
```

2. API Gateway 與 ALB 有重疊。不是每個系統都需要 CDN、WAF、Nginx、ALB、API Gateway 全部上。每多一層就多 latency、成本、設定錯誤、debug 難度。

3. WAF 擋不住所有攻擊。SQL injection 要靠 parameterized query；XSS 要靠 output encoding、CSP、input handling；auth bug 要靠正確 authorization model。

4. DynamoDB 不是 unstructured data database。更精確地說，它是 NoSQL key-value / document database。選它通常是為了明確 access pattern、低延遲、高 scale、低維運。

5. Load balancer 通常不是平衡 outgoing traffic。它主要處理 incoming connection / request routing；response 多半沿著既有連線與 proxy chain 回去。

6. Queue 代表 eventual processing，不代表立刻完成。使用者通常收到 `202 Accepted + job_id`，之後查 job status 或用 WebSocket / webhook 通知。

## 19. 電商下單例子

使用者按「結帳」：

```http
POST /api/orders
Authorization: Bearer <token>
Idempotency-Key: 6f3d...
```

流程：

```text
1. DNS 解析 shop.example.com
2. CDN 提供前端 JS/CSS/image
3. WAF 檢查 request 是否像攻擊
4. ALB 根據 /api/orders route 到 order-service
5. API Gateway 驗證 token、rate limit、schema
6. order-service 檢查庫存
7. payment-service 建立付款
8. PostgreSQL 寫入 order / payment transaction
9. Redis 更新短期 order status cache
10. SQS 放入 send_email_job
11. worker 寄確認信
12. Prometheus / CloudWatch 收 metrics
13. OpenTelemetry trace 記錄整條路徑
14. response 回傳 order_id
```

每層壞掉的症狀：

| Layer | Symptom |
|---|---|
| DNS | 使用者根本連不到 |
| CDN | 靜態資源載入慢或舊 |
| WAF | 誤擋，`403` |
| ALB | target unhealthy，`503` |
| Nginx | upstream timeout，`504` |
| API Gateway | 限流，`429` |
| Auth | token 過期，`401` |
| Authorization | 權限不足，`403` |
| Backend | bug，`500` |
| DB | connection pool 滿，`500` / timeout |
| Queue | 訂單成功但通知延遲 |
| Cache | 使用者看到舊狀態 |
| Observability | 查不到 root cause |

## 20. 對 Enterprise AI Gateway 的翻譯

AI voice agent request path：

```text
Client / Browser / Mobile / Call Center
        |
        v
DNS / Private DNS
        |
        v
WAF / Reverse Proxy / ALB / Nginx
        |
        v
API Gateway / Auth / Tenant Routing
        |
        v
Audio Ingest Service
        |
        v
VAD -> ASR -> Diarization
        |
        v
Agent Orchestrator
        |
        +--> Tool Registry
        +--> Memory / Vector DB
        +--> Policy Engine / Guardrail
        +--> PII Redaction
        +--> Approval Gate
        +--> Model Router
        |
        v
LLM / Self-hosted GPU Model / External Provider
        |
        v
TTS / Response Formatter
        |
        v
Audit Log / Trace / Evaluation
        |
        v
User / Operator / Enterprise System
```

對應：

| 影片概念 | AI Gateway 對應 |
|---|---|
| API Gateway | AI Gateway / model gateway |
| WAF | prompt injection filter / policy engine / PII scanner |
| Load Balancer | model routing / GPU inference load balancing |
| Nginx / Ingress | on-prem reverse proxy / K8s ingress |
| Cache | prompt cache / retrieval cache / session state |
| Database | audit log / user state / tenant config / policy config |
| Queue | async ASR、TTS、eval、report generation |
| Monitoring | token usage、latency、model error、tool failure、PII incidents |
| Auth | tenant identity、RBAC、ABAC、service account |
| Rate limit | per-user、per-tenant、per-model、per-tool、per-cost limit |

可直接使用的工作句：

```text
我會把 AI agent request 當成 production web request 來治理。外層處理 identity、rate limit、schema validation、policy；中層做 orchestration、tool permission、memory access；內層才是 model inference。所有步驟都要有 trace、audit log、error handling、timeout、retry、approval boundary。
```

## 21. 一週上手訓練計畫

目標不是七天變 AWS expert，而是七天後能：

```text
畫出完整 request lifecycle
解釋每層責任
用 Docker Compose 跑出 mini production architecture
用 Nginx 反向代理兩個 backend
用 Redis 做 cache / rate limit
用 PostgreSQL 存資料
用 queue 處理背景任務
用 Prometheus / logs / trace 觀察 request
回答 ALB vs NLB、WAF vs app security、API Gateway vs reverse proxy
把這套架構套到 AI Gateway / voice AI / K8s deployment
```

### 21.1 Day 1: HTTP、DNS、request 基礎

必學：

```text
HTTP method: GET, POST, PUT, PATCH, DELETE
status code: 200, 201, 202, 301, 302, 400, 401, 403, 404, 409, 429, 500, 502, 503, 504
headers
cookies
JWT bearer token
DNS A/CNAME/TXT
TLS / HTTPS
```

實作：

```bash
dig example.com
curl -v https://example.com
curl -I https://example.com
```

FastAPI app：

```python
from fastapi import FastAPI, Request
import time
import uuid

app = FastAPI()

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
    start = time.time()
    response = await call_next(request)
    duration_ms = round((time.time() - start) * 1000, 2)
    response.headers["x-request-id"] = request_id
    print({
        "request_id": request_id,
        "method": request.method,
        "path": request.url.path,
        "duration_ms": duration_ms,
        "status_code": response.status_code,
    })
    return response

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/api/products/{product_id}")
def get_product(product_id: int):
    return {"id": product_id, "name": "demo product"}
```

成果：看懂 request 如何進 backend、如何產生 log、如何帶 request ID。

### 21.2 Day 2: Nginx reverse proxy 與 load balancing

目標：

```text
Client -> Nginx -> backend-1 / backend-2
```

`docker-compose.yml` 概念：

```yaml
services:
  api1:
    build: .
    environment:
      INSTANCE_NAME: api1
    ports:
      - "8001:8000"

  api2:
    build: .
    environment:
      INSTANCE_NAME: api2
    ports:
      - "8002:8000"

  nginx:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - api1
      - api2
```

`nginx.conf`：

```nginx
events {}

http {
    upstream backend_pool {
        server api1:8000;
        server api2:8000;
    }

    server {
        listen 80;

        location / {
            proxy_pass http://backend_pool;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Request-ID $request_id;
        }
    }
}
```

觀察：

```bash
curl -v http://localhost:8080/health
docker compose logs -f nginx
docker compose logs -f api1
docker compose logs -f api2
```

成果：理解 reverse proxy、upstream、proxy headers、load balancing、`502` / `504` 來源。

### 21.3 Day 3: API Gateway 思維

新增功能：

```text
JWT 驗證
API key
Redis rate limit
request schema validation
correlation ID
```

Rate limit pseudo-code：

```python
def check_rate_limit(user_id: str, limit: int = 60):
    key = f"rate:{user_id}"
    current = redis.incr(key)

    if current == 1:
        redis.expire(key, 60)

    if current > limit:
        raise HTTPException(status_code=429, detail="Too Many Requests")
```

理解：

```text
401 = 沒登入或 token 無效
403 = 有登入但權限不足
429 = 超過流量限制
400 = request 格式錯
409 = idempotency / conflict 問題
```

成果：能解釋 API Gateway 和 Nginx 差異。Nginx 偏 proxy/routing/connection；API Gateway 偏 API lifecycle、auth、quota、validation、developer-facing API management。

### 21.4 Day 4: PostgreSQL + Redis cache

資料表：

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    updated_at TIMESTAMP DEFAULT now()
);
```

流程：

```text
GET /api/products/123
-> check Redis product:123
-> miss 時查 PostgreSQL
-> 寫入 Redis TTL 60 秒
-> 回傳 response
```

刻意製造 cache bug：

```text
1. 查 product，cache 起來。
2. 改 DB 裡的 product name。
3. 再查 API。
4. 觀察為什麼還是舊資料。
```

成果：知道 cache invalidation 為什麼難，以及什麼資料不該亂 cache。

### 21.5 Day 5: Queue 與 background worker

Async API：

```text
POST /api/reports
-> 建立 job
-> 丟 queue
-> 回傳 job_id
```

Worker：

```text
worker 從 queue 拿 job
-> 模擬產生報表
-> 寫入 job status table
```

理解：

```text
synchronous request: 使用者等結果
asynchronous request: 使用者拿 job_id，稍後查結果
```

AI 場景：

```text
長音訊 ASR
長文件 embedding
LLM batch evaluation
TTS 合成
PII scan
報表產生
audit log enrichment
```

成果：會講 `202 Accepted + job_id`，並知道 retry、dead-letter queue、idempotency。

### 21.6 Day 6: Observability

要加：

```text
structured logs
request_id
Prometheus metrics
OpenTelemetry tracing
basic dashboard
```

最少 metrics：

```text
http_requests_total
http_request_duration_seconds
http_errors_total
db_query_duration_seconds
cache_hit_total
cache_miss_total
queue_jobs_pending
worker_jobs_failed_total
```

要能回答：

```text
P50 latency 是多少？
P95 latency 是多少？
error rate 是多少？
哪個 endpoint 最慢？
cache hit rate 是多少？
queue backlog 有沒有增加？
```

成果：用 metrics + logs + traces 定位問題。

### 21.7 Day 7: Kubernetes / deployment mental model

至少會看：

```text
Deployment
Service
Ingress
ConfigMap
Secret
HorizontalPodAutoscaler
```

知道：

```text
readinessProbe: 服務是否準備好接流量
livenessProbe: 服務是否活著，需不需要重啟
resources.requests: 預留資源
resources.limits: 最大資源
replicas: 幾個副本
image tag: 部署哪個版本
```

最終 architecture memo：

```text
1. Request path
2. Components
3. Auth model
4. Data stores
5. Async jobs
6. Observability
7. Failure modes
8. Security boundaries
9. Scaling plan
10. Open questions
```

成果：10 分鐘向工程主管講清楚系統如何部署、擴展、debug、保護資料。

## 22. Production Debugging Cheat Sheet

| 狀態碼 / 現象 | 常見位置 | 可能原因 |
|---|---|---|
| DNS `NXDOMAIN` | DNS | domain 沒設定、打錯、zone 錯 |
| `403` | WAF / API Gateway / App | WAF 擋、權限不足、CORS、IP deny |
| `401` | API Gateway / App | token 過期、signature 錯、issuer/audience 錯 |
| `404` | CDN / ALB / Nginx / App | path route 錯、service 沒掛 |
| `409` | App / DB | idempotency conflict、版本衝突 |
| `413` | Nginx / Gateway | request body 太大 |
| `429` | WAF / API Gateway / App | rate limit |
| `500` | App | 程式 bug、未處理 exception |
| `502` | ALB / Nginx | upstream 掛掉、protocol 錯 |
| `503` | LB / App | target unhealthy、服務不可用 |
| `504` | Nginx / Gateway / LB | upstream timeout |
| latency 高 | 任一層 | DB 慢、cache miss、queue backlog、model inference 慢 |
| 資料舊 | CDN / Redis | cache stale |
| 無法追問題 | Observability | 沒有 request ID、trace、structured log |

習慣：

```text
先問：request 到哪一層？
再問：哪一層產生這個 status code？
再問：有沒有 request_id / trace_id？
再問：是 routing、auth、rate limit、backend、DB、cache、queue、model inference 哪一類？
```

## 23. 面試回答模板

問題：

```text
使用者點按鈕後發生什麼事？
```

回答：

```text
使用者點按鈕後，瀏覽器會先透過 DNS 把 domain 解析到目標 endpoint，接著建立 TCP/TLS 連線並送出 HTTP request。request 可能先經過 CDN，如果是可快取的 static asset，edge location 可以直接回應；如果是 API request，就會往 origin 走。進 origin 前通常會經過 WAF，過濾 SQL injection、XSS、bot 或異常流量。之後進入 load balancer，例如 ALB 可以根據 host/path/header 做 L7 routing，NLB 則是在 L4 做 TCP/UDP 層級轉發。接著可能經過 Nginx 或 Kubernetes Ingress，再進 API Gateway。API Gateway 負責 authentication、authorization、rate limit、quota、request validation、logging。最後 request 進 backend service，service 會查 Redis cache、PostgreSQL 或 DynamoDB，必要時把慢任務丟到 queue，例如 SQS 或 Kafka，再由 worker 背景處理。整條路徑應該要有 logs、metrics、traces 與 request ID，這樣 production 出問題時才能定位是 DNS、CDN、WAF、gateway、backend、DB、cache、queue 還是下游服務造成的。
```

進階補句：

```text
我不會在每個系統都硬塞 CDN、WAF、ALB、Nginx、API Gateway。架構要根據 threat model、latency、traffic pattern、deployment environment、team operation capacity 取捨。每加一層都要有明確責任，否則只是增加 debug 難度。
```

## 24. 優先掌握工具與套件

Python / AI backend：

```text
FastAPI
Uvicorn
Pydantic
SQLAlchemy
Alembic
psycopg
redis-py
RQ / Celery
PyJWT / python-jose
OpenTelemetry SDK
prometheus-client
pytest
httpx
```

Node.js / web backend：

```text
Express / NestJS
Prisma
Zod
jsonwebtoken
ioredis
BullMQ
pino
OpenTelemetry JS
Jest
```

Infrastructure：

```text
Docker
Docker Compose
Nginx
PostgreSQL
Redis
Prometheus
Grafana
Kubernetes
kind / k3d / minikube
kubectl
Helm
```

Cloud / AWS：

```text
Route 53
CloudFront
AWS WAF
ALB
NLB
API Gateway
EC2
Lambda
RDS PostgreSQL
DynamoDB
SQS
CloudWatch
EKS
```

Security / identity：

```text
OAuth 2.0
OpenID Connect
JWT
Keycloak
RBAC
ABAC
OPA / policy engine
PII redaction
audit logging
```

Load testing / debugging：

```text
curl
httpie
dig
nslookup
tcpdump
k6
wrk
hey
jq
stern
kubectl logs
kubectl describe
```

## 25. 學習策略

不要只看影片。用一個小型實作打通：

```text
Browser/curl
-> Nginx
-> FastAPI gateway
-> backend service
-> Redis
-> PostgreSQL
-> queue worker
-> Prometheus metrics
-> structured logs with request_id
```

每天回答同一組問題：

```text
這個 request 現在在哪一層？
如果這層壞掉，使用者會看到什麼？
我要去哪裡看 log / metric / trace？
我怎麼證明不是其他層的問題？
```

最終理解：

```text
模型、ASR、TTS、agent 都只是 workload。
能讓 workload 安全、可觀測、可部署、可治理地跑起來，才是系統工程。
```

## References

- Route 53: <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html>
- Route 53 alias to CloudFront: <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html>
- CloudFront: <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html>
- AWS WAF / Shield: <https://docs.aws.amazon.com/decision-guides/latest/waf-or-shield/waf-or-shield.html>
- Application Load Balancer: <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html>
- Network Load Balancer: <https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html>
- Nginx: <https://nginx.org/>
- Kubernetes Service: <https://kubernetes.io/docs/concepts/services-networking/service/>
- Kubernetes Ingress: <https://kubernetes.io/docs/concepts/services-networking/ingress/>
- Amazon API Gateway: <https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html>
- API Gateway throttling: <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html>
- Amazon EC2: <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html>
- AWS Lambda: <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>
- PostgreSQL concepts: <https://www.postgresql.org/docs/current/tutorial-concepts.html>
- DynamoDB: <https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html>
- Redis caching: <https://redis.io/solutions/caching/>
- Amazon SQS: <https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/sqs.html>
- Apache Kafka quickstart: <https://kafka.apache.org/quickstart/>
- OpenID Connect: <https://openid.net/developers/how-connect-works/>
- JWT RFC 7519: <https://datatracker.ietf.org/doc/html/rfc7519>
- OpenTelemetry: <https://opentelemetry.io/docs/what-is-opentelemetry/>
- OpenTelemetry observability primer: <https://opentelemetry.io/docs/concepts/observability-primer/>
- Prometheus: <https://prometheus.io/>
- CloudWatch: <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html>
- Docker Compose: <https://docs.docker.com/compose/>
