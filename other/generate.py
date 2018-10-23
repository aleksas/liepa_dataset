from io import open
from re import compile
from os import system

in_file = 'regina_transcript.txt'
out_file = 'E:\\liepa_dataset\\gen\\test_transcript.txt'
threshold = -50 #db
silence = 0.2 # silence seconds between two concatenated files

sentences = []
questions = []
exclamations = []

caps = 'QWERTYUIOPASDFGHJKLZXCVBNMĄČĘĖĮŠŲŪŽ'

cmd_format = """ffmpeg -loglevel panic -y \
-i %s -i %s -filter_complex \
"\
[0:a] silenceremove=stop_periods=1:stop_duration=1:stop_threshold=%ddB [first],\
[1:a] silenceremove=start_periods=1:start_duration=0:start_threshold=%ddB [second],\
aevalsrc=exprs=0:d=%.1f [silence],\
[first] [silence] [second] concat=n=3:v=0:a=1[outa]\
" \
-map [outa] %s"""

start_index = 0

with open(in_file, 'r', encoding='utf8') as f:
    lines = f.readlines()

    new_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        
        if line[0] in caps:
            if line[-1] == '.':
                sentences.append((i, line))
            elif line[-1] == '?':
                questions.append((i, line))
            elif line[-1] == '!':
                exclamations.append((i, line))
    start_index = len(lines)

sorter = lambda x:len(x[1])
sentences.sort(key=sorter, reverse=False)   # ascending
questions.sort(key=sorter, reverse=True)    # descending
exclamations.sort(key=sorter, reverse=True) # descending

all_sentences = questions + exclamations

plain_sentences, sentences = sentences[:len(all_sentences)], sentences[len(all_sentences):]

all_sentences += plain_sentences

all_sentences.sort(key=sorter, reverse=True)    # descending

pairs = list(zip(all_sentences, sentences[:len(all_sentences)]))

with open(out_file, 'w', encoding='utf8') as f:
    in_dir = 'J:\\liepa_dataset\\MII_LIEPA_SYN_V1\\Regina\\data\\'
    out_dir = 'E:\\liepa_dataset\\gen\\'

    for i in range(len(pairs)):
        a, b = pairs[i]
        
        in_a_0 = '%s%d.wav' % (in_dir, a[0])
        in_a_1 = '%s%d.wav' % (in_dir, b[0])
        
        index = start_index + i
        
        out_a = '%s%d_%d-%d.wav' % (out_dir, index, a[0], b[0])
        
        cmd = cmd_format % (in_a_0, in_a_1, threshold, threshold, silence, out_a)
        system(cmd)
        
        f.write('%d|%d|%d|%s %s\n' % (index, a[0], b[0], a[1], b[1]))
        
