def cpf(x):
    digito1 = 0
    digito2 = 0
    pos = 11
    for i in x:
        if pos > 2:
            digito1 += int(i) * (pos - 1)
            digito2 += int(i) * pos
    digito1 = digito1 % 11
    digito1 = 11 - digito1
    if digito1 > 9:
        digito1 = 0
    
    digito2 += digito1 * 2
    digito2 = digito2 % 11
    digito2 = 11 - digito2
    if digito2 > 9:
        digito2 = 0