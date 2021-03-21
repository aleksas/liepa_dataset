from os.path import exists
from utils.download_google_drive_file import download_file_from_google_drive
from utils.download import download
from utils.untar import extract_all
from argparse import ArgumentParser
from os import rename

from liepa import default_rec_dir, default_syn_dir, default_ann_dir

# For manual download us link: https://drive.google.com/open?id=[ID]
#liepa_voice_recognition_dataset_file_id = '1GSzu9n7I-mUMfaD7jkq_CvwZlZXbz9c7'
#liepa_voice_recognition_dataset_annotation_file_id = '1mrureTyZOlkq0gepwNUcEXQgcKIs9fYS'

liepa_voice_recognition_dataset_file_part1_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/MII_LIEPA_V1_PART1.tar.bz2'
liepa_voice_recognition_dataset_file_part2_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/MII_LIEPA_V1_PART2.tar.bz2'
liepa_voice_recognition_dataset_file_part3_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/MII_LIEPA_V1_PART3.tar.bz2'
liepa_voice_recognition_dataset_file_part4_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/MII_LIEPA_V1_PART4.tar.bz2'
liepa_voice_recognition_dataset_file_part5_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/MII_LIEPA_V1_PART5.tar.bz2'
liepa_voice_recognition_dataset_file_part6_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/MII_LIEPA_V1_PART6.tar.bz2'
liepa_voice_recognition_dataset_annotation_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/anotacijos.tar.bz2'

#liepa_voice_synth_dataset_aiste_file_id = '1nxyQAfl-vbnoSLT6cltjUD-PLBgAT3EJ'
#liepa_voice_synth_dataset_regina_file_id = '1iG1I7z4yRw2wkycstSQIjz0kNQ9pRdVn'
#liepa_voice_synth_dataset_edvardas_file_id = '1Vf9MZMH958RPt9vCgxG0b_USNSDAhMzN'
#liepa_voice_synth_dataset_vladas_file_id = '1s9U1S8NSqg4_wT3UP9qGGzJ9Ki7ie_Yq'

liepa_voice_synth_dataset_aiste_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Aiste.tar.bz2'
liepa_voice_synth_dataset_regina_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Regina.tar.bz2'
liepa_voice_synth_dataset_edvardas_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Edvardas.tar.bz2'
liepa_voice_synth_dataset_vladas_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Vladas.tar.bz2'

default_rec_archive_part1_path = './MII_LIEPA_V1_PART1.tar.bz2'
default_rec_archive_part2_path = './MII_LIEPA_V1_PART2.tar.bz2'
default_rec_archive_part3_path = './MII_LIEPA_V1_PART3.tar.bz2'
default_rec_archive_part4_path = './MII_LIEPA_V1_PART4.tar.bz2'
default_rec_archive_part5_path = './MII_LIEPA_V1_PART5.tar.bz2'
default_rec_archive_part6_path = './MII_LIEPA_V1_PART6.tar.bz2'
default_annotation_archive_path = './Annotations.tar.bz2'
default_aiste_archive_path = './MII_LIEPA_SYN_Aiste_v1.tar.bz2'
default_regina_archive_path = './MII_LIEPA_SYN_Regina_v1.tar.bz2'
default_edvardas_archive_path = './MII_LIEPA_SYN_Edvardas_v1.tar.bz2'
default_vladas_archive_path = './MII_LIEPA_SYN_Vladas_v1.tar.bz2'

#liepa_voice_synth_aiste_wav_file_id = '1myOg7BKRrisbMXiS1u_LniElVSLThKc2'
#liepa_voice_synth_regina_wav_file_id = '16KviJdnB6vmIPxcMhun5u0puECzEEcfP'
#liepa_voice_synth_edvardas_wav_file_id = '1_Pw2DroFKmRWq8q59DfknCzikAFVEJfq'
#liepa_voice_synth_vladas_wav_file_id = '1AaWtUlx0cL0e2KeonN1zhKBsPmMOptuC'

