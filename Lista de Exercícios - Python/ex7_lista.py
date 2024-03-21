lados = int(input('Quantos lados seu polígono selecionado possuí? (entre 3 a 5): '))

if lados == 5:
    print('')
    print('Seu polígono é um PENTÁGONO.')
    exit()

m = int(input('Qual a medida doslados deste polígono?: '))

if lados == 3:
    print('')
    print('Seu polígono é um TRIÂNGULO.')
    print('')

    t = (m*m)/2

    print('A fórmula de sua área é: ')
    print('')
    print('A = B*H/2')
    print(f'A = {m}*{m}/2')
    print(f'A = {t}')

elif lados == 4:
    print('')
    print('Seu polígono é um QUADRADO.')
    print('')

    q = m*m

    print('A fórmula de sua área é: ')
    print('')
    print('A = B*H')
    print(f'A = {m}*{m}')
    print(f'A = {q}')
    