#
#CHECKPOINT 01 - LUCAS DERENZE SIMIDU 1ESA
#
print('---| BOAS VINDAS A VINHERIA AGNELLO |---')
print('')

while True:
    endereco = input('Insira o seu endereço: ')
    if endereco == "":
         endereco = input('Insira o seu endereço: ')
         continue
    else:
         break

while True:
    anonasc = input("Insira seu ano de nascimento: ")
    if anonasc.isnumeric():
        anonasc = int(anonasc)

        idade = 2024 - anonasc

        if idade < 18:
            print('SAI DAQUI SEU SAFADO')
        else:
            print('Você é maior de idade, está liberado para acessar o site')
            break

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
while not (vin == 1 or vin == 2 or vin == 3 or vin == 4 or vin == 5):
    vin = int(input("Qual dos vinhos acima você quer escolher para compra? (1/2/3/4/5): "))
    continue
    while True:
        qtd = input("Qual a quantidade de garrafas que você deseja comprar?: ")


    