from os.path import exists
from utils.download_google_drive_file import download_file_from_google_drive
from utils.untar import extract_all
from argparse import ArgumentParser
from os import rename

from liepa import default_rec_dir, default_syn_dir, default_ann_dir

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

liepa_voice_synth_aiste_wav_file_id = '1myOg7BKRrisbMXiS1u_LniElVSLThKc2'
liepa_voice_synth_regina_wav_file_id = '16KviJdnB6vmIPxcMhun5u0puECzEEcfP'
liepa_voice_synth_edvardas_wav_file_id = '1_Pw2DroFKmRWq8q59DfknCzikAFVEJfq'
liepa_voice_synth_vladas_wav_file_id = '1AaWtUlx0cL0e2KeonN1zhKBsPmMOptuC'

aiste_wav_path = './Aiste.wav'
regina_wav_path = './Regina.wav'
edvardas_wav_path = './Edvardas.wav'
vladas_wav_path = './Vladas.wav'

liepa_voice_synth_aiste_mp3_file_id = '1OAHpTQqA6fRyq9EJeVrHF5Syxr1RO7_b'
liepa_voice_synth_regina_mp3_file_id = '1o2pmQwSHJpR1ZA7VIfBGwJfHqN4SBEBv'
liepa_voice_synth_edvardas_mp3_file_id = '12bVW8n9JgT9OMdmWrqs4o7a9C32rPmdA'
liepa_voice_synth_vladas_mp3_file_id = '1VAyhUUgvOq-UXoOIowCUdu0AhRV-FnPy'

aiste_mp3_path = './Aiste.mp3'
regina_mp3_path = './Regina.mp3'
edvardas_mp3_path = './Edvardas.mp3'
vladas_mp3_path = './Vladas.mp3'

liepa_voice_synth_aiste_m4a_file_id = '17bCNRPC4qCpNasFoyop3GLf8o8Ejc60Z'
liepa_voice_synth_regina_m4a_file_id = '1UO9_7eGzis0-dTCWgB5dJccVAdWpD87F'
liepa_voice_synth_edvardas_m4a_file_id = '1fEuXE9oLyrCGHMIVQhjh0HUyBaOcqAsh'
liepa_voice_synth_vladas_m4a_file_id = '1E2kO0hipO7LRcBulCfaGvWJ_yv6LP7V5'

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

    def download_file(local_archive_path, google_drive_file_id):
        if not exists(local_archive_path) or args.force:
            local_archive_tmp_path = local_archive_path + ".downloading"
            download_file_from_google_drive(google_drive_file_id, local_archive_tmp_path)
            rename(local_archive_tmp_path, local_archive_path)

    if args.get_annotations:
        download_file(default_annotation_archive_path, liepa_voice_recognition_dataset_annotation_file_id)

        if args.extract:
            if not exists(default_ann_dir) or args.force:
                extract_all(default_annotation_archive_path, default_ann_dir)

    if args.get_syn_voices:
        download_file(default_aiste_archive_path, liepa_voice_synth_dataset_aiste_file_id)
        download_file(default_regina_archive_path, liepa_voice_synth_dataset_regina_file_id)
        download_file(default_edvardas_archive_path, liepa_voice_synth_dataset_edvardas_file_id)
        download_file(default_vladas_archive_path, liepa_voice_synth_dataset_vladas_file_id)
        
        download_file(aiste_wav_path, liepa_voice_synth_aiste_wav_file_id)
        download_file(regina_wav_path, liepa_voice_synth_regina_wav_file_id)
        download_file(edvardas_wav_path, liepa_voice_synth_edvardas_wav_file_id)
        download_file(vladas_wav_path, liepa_voice_synth_vladas_wav_file_id)
        
        download_file(aiste_mp3_path, liepa_voice_synth_aiste_mp3_file_id)
        download_file(regina_mp3_path, liepa_voice_synth_regina_mp3_file_id)
        download_file(edvardas_mp3_path, liepa_voice_synth_edvardas_mp3_file_id)
        download_file(vladas_mp3_path, liepa_voice_synth_vladas_mp3_file_id)
        
        download_file(aiste_m4a_path, liepa_voice_synth_aiste_m4a_file_id)
        download_file(regina_m4a_path, liepa_voice_synth_regina_m4a_file_id)
        download_file(edvardas_m4a_path, liepa_voice_synth_edvardas_m4a_file_id)
        download_file(vladas_m4a_path, liepa_voice_synth_vladas_m4a_file_id)

        if args.extract:
            if not exists(default_syn_dir) or args.force:
                extract_all(default_aiste_archive_path, default_syn_dir)
                extract_all(default_regina_archive_path, default_syn_dir)
                extract_all(default_edvardas_archive_path, default_syn_dir)
                extract_all(default_vladas_archive_path, default_syn_dir)

    if args.get_rec_voices:
        download_file(default_rec_archive_path, liepa_voice_recognition_dataset_file_id)

        if args.extract:
            if not exists(local_liepa_rec_dataset_directory) or args.force:
                    extract_all(default_rec_archive_path, local_liepa_rec_dataset_directory)
