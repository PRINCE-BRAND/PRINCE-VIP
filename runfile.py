import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from PRINCE32 import PRINCE
 
        PRINCE()
 
 
 
elif bit == "32bit":
 
        from SSBB import PRINCE
 
 
        PRINCE()
