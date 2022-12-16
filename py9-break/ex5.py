total = totmil = menor = cont = 0
while True:
    produtos = str(input('Diga o nome do produto: '))
    preço = float(input('Diga o preço do produto: '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar(S/N): '))
    if resp == 'N':
        break

print(f'O gasto total foi de {total}')
print(f'ao todo foram {totmil} compras acima de 1000')
