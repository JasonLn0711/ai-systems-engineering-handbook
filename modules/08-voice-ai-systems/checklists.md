# Checklists

## Voice Pipeline

- [ ] Audio source format inspected: file type, duration, sample rate, channels,
  bit depth, clipping risk, and silence profile.
- [ ] Normalization path defined: ffmpeg or equivalent conversion to controlled
  sample rate, mono/stereo policy, PCM or model-required input format.
- [ ] Feature representation chosen for the task: waveform, RMS/ZCR,
  spectrogram, log-Mel, MFCC, or learned encoder input.
- [ ] Audio input quality defined.
- [ ] VAD behavior defined.
- [ ] ASR model and language constraints defined.
- [ ] Diarization need assessed.
- [ ] TTS latency budget defined.
- [ ] Wake word behavior defined.
- [ ] Evaluation data defined.
- [ ] Evaluation report includes CER/WER, DER/JER when relevant, latency, RTF,
  GPU memory, failure cases, and regression-test samples.
