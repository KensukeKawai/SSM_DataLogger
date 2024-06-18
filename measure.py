
# Standard Library
import PySimpleGUI as sg
import math
# Local Module
import param
import globalval as g
import savefile

class measure:
    def __init__(self, selected_index):
        # Constant
        self.ROW_MAX = 4
        self.VAR_PER_TAB = self.ROW_MAX*2
        self.VALUE_NDIGITS = 3
        self.FONTSIZE_VALUE = 90
        self.FONTSIZE_UNIT = round(self.FONTSIZE_VALUE*0.5)
        self.FONTSIZE_FRAME = 35
        self.FRAME_WIDTH = 850
        self.FRAME_HEIGHT = 210
        self.STS_MEASURING = 1
        self.STS_STOP = 2
        #Variable
        self.selected_num = 0
        self.status_z = self.STS_MEASURING
        layout_tab = []
        layout_tabgroup = []
        var_num = 0
        var_num_z = 0
        
        self.selected_num = len(selected_index)
        tab_num = math.ceil(self.selected_num/self.VAR_PER_TAB)
        
        for n in range(tab_num):
            layout = []
            var_num = min(self.selected_num-var_num_z,self.VAR_PER_TAB)
            row_num = math.ceil(var_num/2)
            start = var_num_z
            end = row_num*2+var_num_z
            
            for i in range(start,end,2):
                name1 = (param.param_list[selected_index[i]][0]).replace('_',' ')
                unit1 = sg.Text('    [ '+ param.param_list[selected_index[i]][10] +' ]', font=('Helvetica',self.FONTSIZE_UNIT))
                value1 = [ sg.Text(key=param.param_list[selected_index[i]][0], font=('Helvetica',self.FONTSIZE_VALUE)), unit1 ]
                frame1 = sg.Frame([name1],[value1],size=(self.FRAME_WIDTH,self.FRAME_HEIGHT), font=('Helvetica',self.FONTSIZE_FRAME))
                if i < self.selected_num-1:
                    name2 = (param.param_list[selected_index[i+1]][0]).replace('_',' ')
                    unit2 = sg.Text('    [ '+ param.param_list[selected_index[i+1]][10] +' ]', font=('Helvetica',self.FONTSIZE_UNIT))
                    value2 = [ sg.Text(key=param.param_list[selected_index[i+1]][0], font=('Helvetica',self.FONTSIZE_VALUE)), unit2 ]
                    frame2 = sg.Frame([name2],[value2],size=(self.FRAME_WIDTH,self.FRAME_HEIGHT), font=('Helvetica',self.FONTSIZE_FRAME))
                    frame = [frame1,frame2]
                else:
                    frame = [frame1]
                layout.extend([frame])
                
            tab_name = 'Tab'+str(n)
            layout_tab.extend( [sg.Tab(tab_name,layout)] )
            var_num_z += var_num
            
        layout_tabgroup = [ [sg.TabGroup([layout_tab], font=('Helvetica',20))] ]
        layout_tabgroup.extend( [[
                sg.Text('Rate：', font=('Helvetica',20)),
                sg.Text(key='-refresh time-', font=('Helvetica',24)),
                sg.Text(' [ms]         ', font=('Helvetica',20)),
                sg.Text('Measure Status：', font=('Helvetica',20)),
                sg.Text(key='-messtatus-', font=('Helvetica',24)),
                sg.Text('             ', font=('Helvetica',20)),
                sg.Text('Save：', font=('Helvetica',20)),
                sg.Text(key='-savestatus-', font=('Helvetica',24)),
                sg.Text('             ', font=('Helvetica',20)),
                sg.Button('Start',font=('Helvetica',20),size=(15,0)),
                sg.Button('Save & Stop',font=('Helvetica',20),size=(15,0))
            ]] )
        
        # layout_tabgroup.extend( [[sg.Menu([["File", ["Open", "Save", "Exit"]]])]] )
        
        self.window_measure = sg.Window(g.TOOL_NAME,layout_tabgroup,resizable=True)
        
    # Update Measuremet Tool
    def measure_update(self, selected_index, rec):
        event = self.window_measure.read(timeout=0, timeout_key="-timeout-") # timeout=0にすれば即時updateで更新可能
        
        if (rec.receive_sts == rec.STS_SUCCESS):
            if 'Save & Stop' in event:
                savefile.savefile(rec.timeseries_data)
                [self.window_measure['-refresh time-'].update(' - ')]
                [self.window_measure['-messtatus-'].update('Stop             ')]
                [self.window_measure['-savestatus-'].update('Done      ')]
                self.status_z = self.STS_STOP
                
            elif ((self.status_z == self.STS_STOP) and ('Start' in event)) or (self.status_z == self.STS_MEASURING):
                [self.window_measure[param.param_list[selected_index[i]][0]].update(round(rec.receive_datalist[i], ndigits=self.VALUE_NDIGITS)) for i in range(self.selected_num)]
                [self.window_measure['-refresh time-'].update(rec.refresh_time)]
                [self.window_measure['-messtatus-'].update('Measuring...')]
                [self.window_measure['-savestatus-'].update('Not Done')]
                self.status_z = self.STS_MEASURING

        else:
            [self.window_measure['-refresh time-'].update(' - ')]
            [self.window_measure['-messtatus-'].update('Receive Error ')]
            self.status_z = self.STS_STOP
            
        return event