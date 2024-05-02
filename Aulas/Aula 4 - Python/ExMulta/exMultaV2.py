v = int(input('Insira a velocidade do carro: '))
multa = ''
if v <= 100:
    multa = 0
    print('Isento')
if v <= 120:
    multa = (20/100)*v

elif v <= 150:
    multa = (20/100)*120 + (30/100)*v
else:
    multa = (20/100)*120 + (30/100)*150 + (40/100)*v
    
print(multa)



#ATÉ 100 - isento
#ATÉ 120 - 20% da v
#ATÉ 150 - 20% 120 + 30% da v
# > 150 - 20% 120 + 30% 150 + 40% da v