# Failure Modes

- ASR quality collapses on phone audio, noise, or domain vocabulary.
- Diarization fails with overlapping speakers.
- TTS latency makes interaction feel broken.
- Wake word or VAD triggers too often or misses real speech.
- Audio ingestion silently changes sample rate, channels, bit depth, or loudness,
  so downstream VAD / ASR behavior is unstable.
- RMS-only speech detection passes loud non-speech or drops quiet speech.
- Spectrogram / Mel / MFCC parameters are changed without regression samples,
  making model behavior drift without visible code failure.
