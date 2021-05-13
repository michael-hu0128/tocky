import zipfile, os
from time import time

def unzip_all(path):
    files = os.listdir(path)
    # print(files)
    for filename in files:
        if filename.endswith(".zip"):
            name = os.path.splitext(os.path.basename(filename))[0]
            #print(name)
            zippedfile_directory = os.path.join(path, filename)
            extractedfile_directory = os.path.join(path, name)
            if not os.path.isdir(extractedfile_directory):
                #print(name)
                try:
                    with zipfile.ZipFile(zippedfile_directory) as zipObj:
                        zipObj.extractall(extractedfile_directory)
                    print(zippedfile_directory)
                except:
                    print(f"{filename} unzipping failed -- Invalid file")
                else:
                    print(f"{name} successfully extracted")
                    unzip_all(extractedfile_directory)


if __name__ == '__main__':
    # cwd = os.getcwd()
    folder = '/Users/MichaelHu/Library/Mobile Documents/com~apple~CloudDocs/extracted_prop_values'
    path = '/Users/MichaelHu/Documents/Internship/property_values'
    unzip_all(path)