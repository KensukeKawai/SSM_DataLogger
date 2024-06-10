
# importは、そのファイル内を”実行”する
# Standart Library
import time
import numpy as np
# Local Module
import send
import receive
import communication
import checklist
import measure
import global_val as g


def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

# Global Variable
mode = 0
# 0:Default, Not Put Check Mark and 'Start'
# 1:Put Check Mark and 'Start'
# 2:CLOSED or 'Exit'

# Const

# Instantiate
chk = checklist.checklist()
snd = communication.send()
rec = communication.receive()

while True:
    # send.send_communication_test()
    start_time = time.time()
    
    if mode == 0:
        mode,selected_index = chk.display()
        print(mode)
        
    elif mode == 1: # Checked Mark and 'Start'
        snd.send_measuring(selected_index)      # Send from Toll to ECU
        rec_success, rec_data = rec.receive_measuring(selected_index,snd)     # Receive from ECU
        event = measure.measure_update(selected_index,rec_data)         # Update Measurement Tool
        if event == (None,None): break      # timeout=0の場合WIN_CLOSEDイベント取れない、Closeすると（None,None）になる
        elif event == 'Save':
            print('Save!!!')
        elif event == 'Exit':
            print('Exit!!!')
            
    else:
        break
    
    end_time = time.time()
    g.refresh_time = round((end_time - start_time)*1000)

    # try:

    # except:
    #     print('a')
    #     pass