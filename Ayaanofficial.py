#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

os.system('xdg-open https://facebook.com/groups/478837310770292/')

import requests

try:

    if sys.argv[1]=='update':

        os.system('rm -rf Ayaanofficial.so Ayaanofficial32.so')

except:

    pass

os.system('rm -rf Ayaanofficial Ayaanofficial32.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('Sarfraz.so'):

        os.system('curl -L https://github.com/Ayaanofficial-XD/executables/blob/main/Ayaanofficial.cpython-311.so?raw=true -o Ayaanofficial.so') 

        import Sarfraz

    else:

        import Sarfraz

elif bit == '32bit':

    if not os.path.isfile('Ayaanofficial32.so'):

        os.system('curl -L https://github.com/Ayaanofficial-XD/executables/blob/main/Ayaanofficial32.cpython-311.so?raw=true -o Ayaanofficial32.so') 

        import Ayaanofficial32

    else:

        import Ayaanofficial32

