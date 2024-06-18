
# Standart Library
import serial.tools.list_ports
import PySimpleGUI as sg
# Local Module
import globalval as g

class portselect:
    def __init__(self):
        self.portlist = []
        self.comlist = []
        self.comport = 0
        
        self.ports = list(serial.tools.list_ports.comports())
        for p in self.ports:
            self.portlist.append(p.description)
            self.comlist.append(p.device)
            
        self.layout = [
            [sg.Text("Please Select COM Port", font=('Helvetica',12))],
            [sg.Listbox(self.portlist, size=(0,0))],
            [sg.Text("")],
            [sg.Button("Measure"),sg.Button("Test Mode"),sg.Button("End")]
        ]
        self.window = sg.Window(g.TOOL_NAME, self.layout)
    
    def portselect(self):
        event, values = self.window.read()
        if event == "Measure":
            selected_port = str(values[0])[2:-2]        # Conversion list to str. Remove [''].
            
            if selected_port != '':
                self.comport = self.comlist[self.portlist.index(selected_port)]
                self.window.close()
                print("Select Port: {}".format(selected_port))
                return g.CHECKLIST_MODE
            else:
                print("-----Please Select COM Port!-----")
                self.comport = 0
                return g.PORTSELECT_MODE
        
        elif event == "Test Mode":
            selected_port = str(values[0])[2:-2]        # Conversion list to str. Remove [''].
            
            if selected_port != '':
                self.comport = self.comlist[self.portlist.index(selected_port)]
                print("Select Port: {}".format(selected_port))
                return g.TEST_MODE
            else:
                print("-----Please Select COM Port!-----")
                self.comport = 0
                return g.PORTSELECT_MODE
        
        elif event == sg.WIN_CLOSED or event == "End":
            self.window.close()
            self.comport = 0
            print("-----Bye-----")
            return g.END_MODE
        
        else:
            self.comport = 0
            return g.CHECKLIST_MODE