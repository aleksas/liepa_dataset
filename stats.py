from os import walk
from os.path import join, splitext, split, normpath, exists
from re import sub, search
from argparse import ArgumentParser
import operator

from liepa import default_dir, default_wav_samplerate, default_wav_subtype, filname_pattern
from liepa import valid_lt_symbols, valid_lt2ascii_symbols, valid_ascii_symbols, valid_symbols, valid_mapped_symbols
from liepa import txt_extensions, wav_extensions
from utils.text import silence_indicators, noise_indicators
from utils.audio import wav_duration

stats = {
    'word_count': {},
    'sentence_word_positions': {}
}

def collect_text_stats(file_path, group, utterance_id, utterance_sub_id):
    encoding_problem = []
    mistype_problem = []

    text = None

    with open(file_path, 'r') as f:
        text = f.read()

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

def collect_stats(dataset_path, args):
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

        for filename in files:
            match = filname_pattern.match(filename)
            if not match:
                raise Exception('Filename "%s" does not match valid pattern.' % filename)
            else:
                name, _extension = splitext(filename)

                group = dir_group
                file_path = join(path, group, filename)

                tag = match.group('tag') # _T or _P

                utterance_sub_id = match.group('ut_subid')
                if not utterance_sub_id:
                    utterance_sub_id = ''

                gender =  match.group('sex')
                age_group = match.group('age')
                utterance_id = match.group('ut_id')

                if _extension in txt_extensions:
                    collect_text_stats(file_path, group, utterance_id, utterance_sub_id)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-d','--liepa-dir', help='LIEPA dataset directory (Default: "%s").' % default_dir, default=default_dir)
    parser.add_argument('-w','--print-wordcount', help='Prints word count. Requires -t flag.', action='store_true')
    parser.add_argument('-i','--sentence-inconsistencies', help='Prints sentence inconsistensies. Requires -t flag.', action='store_true')
    parser.add_argument('-a','--run-all-stats', help='Run all stats on LIEPA dataset.', action='store_true')

    args = parser.parse_args()

    if args.run_all_stats:
        args.print_wordcount = True
        args.sentence_inconsistencies = True

    collect_stats(args.liepa_dir, args)

    if args.print_wordcount:
        stats['word_count'] = list(stats['word_count'].items())
        stats['word_count'] = sorted(stats['word_count'], key=lambda tup: tup[1])

        for w,c in stats['word_count']:
            print (w,c)

    if args.sentence_inconsistencies:
        for id, id_dict in stats['sentence_word_positions'].items():
            for position, word_dict in id_dict.items():
                if len(word_dict.keys()) > 1:
                    sorted_items = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
                    base = sorted_items[0][0]
                    base_mapped = ''.join([valid_mapped_symbols[valid_symbols.index(l)] for l in base])
                    info = [sorted_items[0]]
                    for i in range(1, len(sorted_items)):
                        item_mapped = ''.join([valid_mapped_symbols[valid_symbols.index(l)] for l in sorted_items[i][0]])
                        a_part_of_b = item_mapped in base_mapped
                        b_part_of_a = base_mapped in item_mapped
                        a_ratio_to_b = len(set(base_mapped) - set(item_mapped)) / len(set(base_mapped))
                        b_ratio_to_a = len(set(item_mapped) - set(base_mapped)) / len(set(item_mapped))
                        a_to_b_len_ratio = len(base_mapped) / len(item_mapped)
                        b_to_a_len_ratio = len(item_mapped) / len(base_mapped)

                        t_factor = 2
                        if len(set(base_mapped)) <= 3:
                            t_factor =  1
                        threshold = 1/len(set(base_mapped)) * t_factor # two letters
                        good_ratio_a = a_ratio_to_b <= threshold and a_to_b_len_ratio > 0.75
                        good_ratio_b = b_ratio_to_a <= threshold and b_to_a_len_ratio > 0.75
                        good = good_ratio_a or good_ratio_b
                        if good:
                            info.append(sorted_items[i])

                    if len(info) > 1:
                        print(id, position, info)