liepa_voice_synth_aiste_wav_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Aiste.wav'
liepa_voice_synth_regina_wav_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Regina.wav'
liepa_voice_synth_edvardas_wav_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Edvardas.wav'
liepa_voice_synth_vladas_wav_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Vladas.wav'

aiste_wav_path = './Aiste.wav'
regina_wav_path = './Regina.wav'
edvardas_wav_path = './Edvardas.wav'
vladas_wav_path = './Vladas.wav'

#liepa_voice_synth_aiste_mp3_file_id = '1OAHpTQqA6fRyq9EJeVrHF5Syxr1RO7_b'
#liepa_voice_synth_regina_mp3_file_id = '1o2pmQwSHJpR1ZA7VIfBGwJfHqN4SBEBv'
#liepa_voice_synth_edvardas_mp3_file_id = '12bVW8n9JgT9OMdmWrqs4o7a9C32rPmdA'
#liepa_voice_synth_vladas_mp3_file_id = '1VAyhUUgvOq-UXoOIowCUdu0AhRV-FnPy'

liepa_voice_synth_aiste_mp3_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Aiste.mp3'
liepa_voice_synth_regina_mp3_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Regina.mp3'
liepa_voice_synth_edvardas_mp3_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Edvardas.mp3'
liepa_voice_synth_vladas_mp3_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Vladas.mp3'

aiste_mp3_path = './Aiste.mp3'
regina_mp3_path = './Regina.mp3'
edvardas_mp3_path = './Edvardas.mp3'
vladas_mp3_path = './Vladas.mp3'

#liepa_voice_synth_aiste_m4a_file_id = '17bCNRPC4qCpNasFoyop3GLf8o8Ejc60Z'
#liepa_voice_synth_regina_m4a_file_id = '1UO9_7eGzis0-dTCWgB5dJccVAdWpD87F'
#liepa_voice_synth_edvardas_m4a_file_id = '1fEuXE9oLyrCGHMIVQhjh0HUyBaOcqAsh'
#liepa_voice_synth_vladas_m4a_file_id = '1E2kO0hipO7LRcBulCfaGvWJ_yv6LP7V5'

liepa_voice_synth_aiste_m4a_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Aiste.m4a'
liepa_voice_synth_regina_m4a_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Regina.m4a'
liepa_voice_synth_edvardas_m4a_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Edvardas.m4a'
liepa_voice_synth_vladas_m4a_file_url = 'https://github.com/aleksas/liepa_dataset/releases/download/data/Vladas.m4a'


aiste_m4a_path = './Aiste.m4a'
regina_m4a_path = './Regina.m4a'
edvardas_m4a_path = './Edvardas.m4a'
vladas_m4a_path = './Vladas.m4a'

