'''
Trial and error on a few functions that aimed to filter .dat files throughout
directory using a specific pattern. The 4th function worked to filter AND 
insert the property values in a single function, as it called the function
to store the .dat files.
'''

import os, glob
from pathlib import Path
from read_dat import store_dat_archive, store_dat_current
import pandas as pd
from insert_into_db import insert_property


# Function that finds a specified pattern within the specified directory
# def find(directory, pattern):
#     totalFiles = 0
#     for file in glob.glob(directory + pattern, recursive= True):
#         filename = os.path.join(directory, file)
#         totalFiles += 1
#         print(f'{totalFiles}: {filename}')


# Function that finds a specified pattern within entire drive
# def find(pattern):
#     totalFiles = 0
#     for file in glob.iglob(pattern, recursive= True):
#         filename = os.path.join(directory, file)
#         totalFiles += 1
#         print(f'{totalFiles}: {filename}')


# # Practice to find ARCHIVED files, filter for selected variables, and insert into pg database.
# def find(pattern):
#     totalFiles = 0
#     for file in glob.iglob(pattern, recursive= True):
#         filename = os.path.join(directory, file)
#         totalFiles += 1
#         # print(f'{totalFiles}: {filename}')

#     # print(df.head())

def find(pattern):
    filenames = []
    for file in glob.iglob(pattern, recursive= True):
        filenames.append(os.path.join(directory, file))
    #     print(filenames)
    return filenames


if __name__ == '__main__':
    directory = r'/Users/MichaelHu/Documents/Internship'
    # For every file in filenames, run it through the store dat function
    pattern = '**/ARCHIVE_SALES_*.DAT'
    filenames = find(pattern)
    for f in filenames:
        store_dat_archive(f)
    pattern = '**/*_SALES_DATA_*.DAT'
    filenames = find(pattern)
    for f in filenames:
        store_dat_current(f)
