print('''
[1]Idoso
[2]Gestante
[3]deficiente
[4]Nenhuma delas''')
user = int(input('Diga a sua condiç~so atual: '))
if user == 1 or user == 2 or user == 3:
    print('Pode tomar o lugar.')
else:
    print('Não pode tomar o lugar.')  