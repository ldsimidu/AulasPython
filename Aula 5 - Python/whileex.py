qtd = 0
par = 0

while qtd < 5:
    num = int(input("Diga um número: "))
    if num % 2 == 0:
        par = par + 1
    qtd = qtd + 1
print(f"A quantidade de pares é {par} e ímpares é {qtd - par}")