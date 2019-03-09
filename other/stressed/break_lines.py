from io import open
from re import compile

p1 = compile(r'([^\s\.\?!]+\s)?[\t\r\n ]*([^\s\.\?!]+[\.\?!]+)[\t\r\n ]*')
p2 = compile(r'^([IVX]+\.)\n+')
p3 = compile(r'([\t\r\n ]+[IVX]+\.)\n+')
p4 = compile(r'^([A-ZĄ-Ž]\.)\n+')
p5 = compile(r'([\t\r\n ]+[A-ZĄ-Ž]\.)\n+')
p6 = compile(r'([a-zą-ž])\n([0-9a-zą-ž,:])')
p7 = compile(r'\n([a-zą-ž,:])')
p8 = compile(r'\n([\)\]])')
p9 = compile(r'(Nr\.)\n((\d)|([IXVM\d]))')
p10 = compile(r'(\s*((pab)|([dD]r)|(Šv))\.\s*)\n(\s*[A-ZĄ-Ž])')
p11 = compile(r'(\d+\.)\n(\d+)')
p12 = compile(r'\n\s*(")\s*\n')
p13 = compile(r' +')
p14 = compile(r'\n+')
p15 = compile(r'\n\s*(\d+\.)\s*\n')
p16 = compile(r'(\n[“”])|(„\n)')
p17 = compile(r'(mln\.)\n+((JAV\s)|(Lit)|([Ll]t\.?))')

ps = compile(r'[`~^]+')

def split_lines(fname_in):    
    with open(fname_in, 'r', encoding="utf8") as f_in:
        content =  f_in.read()

        content = content.strip()
        content = p1.sub(r'\g<1>\g<2>\n', content)
        content = p2.sub(r'\g<1> ', content)
        content = p3.sub(r' \g<1> ', content)
        content = p4.sub(r'\g<1> ', content)
        content = p5.sub(r' \g<1> ', content)
        content = p6.sub(r'\g<1> \g<2>', content)
        content = p7.sub(r' \g<1>', content)
        content = p8.sub(r'\g<1>', content)
        content = p9.sub(r'\g<1> \g<2>', content)
        content = p10.sub(r'\g<1> \g<2>', content)
        content = p11.sub(r'\g<1> \g<2>', content)
        content = p12.sub(r'\g<1>\n', content)
        content = p13.sub(r' ', content)
        content = p14.sub(r'\n', content)
        content = p15.sub(r'\n\g<1> ', content)
        content = p16.sub(r'"', content)
        content = p17.sub(r'\g<1> \g<2>', content)
        for l in content.splitlines():
            l = l.strip()
            if l:
                yield l

if __name__ == '__main__':
    with open('__final_1.split.txt', 'w', encoding="utf8") as f_out:
        for line in split_lines('__final_1.txt'):
            line = ps.sub('', line)
            f_out.write(line + '\n')