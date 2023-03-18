import os,time,platform
bit = platform.architecture()[0]
if bit=='64bit':
    print('Device 64 Bit')
    from tes import login
    login()

if bit == '32bit':
    print('Device 32 Bit')
    from null import login
    login()
else:
    print('Device LOL')
