# FUNÇÃO QUE RECEBE UMA STRING E CONTA A QUANTIDADE VOGAIS

def meu_in(lista_elementos, elementos):
    for i in range(len(lista_elementos)):
        if lista_elementos[i] == elementos:
            return True
    return False

def conta_vogais(palavra):
    vogais = ['a','e','i','o','u']
    qtd_vogais = 0
    for char in palavra:
        if char in vogais:
            qtd_vogais += 1
        return qtd_vogais

palavra = 'pastel'
qtd_vogais = conta_vogais(palavra)
print(f'{palavra} tem ^{qtd_vogais}')