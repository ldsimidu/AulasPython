 
nome = input('Qual é o seu nome?: ')
while len(nome) < 3:
    nome = input('Qual é o seu nome?: ')

while True:
    idade = input('Qual a sua idade?: ')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        else:
            print('IDADE INVÁLIDA')
    else:
        print('O VALOR DEVE SER UM NÚMERO')

while True:
    salario = input('Qual o seu salário?: ')
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
         break

sexo = input('Qual o seu sexo(f/m)?: ')
while not(sexo == 'f' or sexo == 'm'):
    sexo = input('Qual o seu sexo(f/m)?: ')
    break

eCivil = input('Insira seu Estado Civil(s/c/v/d): ')
while not(eCivil == 's' or eCivil == 'c' or eCivil == 'v' or eCivil == 'd'):
    eCivil = input('Insira seu Estado Civil(s/c/v/d): ')

print(f'Seus dados são: {nome}, {idade}, R${salario}, {sexo} e {eCivil}')
