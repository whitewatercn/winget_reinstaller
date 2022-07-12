#BatchInstall.py
import os
wingets = {"Tencent.TencentMeeting","Tencent.WeChat"}
os.system("winget" + "upgrade --all --accept-package-agreements ----accept-source-agreements")

try:
    for winget in wingets:
        os.system("winget install "+winget)
    print("Successful")        
except:
    print("Failed Somehow")
