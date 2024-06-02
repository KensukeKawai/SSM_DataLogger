# import serial
import time
import numpy as np
import view_list_ports as vlp
import send
import receive
import param
import checklist as cl      # importするとchecklist.py内のwhileループが実行→importはその部品を”実行”

########## API Initialize ##########

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

first = 0

while True:         #checklist.pyのwhileを抜けるとここに入る
    if cl.check_sequence == 1: # Checked Mark and 'Start'
        # Send from Toll to ECU
        send.send_measuring(cl.selected_index)
        # Receive from ECU
        receive_successful, receive_data = receive.receive_measuring(cl.selected_index)

        cl.measure_update(receive_data)
        time.sleep(0.1)

    else:
        break

    # try:

    # except:
    #     print('a')
    #     pass