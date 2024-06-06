
import param
import checklist as cl
import PySimpleGUI as sg
import math
import global_val as g

# Constant
row_max = 4
var_per_tab = row_max*2
value_ndigits = 3
fontsize_value = 90
fontsize_unit = round(fontsize_value*0.5)
fontsize_frame = 35
frame_width = 850
frame_height = 210

# Initialize Variable
trg = 0

# Initialize and Display Measurement Layout
def measure_init():
    global window_measure,trg,window_test
    layout_tab = []
    layout_tabgroup = []
    var_num = 0
    var_num_z = 0
    
    tab_num = math.ceil(cl.selected_num/var_per_tab)
    
    for n in range(tab_num):
        layout = []
        var_num = min(cl.selected_num-var_num_z,var_per_tab)
        row_num = math.ceil(var_num/2)
        start = var_num_z
        end = row_num*2+var_num_z
        
        # for i in range(var_num_z,var_num+var_num_z):
        #     name = (param.param_list[cl.selected_index[i]][0]).replace('_',' ')
        #     unit = sg.Text('    [ '+ param.param_list[cl.selected_index[i]][10] +' ]',font=('Helvetica',fontsize_unit))
        #     value = [ sg.Text(key=param.param_list[cl.selected_index[i]][0], font=('Helvetica',fontsize_value)), unit ]
        #     test = [sg.Text('100')]
            
        #     frame = [sg.Frame([name],[value],size=(800,200),font=('Helvetica',fontsize_frame)),sg.Frame(['test'],[test],size=(800,200),font=('Helvetica',fontsize_frame))]
        #     layout.extend([frame])
            
        # tab_name = 'Tab'+str(n)
        # layout_tab.extend( [sg.Tab(tab_name,layout)] )
        # var_num_z += var_num
        
        for i in range(start,end,2):
            print("z: {}, var_num: {}, row_num: {}, i: {}".format(var_num_z,var_num,row_num,i))
            print("start: {}, end: {}".format(start,end))
            name1 = (param.param_list[cl.selected_index[i]][0]).replace('_',' ')
            unit1 = sg.Text('    [ '+ param.param_list[cl.selected_index[i]][10] +' ]',font=('Helvetica',fontsize_unit))
            value1 = [ sg.Text(key=param.param_list[cl.selected_index[i]][0], font=('Helvetica',fontsize_value)), unit1 ]
            frame1 = sg.Frame([name1],[value1],size=(frame_width,frame_height),font=('Helvetica',fontsize_frame))
            if i < cl.selected_num-1:
                name2 = (param.param_list[cl.selected_index[i+1]][0]).replace('_',' ')
                unit2 = sg.Text('    [ '+ param.param_list[cl.selected_index[i+1]][10] +' ]',font=('Helvetica',fontsize_unit))
                value2 = [ sg.Text(key=param.param_list[cl.selected_index[i+1]][0], font=('Helvetica',fontsize_value)), unit2 ]
                frame2 = sg.Frame([name2],[value2],size=(frame_width,frame_height),font=('Helvetica',fontsize_frame))
                frame = [frame1,frame2]
            else:
                frame = [frame1]
            layout.extend([frame])
            
        tab_name = 'Tab'+str(n)
        layout_tab.extend( [sg.Tab(tab_name,layout)] )
        var_num_z += var_num
        
    layout_tabgroup = [ [sg.TabGroup([layout_tab],font=('Helvetica',20))] ]
    layout_tabgroup.extend( [[sg.Text('Rate：',font=('Helvetica',20)),sg.Text(key='-refresh time-',font=('Helvetica',20)),sg.Text(' [ms]',font=('Helvetica',15))]] )
    window_measure = sg.Window("SSM Measurement Tool v1.0",layout_tabgroup,resizable=True)
    
    trg = 1

# Update Measuremet Tool
def measure_update(receive_data):
    global trg
    if trg == 0: measure_init()
    event = window_measure.read(timeout=0, timeout_key="-timeout-") # timeout=0にすれば即時updateで更新可能
    [window_measure[param.param_list[cl.selected_index[i]][0]].update(round(receive_data[i],ndigits=value_ndigits)) for i in range(cl.selected_num)]
    [window_measure['-refresh time-'].update(g.refresh_time)]
    return event
