def achar_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice_menor = i
        return indice_menor

def meu_index(lista, buscar):
    for i in range (len(lista)):
        if lista[i] == buscar:
            return i
    return False

def meu_in(lista, buscar):
    for i in range (len(lista)):
        if lista[i] == buscar:
            return True
    return False

def forca_opcao(lista_opcoes, msg):
    msg_erro = "\n".join(lista_opcoes)
    opcao = input(msg)
    while not meu_in(lista_opcoes, opcao):
        print(f"Opção inválida! Somente essas: \n{msg_erro}")
        opcao = input(msg)
    return opcao
nomes = ["andre","danilo","celso","lucas","yan","allen","fabio"]
turmas = [2,10,3,1,7,8,1]
nome = forca_opcao(nomes, "Diga um nome: ")
local_nome = meu_index(nomes, nome)
print(f"O professor {nome} tem {turmas[local_nome]} turmas")

indice_maior = 0 
maior = turmas[indice_maior]
for i in range(len(turmas)):
    if turmas[i] > maior:
        maior = turmas[i]
        indice_maior = i