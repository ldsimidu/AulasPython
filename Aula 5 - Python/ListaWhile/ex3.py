paisA = 80000
paisB = 200000
ano = 0
while not(paisA >= paisB):
    paisA = paisA + paisA * 0.03
    paisB = paisB + paisB * 0.015
    ano += 1

print(f'A população do País A será {paisA:.2f} e do País B será {paisB:.2f} no ano {ano}')
