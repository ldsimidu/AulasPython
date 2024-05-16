#FUNÇÃO QUE RECEBE UMA LISTA DE NÚMEROS E RETORNA A SOMA DOS NÚMEROS

def somaNum(lista):
    for i in range(len(lista)):
        return sum(lista)
   
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = somaNum(lista)
print(soma)