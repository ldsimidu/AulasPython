while True:
    try:
        flag1 = "primeiro"
        flag2 = "inteiro"
        a = int(input("Diga um numero: "))
        flag1 = "segundo"
        flag2 = "float"
        b = float(input("Diga outro numero: "))
        print(a/b)
    except ValueError:
        print(f"O {flag1} numero tem que ser {flag2}")
    except ZeroDivisionError:
        print('nao divide por zero porra')

            
    
            
        
            
