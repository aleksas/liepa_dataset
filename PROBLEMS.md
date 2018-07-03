# Problems
LIEPA dataset in it's original form has multiple issues:

- Some word groups (Z###) have audio recordings of multiple words/commands squeezed into one record.
The problem here is splitting such audio records into separe command/word records. Example: **D605/Z020**
On the other hand there are word groups (Z###) that have a dinge word/word command per audio record, e.g. **D245/Z021**.
  - SOLUTION: identify groups or individual audio records without
[silence indicators](https://github.com/aleksas/liepa_dataset/blob/master/utils/text.py#L1-L4),
which usually indicate interval between words / word commands in transcritoon files.
- Some recordings have strong background noise including speceific noise marked in transcription by [noise indicators](https://github.com/aleksas/liepa_dataset/blob/master/utils/text.py#L20-L30).
  - SOLUTION: identify recordings wothout noise indicators.
- Transcriptions contain a significant amount of misspelled words.
Additionally some words may be transcribed according to the actual record (hypothetically) instead of desired transcript.
If that's the case (no proof or indication of such is known) then there have to be two versions of transcripts,
intended transcription and realistic (with misprononcements transcribed).
  - ????
  

# Target
- Identify Voices with least amount of problems (background noise, noise indicators, silence indicators)
  - Silence indicators raise prolems if present in Z### utternace group as thei indicate split between separate words/commands
- Identify Voices with clear/pleasant pronounciation/recording, without audio signal being too loud (usually when recorded too close to mic).
- Identify Voices with longest total audio record.
- Identify Voices with "good" variation in transcribtion length (max - 150, avg ~13, min ~ 1).
- Identify similar Voices as a potential to be combined into single voice (to mitigate lack of training data issue).
