
# def view_list_ports():
    # List of Ports
import serial.tools.list_ports
import PySimpleGUI as sg
import globalval as g

class portselect:
    def __init__(self):
        self.portlist = []
        self.comlist = []
        
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
                comport = self.comlist[self.portlist.index(selected_port)]
                self.window.close()
                print("Select Port: {}".format(selected_port))
                return g.CHECKLIST_MODE, comport
            else:
                print("-----Please Select COM Port!-----")
                return g.PORTSELECT_MODE, 0
        
        elif event == "Test Mode":
            selected_port = str(values[0])[2:-2]        # Conversion list to str. Remove [''].
            
            if selected_port != '':
                comport = self.comlist[self.portlist.index(selected_port)]
                # self.window.close()
                print("Select Port: {}".format(selected_port))
                return g.TEST_MODE, comport
            else:
                print("-----Please Select COM Port!-----")
                return g.PORTSELECT_MODE, 0
        
        elif event == sg.WIN_CLOSED or event == "End":
            self.window.close()
            print("-----Bye-----")
            return g.END_MODE, 0
        
        else:
            return g.CHECKLIST_MODE, 0


# def view_list_ports():
    # List of Ports
# import serial.tools.list_ports

# ports = list(serial.tools.list_ports.comports())
# for p in ports:
#     print(p)
#     print(" device       :", p.device)
#     print(" name         :", p.name)
#     print(" description  :", p.description)
#     print(" hwid         :", p.hwid)
#     print(" vid          :", p.vid)
#     print(" pid          :", p.pid)
#     print(" serial_number:", p.serial_number)
#     print(" location     :", p.location)
#     print(" manufactuer  :", p.manufacturer)
#     print(" product      :", p.product)
#     print(" interface    :", p.interface)
#     print("")