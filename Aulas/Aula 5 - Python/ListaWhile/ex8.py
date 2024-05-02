a = 1
b = 1
print(a, end= ' ')
print(b, end= ' ')
qtd = 10
i = 2
while i < qtd:
    c = a + b
    print(c/b)
    print(c, end=' ')
    a = b
    b = c
    i += 1