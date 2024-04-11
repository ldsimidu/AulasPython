# While (Senha)

senha_cadastrada = '1234'
senha = input('Digite sua senha: ')

while senha_cadastrada != senha:
    print('ACESSO NEGADO')
    senha = input('Digite sua senha novamente: ')

print('ACESSO PERMITIDO')