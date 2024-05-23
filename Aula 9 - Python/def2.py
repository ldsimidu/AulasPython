def verifica_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num

def meu_index(lista,buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
        return False

