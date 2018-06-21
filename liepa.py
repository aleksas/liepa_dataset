from os.path import exists
from utils.download_google_drive_file import download_file_from_google_drive
from utils.untar import extract_subfolders, extract_all
from argparse import ArgumentParser

liepa_dataset_google_drive_archive_id = '1GSzu9n7I-mUMfaD7jkq_CvwZlZXbz9c7'

all_voices = [
    'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09',
    'D10', 'D11', 'D12', 'D13', 'D14', 'D16', 'D17', 'D18',
    'D21', 'D23', 'D25', 'D26', 'D27', 'D28', 'D29', 'D30',
    'D31', 'D32', 'D35', 'D36', 'D37', 'D41', 'D42', 'D43',
    'D44', 'D45', 'D46', 'D47', 'D48', 'D49', 'D50', 'D51',
    'D52', 'D53', 'D54', 'D55', 'D56', 'D57', 'D58', 'D59',
    'D60', 'D61', 'D62', 'D63', 'D64', 'D65', 'D66', 'D67',
    'D68', 'D69', 'D70', 'D71', 'D73', 'D74', 'D75', 'D76',
    'D77', 'D78', 'D79', 'D80', 'D81', 'D82', 'D83', 'D84',
    'D85', 'D86', 'D87', 'D88', 'D89', 'D90', 'D91', 'D92',
    'D93', 'D94', 'D95', 'D96', 'D97', 'D98', 'D99', 'D100',
    'D101', 'D102', 'D103', 'D104', 'D105', 'D106', 'D107', 'D108',
    'D109', 'D110', 'D111', 'D112', 'D113', 'D114', 'D115', 'D116',
    'D117', 'D118', 'D119', 'D121', 'D122', 'D123', 'D124', 'D125',
    'D126', 'D127', 'D128', 'D129', 'D130', 'D131', 'D132', 'D133',
    'D134', 'D135', 'D136', 'D137', 'D138', 'D139', 'D140', 'D141',
    'D142', 'D143', 'D144', 'D145', 'D146', 'D147', 'D148', 'D149',
    'D150', 'D151', 'D152', 'D153', 'D154', 'D155', 'D156', 'D157',
    'D158', 'D159', 'D160', 'D161', 'D162', 'D163', 'D164', 'D165',
    'D166', 'D167', 'D168', 'D169', 'D170', 'D171', 'D172', 'D173',
    'D174', 'D175', 'D176', 'D177', 'D178', 'D179', 'D180', 'D182',
    'D183', 'D184', 'D185', 'D186', 'D187', 'D188', 'D189', 'D190',
    'D191', 'D192', 'D193', 'D194', 'D195', 'D196', 'D197', 'D198',
    'D199', 'D200', 'D201', 'D202', 'D203', 'D204', 'D205', 'D206',
    'D207', 'D208', 'D209', 'D210', 'D211', 'D212', 'D213', 'D214',
    'D216', 'D228', 'D230', 'D234', 'D235', 'D238', 'D240', 'D241',
    'D242', 'D243', 'D244', 'D245', 'D247', 'D248', 'D250', 'D251',
    'D262', 'D263', 'D264', 'D265', 'D266', 'D267', 'D268', 'D269',
    'D270', 'D271', 'D272', 'D273', 'D274', 'D275', 'D276', 'D277',
    'D278', 'D279', 'D280', 'D281', 'D282', 'D283', 'D284', 'D285',
    'D286', 'D287', 'D288', 'D289', 'D290', 'D291', 'D292', 'D301',
    'D302', 'D303', 'D304', 'D305', 'D307', 'D308', 'D309', 'D500',
    'D502', 'D503', 'D504', 'D505', 'D506', 'D507', 'D508', 'D509',
    'D510', 'D511', 'D512', 'D513', 'D514', 'D515', 'D516', 'D517',
    'D518', 'D519', 'D520', 'D522', 'D523', 'D524', 'D525', 'D526',
    'D527', 'D528', 'D529', 'D530', 'D531', 'D532', 'D533', 'D534',
    'D535', 'D536', 'D537', 'D538', 'D539', 'D540', 'D541', 'D543',
    'D544', 'D545', 'D546', 'D547', 'D548', 'D549', 'D550', 'D551',
    'D552', 'D554', 'D555', 'D556', 'D557', 'D558', 'D561', 'D562',
    'D563', 'D564', 'D565', 'D566', 'D567', 'D568', 'D569', 'D570',
    'D571', 'D572', 'D573', 'D574', 'D575', 'D576', 'D577', 'D578',
    'D579', 'D580', 'D581', 'D582', 'D583', 'D584', 'D585', 'D586',
    'D587', 'D588', 'D589', 'D590', 'D593', 'D595', 'D596', 'D597',
    'D598', 'D599', 'D600', 'D601', 'D602', 'D603', 'D604', 'D605',
    'D606', 'D607', 'D608', 'D609', 'D610', 'D611', 'D907']

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

    default_archive_path = './MII_LIEPA_v1.tar.bz2'
    default_dir = './MII_LIEPA_V1'

    parser = ArgumentParser()
    parser.add_argument('-p','--archive-path', help='Path to download LIEPA dataset archive to. (Default: "%s")' % default_archive_path, default=default_archive_path)
    parser.add_argument('-d','--liepa-dir', help='Directory for LIEPA dataset to unpack to. (default: "%s")' % default_dir, default=default_dir)
    parser.add_argument('-v','--voices', nargs='+', help='List of voices to unpack (e.g. -s D256 D512). VERY SLOW!!!')
    args = parser.parse_args()

    local_liepa_dataset_archive_path = args.archive_path
    local_liepa_dataset_directory = args.liepa_dir

    # Download original LIEPA dataset
    if not exists(local_liepa_dataset_archive_path):
        download_file_from_google_drive(liepa_dataset_google_drive_archive_id, local_liepa_dataset_archive_path)

    if args.voices:
        extract_specific_voices(local_liepa_dataset_archive_path, local_liepa_dataset_directory, args.voices)
    else:
        extract_all(local_liepa_dataset_archive_path, local_liepa_dataset_directory)
