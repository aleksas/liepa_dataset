from os.path import exists
from utils.download_google_drive_file import download_file_from_google_drive
from utils.untar import extract_subfolders, extract_all
from argparse import ArgumentParser
from os import rename

from liepa import all_voices, default_archive_path, default_annotation_archive_path, default_dir, default_aiste_archive_path, default_regina_archive_path, default_edvardas_archive_path, default_vladas_archive_path

# For manual download us link: https://drive.google.com/open?id=[ID]
liepa_voice_recognition_dataset_file_id = '1GSzu9n7I-mUMfaD7jkq_CvwZlZXbz9c7'
liepa_voice_recognition_dataset_annotation_file_id = '1mrureTyZOlkq0gepwNUcEXQgcKIs9fYS'

liepa_voice_synth_dataset_aiste_file_id = '1-jLn-uhd8EEDbk7slU7FRr5OO4DVWrzT'
liepa_voice_synth_dataset_regina_file_id = '1mm_h7ixkEgzWuZLjQCBmmmi8LM1mI3-x'
liepa_voice_synth_dataset_edvardas_file_id = '16FbJBL5qz0ySph5YuIC7wviEAnwDjOuG'
liepa_voice_synth_dataset_vladas_file_id = '1FdcKSJm5RkxBDwXVUPXYz_IIqlawPa-7'

# Very slow, better extract all
def extract_specific_voices(local_liepa_dataset_archive_path, local_liepa_dataset_directory, voices):
    # Verify voice names
    for voice in voices:
        if voice not in all_voices:
            raise Exception('"%s" is not a valid name.')

    # Extract specific voices, very slow
    subfolders = ['%s/' % voice for voice in voices]
    extract_subfolders(local_liepa_dataset_archive_path, subfolders, local_liepa_dataset_directory)

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-p','--archive-path', help='Path to download LIEPA dataset archive to. (Default: "%s")' % default_archive_path, default=default_archive_path)
    parser.add_argument('-d','--liepa-dir', help='Directory for LIEPA dataset to unpack to. (default: "%s")' % default_dir, default=default_dir)
    parser.add_argument('-n','--get-annotations', help='Download phoneme, ASCII and UNICODE annotations.',  action='store_true')
    parser.add_argument('-s','--get-synth-voices', help='Download Aiste Vladas Regina Edvardas audio dataset.',  action='store_true')
    parser.add_argument('-f','--force', help='Overwrite files if present.',  action='store_true')
    parser.add_argument('-v','--voices', nargs='+', help='List of voices to unpack (e.g. -v D256 D512).')
    args = parser.parse_args()

    local_liepa_dataset_archive_path = args.archive_path
    local_liepa_dataset_directory = args.liepa_dir
    
    def dounload_file(local_archive_path, google_drive_file_id):
        if not exists(local_archive_path) or args.force:
            local_archive_tmp_path = local_archive_path + ".downloading"
            download_file_from_google_drive(google_drive_file_id, local_archive_tmp_path)
            rename(local_archive_tmp_path, local_archive_path)


    if args.get_annotations:
        dounload_file(default_annotation_archive_path, liepa_voice_recognition_dataset_annotation_file_id)

    if args.get_synth_voices:
        dounload_file(default_aiste_archive_path, liepa_voice_synth_dataset_aiste_file_id)
        dounload_file(default_regina_archive_path, liepa_voice_synth_dataset_regina_file_id)
        dounload_file(default_edvardas_archive_path, liepa_voice_synth_dataset_edvardas_file_id)
        dounload_file(default_vladas_archive_path, liepa_voice_synth_dataset_vladas_file_id)

    # Download original LIEPA dataset
    dounload_file(local_liepa_dataset_archive_path, liepa_voice_recognition_dataset_file_id)
	
    if not exists(local_liepa_dataset_directory) or args.force:
        if args.voices:
            extract_specific_voices(local_liepa_dataset_archive_path, local_liepa_dataset_directory, args.voices)
        else:
            extract_all(local_liepa_dataset_archive_path, local_liepa_dataset_directory)
