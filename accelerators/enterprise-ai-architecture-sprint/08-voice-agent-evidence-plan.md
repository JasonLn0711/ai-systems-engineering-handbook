# Voice Agent Evidence Plan

## Purpose

Turn a voice-agent demo into measurable system evidence. Voice AI readiness is
not proven by ASR alone. It requires a real-time loop, audio segmentation,
speaker handling, TTS latency, interruption behavior, and clear limits.

## Target System

```text
microphone / audio file
-> VAD
-> ASR
-> optional diarization
-> LLM / agent
-> TTS
-> playback
-> logs and metrics
```

## Evidence Output

- Voice pipeline diagram.
- Demo script.
- Latency breakdown.
- Audio quality notes.
- Failure-mode list.
- Scope-control statement.

## Minimum Viable Demo

- One 2-3 minute recording.
- Captured screen or terminal.
- Subtitles or transcript.
- ASR result.
- LLM response.
- TTS playback.
- p50/p95 latency table over several turns.
- Clear statement of model/runtime/hardware.

## Latency Table

| Turn | VAD segment ms | ASR ms | LLM first token ms | LLM complete ms | TTS ms | End-to-end ms | Notes |
|---|---:|---:|---:|---:|---:|---:|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

## Evidence Dimensions

| Dimension | Evidence question |
|---|---|
| VAD | Does speech segment naturally or wait for max timeout? |
| ASR | Are domain terms transcribed correctly enough for downstream use? |
| Diarization | Can the system separate speakers or clearly state it cannot? |
| LLM | Does the response follow scope and source boundary? |
| TTS | Is speech understandable, timely, and appropriate for the context? |
| Barge-in | Can user interruption stop or supersede prior output? |
| Logs | Can timing and model decisions be reconstructed? |
| Safety | Are high-risk outputs routed to scope control or review? |

## Failure Modes

- ASR is acceptable but end-to-end latency is unusable.
- VAD waits too long and makes conversation feel broken.
- TTS is natural but too slow for real-time interaction.
- Diarization is assumed but not measured.
- Wake word or always-listening behavior lacks activation boundary.
- Voice clone demo ignores consent, identity, or safety controls.
- Logs capture text but not audio timing or model runtime.

## Validation Checklist

- [ ] Demo identifies hardware, model, and runtime.
- [ ] Latency is measured by component.
- [ ] p50 and p95 are reported.
- [ ] Audio source and noise condition are described.
- [ ] Known limits are stated.
- [ ] Safety and human-review boundaries are explicit.
- [ ] The demo can be repeated from documented steps.

## Linked Modules And Labs

- `modules/08-voice-ai-systems/`
- `modules/05-llm-application-architecture/`
- `modules/09-security-red-teaming/`
- `labs/voice-ai/`

## Next Implementation Gate

Record a small ASR -> LLM -> TTS demo with component-level timings and a
follow-up note explaining which parts are production-ready, prototype-only, or
future validation work.
