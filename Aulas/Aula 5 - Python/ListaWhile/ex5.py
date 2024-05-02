a = input('Insira um número: ')
while not a.isnumeric():
    a = input('Insira um número: ')
a = int(a)

b = input('Insira um número: ')
while not b.isnumeric():
    b = input('Insira um número: ')
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a)
    a += 1