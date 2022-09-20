#%% use glob to get all the csv files in the folder
import glob
import os
import pathlib

#%%
script_direction = str(pathlib.Path(__file__).parent.resolve()) + "/"
folder_path = script_direction
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
