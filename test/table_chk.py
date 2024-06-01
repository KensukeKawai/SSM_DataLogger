#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string

"""
    Basic use of the Table Element
    
    Copyright 2022 PySimpleGUI
"""

BLANK_BOX = '☐'
CHECKED_BOX = '☑'

# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [BLANK_BOX if i % 2 else CHECKED_BOX] + [word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x])+' ..' for x in range(len(data[0]))]

# ------ Window Layout ------
layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    auto_size_columns=False,
                    col_widths=[10, 10, 20, 20 ,30, 5],
                    # cols_justification=('left','center','right','c', 'l', 'bad'),       # Added on GitHub only as of June 2022
                    display_row_numbers=True,
                    justification='center',
                    num_rows=20,
                    # alternating_row_color='lightblue',
                    key='-TABLE-',
                    selected_row_colors='red on yellow',
                    enable_events=True,
                    expand_x=False,
                    expand_y=True,
                    vertical_scroll_only=False,
                    # select_mode=sg.TABLE_SELECT_MODE_EXTENDED,
                    enable_click_events=True,           # Comment out to not enable header and other clicks
                    tooltip='This is a table', font='_ 14')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Change Colors')],
          [sg.Text('Read = read which rows are selected')],
          [sg.Text('Double = double the amount of data in the table')],
          [sg.Text('Change Colors = Changes the colors of rows 8 and 9'), sg.Sizegrip()]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout, resizable=True)

# ------ Event Loop ------
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Double':
        for i in range(1,len(data)):
            data.append(data[i])
        window['-TABLE-'].update(values=data[1:][:])
    elif event == 'Change Colors':
        window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))
    elif event == '-TABLE-' and values[event]:
        row = values[event][0] + 1
        data[row][0] = CHECKED_BOX if data[row][0] == BLANK_BOX else BLANK_BOX
        window['-TABLE-'].update(values=data[1:][:])

window.close()

