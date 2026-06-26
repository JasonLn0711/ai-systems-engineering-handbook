# Module 08: Voice AI Systems

## Purpose

Teach complete voice AI systems, not only ASR.

## Core Questions

- How do audio capture, VAD, ASR, diarization, LLM reasoning, TTS, playback, interruption, and latency fit together?
- Why do sampling rate, phone audio, noise, hotwords, speaker overlap, and Taiwan Mandarin matter?
- How do you evaluate voice systems beyond a single demo?

## Suggested Chapters

- Audio Signal Basics.
- Sampling Rate, 8 kHz, 16 kHz, And Phone Audio.
- VAD And Speech Segmentation.
- ASR Architecture.
- Breeze ASR, Whisper, And Domain Adaptation.
- Diarization, Speaker Embedding, And Overlap.
- Hotwords And Domain Vocabulary.
- TTS And Voice Cloning.
- Prosody, Emotion, And Taiwan Accent.
- Wake Word And Physical AI.
- Real-Time Voice Agent Latency Budget.
- Noise Reduction And Far-Field Audio.
- Environmental Sound Detection.
- Voice AI Evaluation.

## Companion Learning Notes

- `audio-signal-processing-for-machine-learning-video-notes.md`: agent-readable
  record of Jason's study of `Audio Signal Processing for Machine Learning`.
  Use it as the audio-intake bridge from waveform / sample rate / RMS / STFT /
  Mel / MFCC into VAD, ASR, diarization, service APIs, deployment, and
  evaluation.

## First Labs

- Build a VAD segmentation demo.
- Run batch ASR.
- Measure ASR -> LLM -> TTS latency.
