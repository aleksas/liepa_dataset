from io import open
from sandara import Sandara

files = ['regina_transcript.txt', 'aiste_transcript.txt']
replace = '?,.'

sa = Sandara()

for file in files:
    lines = None
    with open(file, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        for ch in replace:
            line = line.replace(ch, '')
        new_line = sa.process(line.strip())
        new_lines.append(new_line)
    

    with open(file+'_stressded', 'w') as f:
        f.write('\n'.join(new_lines))
