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
