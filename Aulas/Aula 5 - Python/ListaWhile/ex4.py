cont = 0
soma = 0
media = 0

while cont < 5:
    num = input(f'Diga o {cont + 1} número:\n -> ')
    while not num.isnumeric():
        num = input(f'Diga o {cont + 1} número:\n -> ')
    num = int(num)
    cont = cont + 1
    soma = soma + num
media = soma/cont

print(f'A {soma} e {media}')
