lista_opcao = ['1','2']

indices = {}


def escolha(lista,msg):
    escolha = input(msg)
    while not escolha in lista:
        print('Sua opção não é valida')
        escolha = input(msg)
    return escolha

def acha_index(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

carros = {
    'modelo' : ['opala','marea','kombi','celtinha','uno','monza','corcel'],
    'potência (cv)' : [172,130,250,140,100,120,150],
    'consumo (km/l)' : [1,3,8,7,15,2,1.5],
    'cor' : ['laranja','verde','branca','preto','prata','preto','corcel'],
    'ano' : ['1972','2004','1985','2014','2001','1980','1975']
}

for i in range(len(carros['modelo'])):
    nome = carros['modelo'][i]
    indices[nome] = i
print(indices)

#print(pd.DataFrame(carros))

'''for key in carros.keys():
    print(key,carros[modelo])'''


opcao_menu = escolha('Qual carro vc quer ver?',carros['modelo'])
index_escolha = acha_index(carros['modelo'], opcao_menu)
for key in carros.key():
    print(key, carros[key][index_escolha])
'''if opcao_menu == '1':
    for i in range(len(carros['modelo']))
    if carros['modelo'][i] == opcao_menu:
        index_escolha = i
        break
for key in carros.key():
    print(key,carro)'''


