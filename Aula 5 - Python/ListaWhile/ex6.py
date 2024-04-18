senha = input('Insira sua senha:\n->')
usuario = input('Diga seu usuário:\n->')

while senha == usuario:
    print('O nome de usuário e senha não podem ser iguais')
    senha = input('Insira sua senha:\n->')
    suario = input('Diga seu usuário:\n->')