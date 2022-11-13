import PySimpleGUI as pg

#step 1: Set the theme
pg.theme('DarkAmber')
#step 2: create layout
layout = [
    [pg.Text('user')],
    [pg.InputText()],
    [pg.Button('ok'), pg.Button('cancel')],
]
#step 3: creat window
window = pg.Window('Feorm', layout)
#step 4: event loop
while True:
    event, values = window.read()
    if event == 'cancel' or  event == pg.WIN_CLOSED :
        break
    print(values[0])
#step 5: close 
window.close()