qtd = 0
pares = 0
while qtd < 10:
    num = input(f'Insira {qtd + 1} número: ')
    if not num.isnumeric():
        num = input(f'Insira {qtd + 1} número: ')
        continue
    num = int(num)
    if num % 2 == 0:
        pares = pares + 1
    qtd = qtd + 1
impares = qtd - pares
print(impares)