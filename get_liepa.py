from os.path import exists
from utils.download_google_drive_file import download_file_from_google_drive
from utils.untar import extract_subfolders, extract_all
from argparse import ArgumentParser
from os import rename

from liepa import all_voices, default_rec_dir, default_syn_dir, default_ann_dir

# For manual download us link: https://drive.google.com/open?id=[ID]
liepa_voice_recognition_dataset_file_id = '1GSzu9n7I-mUMfaD7jkq_CvwZlZXbz9c7'
liepa_voice_recognition_dataset_annotation_file_id = '1mrureTyZOlkq0gepwNUcEXQgcKIs9fYS'

liepa_voice_synth_dataset_aiste_file_id = '1nZzvih_op9lYZvVtA8hMhyZE4M7jUv_T'
liepa_voice_synth_dataset_regina_file_id = '1fsjg6iNUlzaVbDG7j3n6hv-7Pk2hMfwK'
liepa_voice_synth_dataset_edvardas_file_id = '19BXuFqfF8z2fK4FUG9lZhljDNit1tUBi'
liepa_voice_synth_dataset_vladas_file_id = '1dwhApCOUX1FZfQj8yp82LKdx-PAcSMGT'

default_rec_archive_path = './MII_LIEPA_REC_v1.tar.bz2'
default_annotation_archive_path = './Annotations.tar.bz2'
default_aiste_archive_path = './MII_LIEPA_SYN_Aiste_v1.tar.bz2'
default_regina_archive_path = './MII_LIEPA_SYN_Regina_v1.tar.bz2'
default_edvardas_archive_path = './MII_LIEPA_SYN_Edvardas_v1.tar.bz2'
default_vladas_archive_path = './MII_LIEPA_SYN_Vladas_v1.tar.bz2'

# Very slow, better extract all
def extract_specific_voices(archive_path, dst_dataset_directory, voices):
    # Verify voice names
    for voice in voices:
        if voice not in all_voices:
            raise Exception('"%s" is not a valid name.')

    # Extract specific voices, very slow
    subfolders = ['%s/' % voice for voice in voices]
    extract_subfolders(archive_path, subfolders, dst_dataset_directory)

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-s','--get-syn-voices', help='Download Aiste Vladas Regina Edvardas audio dataset.',  action='store_true')
    parser.add_argument('-r','--get-rec-voices', help='Download LIEPA recognition dataset.',  action='store_true')
    parser.add_argument('-x','--extract', help='Extract files from archives.',  action='store_true')
    parser.add_argument('-n','--get-annotations', help='Download phoneme, ASCII and UNICODE annotations for recognition dataset.',  action='store_true')
    parser.add_argument('-e','--liepa-rec-dir', help='Directory for LIEPA recognition dataset to unpack to. (default: "%s")' % default_rec_dir, default=default_rec_dir)
    parser.add_argument('-d','--liepa-syn-dir', help='Directory for LIEPA synth dataset to unpack to. (default: "%s")' % default_syn_dir, default=default_syn_dir)
    parser.add_argument('-f','--force', help='Overwrite files if present.',  action='store_true')
    parser.add_argument('-v','--voices', nargs='+', help='List of voices to unpack (e.g. -v D256 D512).')
    args = parser.parse_args()

    local_liepa_rec_dataset_directory = args.liepa_rec_dir
    local_liepa_syn_dataset_directory = args.liepa_syn_dir

    if not args.get_annotations and not args.get_rec_voices:
        args.get_syn_voices = True
        args.extract = True

    def dounload_file(local_archive_path, google_drive_file_id):
        if not exists(local_archive_path) or args.force:
            local_archive_tmp_path = local_archive_path + ".downloading"
            download_file_from_google_drive(google_drive_file_id, local_archive_tmp_path)
            rename(local_archive_tmp_path, local_archive_path)


    if args.get_annotations:
        dounload_file(default_annotation_archive_path, liepa_voice_recognition_dataset_annotation_file_id)

        if args.extract:
            if not exists(default_ann_dir) or args.force:
                extract_all(default_annotation_archive_path, default_ann_dir)

    if args.get_syn_voices:
        dounload_file(default_aiste_archive_path, liepa_voice_synth_dataset_aiste_file_id)
        dounload_file(default_regina_archive_path, liepa_voice_synth_dataset_regina_file_id)
        dounload_file(default_edvardas_archive_path, liepa_voice_synth_dataset_edvardas_file_id)
        dounload_file(default_vladas_archive_path, liepa_voice_synth_dataset_vladas_file_id)

        if args.extract:
            if not exists(default_syn_dir) or args.force:
                extract_all(default_aiste_archive_path, default_syn_dir)
                extract_all(default_regina_archive_path, default_syn_dir)
                extract_all(default_edvardas_archive_path, default_syn_dir)
                extract_all(default_vladas_archive_path, default_syn_dir)

    if args.get_rec_voices:
        dounload_file(default_rec_archive_path, liepa_voice_recognition_dataset_file_id)

        if not exists(local_liepa_rec_dataset_directory) or args.force:
            if args.extract and args.voices:
                extract_specific_voices(default_rec_archive_path, local_liepa_rec_dataset_directory, args.voices)
            else:
                extract_all(default_rec_archive_path, local_liepa_rec_dataset_directory)
