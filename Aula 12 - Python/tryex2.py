#PEÇA PARA O USUARIO DIGITAR UMA CHAVE DO DICIONARIO E UM INDEICE, PRINT O ELEMENTO 
#CORRESPONDENTE A ESSES INDICE NA LISTA DA CHAVE

dic = {
    'chave1':[1,2,3,4],
    'chave2':[5,6,7,8]
}
while True:
    try:
        chave = input(f"Diga um chave: {dic.keys()}")
        
        if chave not in dic.keys():
            raise KeyError
        
        i = int(input("Diga um indice: "))
        print(dic[chave][i])
    except ValueError:
        print("Deve ser numero")
    except IndexError:
        print("Esse indice nao existe") 
    except KeyError:
        print("somente as chaves disponiveis")
