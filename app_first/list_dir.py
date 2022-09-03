from glob import glob



def list_dir():
    list_files = []
    for i in glob('*'):
        list_files.append(i)
    return list_files





