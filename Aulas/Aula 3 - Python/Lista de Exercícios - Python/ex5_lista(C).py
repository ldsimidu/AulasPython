a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
c = int(input('Insira o terceiro valor: '))

maior = a
if b > maior:
    b = maior
    if c > maior:
        c = maior

menor = a
if b < menor:
    menor = b
    if c < menor:
        c = menor
        
meio = a + b + c - menor - maior
print(menor, meio, maior)