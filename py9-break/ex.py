esc = int(input('Digite um número: '))
esc2 = int(input('Digite outro número: '))
n = 0
while n != 5:
    print('''
    [1]Soma
    [2]Subtração
    [3]maior
    [4]Digitar outros números
    [5]sair''')
    n = int(input('Diga a sua esccolha: '))
    if n == 1:
        s = esc + esc2
        print(f'A soma entre {esc} e {esc2} é de {s}')
    elif n == 2:
        sub = esc - esc2
        print(f'A subtração entre{esc} e {esc2} é de {sub}')
    elif n == 3:
        if esc > esc2:
            maior = esc
        else:
            maior = esc2
        print(f'Entre {esc} e {esc2} o maior é {maior}')
    elif n == 4:
        print('Informe os novos valores')
        esc= int(input('Primeiro valor: '))
        esc2 = int(input('Segundo valor: '))
    elif n == 5:
        print('Finalizando...')
        
        

    
print('Fim')