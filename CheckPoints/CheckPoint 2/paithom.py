vinho1 = 'penis'
vinho2 = 'xoxota'
vinho3 = 'peitihos'
preco1 = 10
preco2 = 20
preco3 = 30
ferte = 10
valor_total = 0
qtd1 = 0
qtd2 = 0
qtd3 = 0
opcoes = f'{vinho1} - {preco1}\n{vinho2} - {preco2}\n{vinho3} - {preco3}'

print('bem vindo')
ano = input('diga seu nascimeno: ')
while not ano.isnumeric:
    ano = input('diga seu nascimeno: ') 
ano = int(ano)   
idade = 2024 - ano
if idade < 18:
    print('cai fora')
else:
    endereço = input('dia seu endereço: ')
    while True:
        print(f'escolhe ai {opcoes}')
        escolha = input('qq ce quer\n--->')
        while not (escolha == vinho1 or escolha == vinho2 or escolha == vinho3):
            print(f'errou caralho burro escolhe ai: \n{opcoes}')
            escolha = input('qq ce quer\n--->')
        qtd = input(f'quantas birita de {escolha} ce quer --->')
        while not qtd.isnumeric():
            print('Deve ser um numero: ')
            qtd = input(f'quantas birita de {escolha} ce quer --->')
        qtd = int(qtd)
        if escolha == vinho1:
            valor_atual = preco1*qtd
            qtd1 += qtd
        elif escolha == vinho2:
            valor_atual = preco2*qtd
            qtd2 += qtd
        else:
            valor_atual = preco3*qtd
            qtd3 = qtd
        valor_total += valor_atual
        proceder = input('quer mais seu alcoolatra fudido? (s/n): ')
        while proceder != 's' and proceder != 'n':
            print('fala direito fila da puta')
            proceder = input('quer mais seu alcoolatra fudido? (s/n): ')
        if proceder == 'n':
            break
    if valor_total > 500:
        frete = 0
        print('a de graça cuzao')
    valor_total += frete
    print(f'ce vai gastar {valor_total:.2f} conto em'
          f'\n{qtd1} de {vinho1}\n{qtd2} de {vinho2}'
          f'\n{qtd3} de {vinho3}\n e chega ai na {endereço}.')