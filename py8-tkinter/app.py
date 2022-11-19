n1 = float(input('Digite um numero: '))
n2 = float(input('Digite o segunddo numero: '))

print('''
[1]Soma
[2]Subtração
[3]Divisão
[4]Multiplicação''')

calculo = int(input('Qual operação vcê deseija realizar: '))

if calculo == 1:
    print(n1 + n2)
elif calculo == 2:
    print(n1-n2)
elif calculo == 3:
    print(n1/n2)
elif calculo == 4:
    print(n1*n2)
else:
    print('Operação não reconhecida.')