#%%
from zipfile import ZIP_STORED, ZipFile
import os

#%%
cwd = os.getcwd().replace(os.sep, "/") + "/"
print(cwd)
with ZipFile(file=cwd + "zip_sample2.zip", mode="w", compression=ZIP_STORED) as myzip:
    myzip.write(cwd + "file_1.txt")
