
import param
import checklist as cl
import PySimpleGUI as sg

measure_layout = []
trg = 0

# Initialize and Display Measurement Layout
def measure_init():
    global window_measure,trg
    measure_layout.extend([sg.Text(key=param.param_list[cl.selected_index[i]][0])] for i in range(cl.selected_num))
    window_measure = sg.Window("SSM Measurement Tool v1.0",measure_layout,resizable=True)
    trg = 1

# Update Measuremet Tool
def measure_update(receive_data):
    global trg
    if trg == 0: measure_init()
    event = window_measure.read(timeout=0, timeout_key="-timeout-") # timeout=0にすれば即時updateで更新可能
    [window_measure[param.param_list[cl.selected_index[i]][0]].update(receive_data[i]) for i in range(cl.selected_num)]
    
    return event