if __name__ == '__main__':

    parser = ArgumentParser()
    parser.add_argument('-s','--get-syn-voices', help='Download Aiste Vladas Regina Edvardas audio dataset.',  action='store_true')
    parser.add_argument('-r','--get-rec-voices', help='Download LIEPA recognition dataset.',  action='store_true')
    parser.add_argument('-x','--extract', help='Extract files from archives.',  action='store_true')
    parser.add_argument('-n','--get-annotations', help='Download phoneme, ASCII and UNICODE annotations for recognition dataset.',  action='store_true')
    parser.add_argument('-e','--liepa-rec-dir', help='Directory for LIEPA recognition dataset to unpack to. (default: "%s")' % default_rec_dir, default=default_rec_dir)
    parser.add_argument('-d','--liepa-syn-dir', help='Directory for LIEPA synth dataset to unpack to. (default: "%s")' % default_syn_dir, default=default_syn_dir)
    parser.add_argument('-f','--force', help='Overwrite files if present.',  action='store_true')
    args = parser.parse_args()

    local_liepa_rec_dataset_directory = args.liepa_rec_dir
    local_liepa_syn_dataset_directory = args.liepa_syn_dir

    if not args.get_annotations and not args.get_rec_voices:
        args.get_syn_voices = True
        args.extract = True

    def download_google_file(local_archive_path, google_drive_file_id):
        if not exists(local_archive_path) or args.force:
            print(f'Downloading {local_archive_path}...')
            local_archive_tmp_path = local_archive_path + ".downloading"
            download_file_from_google_drive(google_drive_file_id, local_archive_tmp_path)
            print(f'Downloaded {local_archive_path}')
            rename(local_archive_tmp_path, local_archive_path)

    def download_file(local_archive_path, url):
        if not exists(local_archive_path) or args.force:
            print(f'Downloading {local_archive_path}...')
            local_archive_tmp_path = local_archive_path + ".downloading"
            download(url, local_archive_tmp_path)
            print(f'Downloaded {local_archive_path}')
            rename(local_archive_tmp_path, local_archive_path)

    if args.get_annotations:
        download(default_annotation_archive_path, liepa_voice_recognition_dataset_annotation_file_url)

        if args.extract:
            if not exists(default_ann_dir) or args.force:
                extract_all(default_annotation_archive_path, default_ann_dir)

    if args.get_syn_voices:
        download_file(default_aiste_archive_path, liepa_voice_synth_dataset_aiste_file_url)
        download_file(default_regina_archive_path, liepa_voice_synth_dataset_regina_file_url)
        download_file(default_edvardas_archive_path, liepa_voice_synth_dataset_edvardas_file_url)
        download_file(default_vladas_archive_path, liepa_voice_synth_dataset_vladas_file_url)
        
        download_file(aiste_wav_path, liepa_voice_synth_aiste_wav_file_url)
        download_file(regina_wav_path, liepa_voice_synth_regina_wav_file_url)
        download_file(edvardas_wav_path, liepa_voice_synth_edvardas_wav_file_url)
        download_file(vladas_wav_path, liepa_voice_synth_vladas_wav_file_url)
        
        download_file(aiste_mp3_path, liepa_voice_synth_aiste_mp3_file_url)
        download_file(regina_mp3_path, liepa_voice_synth_regina_mp3_file_url)
        download_file(edvardas_mp3_path, liepa_voice_synth_edvardas_mp3_file_url)
        download_file(vladas_mp3_path, liepa_voice_synth_vladas_mp3_file_url)
        
        download_file(aiste_m4a_path, liepa_voice_synth_aiste_m4a_file_url)
        download_file(regina_m4a_path, liepa_voice_synth_regina_m4a_file_url)
        download_file(edvardas_m4a_path, liepa_voice_synth_edvardas_m4a_file_url)
        download_file(vladas_m4a_path, liepa_voice_synth_vladas_m4a_file_url)

        if args.extract:
            if not exists(default_syn_dir) or args.force:
                extract_all(default_aiste_archive_path, default_syn_dir)
                extract_all(default_regina_archive_path, default_syn_dir)
                extract_all(default_edvardas_archive_path, default_syn_dir)
                extract_all(default_vladas_archive_path, default_syn_dir)

    if args.get_rec_voices:
        download_file(default_rec_archive_part1_path, liepa_voice_recognition_dataset_file_part1_url)
        download_file(default_rec_archive_part2_path, liepa_voice_recognition_dataset_file_part2_url)
        download_file(default_rec_archive_part3_path, liepa_voice_recognition_dataset_file_part3_url)
        download_file(default_rec_archive_part4_path, liepa_voice_recognition_dataset_file_part4_url)
        download_file(default_rec_archive_part5_path, liepa_voice_recognition_dataset_file_part5_url)
        download_file(default_rec_archive_part6_path, liepa_voice_recognition_dataset_file_part6_url)

        if args.extract:
            if not exists(local_liepa_rec_dataset_directory) or args.force:
                    extract_all(default_rec_archive_part1_path, local_liepa_rec_dataset_directory)
                    extract_all(default_rec_archive_part2_path, local_liepa_rec_dataset_directory)
                    extract_all(default_rec_archive_part3_path, local_liepa_rec_dataset_directory)
                    extract_all(default_rec_archive_part4_path, local_liepa_rec_dataset_directory)
                    extract_all(default_rec_archive_part5_path, local_liepa_rec_dataset_directory)
                    extract_all(default_rec_archive_part6_path, local_liepa_rec_dataset_directory)
