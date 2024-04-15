nota = input("Insira sua nota: ")
while not nota.isnumeric():
    nota = input("Insira sua nota: ")

print(f'Sua nota é {nota}')