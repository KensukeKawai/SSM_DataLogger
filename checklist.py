
import time
import param
import PySimpleGUI as sg

BLANK_BOX = '☐'
CHECKED_BOX = '☑'
table_data = []
selected_index = []
measure_layout = []

check_sequence = 0
# 0:View List
# 1:Put Check Mark and 'Start'
# 2:Not Put Check Mark and 'Start'
# 3:CLOSED or 'Exit'

param_num = len(param.param_list)

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

window_checklist = sg.Window("SSM Measuring Tool v1.0", checklist_layout, resizable=True)


def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

def measure_init():
    measure_layout.extend([sg.Text(key=param.param_list[selected_index[i]][0])] for i in range(selected_num))
    return sg.Window("SSM Measurement Tool v1.0",measure_layout,resizable=True)

def measure_update(receive_data):
    window_measure.read(timeout=0, timeout_key="-timeout-") # timeout=0にすれば即時updateで更新可能
    [window_measure[param.param_list[selected_index[i]][0]].update(receive_data[i]) for i in range(selected_num)]

while True:
    event, values = window_checklist.read()
    # print(event, values)
    
    if event == '-TABLE-' and values[event]:
        row = values[event][0]
        if table_data[row][0] == BLANK_BOX:
            table_data[row][0] = CHECKED_BOX
        else:
            table_data[row][0] = BLANK_BOX
        window_checklist['-TABLE-'].update(values=table_data)
        
    if event in (None, 'Start'):
        # 選択したパラメータのIndexを取得
        table_selected = [table_data[i][0] for i in range(param_num)]
        selected_index = my_index_multi(table_selected,CHECKED_BOX)
        selected_num = len(selected_index)
        print("Checked Index: {}".format(selected_index))
        check_sequence = 1 if selected_index else 2     # チェック入れたか判定
        if check_sequence == 1:
            print("-----Start Measurement!-----")
            window_measure = measure_init()
            time.sleep(1)
            break
        else:
            print("-----Please Put Check Mark and Push 'Start' Button!-----")
    
    if (event == sg.WIN_CLOSED) or (event in (None,'Exit')):
        check_sequence = 3
        print("-----Bye-----")
        break

window_checklist.close()
