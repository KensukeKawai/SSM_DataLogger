
# importは、そのファイル内を”実行”する
# Standart Library
import time
import numpy as np
# Local Module
import communication
import checklist
import measure
import portselect
import globalval as g


def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

# Global Variable
mode = g.PORTSELECT_MODE

# Const

# Instantiate
port = portselect.portselect()
chk = checklist.checklist()
rec = communication.receive()

while True:
    if mode == g.PORTSELECT_MODE:
        mode,selected_port = port.portselect()
        if mode == g.CHECKLIST_MODE or mode == g.TEST_MODE:
            snd = communication.send(selected_port)     # Instantiate Send Class with Selected COMPort
    
    elif mode == g.CHECKLIST_MODE:
        mode,selected_index = chk.display()
        
    elif mode == g.MEASUREMENT_MODE: # Checked Mark and 'Start'
        start_time = time.time()
        
        snd.send_measuring(selected_index)      # Send from Toll to ECU
        rec_success, rec_data = rec.receive_measuring(selected_index,snd)     # Receive from ECU
        event = measure.measure_update(selected_index,rec_data)         # Update Measurement Tool
        
        end_time = time.time()
        g.refresh_time = round((end_time - start_time)*1000)
        
        if event == (None,None): break      # timeout=0の場合WIN_CLOSEDイベント取れない、Closeすると（None,None）になる
        
        elif event == 'Save':
            print('Save!!!')
            
        elif event == 'Exit':
            print('Exit!!!')
    
    elif mode == g.TEST_MODE:
        snd.send_communication_test()
        # port.window.close()
        print("TEST_MODE!")
        # Receiveのtestインスタンスメソッドをここでコールする
        # CLOSED,END押されたときに正常終了する処理を追加
    
    else:
        break

    # try:

    # except:
    #     print('a')
    #     pass