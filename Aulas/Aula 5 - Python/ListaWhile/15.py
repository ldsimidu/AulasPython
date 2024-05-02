boldonario = 0
polvo = 0
papa = 0
daciolo = 0
nulo = 0
branco = 0

print('------ URNA ELETRÔNICA ------')
print('')
print('1 - CAIR BOLDONARIO')
print('')
print('2 - POLVO INÁCIO DA SILVA')
print('')
print('3 - PAPA FRANCISCO')
print('')
print('4 - DACIOLO')
print('')
print('5 - NULO')
print('')
print('6 - BRANCO')
print('')


while True:
    voto = input('QUAL CANDIDATO DESEJA VOTAR? (0 PARA SAIR): ')
    while not(voto == '0' or voto == '1' or voto == '2' or voto == '3' or voto == '4' or voto == '5' or voto == '6'):
        print('------ URNA ELETRÔNICA ------')
        print('')
        print('1 - CAIR BOLDONARIO')
        print('')
        print('2 - POLVO INÁCIO DA SILVA')
        print('')
        print('3 - PAPA FRANCISCO')
        print('')
        print('4 - DACIOLO')
        print('')
        print('5 - NULO')
        print('')
        print('6 - BRANCO')
        print('')
        voto = input('QUAL CANDIDATO DESEJA VOTAR? (0 PARA SAIR): ')

    if voto == '0':
        print('SESSÃO ENCERRADA')
        break
    elif voto == '1':
        boldonario += 1
    elif voto == '2':
        polvo += 1
    elif voto == '3':
        papa += 1
    elif voto == '4':
        daciolo += 1
    elif voto == '5':
        nulo += 1
    elif voto == '6':
        branco += 1
    else:
        branco += 1

    total = boldonario + polvo + papa + daciolo

    print('VOTO COMPUTADO')
    print('')
    print('------ RESULTADOS ------')
    print('')
    print(f'CAIR BOLDONARIO RECEBEU {boldonario} VOTOS')
    print('')
    print(f'CAIR POLVO INÁCIO DA SILVA RECEBEU {polvo} VOTOS')
    print('')
    print(f'CAIR PAPA FRANCISCO RECEBEU {papa} VOTOS')
    print('')
    print(f'CAIR DACIOLO RECEBEU {daciolo} VOTOS')
    print('')
    print('-------------------------------------------')
    print('')
    print(f'NULOS FORAM {100*nulo/total:.2f}% VOTOS')
    print('')
    print(f'BRANCOS RECEBEU {100*branco/total:.2f}% VOTOS')
    print('')
    print('')
    print(f'O TOTAL DE VOTOS FORAM {total}')
    print('')
