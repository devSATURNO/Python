n = 0
tr = int(input('Diga o primeiro termo: '))
tp = int(input('Qual o factor de progressão: '))
termo = tr
cont = 1
while cont <= 10:
    print(f'{termo}')
    termo += tp
    cont += 1

