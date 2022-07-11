#BatchInstall.py
import os
wingets = {"upgrade --all --accept-package-agreements ----accept-source-agreements" /
        "Tencent.TencentMeeting","Tencent.WeChat"}
try:
    for winget in wingets:
        os.system("winget install "+winget)
    print("Successful")        
except:
    print("Failed Somehow")
