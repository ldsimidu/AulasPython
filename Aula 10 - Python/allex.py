'''import matplotlib.pyplot as plt
def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz
lado = 1000
linhas = lado
colunas = lado
raio = lado//2
raio_menor = 0.99*raio
circulo = cria_matriz(linhas,colunas)
for i in range(linhas):
    for j in range(colunas):
        if abs((i - raio)**2 + (j - raio)**2 - raio**2) <=5*raio:
        #if (i - raio)**2 + (j - raio)**2 <= raio**2 and (i - raio)**2 + (j - raio)**2 >= raio_menor**2:
            circulo[i][j] = 1

plt.imshow(circulo,'Blues')
plt.colorbar()
plt.show()
from random import choice
dic = {"oi": ['ola','salve','aoba','coe'],'tchau':['flw','nois','tmj','marcha']}
while True:
    resp = input("fala oi ou tchau: ")
    print(choice(dic[resp]))'''
'''dic = {
    'chave':'valor'
    'chave2':'valor2'
}
print(dic['chave'])
dic['nova chave'] = 'novo valor'
print(dic)
dic['chave'] = 1
print(dic)'''
'''
dic = {
    'chave' : 1
}
dic['chave'] = [dic['chave']]
dic['chave'].append(3)
print(dic['chave'][1])
dic['chave'] = 4
print(dic)
import pandas as pd
numeros = {'pares':[]}
numeros['impar'] = []

for i in range(20):
    if i%2==0:
        numeros['pares'].append(i)
    else:
        numeros['impar'].append(i)
print(pd.DataFrame(numeros))


frase = 'morumbi é panetone'
frase = frase.replace('morumbi','morumbis')
print(frase)
'''
formas = {
    'tres': 'triângulo',
    'quatro': 'quadrado',
    'cinco': 'pentágono',
    'seis': 'hexágono',
    'sete': 'heptágono',
    'oito': 'octógono',
}
escolhido = input("Digite quantos lados tem a forma:\n->")
for key in formas.keys():
    escolhido = escolhido.replace(key,formas[key])
escolhido.replace('','')
print(escolhido)