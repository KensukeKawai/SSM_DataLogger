
# Standard Library
import time
import PySimpleGUI as sg
# Local Module
import param
import globalval as g

class checklist:
    def __init__(self):        #self.はインスタンス変数、つかないのはメソッド内ローカル変数
        # Const
        self.BLANK_BOX = '☐'
        self.CHECKED_BOX = '☑'
        # Valiable
        self.param_num = len(param.param_list)
        self.table_data = []
        self.selected_index = []
        self.selected_num = 0
        
        for i in range(self.param_num):
            data = [self.BLANK_BOX, param.param_list[i][0], param.param_list[i][10]]
            self.table_data.append(data)
        
        self.checklist_layout = [
            [sg.Table(values = self.table_data,
                    headings = ["Chk","Parameter","Unit"],
                    max_col_width = self.param_num,
                    auto_size_columns = False,
                    display_row_numbers = True,
                    justification = "right",
                    select_mode = sg.TABLE_SELECT_MODE_EXTENDED,
                    enable_events = True,
                    key = '-TABLE-',
                    row_height = 18,
                    font = 'Helvetica 11',
                    col_widths = [5,30,8],
                    size = (1,45),
                    alternating_row_color='#3d5f80'
                    )],
            [sg.Button("Start",font=('Helvetica',15),size=(10,0)), sg.Button("Exit",font=('Helvetica',15),size=(10,0))],
            [sg.Menu([["File", ["Open", "Save", "Exit"]]])]
        ]

        self.window_checklist = sg.Window(g.TOOL_NAME, self.checklist_layout, resizable=True)
        
    def my_index_multi(self, l, x):
        return [i for i, _x in enumerate(l) if _x == x]

    def display(self):
        event, values = self.window_checklist.read()
        
        if event == '-TABLE-' and values[event]:
            row = values[event][0]
            if self.table_data[row][0] == self.BLANK_BOX:
                self.table_data[row][0] = self.CHECKED_BOX
            else:
                self.table_data[row][0] = self.BLANK_BOX
            self.window_checklist['-TABLE-'].update(values=self.table_data)
            
        if event == 'Start':
            # 選択したパラメータのIndexを取得
            table_selected = [self.table_data[i][0] for i in range(self.param_num)]
            self.selected_index = self.my_index_multi(table_selected, self.CHECKED_BOX)
            print("Checked Index: {}".format(self.selected_index))
            
            if self.selected_index:      # チェック入れたか判定
                print("-----Start Measurement!-----")
                self.window_checklist.close()
                time.sleep(1)
                return g.MEASUREMENT_MODE
            else:
                print("-----Please Put Check Mark and Push 'Start' Button!-----")
                return g.CHECKLIST_MODE
        
        if (event == sg.WIN_CLOSED) or (event == 'Exit') or (event == None):
            print("-----Bye-----")
            self.window_checklist.close()
            return g.END_MODE
        else:
            return g.CHECKLIST_MODE