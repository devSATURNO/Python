from PySimpleGUI import PySimpleGUI as sg
#layout
sg.theme('Reddit')
layout=[
    [sg.Text('user'), sg.Input(key='user')],
    [sg.Text('password'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('entrar')]
]
#janela
janela= sg.Window('tela de login', layout)
#lereventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'entrar':
        if valores['user'] =='lecio' and valores['password'] == '12345':
            print('welcome')
