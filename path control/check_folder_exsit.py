import os

# 要檢查的目錄路徑
folderpath = "/var/log"

# 檢查目錄是否存在
if os.path.isdir(folderpath):
    print("目錄存在。")
else:
    print("目錄不存在。")
