print('--INSIRA AS MEDIDAS DOS LADOS DO TRIÂNGULO--')
l1 = int(input('Insira a primeira medida: '))
l2 = int(input('Insira a segunda medida: '))
l3 = int(input('Insira a terceira medida: '))

if l1 == l2 and l1 == l3:
    print('TRINÂNGULO EQUILÁTERO')
elif l2 == l3 or l1 == l2 or l1 == l3:
    print('TRINÂNGULO ISÓCELES') 
else:
    print('TRINÂNGULO ESCALENO')