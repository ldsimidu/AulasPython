def verifica_numero(msg,msg_erro):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    num = int(num)
    return num

qtd = verifica_numero("Diga a qtd: ", 'Qtd deve ser um numero!')
ano = verifica_numero("Diga seu ano de nascimento: ",'Ano é um número!')
print(qtd,ano)