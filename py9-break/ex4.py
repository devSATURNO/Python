tot18 = totm = totf= 0
while True:
    idade = int(input('Diga a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Diga o se sexo(F/M): '))
        if idade >= 18:
            tot18 += 1
        elif sexo == 'M':
            totm += 1
        elif sexo == 'F' and idade >= 20:
            totf += 1
    resp= ' '
    while resp not in 'SN':
            resp = str(input('Quer continuar(S/N): '))
    if resp == 'N':
        break
print('Acabou')
print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'O total de homens é de {totf} e de mulheres é {totf}')
