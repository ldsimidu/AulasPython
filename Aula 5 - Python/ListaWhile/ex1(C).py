while True:
    nota = input("Insira sua nota: ")
    if nota.isnumeric():
        if int(nota) > 0 and int(nota) < 10:
            nota = int(nota)
            break