lista = ['lucas', 'marcos', 'djalma', 'gabriel', 'caio', 'ricardo']
buscar = 'lucas'
achou = False
for i in range(len(lista)):
    if lista[i] == buscar:
        achou = True
        print('Achei o Lucas')
        break

if achou == False:
    print('nao achei o mlk')
