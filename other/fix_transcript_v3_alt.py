from codecs import open
from re import findall, sub, IGNORECASE
import sys
    
with open('../transcript.txt', 'r') as f:
    lines = f.readlines()

search_patterns = [None] * len(lines)

for i, line in enumerate(lines):
    line = line.strip()
    line = sub(r'[\wą-ž]', r'\g<0>[~`^]?', line)
    line = sub(r' ', r'[\s:;,]+', line)
    line = sub(r'$', r'[\.:;\?!,]*', line)
    search_patterns[i] = line

with open('__final_1.txt', 'r') as f:
    text = f.read()

with open('../transcript_stressed_updated.txt', 'r') as f:
    res = f.readlines()

for i, p in enumerate(search_patterns):
    f = findall(p, text, IGNORECASE) 
    if f:
        f = list(set(f))
        f.sort(key=len, reverse=True)
        line = sub('[\r\n]', ' ', f[0]) 
        line = sub(' +', ' ', line) 
        res[i] = line + '\n'
        print(line)

#with open('../transcript_stressed_v3.txt', 'w') as f:
#    f.writelines(res)



