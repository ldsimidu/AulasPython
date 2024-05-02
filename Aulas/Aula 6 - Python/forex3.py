senha_cadastrada = '1234'
for i in range(5):
    senha = input('Diga a sua senha: ')
    if senha == senha_cadastrada:
        print('ACESSO LIBERADO!')
        break
    print(f'VOCE É HACKER SEU CANALHA, VOCE TEM {4 - i} TENTATIVAS')
if senha != senha_cadastrada:
    print('SAI SEU CANALHA')