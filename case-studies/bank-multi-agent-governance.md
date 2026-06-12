# Case Study — Bank Multi-Agent Governance

## Scenario

大型銀行同時導入多個 AI agent：內部知識查詢、銷售支援、報告撰寫、第三方 agent。公司需提供 AI Gateway 與 governance layer，統一管理資料、工具、權限、audit log、approval gate 與 red-team eval。

## Key Questions

1. 所有 agent 是否共用 KB / SQL / MCP server？
2. 不同任務如何透過 skill / adapter 特化？
3. 如何避免低權限 agent 間接取得高權限資料？
4. 如何保留完整決策紀錄供稽核？
5. 如何降低新增第 N 個 agent 的 governance 成本？

## Related Modules

- `modules/07-ai-gateway-agent-governance/`
- `modules/06-rag-data-pipeline/`
- `modules/09-security-red-teaming/`
- `modules/04-gpu-inference-infrastructure/`
