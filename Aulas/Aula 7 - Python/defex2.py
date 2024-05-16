def voto(nome, idade):
    if idade < 16:
        return(False)
    else:
        return(True)

eleitor = input('Nome: ')
idade = int(input('Idade: '))

while True:

    if not idade:
        break

    if voto(eleitor, idade):
        print('Pode votar paezao')
    else:
        print('n pd votar')
        
print('fim')
