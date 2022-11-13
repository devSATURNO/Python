from random import randint

item = ( 'pedra', 'papel', 'tesora')

print('''
[0]pedra
[1]papel
[2]tesoura''')
computador = randint(0,2)

user = int(input('Diga a sua escolha: '))
print(f'Computador jogou {computador}')

if computador == 0:
    if user == 0:
        print('empate')
    elif user == 1:
        print('Jogador ganhou!')
    elif user == 2:
        print('Jogador perdeu')
elif computador == 1:
    if user == 0:
        print('jogador ganhou ')
    elif user == 1:
        print('empate')
    elif user == 2:
        print('jogador prdeu')
elif computador == 2:
    if user == 0:
        print('jogador ganhou')
    elif user == 1:
        print('Jogador perdeu')
    elif user == 2:
        print('empate')
