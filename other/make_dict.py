"""
Should be ran from directory containing ANSI fonemommis and UNICODE folders from 
anotacijos.tar.bz2.
Will create dict.txt' file.
"""

import codecs
from os import walk
from os.path import join, exists, splitext
from re import compile 

valid_lt_symbols = u'ĄČĘĖĮŠŲŪŽąčęėįšųūž'
valid_lt2ascii_symbols = 'ACEEISUUZaceeisuuz'
valid_ascii_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'(),-.:;? _\r\n\t'
valid_symbols = valid_lt_symbols + valid_ascii_symbols
valid_mapped_symbols = valid_lt2ascii_symbols + valid_ascii_symbols

valid_ascii_symbols = set(valid_ascii_symbols.encode('ascii'))
valid_utf8_symbol_set = set(valid_symbols.encode('utf-8'))
valid_utf16_symbol_set = set(valid_symbols.encode('utf-16'))
valid_utf8_sig_symbol_set = set(valid_symbols.encode('UTF-8-SIG'))
valid_windows_1257_symbols_set = set(valid_symbols.encode('windows-1257') + b'\x9a')


def collect_text_problems(file_path):
    encoding_problem = []

    text = None
    try:
        with open(file_path, 'rb') as f:
            raw_text = f.read()

        raw_text_symbol_set = set(raw_text) - set('\x1f')

        diff_ascii = raw_text_symbol_set - valid_ascii_symbols
        diff_win_1257 = raw_text_symbol_set - valid_windows_1257_symbols_set
        diff_utf_16 = raw_text_symbol_set - valid_utf16_symbol_set
        diff_utf_8_sig = raw_text_symbol_set - valid_utf8_sig_symbol_set
        diff_utf_8 = raw_text_symbol_set - valid_utf8_symbol_set

        # lets consider ascii text to be utf-8 since utf8 and ascii ar compatible
        # it just means that text does not have any special chars
        if len(diff_ascii) == 0 or len(diff_utf_8) == 0:
            charenc = 'utf-8'
        elif len(diff_win_1257) == 0:
            charenc = 'windows-1257'
        elif len(diff_utf_16) == 0:
            charenc = 'utf-16'
        elif len(diff_utf_8_sig) == 0:
            charenc = 'UTF-8-SIG'
        else:
            result = chardet.detect(raw_text)
            charenc = result['encoding']

            if charenc in [
                'Windows-1254', 'windows-1251',
                'Windows-1252', 'ISO-8859-1',
                'ISO-8859-9']:
                charenc = 'windows-1257'

        if charenc == 'windows-1257':
            raw_text = raw_text.replace(b'\x9a', b'\xfe')

        raw_text = raw_text.replace(b'\x1f', b'')

        if file_path.endswith('S566Mh_026_29.txt'):
            raw_text = raw_text.replace('˛'.encode(charenc), 'ž'.encode(charenc))

        text = raw_text.decode(charenc).lower()

        diff_set = set(text) - set(valid_symbols)

        if len(diff_set) > 0:
            raise Exception(','.join(diff_set))

        if charenc != 'utf-8':
            problem = '"%s" has %s encoding but utf-8 is required.' % (file_path, charenc)
            encoding_problem = [(file_path, charenc, 'utf-8', problem)]
    except Exception as e:
        encoding_problem = [(file_path, 'utf-8', str(e))]
        raise Exception(encoding_problem)

    return encoding_problem

def fix_encoding_problem(file_path, src_enc, dst_enc):
    with open(file_path, 'rb') as f:
        raw_text = f.read()

    if src_enc == 'windows-1257':
        raw_text = raw_text.replace(b'\x9a', b'\xfe')

    if file_path.endswith('S566Mh_026_29.txt'):
        raw_text = raw_text.replace('˛'.encode(src_enc), 'ž'.encode(src_enc))

    text = raw_text.decode(src_enc)

    with codecs.open(file_path,'w', encoding='utf8') as f:
        f.write(text)




pattern_word = compile(r"^\s*\d+\s+\d+\s+([\_\-\w]+'?)\s+([\_\-\d\w']+)\s*$")
pattern_fon = compile(r"^\s*\d+\s+\d+\s+([\_\-\w]+'?)\s*$")

ansi_dir = './ANSI/'
unicode_dir = './UNICODE/'
fon_dir = './fonemommis/'
dict_file = 'dict.txt'

words = {}



for root, subdirs, files in walk(ansi_dir):
	count = 0
	
	for file in files:
		ansi_path = join(ansi_dir, file)
		unicode_path = join(unicode_dir, file)
		
		name, _extension = splitext(file)
		
		fon_path = join(fon_dir, name + '.la2')
		
		unicode_text = None
		ansi_text = None
		fon_text = None
		
		
		if exists(ansi_path) and exists(unicode_path) and exists(fon_path):
			count += 1
			
			if count > 100000:
				break
		
			encoding_problem = collect_text_problems(unicode_path)
			
			if len(encoding_problem) != 0:
				fix_encoding_problem(encoding_problem[0][0], encoding_problem[0][1], encoding_problem[0][2])
			
			with open(ansi_path, 'r') as f:
				ansi_text = f.read().strip()
		
			with open(unicode_path, 'rb') as f:
				unicode_text = f.read().decode('utf-8').strip()
			
			a_splits = ansi_text.split()
			u_splits = unicode_text.split()
			
			if len(u_splits) == len(a_splits):
				with open(fon_path, 'r') as f:
					fon_text = f.read().strip()
				
				f_splits = []
				f_splits_b = []
				f_lines = fon_text.splitlines()
				fons = []
				for line in f_lines:
					m = pattern_word.match(line)
					if m:
						if len(fons) > 0:
							f_splits_b.append(fons)
						fons = []
						fon = m.group(1)
						word = m.group(2)
						f_splits.append(word)
						fons.append(fon)
						
					m = pattern_fon.match(line)
					if m:
						fon = m.group(1)
						fons.append(fon)
				
				if len(fons) > 0:
					f_splits_b.append(fons)
				
				if len(a_splits) == len(f_splits_b) and a_splits == f_splits:
				
					for i in range(len(f_splits)):
						a_word = f_splits[i]
						u_word = u_splits[i]
						
						if a_word not in words:
							words[a_word] = (u_word, f_splits_b[i])
				
	with codecs.open(dict_file, 'w', encoding='utf8') as f:
		lines = []
		
		sorted_by_value = sorted(words.items(), key=lambda kv: len(kv[1][1]), reverse=True)
		
		for ansi, pair in sorted_by_value:
			items = []
			print(ansi)
			print(pair[0].encode('utf-8'))
			print(' '.join(pair[1]))
			items.append(ansi)
			items.append(pair[0])
			items.append(' '.join(pair[1]))
			
			lines.append(';'.join(items))
		
		text = '\r\n'.join(lines)
		f.write(text)
