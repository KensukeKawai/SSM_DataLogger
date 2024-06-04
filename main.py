
# importは、そのファイル内を”実行”する
# import serial
import time
import numpy as np
import view_list_ports as vlp
import send
import receive
import param
import checklist as cl
import measure as ms


def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

# Global Variable
check_sequence = 0
# 0:Default
# 1:Put Check Mark and 'Start'
# 2:Not Put Check Mark and 'Start'
# 3:CLOSED or 'Exit'

# Const
SLEEP_TIME_S = 0.1

while True:         #checklist.pyのwhileを抜けるとここに入る
    if check_sequence == 0:
        check_sequence = cl.checklist_display()
    elif check_sequence == 1: # Checked Mark and 'Start'
        send.send_measuring(cl.selected_index)      # Send from Toll to ECU
        receive_successful, receive_data = receive.receive_measuring(cl.selected_index)     # Receive from ECU
        event = ms.measure_update(receive_data)         # Update Measurement Tool
        time.sleep(SLEEP_TIME_S)
        if event == (None,None): break      # timeout=0の場合WIN_CLOSEDイベント取れない、Closeすると（None,None）になる
    else: break

    # try:

    # except:
    #     print('a')
    #     pass