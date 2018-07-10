from os import walk
from os.path import join, splitext, split, normpath, exists
from re import sub, search
from argparse import ArgumentParser
import operator

from liepa import default_rec_dir, default_wav_samplerate, default_wav_subtype, filname_pattern
from liepa import valid_lt_symbols, valid_lt2ascii_symbols, valid_ascii_symbols, valid_symbols, valid_mapped_symbols
from liepa import txt_extensions, wav_extensions
from utils.text import silence_indicators, noise_indicators
from utils.audio import wav_duration

stats = {
    'word_count': {},
    'sentence_word_positions': {},
    'utterance_wordcount': {}
}

def collect_text_stats(file_path, voice, group, utterance_id, utterance_sub_id, gender, age_group):
    text = None

    with open(file_path, 'r') as f:
        text = f.read().strip()

    text_length = len(text)

    words = text.lower().split()

    if args.print_wordcount:
        for w in words:
            if w not in stats['word_count']:
                stats['word_count'][w] = 0
            stats['word_count'][w] += 1

    if args.utterance_stats:
        if 'voice' not in stats['utterance_wordcount']:
            stats['utterance_wordcount']['voice'] = {}
            stats['utterance_wordcount']['group'] = {}
            stats['utterance_wordcount']['utterance'] = {}

        if voice not in stats['utterance_wordcount']['voice']:
            stats['utterance_wordcount']['voice'][voice] = {'words': 0, 'silence_indicators': 0, 'noise_indicators':0, 'max_len':0, 'min_len':99999, 'total_len':0, 'count':0, 'words_clean': 0, 'max_len_clean':0, 'min_len_clean':99999, 'total_len_clean':0, 'count_clean':0, 'age_group':age_group, 'gender':gender}

        stats['utterance_wordcount']['voice'][voice]['count'] +=1
        stats['utterance_wordcount']['voice'][voice]['total_len'] +=text_length
        stats['utterance_wordcount']['voice'][voice]['max_len'] = max(stats['utterance_wordcount']['voice'][voice]['max_len'], text_length)
        stats['utterance_wordcount']['voice'][voice]['min_len'] = min(stats['utterance_wordcount']['voice'][voice]['min_len'], text_length)

        has_silence_indicator = False
        has_noise_indicator = False
        word_count = 0
        for w in words:
            if w in silence_indicators:
                stats['utterance_wordcount']['voice'][voice]['silence_indicators'] += 1
                has_silence_indicator = True
            elif w in noise_indicators:
                stats['utterance_wordcount']['voice'][voice]['noise_indicators'] += 1
                has_noise_indicator = True
            else:
                word_count += 1
        stats['utterance_wordcount']['voice'][voice]['words'] += word_count

        has_indicator = has_silence_indicator or has_noise_indicator
        if not has_silence_indicator or group[0] != 'Z':
            stats['utterance_wordcount']['voice'][voice]['words_clean'] += word_count

            stats['utterance_wordcount']['voice'][voice]['count_clean'] +=1

            stats['utterance_wordcount']['voice'][voice]['total_len_clean'] +=text_length

            stats['utterance_wordcount']['voice'][voice]['max_len_clean'] = max(stats['utterance_wordcount']['voice'][voice]['max_len_clean'], text_length)

            stats['utterance_wordcount']['voice'][voice]['min_len_clean'] = min(stats['utterance_wordcount']['voice'][voice]['min_len_clean'], text_length)


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
                    collect_text_stats(file_path, voice, group, utterance_id, utterance_sub_id, gender, age_group)

if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-d','--liepa-dir', help='LIEPA dataset directory (Default: "%s").' % default_rec_dir, default=default_rec_dir)
    parser.add_argument('-w','--print-wordcount', help='Prints word count. Requires -t flag.', action='store_true')
    parser.add_argument('-i','--sentence-inconsistencies', help='Prints sentence inconsistensies. Requires -t flag.', action='store_true')
    parser.add_argument('-u','--utterance-stats', help='Word stats per voice, group.', action='store_true')
    parser.add_argument('-a','--run-all-stats', help='Run all stats on LIEPA dataset.', action='store_true')

    args = parser.parse_args()

    if args.run_all_stats:
        args.print_wordcount = True
        args.sentence_inconsistencies = True
        args.utterance_stats = True

    collect_stats(args.liepa_dir, args)

    if args.print_wordcount:
        stats['word_count'] = list(stats['word_count'].items())
        stats['word_count'] = sorted(stats['word_count'], key=lambda tup: tup[1])

        for w,c in stats['word_count']:
            print (w,c)

    if args.utterance_stats:

        def calc_score(voice_stats):
            return voice_stats['words'] / (voice_stats['words'] + voice_stats['silence_indicators'] + voice_stats['noise_indicators'])

        stats_utterance_wordcount_voice = list(stats['utterance_wordcount']['voice'].items())
        stats_utterance_wordcount_voice = sorted(stats_utterance_wordcount_voice, key=lambda voice: calc_score(voice[1]), reverse=True)

        for voice, voice_stats in stats_utterance_wordcount_voice:
            score = calc_score(voice_stats)

            age_group, gender = voice_stats['age_group'], voice_stats['gender']
            words, silence_indicators, noise_indicators =  voice_stats['words'], voice_stats['silence_indicators'], voice_stats['noise_indicators']

            max_len, min_len = voice_stats['max_len'], voice_stats['min_len']
            count = voice_stats['count']
            avg_len = voice_stats['total_len'] / count

            max_len_clean, min_len_clean = voice_stats['max_len_clean'], voice_stats['min_len_clean']
            words_clean = voice_stats['words_clean']
            count_clean = voice_stats['count_clean']
            if count_clean > 0:
                avg_len_clean = voice_stats['total_len_clean'] / count_clean
            else:
                avg_len_clean = 0

            if voice_stats['words'] > 1000 and gender == 'M' and age_group in 'klm':
                print (voice, age_group, gender, score, words, silence_indicators, noise_indicators, count, max_len, min_len, avg_len, words_clean, count_clean, max_len_clean, min_len_clean, avg_len_clean)

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
