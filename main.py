# import serial
import time
import numpy as np
import view_list_ports as vlp
import send
import receive
import param

########## API Initialize ##########

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

setparam_num = [0,1,2]
# print(setparam_num)

while True:
    send.send2ecu(setparam_num)
    time.sleep(1)

    # try:

    # except:
    #     print('a')
    #     pass