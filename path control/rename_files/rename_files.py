import os
from myPath import get_script_directory

dir = get_script_directory().replace(os.sep, "/")
dir = dir + "files/"
print(dir)
dir_list = os.listdir(dir)
print(dir_list)

for i in range(1, len(dir_list)+1):
    new_name = "myfiles_"
    if i < 10:
        new_name = new_name + "0" + str(i) + ".txt"
    elif i < 100:
        new_name = new_name + str(i) + ".txt"
    os.rename(dir + dir_list[i-1], dir + new_name)

dir_list = os.listdir(dir)
print(dir_list)
