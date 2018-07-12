from os import walk, makedirs, rename
from os.path import join, splitext, split, normpath, abspath, exists
from re import sub, search
from argparse import ArgumentParser
import codecs
import chardet
import operator

from liepa import default_syn_dir, default_wav_samplerate, default_wav_subtype, syn_filname_pattern
from liepa import valid_lt_symbols, valid_lt2ascii_symbols, valid_ascii_symbols, valid_symbols, valid_mapped_symbols
from liepa import txt_extensions, wav_extensions
from liepa import syn_dataset_voices
from utils.audio import resample, wav_duration
from utils.text import regex_replacements, silence_indicators, noise_indicators

valid_ascii_symbols = set(valid_ascii_symbols.encode('ascii'))
valid_utf8_symbol_set = set(valid_symbols.encode('utf-8'))
valid_utf16_symbol_set = set(valid_symbols.encode('utf-16'))
valid_utf8_sig_symbol_set = set(valid_symbols.encode('UTF-8-SIG'))
valid_windows_1257_symbols_set = set(valid_symbols.encode('windows-1257') + b'\x9a')

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

def fix_multiline(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    
    text = ' '.join(text.split())

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

def collect_text_problems(file_path, utterance_id):
    encoding_problem = []
    multiline_problem = []

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

        text = raw_text.decode(charenc).lower()

        text_set = set(text)
        diff_set = text_set - set(valid_symbols)

        if len(diff_set) > 0:
            raise Exception(','.join(diff_set))

        if charenc != 'utf-8':
            problem = '"%s" has %s encoding but utf-8 is required.' % (file_path, charenc)
            encoding_problem = [(file_path, charenc, 'utf-8', problem)]
    except Exception as e:
        encoding_problem = [(file_path, 'utf-8', str(e))]
        raise Exception(encoding_problem)

    if text_set & set('\r\n'):
        problem = '"%s" has special line chars.' % file_path
        multiline_problem = [(file_path, problem)]

    return encoding_problem, multiline_problem

def validate_static_value(static_name, voice, static, test):
    if not test:
        raise Exception('%s can not be %s for speaker "%s".' % (static_name, test, voice))
    elif static and static != test:
        raise Exception('%s "%s" for speaker "%s" does not match prvious "%s".' % (static_name, test, voice, static))

    return test

def collect_problems(dataset_path, args):
    encoding_problems = []
    multiline_problems = []
    samplerate_problems = []
    data_found = False

    dataset_path = normpath(abspath(dataset_path))
    if not exists(dataset_path):
        raise Exception()

    for root, _, files in walk(dataset_path):
        age_group = None
        gender = None

        root = normpath(root)
        path, leaf = split(root)
        if path == '':
            continue

        dir_group = leaf
        if dir_group != 'data':
            continue

        _, voice = split(path)

        if voice not in syn_dataset_voices:
            raise Exception('Voice name "%s" must be one of {}.' % syn_dataset_voices)

        for filename in files:
            match = syn_filname_pattern.match(filename)
            if not match:
                raise Exception('Filename "%s" does not match valid pattern.' % filename)
            else:
                data_found= True
                _, _extension = splitext(filename)

                file_path = join(path, 'data', filename)

                if _extension in wav_extensions and args.run_samplerate_test:
                    samplerate_problems += collect_samplerate_problems(file_path, args.audio_subtype)

                utterance_id = match.group('ut_id')

                if _extension in txt_extensions and args.run_transcript_test:
                    encoding_problem, multiline_problem = collect_text_problems(file_path, utterance_id)
                    encoding_problems += encoding_problem
                    multiline_problems += multiline_problem
    
    if not data_found:
        raise Exception()

    return (
        encoding_problems,
        multiline_problems,
        samplerate_problems)

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-d','--liepa-dir', help='LIEPA synthesize dataset directory (Default: "%s").' % default_syn_dir, default=default_syn_dir)
    parser.add_argument('-t','--run-transcript-test', help='LIEPA dataset transcript encoding and mistype testing.', action='store_true')
    parser.add_argument('-r','--run-samplerate-test', help='LIEPA dataset audio samplerate testing.', action='store_true')
    parser.add_argument('-s','--audio-subtype', choices=['PCM_16','PCM_24','PCM_32'], help='Set audio subtype. Requires -r flag.')
    parser.add_argument('-a','--run-all-tests', help='Run all tsts on LIEPA dataset.', action='store_true')
    parser.add_argument('-x','--fix-problems', help='Fix LIEPA dataset problems. Overwrite existing files.', action='store_true')

    args = parser.parse_args()

    if args.run_all_tests:
        args.run_transcript_test = True
        args.run_samplerate_test = True
        args.audio_subtype = 'PCM_16'

    result = collect_problems(args.liepa_dir, args)
    encoding_problems, multiline_problems, samplerate_problems = result

    for path, src_enc, dst_enc, comment in encoding_problems:
        if args.fix_problems:
            fix_encoding_problem(path, src_enc, dst_enc)
        else:
            print ('Change encoding from %s to %s encoding for "%s". %s' % (src_enc, dst_enc, path, comment))

    for path, comment in multiline_problems:
        if args.fix_problems:
            fix_multiline(path)
        else:
            print ('Fix multiline problem for %s. %s' % (path, comment))

    for path, src_samplerate, dst_samplerate, subtype, comment in samplerate_problems:
        if args.fix_problems:
            fix_sample_rate_problem(path, src_samplerate, dst_samplerate, subtype)
        else:
            print ('Resample "%s" from %d to %d fps. %s' % (path, src_samplerate, dst_samplerate, comment))
