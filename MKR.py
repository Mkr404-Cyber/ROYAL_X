#coding=utf-8
import os, sys, time
A = '\x1b[1;92m'
print(f'\n{A} MKR COME BACK \x1b[1;97m')
import platform
os.system('xdg-open https://t.me/onemancyberarmy22')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf Mkr.so Mkr32.so')
except:
    pass
os.system('rm -rf Mkr.so Mkr64.so')
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Mkr64.so'):                                                                                                                          
        os.system('curl -L https://github.com/X-R-404/X/blob/main/Mkr64.cpython-311.so?raw=true -o Mkr64.so')
        import Mkr64
    else:
        import Mkr64
elif bit == '32bit':
    if not os.path.isfile('Mkr32.so'):
        os.system('curl -L https://github.com/X-R-404/X/blob/main/Mkr32.cpython-311.so?raw=true -o Mkr32.so')
        import Mkr32
    else:
        print("\x1b[1;92m 32 bit Coming Soon...");time.sleep(2)
else:
	print("\x1b[1;92m Not Support Your Phone")
