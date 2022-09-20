#%%
import numpy as np
import pathlib

#%%
direction = str(pathlib.Path(__file__).parent.resolve()) + "/"

file_path = direction + "N09_M07_F10_K001_1.txt"
content = np.loadtxt(file_path, dtype="float64", delimiter=",")
# %%
