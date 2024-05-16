#FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS E TEROTRNA UMA LISTA SOMENTE COM OS PARES

def numPares(lista):
    listapar = []
    for i in lista:
        if i % 2 == 0:
            listapar.append(i)
    return listapar

def numImpares(lista):
    listaimp = []
    for i in lista:
        if i % 2 == 1:
            listaimp.append(i)
    return listaimp

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par = numPares(lista)
print(par)

impar = numImpares(lista)
print(impar)
