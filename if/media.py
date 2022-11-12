mac = float(input('Diga a média do aluno:'))
pp = float(input('Diga a média do aluno: '))
pt = float(input('Diga a média do aluno:'))

mf = (mac + pp + pt)/3
print(f'Amédia final do aluno foi {mf}')

if mf < 10:
    print('Não apto.')
if mf == 9:
    print('Recurso')
if mf >= 10:
    print('Apto')