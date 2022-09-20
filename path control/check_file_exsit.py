import os

# 要檢查的檔案路徑
filepath = "/etc/motd"

# 檢查檔案是否存在
if os.path.isfile(filepath):
    print("檔案存在。")
else:
    print("檔案不存在。")
