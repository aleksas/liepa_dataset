# LIEPA dataset
LIEPA dataset stats and tools for cleanup.

## Install requirements

For audio processing script needs `soundfile`, `matplotlib` and `resampy` packages.

To install run:

> pip install -r requirements.txt

## LIEPA synthesis dataset
Dataset contains audio utterances and phoneme transcriptions for 4 speakers.

### Getting dataset

To download and unpack locally dataset run following command:

> python get_liepa.py


### Clean dataset

To clean data integrity run following command:

> python clean_syn.py -a

### Fix dataset

To fix known issues in dataset run following command:

> python clean_syn.py -ax

## LIEPA recognition dataset
Dataset contains audio utterances and transcriptions for over 300 speakers.

### Getting dataset

To download and unpack locally dataset run following command:

> python get_liepa.py -rx

To download and unpack locally dataset additional annotations run following command:

> python get_liepa.py -nx

### Clean dataset

To clean data integrity run following command:

> python clean_rec.py -a

It should output file/directory naming issues, audio file framerate isssues and transcription encoding.

### Fix dataset

To fix known issues in dataset run following command:

> python clean.py -u -x

Will fix file structure.
The next command will fix all other issues including forsing wav PCM_16 encoding.

> python clean.py -a -x

You can also call `> python clean.py -h` to see help.

### Get dataset stats

To get wordcount run following command:

### Dataset structure
[Decode LIEPA dataset structure](STRUCTURE.md)

> python stats.py -w

## Dataset Problems

- [See PROBLEMS](PROBLEMS.md)
