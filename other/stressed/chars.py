from io import open

def analyze(fname):
    chars = set([])
    
    with open(fname, encoding="utf8") as f:
        chars |= set(f.read())
    
    return chars
    
if __name__ == '__main__':
    chrestomatija = analyze('chrestomatija.txt')
    marti = analyze('marti.txt')
    final = analyze('__final_1.txt')
    
    #print (chrestomatija - marti)
    #print (marti - chrestomatija)
    print (final - chrestomatija)