from random import randint
pc = randint(1,10)
n= int(input('Digite um número: '))
escolha = str(input('Qual a sua escolha:  '))

while True:
    jogada = n + pc
    div = jogada%2
    if div == 0 and escolha == 'par':
        print('Jogador ganhou!')
    elif div == 1 and escolha == 'impar':
        print('Escolha certa, jogaodr ganhou!')
    else: 
        print('Errado ;-;')
    break