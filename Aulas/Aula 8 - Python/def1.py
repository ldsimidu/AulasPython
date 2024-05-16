def checa_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num #return -> torna variável indepentedente

anonas = checa_numero('Diga seu ano de nascimento: ')
qtdgar = checa_numero('Diga a quantidade de garrafas: ')
print(anonas, qtdgar)