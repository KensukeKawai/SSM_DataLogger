
# https://docs.pysimplegui.com/en/latest/cookbook/ecookbook/layouts/to-do-list-using-generated-layout/

from PySimpleGUI import Window, Text, Button, CBox, Input, theme

theme('DarkAmber')   # Add a little color for fun

layout =  [[Text('My To Do List', font='Helvetica 15')]]  # a title line t
layout += [[Text(f'{i}. '), CBox('', key=f'-CB{i}-'), Input(k=f'-IN{i}-')] for i in range(1, 6)]  # the checkboxes and descriptions
layout += [[Button('Save'), Button('Load'), Button('Exit')]]  # the buttons

window = Window('To Do List Example', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break

window.close()
