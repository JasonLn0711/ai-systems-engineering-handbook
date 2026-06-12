# Cross-Module Dependency Map

```text
00 foundations
├── 01 linux-os-networking
├── 02 cloud-onprem-private-cloud
├── 05 llm-application-architecture
└── 11 spec-sdd-ai-coding-workflow

01 linux-os-networking
└── 03 container-k8s-devops
    └── 04 gpu-inference-infrastructure

05 llm-application-architecture
├── 06 rag-data-pipeline
├── 07 ai-gateway-agent-governance
└── 08 voice-ai-systems

06 rag-data-pipeline
└── 07 ai-gateway-agent-governance

09 security-red-teaming
├── 06 rag-data-pipeline
├── 07 ai-gateway-agent-governance
├── 08 voice-ai-systems
└── 10 enterprise-delivery-fae

10 enterprise-delivery-fae
└── all deployment and governance modules
```

When adding a chapter, identify its upstream prerequisites and downstream system impact.
