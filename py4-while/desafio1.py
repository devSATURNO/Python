n = 0
male = 'm'
female = 'f'

while n != 0:
    gender = str(input('What is your gender'))
    if gender == male:
        print('Hello sir')
    if gender == female:
        print('Hello mam')
    else:
        print('Invalid')
    n = n + 1
    
    