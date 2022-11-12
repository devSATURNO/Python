'''while utilia-se quando queremos repetir um processo sem fim definido
toda vez q usa o while tem que dar valor a variavel primeiro'''

''''n = 1
while n != 0: #dizer diferente em ppython é !=
    n = int(input('Digite um número: '))
print('fim')    '''

''''r = 's'
parar = 'n'
while r == 's':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? S/N: '))
    if r == parar:
        print('teu cu')'''


n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n %2 == 0:
            par += 1
        else:
            impar += 2
print(f'Você digitou {par} números pares e {impar} números impares')
