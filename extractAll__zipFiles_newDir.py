#https://stackoverflow.com/questions/28339000/unzip-zip-files-in-folders-and-subfolders

from pathlib import Path
import zipfile
import fnmatch
import os
from time import time


def recursive_extract(cwd, pattern, target_folder):
    for root, dirs, files in os.walk(cwd):
        for filename in fnmatch.filter(files, pattern):
            subFolder_zip = os.path.join(root, filename)
            # print(subFolder_zip)
            zipfile.ZipFile(subFolder_zip).extractall(path=target_folder)
            zipfile.ZipFile(subFolder_zip).close()
            # print(os.listdir(cwd))
        for f in os.listdir(target_folder):
            if f.endswith('.zip'):
                name = os.path.join(target_folder, f)
                #print(name)
                zipfile.ZipFile(name).extractall(path=target_folder)
                zipfile.ZipFile(name).close()
        print(f'All .zip files extracted')


if __name__ == '__main__':
    cwd = r"/Users/MichaelHu/Documents/Internship/property_values"
    pattern = '*.zip'
    target_folder = r'/Users/MichaelHu/Documents/Internship/extracted_property_values'
    start = time()
    recursive_extract(cwd, pattern, target_folder)
    end = time()
    print(f'Process took: ', end - start, f'seconds to complete.')
    # path = Path('/Users/yumip/OneDrive/Desktop/Tocky/extract/')
    # print(len(list(path.glob('**/*.dat'))))