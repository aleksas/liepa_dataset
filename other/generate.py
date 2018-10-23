from io import open
from re import compile
from os import system, makedirs
from string import ascii_uppercase
from os.path import join, exists
from shutil import copyfile

in_file_0 = '../other/regina_transcript.txt'
in_file_1 = '../other/regina_transcript_stressed.txt'
in_dir = '../MII_LIEPA_SYN_V1/Regina/data'
out_dir = '../gen'
out_file = join(out_dir, 'transcript.txt')

threshold = -50 #db
silence = 0.2 # silence seconds between two concatenated files

sentences = []
questions = []
exclamations = []

if not exists(out_dir):
    makedirs(out_dir)

caps = ascii_uppercase + 'ĄĘĖČĮŲŪŠŽ'

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

lines_0, lines_1 = [], []

with open(in_file_0, 'r', encoding='utf8') as f:
    lines_0 = f.readlines()

with open(in_file_1, 'r', encoding='utf8') as f:
    lines_1 = f.readlines()

line_count = len(lines_0)

if line_count != len(lines_1):
    raise Exception("Input files have different number of lines.")

new_lines = []

for i in range(line_count):
    line_0 = lines_0[i].strip()

    new_lines.append((i, line_0, [i]))
    
    if line_0[0] in caps:
        if line_0[-1] == '.':
            sentences.append((i, line_0))
        elif line_0[-1] == '?':
            questions.append((i, line_0))
        elif line_0[-1] == '!':
            exclamations.append((i, line_0))

    src = join(in_dir, '%d.wav' % i)
    dst = join(out_dir, '%d.wav' % i)

    copyfile(src, dst)

sorter = lambda x:len(x[1])
sentences.sort(key=sorter, reverse=False)   # ascending
questions.sort(key=sorter, reverse=True)    # descending
exclamations.sort(key=sorter, reverse=True) # descending

all_sentences = questions + exclamations

plain_sentences, sentences = sentences[:len(all_sentences)], sentences[len(all_sentences):]

all_sentences += plain_sentences

all_sentences.sort(key=sorter, reverse=True)    # descending

pairs = list(zip(all_sentences, sentences[:len(all_sentences)]))

start_index = len(new_lines)

for i in range(len(pairs)):
    a, b = pairs[i]

    index = start_index + i
    
    in_a_0 = join(in_dir, '%d.wav' % a[0])
    in_a_1 = join(in_dir, '%d.wav' % b[0])
    
    out_a = join(out_dir, '%d.wav' % index)
    
    cmd = cmd_format % (in_a_0, in_a_1, threshold, threshold, silence, out_a)
    system(cmd)

    line = '%s %s' % (a[1], b[1])

    new_lines.append((index, line, [a[0], b[0]]))

new_lines_2 = []
start_index = len(new_lines)

for i, line, indeces in new_lines:

    line = ''
    if len(indeces) == 1:
        line = lines_1[indeces[0]].strip()
    elif len(indeces) == 2:
        line = ' '.join([lines_1[i].strip() for i in indeces])
    else:
        raise Exception()

    index = start_index + i

    new_lines_2.append((index, line, [i]))

    src = join(out_dir, '%d.wav' % i)
    dst = join(out_dir, '%d.wav' % index)

    copyfile(src, dst)

with open(out_file, 'w', encoding='utf8') as f:
    for i, line, _ in new_lines + new_lines_2:
        f.write('%s\n' % line)