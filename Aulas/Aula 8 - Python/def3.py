def meu_in(lista_elementos, elemento):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return True
    return False




lista = ['lucas', 'marcos', 'djalma', 'gabriel', 'caio', 'ricardo']
buscar = 'lucas'

pdp = meu_in(lista, buscar)
print(pdp)
