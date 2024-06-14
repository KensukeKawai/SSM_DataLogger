
# Standart Library
import time
# Local Module
import communication
import checklist
import measure
import portselect
import savefile
import globalval as g

# Global Variable
mode = g.PORTSELECT_MODE
refresh_time = 0
# Const

# Instantiate
portgui = portselect.portselect()
chkgui = checklist.checklist()

while True:
    # Port Select Mode
    if mode == g.PORTSELECT_MODE:
        mode = portgui.portselect()
        if mode == g.CHECKLIST_MODE or mode == g.TEST_MODE:
            snd = communication.send(portgui.comport)     # Instantiate Send Class with Selected COMPort
    
    # Check List Mode
    elif mode == g.CHECKLIST_MODE:
        mode = chkgui.display()
        if mode == g.MEASUREMENT_MODE:
            rec = communication.receive(chkgui.selected_index) # Instantiate Receive Class with selected index
            mesgui = measure.measure(chkgui.selected_index)    # Instantiate measure Class with selected index
    
    # Measurement Mode
    elif mode == g.MEASUREMENT_MODE: # Checked Mark and 'Start'
        
        snd.send_measuring(chkgui.selected_index)      # Send from Toll to ECU
        rec.receive_measuring(chkgui.selected_index, snd)     # Receive from ECU
        event = mesgui.measure_update(chkgui.selected_index, rec.receive_datalist, rec.refresh_time)         # Update Measured Value
        
        if event == (None,None): break      # timeout=0の場合WIN_CLOSEDイベント取れない、Closeすると（None,None）になる
        
        elif 'Save' in event:
            savefile.savefile(rec.timeseries_data)
            print('Save!!!')
            break
            
        elif 'Exit' in event:
            print('Exit!!!')
            break
    
    # Test Mode
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