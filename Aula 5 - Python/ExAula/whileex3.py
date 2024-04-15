# While (Senha Tentativas Limitadas)

senha_cadastrada = '1234'
senha = input('Digite sua senha: ')
cont = 1

while senha_cadastrada != senha and cont < 3:
    print(f'VOCE E HACKER??? Voce so tem mais {3 - cont} tentativas')
    print('ACESSO NEGADO')
    senha = input('Digite sua senha novamente: ')
    cont += 1

if senha == senha_cadastrada:
    print('ACESSO PERMITIDO')
else:
    print('SAI HACKER!!!')