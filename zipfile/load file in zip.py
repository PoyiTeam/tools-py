# %%
from zipfile import ZipFile
import os
import numpy as np
import PIL

# %%
cwd = os.getcwd().replace(os.sep, "/") + "/"
print(cwd)
path_zip = cwd + "zip_sample.zip"
myZip = ZipFile(file=path_zip)
zip_list = myZip.namelist()
print(zip_list)
# %%
myfile = myZip.open(name=zip_list[0], mode="r")
np.loadtxt(myfile, delimiter=",")
# %%
myfile = myZip.open(name=zip_list[2], mode="r")
PIL.Image.open(myfile)
