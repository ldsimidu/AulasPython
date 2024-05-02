#
#CHECKPOINT 01 - LUCAS DERENZE SIMIDU 1ESA
#
print('---| BOAS VINDAS A VINHERIA AGNELLO |---')
print('')
endereco = input('Por favor, insira seu endereço: ')
datanasc = int(input('Agora, por favor, insira seu ano de nascimento: '))


if 2024 - datanasc < 18:
    print('Você não pode entrar neste site, não é permitida a venda de bebidas alcoolicas para menores de 18 anos.')
else:
    print('')
    print('---| TABELA DE VINHOS |---')
    print('')
    print('1 - Chateau Le Pin | R$ 27,000') #VINHO 1
    print('')
    print('2 - Merci Bo Cue   | R$ 85,00') #VINHO 2
    print('')
    print('3 - Buce Tin Mor   | R$ 560,00') #VINHO 3
    print('')
    print('4 - Pi Cader Mell  | R$ 90,00') #VINHO 4
    print('')
    print('5 - Chateau Rose   | R$ 74,00') #VINHO 5
    print('')
    print('--------------------------------------')
    vin = int(input("Qual dos vinhos acima você quer escolher para compra? (1/2/3/4/5): "))
    qtd = int(input("Qual a quantidade de garrafas que você deseja comprar?: "))

    vinho1 = 27000
    vinho2 = 85
    vinho3 = 560
    vinho4 = 90
    vinho5 = 74


    if vin == 1:
        preco = vinho1 * qtd
    elif vin == 2:
        preco = vinho2 * qtd
    elif vin == 3:
        preco = vinho3 * qtd
    elif vin == 4:
        preco = vinho4 * qtd
    elif vin == 5:
        preco = vinho5 * qtd
    else:
        print("Vinho não identificado!")

    print('')
    print(f'O valor total será de R${preco}!')
    
    if preco > 100:
        print('')
        print(f'Por conta do valor gasto ser R${preco}, já que é um valor maior que R$100, seu frete será grátis!')
    else:
        print('')
        print(f'Por conta do valor gasto ser R${preco} e seu endereço ser {endereco}, você receberá R$30,00 de frete!')
        preco = preco + 30
    
    print('')
    print("---| MUITO OBRIGADO PELA SUA COMPRA! VOLTE SEMPRE AO NOSSO SITE! |---")
    print('')
    print(f'Seu valor gasto total é de: R${preco}')
    print('')



