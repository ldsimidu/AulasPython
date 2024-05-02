#PEÇA 10 NUMEROS PARA O USUARIO E CONTE A QUANTIDADE DE PARES E IMPARES
print('EXERCICIO 2')
par = 0
imp = 0
for i in range(10):
    num = input('INSIRA UM NUMERO: ')
    while not num.isnumeric():
        num = input('Insira um numero: ')
    num = int(num)
    
    if num%2 == 0:
        par += 1
    else:
        imp += 1

print(f'NUMEROS PARES: {par}\nNUMEROS IMPARES: {imp}')