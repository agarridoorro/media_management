import os
import shutil
from datetime import datetime

print(datetime.now(), "Initializing...")

if not os.path.isfile('/config/auth.json'):
    shutil.copyfile('/app/config/auth.json', '/config/auth.json')
    print ('Created /config/auth.json')
if not os.path.isfile('/config/params.json'):
    shutil.copyfile('/app/config/params.json', '/config/params.json')
    print ('Created /config/params.json')