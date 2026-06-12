# Module 04: GPU And AI Inference Infrastructure

## Purpose

Teach AI compute planning for local and enterprise inference.

## Core Questions

- How do model weights, quantization, KV cache, batch size, context length, and concurrency affect VRAM?
- When should teams use vLLM, Ollama, cloud APIs, hosted compute, or local GPUs?
- How do you plan capacity for multiple models and multiple tasks?

## Suggested Chapters

- AI Inference Compute Mental Model.
- GPU, VRAM, Model Weights, Activation, And KV Cache.
- Quantization: INT4, INT8, FP16.
- vLLM, Ollama, And Model Serving.
- Concurrency, Batching, Throughput, And Latency.
- Multi-Model GPU Scheduling.
- Capacity Planning For Enterprise AI.
- CUDA vs ROCm.
- Cloud Token Cost vs Local GPU Cost.
- GPU Failure And Debugging.

## First Labs

- Estimate VRAM for an LLM deployment.
- Run a local model with vLLM or Ollama.
- Measure latency and throughput.
