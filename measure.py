
# Standard Library
import PySimpleGUI as sg
import math
# Local Module
import param
import globalval as g

# Constant
ROW_MAX = 4
VAR_PER_TAB = ROW_MAX*2
VALUE_NDIGITS = 3
FONTSIZE_VALUE = 90
FONTSIZE_UNIT = round(FONTSIZE_VALUE*0.5)
FONTSIZE_FRAME = 35
FRAME_WIDTH = 850
FRAME_HEIGHT = 210

# Initialize Variable
trg = 0

# Initialize and Display Measurement Layout
def measure_init(selected_num,selected_index):
    global window_measure,trg,window_test
    layout_tab = []
    layout_tabgroup = []
    var_num = 0
    var_num_z = 0
    
    tab_num = math.ceil(selected_num/VAR_PER_TAB)
    
    for n in range(tab_num):
        layout = []
        var_num = min(selected_num-var_num_z,VAR_PER_TAB)
        row_num = math.ceil(var_num/2)
        start = var_num_z
        end = row_num*2+var_num_z
        
        for i in range(start,end,2):
            name1 = (param.param_list[selected_index[i]][0]).replace('_',' ')
            unit1 = sg.Text('    [ '+ param.param_list[selected_index[i]][10] +' ]',font=('Helvetica',FONTSIZE_UNIT))
            value1 = [ sg.Text(key=param.param_list[selected_index[i]][0], font=('Helvetica',FONTSIZE_VALUE)), unit1 ]
            frame1 = sg.Frame([name1],[value1],size=(FRAME_WIDTH,FRAME_HEIGHT),font=('Helvetica',FONTSIZE_FRAME))
            if i < selected_num-1:
                name2 = (param.param_list[selected_index[i+1]][0]).replace('_',' ')
                unit2 = sg.Text('    [ '+ param.param_list[selected_index[i+1]][10] +' ]',font=('Helvetica',FONTSIZE_UNIT))
                value2 = [ sg.Text(key=param.param_list[selected_index[i+1]][0], font=('Helvetica',FONTSIZE_VALUE)), unit2 ]
                frame2 = sg.Frame([name2],[value2],size=(FRAME_WIDTH,FRAME_HEIGHT),font=('Helvetica',FONTSIZE_FRAME))
                frame = [frame1,frame2]
            else:
                frame = [frame1]
            layout.extend([frame])
            
        tab_name = 'Tab'+str(n)
        layout_tab.extend( [sg.Tab(tab_name,layout)] )
        var_num_z += var_num
        
    layout_tabgroup = [ [sg.TabGroup([layout_tab],font=('Helvetica',20))] ]
    layout_tabgroup.extend( [[sg.Text('Rate：',font=('Helvetica',20)),sg.Text(key='-refresh time-',font=('Helvetica',20)),sg.Text(' [ms]',font=('Helvetica',15))]] )
    # layout_tabgroup.extend( [sg.Menu([["File", ["Open", "Save", "Exit"]]])] )
    window_measure = sg.Window(g.TOOL_NAME,layout_tabgroup,resizable=True)
    
    trg = 1

# Update Measuremet Tool
def measure_update(selected_index,receive_data):
    global trg
    selected_num = len(selected_index)
    if trg == 0: measure_init(selected_num,selected_index)
    event = window_measure.read(timeout=0, timeout_key="-timeout-") # timeout=0にすれば即時updateで更新可能
    [window_measure[param.param_list[selected_index[i]][0]].update(round(receive_data[i],ndigits=VALUE_NDIGITS)) for i in range(selected_num)]
    [window_measure['-refresh time-'].update(g.refresh_time)]
    return event
