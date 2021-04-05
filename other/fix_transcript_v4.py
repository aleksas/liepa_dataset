from codecs import open
from re import findall, sub, compile
import sys

_utf8_stress_map = {
    0: u'\u0300', # grave
    1: u'\u0301', # acute
    2: u'\u0303', # tilde
    3: u'\u0301', # acute
}

_ascii_stress_map = {
    0: "`", # grave
    1: "^", # acute - no printable acute accent in ascii table only in extended ASCII:239
    2: "~", # tilde
    3: "^", # acute
}

acc_map_v2 = {
    compile('2'):(_ascii_stress_map[0], _utf8_stress_map[0]),
    compile('3'):(_ascii_stress_map[1], _utf8_stress_map[1]),
    compile('4'):(_ascii_stress_map[2], _utf8_stress_map[2]),
    compile('5'):('', ''),
}

voices = 'regina', 'aiste', 'vladas', 'edvardas'
p = compile(u"[a-zą-žA-ZĄ-Ž]")
d = compile("[ \t,.?!\n]+")

with open('other/regina_transcript_stressed.txt', 'r') as f:
    lines_stressed = f.readlines()

with open('other/regina_transcript_stressed_v2.txt', 'r') as f:
    lines_stressed_v2 = f.readlines()

stress_map = {sub('[\?!., \d]', '',k).lower():v for k,v in zip(lines_stressed, lines_stressed_v2)}

for voice in voices:
    with open('other/' + voice + '_transcript_stressed.txt', 'r') as f:
        lines = f.readlines()

    lines_ascii = list(lines)
    lines_utf8 = list(lines)

    for i in range(len(lines)):
        line = sub('[\?!.,\d ]', '',lines[i]).lower()
        
        if line in stress_map:
            tmp = list(lines[i])
            for s,t in zip(p.finditer(stress_map[line]), p.finditer(lines[i])):
                tmp[t.start()] = stress_map[line][s.start()]

            for s,t in zip(reversed(list(d.finditer(stress_map[line]))), reversed(list(d.finditer(lines[i])))):
                tmp[t.start() : t.end()] = stress_map[line][s.start():s.end()]

            lines_ascii[i] = ''.join(tmp)
            lines_utf8[i] = ''.join(tmp)
        
        for k,(v_ascii, v_utf8) in acc_map_v2.items():
            lines_ascii[i] = k.sub(v_ascii, lines_ascii[i])
            lines_utf8[i] = k.sub(v_utf8, lines_utf8[i])
        
    with open('other/' + voice + '_transcript_stressed_v4_ascii.txt', 'w') as f:
        f.writelines(lines_ascii)
        
    with open('other/' + voice + '_transcript_stressed_v4_utf8.txt', 'w') as f:
        f.writelines(lines_utf8)



