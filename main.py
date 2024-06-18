
# Standart Library
import time
# Local Module
import communication
import checklist
import measure
import portselect
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
        if mode == g.CHECKLIST_MODE:
            snd = communication.send(portgui.comport)               # Instantiate Send Class with Selected COMPort
        elif mode == g.TEST_MODE:
            sndtest = communication.send(portgui.comport)           # Instantiate Send Class with Selected COMPort for Com Test
            rectest = communication.receive([0])                    # Instantiate Receive Class for Com Test          
    
    # Check List Mode
    elif mode == g.CHECKLIST_MODE:
        mode = chkgui.display()
        if mode == g.MEASUREMENT_MODE:
            rec = communication.receive(chkgui.selected_index)      # Instantiate Receive Class with selected index
            mesgui = measure.measure(chkgui.selected_index)         # Instantiate measure Class with selected index
    
    # Measurement Mode
    elif mode == g.MEASUREMENT_MODE: # Checked Mark and 'Start'
        
        snd.send_measuring(chkgui.selected_index)                   # Send from Toll to ECU
        rec.receive_measuring(chkgui.selected_index, snd)           # Receive from ECU
        event = mesgui.measure_update(chkgui.selected_index, rec)   # Update Measured Value
        
        if event == (None,None):        # timeout=0の場合WIN_CLOSEDイベント取れない、Closeすると（None,None）になる
            print('-----Bye-----')
            break
        
        elif 'RecError' in event:
            print('Receive Error!!!')
            break
    
    # Test Mode(Single Call)
    elif mode == g.TEST_MODE:
        print("TEST_MODE!")
        sndtest.send_communication_test()
        mode = rectest.rec_communication_test(sndtest)
        del sndtest, rectest        # Delete Instance
    
    else:
        break