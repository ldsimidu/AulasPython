print('--INSIRA OS ÂNGULOS DOS TRIÂNGULOS--')
a1 = int(input('Insira o primeiro ângulo: '))
a2 = int(input('Insira o segundo ângulo: '))
a3 = int(input('Insira o terceiro ângulo: '))

if a1 == 90 or a2 == 90 or a3 == 90:
    print('TRINÂNGULO RETÂNGULO')
elif a1 > 90 or a2 > 90 or a3 > 90:
    print('TRINÂNGULO OBTUSÂNGULO')
elif a1 < 90 and a2 < 90 and a3 < 90:
    print('TRINÂNGULO ACUTÂNGULO')