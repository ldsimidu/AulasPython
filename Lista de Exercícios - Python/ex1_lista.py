v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))

v = v1 > v2

if v == True:
    print(f'O valor {v1} é maior que {v2}')
else:
    print(f'O valor {v2} é maior que {v1}')