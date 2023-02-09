import os
try: 
    execfile('r3dth1rth33n/tor/create_basic_tor_proxy.py')
    print(exec)
except:
    os.system('python create_basic_tor_proxy.py')
    print('end')