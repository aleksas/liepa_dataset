"""
Run this script from within any of four voice db files
to create crude transcrip file. It takes 'db_fon.txt' containing phoneme transcription, 
'db_tr.txt' containing a dictionary of word phoneme transcriptions and uses that to generate a rough
transcription file 'db_tr.txt'.
"""

from re import compile
import codecs

fon_file = 'db_fon.txt'
out_file = 'db_tr.txt'
dict_file = 'dict.txt'

word_dict = []

with open(dict_file, 'rb') as f:
	text = f.read().decode('utf-8')

lines = text.splitlines()

for line in lines:
	tup = line.split(';')
	if len(tup) == 3:
		word_dict.append(tup)

with open(fon_file, 'r') as f:
	text = f.read()

lines = text.splitlines()

new_lines = []
for line in lines:
	words = line.split('+')
	ws = []
	for word in words:
		word = word.replace('-', ' ')
		for w in word_dict:
			word = word.replace(w[2], w[1])
		ws.append(word.replace(' ', ''))
	new_lines.append(' '.join(ws))

with codecs.open(out_file,'w', encoding='utf8') as f:
	f.write('\r\n'.join(new_lines))

