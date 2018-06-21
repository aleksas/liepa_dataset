# REFERENCE: https://stackoverflow.com/a/29416112/1433554

from tarfile import open

def extract_all(tar_bz2_path, dst_dir='./'):
    with open(tar_bz2_path, "r:bz2") as tar:
        tar.extractall(dst_dir)

def extract_subfolders(tar_bz2_path, subfolders, dst_dir='./'):
    with open(tar_bz2_path, "r:bz2") as tar:
        for subfolder in subfolders:
            subdir_and_files = [
                tarinfo for tarinfo in tar.getmembers()
                if tarinfo.name.startswith(subfolder)
            ]
            tar.extractall(dst_dir, members=subdir_and_files)

if __name__ == '__main__':
    #extract_all('./a.tar.bz2')

    #speakers = ['D245', 'D30']
    #subfolders = ['a/%s/' % speaker for speaker in speakers]
    #extract_speakers('./a.tar.bz2', subfolders, 'dst_dir')

    pass
