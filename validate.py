from os import walk, makedirs, rename
from os.path import join, splitext, split, normpath, exists
from re import compile, sub, search
from argparse import ArgumentParser
import codecs
import chardet
import operator

from liepa import default_dir, default_wav_samplerate, default_wav_subtype
from utils.audio import resample, wav_duration
from utils.text import mistypes, regex_replacements, silence_indicators, noise_indicators

txt_extensions = ['.txt', '.TXT']
wav_extensions = ['.wav', '.WAV']

valid_lt_symbols = u'ĄČĘĖĮŠŲŪŽąčęėįšųūž'
valid_ascii_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\'(),-.:;? _\r\n\t'
valid_symbols = valid_lt_symbols + valid_ascii_symbols
valid_ascii_symbols = set(valid_ascii_symbols.encode('ascii'))
valid_utf8_symbol_set = set(valid_symbols.encode('utf-8'))
valid_utf16_symbol_set = set(valid_symbols.encode('utf-16'))
valid_utf8_sig_symbol_set = set(valid_symbols.encode('UTF-8-SIG'))
valid_windows_1257_symbols_set = set(valid_symbols.encode('windows-1257') + b'\x9a')

pattern = compile(r'(?P<type>ZS?|SS?)?(?P<voice>\d+)(?P<sex>M|V)(?P<age>[a-r])_(?P<ut_id>(?P<ut_id_d>\d+)[abc]?)(_(?P<ut_subid>\d+[abc]?))?(?P<tag>_[TP])?(?P<ext>\.(wav|txt))')

# Some files have incorrect utterance type indicator, parent directories indicate correctly.
known_utterance_type_naming_exceptions = [
    ('D57', 'S007'), ('D57', 'S008'),
    ('D556', 'S013'), ('D556', 'S014'),
    ('D556', 'Z000'), ('D556', 'Z001'),
    ('D556', 'Z020'), ('D556', 'Z060')
    ]

"""
known_utterance_type_naming_exceptions += [
    ('D057', 'S007'), ('D057', 'S008')
    ]
"""

known_voice_directory_file_naming_exceptions = range(2, 100)

known_voice_naming_exceptions = [('D251', 'Z026'), ('D515', 'S012'), ('D515', 'Z000'), ('D516', 'S012')]

stats = {
    'word_count': {},
    'sentence_word_positions': {}
}

def collect_samplerate_problems(file_path, subtype):
    duration, samples, samplerate = wav_duration(file_path)

    _, filename = split(file_path)

    if default_wav_samplerate != samplerate or subtype != None:
        if subtype == None:
            subtype = default_wav_subtype
        problem = '"%s" has %d samplerate, default is %d. New subtype - %s.' % (filename, samplerate, default_wav_samplerate, subtype)
        return [(file_path, samplerate, default_wav_samplerate, subtype, problem)]

    return []

def fix_sample_rate_problem(path, src_sr, dst_sr, subtype):
    resample(path, src_sr, dst_sr, subtype)

def fix_naming_problem(src, dst):
    rename(src, dst)

def fix_layering_problem(dst_dir, src, dst):
    if not exists(dst_dir):
        makedirs(dst_dir)

    rename(src, dst)

def fix_mistypes(file_path):
    with open(file_path, 'r') as f:
        text = f.read().lower()

    for mistype in mistypes:
        text = text.replace(mistype[0], mistype[1])

    for replacement in regex_replacements:
        text = sub(replacement[0], replacement[1], text)

    with open(file_path, 'w') as f:
        f.write(text)

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

def collect_text_problems(file_path, group, utterance_id, utterance_sub_id):
    encoding_problem = []
    mistype_problem = []

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

    for mistype in mistypes:
        if mistype[0] in text:
            problem = '"%s" contains mistypes.' % (file_path)
            mistype_problem = [(file_path, problem)]
            break

    for regex_replacement in regex_replacements:
        m = search(regex_replacement[0], text)
        if m:
            problem = '"%s" contains replacements.' % (file_path)
            mistype_problem = [(file_path, problem)]
            break

    if args.print_wordcount:
        words = text.split()
        for w in words:
            if w not in stats['word_count']:
                stats['word_count'][w] = 0
            stats['word_count'][w] += 1
            
    if args.sentence_inconsistencies:
        id = (group, utterance_id, utterance_sub_id)
        clean_text = text
        for indicator in silence_indicators + noise_indicators:
            clean_text = clean_text.replace(indicator, ' ')

        if id not in stats['sentence_word_positions']:
            stats['sentence_word_positions'][id] = {}

        words = clean_text.split()
        for i in range(len(words)):
            if i not in stats['sentence_word_positions'][id]:
                stats['sentence_word_positions'][id][i] = {}

            if words[i] not in stats['sentence_word_positions'][id][i]:
                stats['sentence_word_positions'][id][i][words[i]] = 0

            stats['sentence_word_positions'][id][i][words[i]] += 1

    return encoding_problem, mistype_problem

