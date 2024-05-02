profs = ['Andre','Lucas','Yan','Danilo','Allen','Fabio','Celso']
achou = False
for i in range(len(profs)):
    if profs[i] == 'Danilo':
        achou = True
        print(f'Achei o {profs[i]} no índice {i}')
        break
if achou == False:
    print('Não ta na lista')
