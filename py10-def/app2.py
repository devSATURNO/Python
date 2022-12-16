def regist(nome, idade):
    nome = str(input('Qual o seu nome?: '))
    idade = int(input('Qual a sua idade?: '))
    if nome == 'Lécio':
        print('Bonito')
    elif idade == 15:
        print('Gostoso')
    else:
        print('ok')
    regist(nome,idade)
