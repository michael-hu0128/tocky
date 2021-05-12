# https://stackoverflow.com/questions/56201516/how-can-i-extract-multiple-zip-files

import os
from zipfile import ZipFile
from time import time


def extract_all_zipFile(cwd, target_folder):
    for f in os.listdir(cwd):
        if f.endswith(".zip"):
            z = ZipFile(f, 'r')
            z.extractall(path = target_folder)
            z.close()


if __name__ == '__main__':
    cwd = os.chdir('/Users/MichaelHu/Documents/Internship/property_values')
    target_folder = '/Users/MichaelHu/Documents/Internship/extracted_property_values'
    start = time()
    extract_all_zipFile(cwd, target_folder)
    end = time()
    print(f'Process took: ', end - start, f'seconds.')