num = input('Diga um número: ')
while not num.isnumeric():
    num = input('Diga um número')
num = int(num)
fatorial = num
fatorial_string = f'{num} != {num}'
while num > 1:
    num -= 1
    fatorial *= num
    fatorial_string += f'*{num}'
fatorial_string += f' = {fatorial}'
print(fatorial_string)