#%%
import pathlib
import os

direction = str(pathlib.Path(__file__).parent.resolve())
folder_path = direction
folder_content = os.listdir(folder_path)

print(folder_path + '資料夾內容：')
for item in folder_content:
    if os.path.isdir(folder_path + '\\' + item):
        print('資料夾：' + item)
    elif os.path.isfile(folder_path + '\\' + item):
        print('檔案：' + item)
    else:
        print('無法辨識：' + item)