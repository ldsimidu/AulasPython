i = 2
num = 17
while i < num:
    print(f'{num}%{i} = {num%i}')
    if num % i == 0:
        print(f'{num} não é primo!')
        break
    i += 1
    if i == num - 1:
        print('é primo')
    

print('--------------------')

i = 2
num = 17
while i < num/2:
    print(f'{num}%{i} = {num%i}')
    if num % i == 0:
        print(f'{num} não é primo!')
        break
    i += 1
    if i == num/2:
        print('é primo')


print('--------------------')

i = 2
num = 17
while i < num**0.5:
    print(f'{num}%{i} = {num%i}')
    if num % i == 0:
        print(f'{num} não é primo!')
        break
    i += 1
    if i == num**0.5:
        print('é primo')