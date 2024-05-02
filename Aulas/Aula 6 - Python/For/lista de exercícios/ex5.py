vogais = 0
palavra = input('Diga uma palavra: ')
for char in palavra:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vogais += 1
print(f'Há {vogais} vogais e {len(palavra) - vogais} consoantes na sua palavra')