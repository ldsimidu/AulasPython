'''
print('')
print('----------EXEMPLO 1----------')
print('')

idoso = input('Você é idoso? ')
cad = input('Você é cadeirante? ')
estacionar = False
if idoso == 'sim' or cad == 'sim':
    print('Pode estacionar')
    estacionar = True
else:
    print('Você não pode estacionar')


print('')
print('----------EXEMPLO 2----------')
print('')

c1 = str(input('Digite qualquer caractere: '))

if (c1 == 'a' or c1 == 'e' or c1 == 'i' or c1 == 'o' or c1 == 'u'):
    print(f'{c1} é uma vogal')
else:
    print(f'{c1} é uma consoante')


print('')
print('----------EXEMPLO 3----------')
print('')

nota = int(input('Insira sua nota: '))
if nota >= 6:
    print('Aprovado')
elif nota<6 and nota>= 4:
    print('Exame, piranha')
else:
    print('O SENHOR FIAP TE REPROVOU')


print('')
print('----------EXEMPLO 4----------')
print('')

c1 = str(input('Digite uma letra: '))
v = 'é uma vogal'
vogal = False

if c1 == 'a':
    vogal = True
elif c1 == 'e':
    vogal = True
elif c1 == 'i':
    vogal = True
elif c1 == 'o':
    vogal = True
elif c1 == 'u':
    vogal = True
else:
    print(f'{c1} é uma consoante')
if vogal == True:
    print(f"{c1}", v)
'''

s = float(input('Informe seu salário: R$ '))

d2 = s * 0.075
d3 = s * 0.15
d4 = s * 0.225
d5 = s * 0.275

if s <= 1903.98:
    print('Desconto do seu salário: Isento')

elif s >= 1903.99 and s <= 2826.65:
    s = s - d2
    print(f'Desconto do seu salário: 7,5% ({d2}) e seu salário atual será de {s}')

elif s >= 2826.66 and s <= 3751.05:
    s = s - d3
    print(f'Desconto do seu salário: 15% ({d3}) e seu salário atual será de {s}')

elif s >= 3751.06 and s <= 4664.68:
    s = s - d4
    print('Desconto do seu salário: 22,5%')

elif s > 4664.68:
    s = s - d5
    print('Desconto do seu salário: 27,5%') 

