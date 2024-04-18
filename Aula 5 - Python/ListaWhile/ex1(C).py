while True:
    nota = input("Insira sua nota: ")
    if nota.isnumeric():
        nota = int(nota)
        if int(nota) > 0 and int(nota) < 10:
            break
        print('Você não digitou um número entre 0 e 10')
    else:
        print('Você não digitou um número')