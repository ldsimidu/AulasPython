q = int(input('Insira a quantidade de maçãs compradas: '))

if q >= 12:
    maca = 0.25
else:
    maca = 0.30

v = q*maca
print(f'O cliente levou {q} maçãs, seu valor gasto foi R${v}')