import os
from zipfile import ZipFile, ZIP_STORED


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


with ZipFile('myzipfile.zip', 'w', ZIP_STORED) as myZip:
    zipdir('tmp/', myZip)
