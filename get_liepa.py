from os.path import exists
from utils.download_google_drive_file import download_file_from_google_drive
from utils.untar import extract_subfolders, extract_all
from argparse import ArgumentParser
from os import rename

from liepa import all_voices, default_archive_path, default_dir

# Manual download link: https://drive.google.com/open?id=1GSzu9n7I-mUMfaD7jkq_CvwZlZXbz9c7
liepa_dataset_google_drive_archive_id = '1GSzu9n7I-mUMfaD7jkq_CvwZlZXbz9c7'

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
    parser.add_argument('-v','--voices', nargs='+', help='List of voices to unpack (e.g. -s D256 D512).')
    args = parser.parse_args()

    local_liepa_dataset_archive_path = args.archive_path
    local_liepa_dataset_directory = args.liepa_dir

    # Download original LIEPA dataset
    if not exists(local_liepa_dataset_archive_path):
        local_liepa_dataset_archive_tmp_path = local_liepa_dataset_archive_path + ".downloading"
        download_file_from_google_drive(liepa_dataset_google_drive_archive_id, local_liepa_dataset_archive_tmp_path)
        rename(local_liepa_dataset_archive_tmp_path, local_liepa_dataset_archive_path)

    if args.voices:
        extract_specific_voices(local_liepa_dataset_archive_path, local_liepa_dataset_directory, args.voices)
    else:
        extract_all(local_liepa_dataset_archive_path, local_liepa_dataset_directory)
