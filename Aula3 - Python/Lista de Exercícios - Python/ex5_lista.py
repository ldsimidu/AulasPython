'''
v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))
v3 = int(input('Insira o terceiro valor: '))

o1 = v1>v2>v3
o2 = v2>v1>v3
o3 = v3>v1>v2
o4 = v1>v3>v2
o5 = v2>v3>v1
o6 = v3>v2>v1

if o1 == True:
    print(f'A ordem crescente dos valores é: {v1},{v2},{v3}')
elif o2 == True:
    print(f'A ordem crescente dos valores é: {v2},{v1},{v3}')
elif o3 == True:
    print(f'A ordem crescente dos valores é: {v3},{v1},{v2}')
elif o4 == True:
    print(f'A ordem crescente dos valores é: {v1},{v3},{v2}')
elif o5 == True:
    print(f'A ordem crescente dos valores é: {v2},{v3},{v1}')
elif o6 == True:
    print(f'A ordem crescente dos valores é: {v3},{v2},{v1}')
'''


'''aux = v1
    v1 = v2
    v2 = aux'''


a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))

if a>b and a>c:
    aux = a
    a = c
    c = aux        
elif b>c:
    aux = b
    b = c
    c = aux
    
if a>b:
    aux = b
    b = a
    a = aux

print(a, b ,c)
