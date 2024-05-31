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

setparam_num = [6,23,24,0,12,10,14,7]

while True:
    send.send_measuring(setparam_num)
    receive.receive_measuring(setparam_num)
    time.sleep(1)

    # try:

    # except:
    #     print('a')
    #     pass