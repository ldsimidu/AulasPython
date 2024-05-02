i = 0
primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
while True:
    num = input(f'Diga o {i} número: ')
    while not num.isnumeric():
        num = input('Diga um número: ')
    num = int(num)
    if num <= 25:
        primeiro += 1
    elif num <= 50:
        segundo += 1
    elif num <= 75:
        terceiro += 1
    elif num <= 100:
        quarto += 1
    else:
        break
    i += 1
    print(f'Você digitou {primeiro} números entre 0 a 25\n')
    print(f'Você digitou {segundo} números entre 25 a 50\n')
    print(f'Você digitou {terceiro} números entre 50 a 75\n')
    print(f'Você digitou {quarto} números entre 75 a 100\n')

