from os import walk
from os.path import join, splitext, split, normpath
from re import compile
import wave
import contextlib

txt_extensions = ['.txt', '.TXT']
wav_extensions = ['.wav', '.WAV']

default_wav_framerate = 22050

age_groups = {
    'c', (12, 12),
    'd', (13, 13),
    'e', (14, 14),
    'f', (15, 15),
    'g', (16, 16),
    'h', (17, 17),
    'i', (18, 18),
    'j', (19, 19),
    'k', (20, 20),
    'l', (21, 25),
    'm', (26, 30),
    'n', (31, 40),
    'o', (41, 50),
    'p', (51, 60),
    'r', (61, -1)  # over 61
    }

valid_utf8_symbols = u'AĄBCČDEĘĖFGHIĮJKLMNOPQRSŠTUŲŪVWXYZŽaąbcčdeęėfghiįjklmnopqrsštuųūvwxyzž!\'(),-.:;? _'
valid_utf8_symbol_set = set(valid_utf8_symbols)

pattern = compile(r'(ZS?|SS?)?(\d+)(M|V)([a-r])_(\d+[abc]?)(_(\d+[abc]?))?(_[TP])?(\.(wav|txt))')

# Some files have incorrect utterance type indicator, parent directories indicate correctly.
known_utterance_type_naming_exceptions = [
    ('D57', 'S007'), ('D57', 'S008'),
    ('D556', 'S013'), ('D556', 'S014'),
    ('D556', 'Z000'), ('D556', 'Z001'),
    ('D556', 'Z020'), ('D556', 'Z060')
    ]

known_voice_directory_file_naming_exceptions = range(2, 100)

known_voice_naming_exceptions = [('D251', 'Z026'), ('D515', 'S012'), ('D515', 'Z000'), ('D516', 'S012')]