def cleanup_naming_problems(naming_problems):
    clean_naming_problems = []

    for src, dst, comment in naming_problems:
        duplicate = False
        for src_, dst_, _ in clean_naming_problems:
            if src == src_:
                if dst == dst_:
                    duplicate = True
                else:
                    raise Exception('Problems have multiple solutions:\n\t%s > %s\n\t%s > %s' % (src, dst, src, src_))
        if not duplicate:
            clean_naming_problems.append((src, dst, comment))
    return clean_naming_problems

def validate_static_value(static_name, voice, static, test):
    if not test:
        raise Exception('%s can not be %s for speaker "%s".' % (static_name, test, voice))
    elif static and static != test:
        raise Exception('%s "%s" for speaker "%s" does not match prvious "%s".' % (static_name, test, voice, static))

    return test

def collect_problems(dataset_path, args):
    encoding_problems = []
    mistype_problems = []
    samplerate_problems = []
    directory_naming_problems = []
    file_naming_problems = []
    layering_problems = []

    for root, subdirs, files in walk(dataset_path):
        age_group = None
        gender = None

        root = normpath(root)
        path, leaf = split(root)
        if path == '':
            continue

        dir_group = None
        if leaf[0] in ['D', '.']:
            path = root
        else:
            dir_group = leaf
            utternace_group_type = dir_group[0]

            if utternace_group_type not in ['Z', 'S']:
                raise Exception('Utternace type "%s" does not match valid pattern.' % utternace_group_type)

        db_root, voice = split(path)

        if voice[0] != 'D':
            raise Exception('Voice name "%s" does not start with "D".' % voice[0])

        voice_id = voice[1:]
        correct_voice_id  = '%03d' % int(voice_id)
        correct_path = join(db_root, 'D'+ correct_voice_id)
        if voice_id != correct_voice_id and args.run_naming_test:
            problem = 'Voice id is "%s" but should be "%s".' % (voice_id, correct_voice_id)
            if int(voice_id) not in known_voice_directory_file_naming_exceptions:
                raise Exception(problem)
            else:
                correct_voice_path = join(db_root, 'D' + correct_voice_id)
                directory_naming_problems.append((path, correct_voice_path, problem))

        for filename in files:
            match = pattern.match(filename)
            if not match:
                raise Exception('Filename "%s" does not match valid pattern.' % filename)
            else:
                name, _extension = splitext(filename)

                if dir_group:
                    group = dir_group
                    file_path = join(path, group, filename)
                else:
                    group = match.group('type') + match.group('ut_id_d')

                    file_path = join(path, filename)
                    fixed_dir = join(path, group)
                    fixed_file_path = join(fixed_dir, filename)
                    utternace_group_type = match.group('type')

                    if args.run_structure_test:
                        problem = 'File "%s" is missing group "%s" folder.' % (file_path, group)
                        layering_problems.append((file_path, fixed_dir, fixed_file_path, problem))

                if _extension in wav_extensions and args.run_samplerate_test:
                    samplerate_problems += collect_samplerate_problems(file_path, args.audio_subtype)

                tag = match.group('tag') # _T or _P

                if not tag:
                    tag = ''

                utterance_sub_id = match.group('ut_subid')
                if not utterance_sub_id:
                    utterance_sub_id = ''

                gender = validate_static_value('Gender', voice, gender, match.group('sex'))
                age_group = validate_static_value('Age group', voice, age_group, match.group('age'))

                utterance_id = match.group('ut_id')

                correct_filename = '%s%s%s%s_%s_%s%s%s' % (utternace_group_type, correct_voice_id, gender, match.group('age'), utterance_id, utterance_sub_id, tag, match.group('ext'))
                correct_file_path = join(path, group, correct_filename)

                if _extension in txt_extensions and args.run_transcript_test:
                    encoding_problem, mistype_problem = collect_text_problems(file_path, group, utterance_id, utterance_sub_id)
                    encoding_problems += encoding_problem
                    mistype_problems  += mistype_problem

                if args.run_naming_test:
                    if voice_id != match.group('voice'):
                        problem = 'Voice id "%s" does not match with id "%s" from filename "%s".' % (voice_id, match.group('voice'), file_path)
                        can_continue = False
                        for exc in  known_voice_naming_exceptions:
                            if voice == exc[0] and group == exc[1]:
                                can_continue = True
                                file_naming_problems.append((file_path, correct_file_path, problem))

                        if not can_continue and int(voice_id) not in known_voice_directory_file_naming_exceptions:
                            raise Exception(problem)

                    if match.group('type') != utternace_group_type:
                        problem = 'Utterance group "%s" for "%s" voice is of type "%s", but utterance "%s" is of type "%s". Path: "%s".' % (group, voice, utternace_group_type, filename, match.group(1), root)
                        can_continue = False
                        for exc in known_utterance_type_naming_exceptions:
                            if voice == exc[0] and group == exc[1]:
                                can_continue = True
                                file_naming_problems.append((file_path, correct_file_path, problem))

                        if not can_continue:
                            raise Exception(problem)

    return (
        encoding_problems,
        mistype_problems,
        samplerate_problems,
        layering_problems,
        cleanup_naming_problems(file_naming_problems),
        cleanup_naming_problems(directory_naming_problems))

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-d','--liepa-dir', help='LIEPA dataset directory (Default: "%s").' % default_dir, default=default_dir)
    parser.add_argument('-t','--run-transcript-test', help='LIEPA dataset transcript encoding and mistype testing.', action='store_true')
    parser.add_argument('-r','--run-samplerate-test', help='LIEPA dataset audio samplerate testing.', action='store_true')
    parser.add_argument('-n','--run-naming-test', help='LIEPA dataset file and directory naming testing.', action='store_true')
    parser.add_argument('-u','--run-structure-test', help='LIEPA dataset file and directory structure testing.', action='store_true')
    parser.add_argument('-s','--audio-subtype', choices=['PCM_16','PCM_24','PCM_32'], help='Set audio subtype. Requires -r flag.')
    parser.add_argument('-w','--print-wordcount', help='Prints word count. Requires -t flag.', action='store_true')
    parser.add_argument('-i','--sentence-inconsistencies', help='Prints sentence inconsistensies. Requires -t flag.', action='store_true')
    parser.add_argument('-a','--run-all-tests', help='Run all tsts on LIEPA dataset.', action='store_true')
    parser.add_argument('-x','--fix-problems', help='Fix LIEPA dataset problems. Overwrite existing files.', action='store_true')

    args = parser.parse_args()

    if args.run_all_tests:
        args.run_transcript_test = True
        args.run_samplerate_test = True
        args.run_naming_test = True
        args.run_structure_test = True
        args.audio_subtype = 'PCM_16'

    result = collect_problems(args.liepa_dir, args)
    encoding_problems, mistype_problems, samplerate_problems, layering_problems, file_naming_problems, directory_naming_problems = result

    if args.print_wordcount:
        stats['word_count'] = list(stats['word_count'].items())
        stats['word_count'] = sorted(stats['word_count'], key=lambda tup: tup[1])

        for w,c in stats['word_count']:
            print (w,c)

    if args.sentence_inconsistencies:
        print ()
        for id, id_dict in stats['sentence_word_positions'].items():
            for position, word_dict in id_dict.items():
                if len(word_dict.keys()) > 1:
                    sorted_items = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
                    print (id, position)
                    for item in sorted_items:
                        print ('\t' + str(item))
                    print ()


    # DO ENCODING CORRECTIONS BEFORE FILE RENAMING OR MOVING
    for path, src_enc, dst_enc, comment in encoding_problems:
        if args.fix_problems:
            fix_encoding_problem(path, src_enc, dst_enc)
        else:
            print ('Change encoding from %s to %s encoding for "%s". %s' % (src_enc, dst_enc, path, comment))

    # DO MISTYPE CORRECTIONS BEFORE FILE RENAMING OR MOVING
    for path, comment in mistype_problems:
        if args.fix_problems:
            fix_mistypes(path)
        else:
            print ('Fix mistypes in "%s".' % path)

    # DO RESAMPLING BEFORE FILE RENAMING OR MOVING
    for path, src_samplerate, dst_samplerate, subtype, comment in samplerate_problems:
        if args.fix_problems:
            fix_sample_rate_problem(path, src_samplerate, dst_samplerate, subtype)
        else:
            print ('Resample "%s" from %d to %d fps. %s' % (path, src_samplerate, dst_samplerate, comment))

    # Layering files and directories
    for src, dst_dir, dst, comment in layering_problems:
        if args.fix_problems:
            fix_layering_problem(dst_dir, src, dst)
        else:
            print ('MKDIR "%s" and MOVE "%s" to "%s". %s' % (dst_dir, src, dst, comment))

    # Rename files
    for src, dst, comment in file_naming_problems:
        if args.fix_problems:
            fix_naming_problem(src, dst)
        else:
            print ('Rename file "%s" to "%s". %s' % (src, dst, comment))

    # Rename directories
    for src, dst, comment in directory_naming_problems:
        if args.fix_problems:
            fix_naming_problem(src, dst)
        else:
            print ('Rename directory "%s" to "%s". %s' % (src, dst, comment))
