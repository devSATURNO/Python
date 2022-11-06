from socket import SOMAXCONN


n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

print('''
[+]Soma
[-]Subtração
[x]Multiplicação
[:]Divisào''')

userchoice = input('Qual a operação desejada: ')

soma = n1+n2

subtracao = n1 - n2

multiplicacao = n1 * n2

divisao = n1/n2

if userchoice == soma :
    print(soma)

if userchoice == subtracao :
    print(subtracao)

if userchoice == multiplicacao :
    print(multiplicacao)

if userchoice == divisao :
    print(divisao)

else:
    print('Operação não suportada.')
