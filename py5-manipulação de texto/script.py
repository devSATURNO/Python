nome = str(input('Diga o seu nome:'))
print('''
[1]miasculas
[2]minusculas
[3]quantas letras tem
[4] quantas letras tem o primeiro''')
user = int(input('DIga a sua escolha: '))
if user == 1:
    print(nome.upper)
elif user == 2:
    print(nome.lower)
elif user == 3:
    print(len(nome.strip))

