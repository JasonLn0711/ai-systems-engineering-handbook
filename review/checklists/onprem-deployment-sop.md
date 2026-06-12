---
id: sop.onprem-deployment
status: draft
owner: TBD
last_updated: 2026-06-12
type: sop
domain: infrastructure
confidentiality: internal
---

# SOP — On-Prem AI Service Deployment

## Purpose

建立地端 AI 服務部署的標準流程。

## Preconditions

- 已確認客戶網路限制。
- 已確認 GPU / CPU / RAM / storage。
- 已確認 OS、driver、CUDA/ROCm、Docker/K8s 版本。
- 已確認模型與資料不得外流的政策。
- 已確認 rollback plan。

## Procedure

1. Customer environment discovery。
2. Hardware inventory。
3. Network and firewall mapping。
4. OS and driver check。
5. Container image preparation。
6. Model artifact verification。
7. Secrets and environment variables setup。
8. Service deployment。
9. Health check。
10. Latency / throughput / VRAM benchmark。
11. Security check。
12. Customer acceptance test。
13. Handoff document。

## Verification

- [ ] Service reachable only from allowed network.
- [ ] No secrets printed in logs.
- [ ] Model checksum verified.
- [ ] GPU memory usage recorded.
- [ ] Error logs collected.
- [ ] Rollback tested.

## Rollback

回復前一版 container image、model artifact、config map 與 service routing。
