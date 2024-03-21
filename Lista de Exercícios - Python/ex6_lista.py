s = int(input('Insira o sexo, masculino(1) ou feminino(2): '))
h = float(input('Insira sua altura: '))

if s == 1:
    pi = (72.7 * h) - 58
else:
    pi = (62.1 * h) - 44.7

print(f'Tendo em vista seu sexo ({s}) e sua altura de {h}, seu Peso Ideal é {pi}')
