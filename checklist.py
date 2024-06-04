
import time
import param
import PySimpleGUI as sg

# Global Variable
param_num = len(param.param_list)
table_data = []

# Constant
BLANK_BOX = '☐'
CHECKED_BOX = '☑'

for i in range(param_num):
    cha = [BLANK_BOX, param.param_list[i][0], param.param_list[i][10]]
    table_data.append(cha)

checklist_layout = [
    [sg.Table(values=table_data,
        headings=["Chk","Parameter","Unit"],
        max_col_width=param_num,
        auto_size_columns=False,
        display_row_numbers=True,
        justification="right",
        select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
        enable_events=True,
        key='-TABLE-',
        row_height=15,
        font='Helvetica 9',
        col_widths = [5,30,8],
        size = (1,60)
        )],
    [sg.Button("Start"),sg.Button("Exit")]
]

window_checklist = sg.Window("SSM Measurement Tool v1.0", checklist_layout, resizable=True)

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

def checklist_display():
    global selected_index
    global selected_num
    event, values = window_checklist.read()
    
    if event == '-TABLE-' and values[event]:
        row = values[event][0]
        if table_data[row][0] == BLANK_BOX:
            table_data[row][0] = CHECKED_BOX
        else:
            table_data[row][0] = BLANK_BOX
        window_checklist['-TABLE-'].update(values=table_data)
        
    if event == 'Start':
        # 選択したパラメータのIndexを取得
        table_selected = [table_data[i][0] for i in range(param_num)]
        selected_index = my_index_multi(table_selected,CHECKED_BOX)
        selected_num = len(selected_index)        
        print("Checked Index: {}".format(selected_index))
        
        if selected_index:      # チェック入れたか判定
            print("-----Start Measurement!-----")
            window_checklist.close()
            time.sleep(1)
            return 1
        else:
            print("-----Please Put Check Mark and Push 'Start' Button!-----")
            return 0
    
    if (event == sg.WIN_CLOSED) or (event == 'Exit') or (event == None):
        print("-----Bye-----")
        window_checklist.close()
        return 3
    else:
        return 0