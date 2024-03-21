v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))
v3 = int(input('Insira o terceiro valor: '))

if v1>v2 and v1>v3:
    print(f'{v1} é o maior valor.')
elif v2>v3:
    print(f'{v2} é o maior valor.')
else:
    print(f'{v3} é o maior valor.')