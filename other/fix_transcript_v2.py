from codecs import open
from re import findall, sub
import sys

with open('regina_transcript.txt', 'r') as f:
    lines = f.readlines()

with open('transcript_stressed.txt', 'r') as f:
    lines_stressed = f.readlines()

if len(lines_stressed) > len(lines):
    raise Exception()

for i, (line, line_stressed) in enumerate(zip(lines, lines_stressed)):
    line = line.strip()
    line_stressed = line_stressed.strip()

    if line[-1] in '?!.':
        line_stressed += line[-1]

    if line[0] == line[0].upper():
        line_stressed =  line_stressed[0].upper() + line_stressed[1:]

    lines_stressed[i] = line_stressed
    
    line_ = line.replace(',', ' , ')
    a = line_.split()
    b = line_stressed.split()

    start = 0

    for ai, a0 in enumerate(a):
        for bi, b0 in enumerate(b[start:]):
            a0_ = a0
            b0_ = sub('[~`^]', '', b0)

            if a0_ == b0_:
                start += bi + 1

                a[ai] = b0

                break

    a = ' '.join(a).replace(' ,', ',')
    lines[i] = a + '\n'

with open('regina_transcript_stressed_v2.txt', 'w') as f:
    f.writelines(lines)



