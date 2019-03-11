from io import open
from re import compile

p1 = compile(r'([^\s\.\?!]+\s)?[\t\r\n ]*([^\s\.\?!]+[\.\?!]+)[\t\r\n ]*')
p2 = compile(r'^([IVX]+\.)\n+')
p3 = compile(r'([\t\r\n ]+[IVX]+\.)\n+')
p4 = compile(r'^([A-ZĄ-Ž]\.)\n+')
p5 = compile(r'([\t\r\n "]+[A-ZĄ-Ž]\.)\n+')
p6 = compile(r'([a-zą-ž])\n([0-9a-zą-ž,:%])')
p7 = compile(r'\n([a-zą-ž,:])')
p8 = compile(r'\n([\)\]])')
p9 = compile(r'(Nr\.)\n((\d)|([IXVM\d]))')
p10 = compile(r'(\s*((pab)|p|d|m|([Šš]vč)|([dD]r)|(Šv)|(str)|(pr)|(Th))\.\s*)\n(\s*[A-ZĄ-Ž\-])')
p11 = compile(r'(\d+\.)\n(\d+)')
p12 = compile(r'\n\s*(")\s*\n')
p13 = compile(r' +')
p14 = compile(r'\n+')
p15 = compile(r'\n\s*(\d+\.)\s*\n')
p16 = compile(r'(\n[“”])|(„\n)')
p17 = compile(r'(((mln)|(mlrd)|(tūkst))\.)\n+((JAV\s)|(Lit)|([Ll]t\.?))')
p18 = compile(r'(\s*((str)|g|([Žž]r))\.\s*)\n(\s*\d+)')
p19 = compile(r'(\d+-)\n(\d+)')
p20 = compile(r'^(\d+\.)\s*\n([“”„"]?\s*[A-ZĄ-Ž])')
p21 = compile(r'([a-zą-ž])(\s*\n)+\s*(\d+\s*%)')
p22 = compile(r'(\d+)\s*\.\s*(\d+)\s+(punkt)')

ps = compile(r'[`~^]+')

np = compile(r'(\d+)|([IVXMD](\s|\.))')

def split_lines(filenames):
    for filename in filenames:
        with open(filename, 'r', encoding="utf8") as f_in:
            for line in f_in:
                line = ps.sub('', line)

                content = line.strip()
                content = p1.sub(r'\g<1>\g<2>\n', content)
                content = p2.sub(r'\g<1> ', content)
                content = p3.sub(r' \g<1> ', content)
                content = p4.sub(r'\g<1> ', content)
                content = p5.sub(r' \g<1> ', content)
                content = p6.sub(r'\g<1> \g<2>', content)
                content = p7.sub(r' \g<1>', content)
                content = p8.sub(r'\g<1>', content)
                content = p9.sub(r'\g<1> \g<2>', content)
                content = p10.sub(r'\g<1> \g<10>', content)
                content = p11.sub(r'\g<1> \g<2>', content)
                content = p12.sub(r'\g<1>\n', content)
                content = p13.sub(r' ', content)
                content = p14.sub(r'\n', content)
                content = p15.sub(r'\n\g<1> ', content)
                content = p16.sub(r'"', content)
                content = p17.sub(r'\g<1> \g<6>', content)
                content = p18.sub(r'\g<1> \g<5>', content)
                content = p19.sub(r'\g<1>\g<2>', content)
                content = p20.sub(r'\g<1> \g<2>', content)
                content = p21.sub(r'\g<1> \g<3>', content)
                content = p22.sub(r'\g<1>.\g<2> \g<3>', content)

                for l in content.splitlines():
                    l = l.strip()
                    if l:
                        yield l

def has_numeric(text):
    return np.match(text) != None

if __name__ == '__main__':
    with open('__final_1.split.txt', 'w', encoding="utf8") as f_out:
        with open('__final_1.split.num.txt', 'w', encoding="utf8") as nf_out:
            for line in split_lines(['__final_1.txt', 'chrestomatija.txt']):
                f_out.write(line + '\n')

                if has_numeric(line):
                    nf_out.write(line + '\n')