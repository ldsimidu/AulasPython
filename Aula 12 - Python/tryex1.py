#causando um erro propositalmente
opcoes = ['a','b','c']
while True:
    try:
        opcao = input(f'Diga uma dessas opções: {opcoes}')
        if opcao not in opcoes:
            raise 
    except:
        print('Opção inválida')