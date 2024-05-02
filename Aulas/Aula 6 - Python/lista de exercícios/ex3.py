#PEÇA 10 NUMEROS PARA O USUARIO E FAÇA A SOMA E A MEDIA
soma = 0
media = 0
for i in range(10):
    num = input('Insira um número: ')
    while not num.isnumeric():
        num = input('Insira um número: ')
    num = int(num)
    soma += num

media = soma/10
print(media)