salario = 1000
taxa = 0.015
partida = 1995
while partida < 2000:
    salario *= 1 + taxa
    taxa *= 2
    partida += 1
print(salario)