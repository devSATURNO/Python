import random

pc = random.randint(0 , 2)
n = 's'
while n =='s':
    user = int(input('Digite um número: '))
    if user != pc:
        print('Voçê errou!')
        n = str(input('Quer tentar denovo?(s/n): '))
    elif user == pc:
        print('Voçê acertou!')
        break 
print('fim')