v = int(input('Insira a velocidade do carro: '))

m1 = (20/100)*v
m2 = (20/100)*120 + (30/100)*v
m3 = (20/100)*120 + (30/100)*150 + (40/100)*v

if v <= 100:
    print('Isento')
elif v <= 120:
    print(m1)
elif v <= 150:
    print(m2)
else:
    print(m3)


#ATÉ 100 - isento
#ATÉ 120 - 20% da v
#ATÉ 150 - 20% 120 + 30% da v
# > 150 - 20% 120 + 30% 150 + 40% da v