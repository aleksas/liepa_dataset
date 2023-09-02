FROM python:3.10

RUN python3 -m pip install --upgrade pip chardet soundfile numpy resampy

WORKDIR /liepa-dataset
