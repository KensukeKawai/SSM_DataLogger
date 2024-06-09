
# importは、そのファイル内を”実行”する
# import serial
import time
import numpy as np
# import view_list_ports as vlp
import send
import receive
import param
import checklist as cl
import measure as ms
import global_val as g


def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

# Global Variable
check_sequence = 0
# 0:Default
# 1:Put Check Mark and 'Start'
# 2:Not Put Check Mark and 'Start'
# 3:CLOSED or 'Exit'

# Const

while True:
    # send.send_communication_test()
    start_time = time.time()
    if check_sequence == 0:
        check_sequence = cl.checklist_display()
    elif check_sequence == 1: # Checked Mark and 'Start'
        send.send_measuring(cl.selected_index)      # Send from Toll to ECU
        receive_successful, receive_data = receive.receive_measuring(cl.selected_index)     # Receive from ECU
        event = ms.measure_update(receive_data)         # Update Measurement Tool
        if event == (None,None): break      # timeout=0の場合WIN_CLOSEDイベント取れない、Closeすると（None,None）になる
        elif event == 'Save':
            print('Save!!!')
        elif event == 'Exit':
            print('Exit!!!')
    else: break
    end_time = time.time()
    g.refresh_time = round((end_time - start_time)*1000)

    # try:

    # except:
    #     print('a')
    #     pass