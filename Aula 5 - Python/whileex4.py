# EXERCICIO SOMA 01 (1 + 2 + 3 + ... + 98 + 99 + 100)

num1 = 1
num2 = 2

i = 1
soma = num1 + num2

while i < 50:
    num1 += 2
    num2 += 2

    soma += num1 + num2
    i += 1

print(f'A soma de 1 + 2 + 3 + ... + 98 + 99 + 100 = {soma}')