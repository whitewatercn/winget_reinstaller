#BatchInstall.py
import os
wingets = {"Tencent.TencentMeeting","Tencent.WeChat"}
try:
    for winget in wingets:
        os.system("winget install "+winget)
    print("Successful")        
except:
    print("Failed Somehow")
