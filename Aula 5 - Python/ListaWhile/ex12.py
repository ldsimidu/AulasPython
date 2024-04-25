cont = 0
soma = 0
while True:
    qtd = input('Insira a quantidade de notas: ')
    if qtd.isnumeric():
        qtd = int(qtd)
        break
    else:
        print('INSIRA UM VALOR VÁLIDO')
        continue

while cont < qtd:
    n = input('Insira sua nota: ')
    
    if  n.isnumeric():
        n = int(n)
        cont += 1
        soma = soma + n

    else:
        print('INSIRA UM VALOR VÁLIDO')
        continue

media = soma/qtd
print(media)