def wav_duration(path):
    with contextlib.closing(wave.open(path,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        return (frames / float(rate)), frames, rate

def collect_audio_sampling_problems(file_path):
    duration, frames, framerate = wav_duration(file_path)

    _, filename = split(file_path)

    if default_wav_framerate != framerate:
        problem = '"%s" has %d framerate, default is %d.' % (filename, framerate, default_wav_framerate)
        return [(file_path, framerate, default_wav_framerate, problem)]

    return []

def collect_encoding_problems(file_path):
    text = None
    try:
        with open(file_path) as fin:
            text = fin.read()

        text_char_set = set(text)
        diff_set = text_char_set - valid_utf8_symbol_set

        if len(diff_set) > 0:
            problem = '"%s" contains invalid symbols.' % file_path
            return [(file_path, problem)]
    except Exception as e:
        return [(file_path, str(e))]
    return []

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

def cleanup_sampling_problems(sampling_problems):
    clean_sampling_problems = []

    for path, src_framerate, dst_framerate, comment in sampling_problems:
        duplicate = False
        for path_, src_framerate_, dst_framerate_, _ in clean_sampling_problems:
            if path == path_:
                if src_framerate == src_framerate_ and dst_framerate == dst_framerate_:
                    duplicate = True
                else:
                    raise Exception('Sampling problems have multiple solutions: %s, %s.' % (path, path_))
        if not duplicate:
            clean_sampling_problems.append((path, src_framerate, dst_framerate, comment))

    return clean_sampling_problems

def cleanup_encoding_problems(encoding_problems):
    clean_encoding_problems = []

    for path, comment in encoding_problems:
        duplicate = False
        for path_, _ in clean_encoding_problems:
            if path == path_:
                duplicate = True
        if not duplicate:
            clean_encoding_problems.append((path, comment))

    return clean_encoding_problems

def validate_static_value(static_name, voice, static, test):
    if not static:
        return test
    elif static != test:
        raise Exception('%s "%s" for speaker "%s" does not match prvious "%s".' % (static_name, test, voice, gender))

def collect_problems(dataset_path='./'):
    encoding_problems = []
    sampling_problems = []
    naming_problems = []

    for root, subdirs, files in walk(dataset_path):
        age_group = None
        gender = None

        root = normpath(root)
        path, leaf = split(root)
        if path == '':
            continue

        if leaf[0] in ['D', '.']:
            continue

        group = leaf

        db_root, voice = split(path)
        utternace_group_type = group[0]

        if utternace_group_type not in ['Z', 'S']:
            raise Exception('Utternace type "%s" does not match valid pattern.' % utternace_group_type)

        if voice[0] != 'D':
            raise Exception('Voice name "%s" does not start with "D".' % voice[0])

        voice_id = voice[1:]
        correct_voice_id  = '%03d' % int(voice_id)
        if voice_id != correct_voice_id:
            problem = 'Voice id is "%s" but should be "%s".' % (voice_id, correct_voice_id)
            if int(voice_id) not in known_voice_directory_file_naming_exceptions:
                raise Exception(problem)
            else:
                correct_voice_path = join(db_root, 'D' + correct_voice_id)
                naming_problems.append((path, correct_voice_path, problem))

        for filename in files:
            file_path = join(root, filename)
            name, _extension = splitext(filename)
            full_path = join(root, filename)

            if _extension in wav_extensions:
                sampling_problems += collect_audio_sampling_problems(full_path)

            if _extension in txt_extensions:
                encoding_problems += collect_encoding_problems(full_path)

            match = pattern.match(filename)
            if not match:
                raise Exception('Filename "%s" does not match valid pattern.' % filename)
            else:
                tag = match.group(8) # _T or _P
                if not tag:
                    tag = ''

                utterance_sub_id = match.group(6)
                if not utterance_sub_id:
                    utterance_sub_id = ''

                gender = validate_static_value('Gender', voice, gender, match.group(3))
                age_group = validate_static_value('Age group', voice, age_group, match.group(4))

                utternace_id = match.group(5)

                correct_filename = '%s%s%s%s_%s%s%s%s' % (utternace_group_type, correct_voice_id, gender, match.group(4), utternace_id, utterance_sub_id, tag, match.group(9))
                correct_full_path = join(root, correct_filename)

                if voice_id != match.group(2):
                    problem = 'Voice id "%s" does not match with id "%s" from filename "%s".' % (voice_id, match.group(2), full_path)
                    can_continue = False
                    for exc in  known_voice_naming_exceptions:
                        if voice == exc[0] and group == exc[1]:
                            can_continue = True
                            naming_problems.append((full_path, correct_full_path, problem))

                    if not can_continue and int(voice_id) not in known_voice_directory_file_naming_exceptions:
                        raise Exception(problem)

                if match.group(1) != utternace_group_type:
                    problem = 'Utterance group "%s" for "%s" voice is of type "%s", but utterance "%s" is of type "%s". Path: "%s".' % (group, voice, utternace_group_type, filename, match.group(1), root)
                    can_continue = False
                    for exc in known_utterance_type_naming_exceptions:
                        if voice == exc[0] and group == exc[1]:
                            can_continue = True
                            naming_problems.append((full_path, correct_full_path, problem))

                    if not can_continue:
                        raise Exception(problem)

    return cleanup_encoding_problems(encoding_problems), cleanup_sampling_problems(sampling_problems), cleanup_naming_problems(naming_problems)

if __name__ == '__main__':
    encoding_problems, sampling_problems, naming_problems = collect_problems('./Garsynas')

    # DO ENCODING CORRECTIONS BEFORE FILE RENAMING
    for path, comment in encoding_problems:
        print ('Correct encoding for "%s". %s' % (path, comment))

    # DO RESAMPLING BEFORE FILE RENAMING
    for path, src_framerate, dst_framerate, comment in sampling_problems:
        print ('Resample "%s" from %d to %d fps. %s' % (path, src_framerate, dst_framerate, comment))

    # Rename files
    for src, dst, comment in naming_problems:
        print ('Rename "%s" to "%s". %s' % (src, dst, comment))
