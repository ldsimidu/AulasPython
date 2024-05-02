lista = [1, True,3.2,'danilo',['dtdf', False]]
'''print(type(lista))
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
#print(lista[5])'''
lista[4] = input('buceta: ')
print(lista)
for i in range(len(lista)):
    print(f'lista[{i}] = {lista[i]}')

for i in range(len(lista)):
    lista[i] = 1
print(lista)