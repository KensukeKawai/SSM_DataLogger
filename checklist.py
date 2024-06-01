import numpy as np
import param
import PySimpleGUI as sg
import string

BLANK_BOX = '☐'
CHECKED_BOX = '☑'

param_num = len(param.param_list)

table_data = []
for i in range(param_num):
    cha = [BLANK_BOX, param.param_list[i][0], param.param_list[i][10]]
    table_data.append(cha)

layout = [
    [sg.Table(values=table_data,
        headings=["Chk","Parameter","Unit"],
        max_col_width=param_num,
        auto_size_columns=False,
        display_row_numbers=True,
        justification="right",
        select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
        enable_events=True,
        key='-TABLE-',
        row_height=14,
        font='Helvetica 10',
        col_widths = [5,30,8],
        size = (1,60)
        )],
    [sg.Button("OK"),sg.Button("Exit")]
]
window = sg.Window("Table Widget Example", layout, resizable=True)
table = window['-TABLE-']

while True:
    event, values = window.read()
    print(event, values)
    if event == '-TABLE-' and values[event]:
        row = values[event][0]
        if table_data[row][0] == BLANK_BOX:
            table_data[row][0] = CHECKED_BOX
        else:
            table_data[row][0] = BLANK_BOX
        window['-TABLE-'].update(values=table_data)
        
    if event == sg.WIN_CLOSED:
        break
    if event in (None,'Exit'):
        break

window.close()
