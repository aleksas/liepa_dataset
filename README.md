# liepa_dataset
LIEPA dataset stats and tools for cleanup.

## Install requirements

For audio processing script needs `soundfile`, `matplotlib` and `resampy` packages.

To install run:

> pip install -r requirements.txt

## Getting LIEPA dataset

To download and unpack locally LIEPA dataset run following command:

> python get_liepa.py

## Clean dataset

To clean data integrity run following command:

> python clean.py -a

It should output file/directory naming issues, audio file framerate isssues and transcription encoding.

## Fix dataset

To fix known issues in dataset run following command:

> python clean.py -u -x

Will fix file structure.
The next command will fix all other issues including forsing wav PCM_16 encoding.

> python clean.py -a -x

You can also call `> python clean.py -h` to see help.

## Get dataset stats

To get wordcount run following command:

> python stats.py -w

## Problems after fixing

- [See PROBLEMS](PROBLEMS.md)

# Dataset structure
[Decode LIEPA dataset structure](STRUCTURE.md)
