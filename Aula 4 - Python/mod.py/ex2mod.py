n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))
n3 = int(input('Insira outro número: '))
n4 = int(input('Insira outro número: '))
n5 = int(input('Insira outro número: '))

qtdpar = 0
qtdimp = 0

if n1%2 == 0:
    qtdpar = qtdpar + 1
else:
    qtdimp = qtdimp + 1

if n2%2 == 0:
    qtdpar = qtdpar + 1
else:
    qtdimp = qtdimp + 1

if n3%2 == 0:
    qtdpar = qtdpar + 1
else:
    qtdimp = qtdimp + 1

if n4%2 == 0:
    qtdpar = qtdpar + 1
else:
    qtdimp = qtdimp + 1

if n5%2 == 0:
    qtdpar = qtdpar + 1
else:
    qtdimp = qtdimp + 1



print(f'Você escreveu {qtdpar} números pares e {qtdimp} números ímpares')

