num = 1

while num < 10:
    i = 1
    while i <= 10:
        print('')
        print(f'{num} X {i} = {num*i}')
        print('')
        i = i + 1
        if i == 11:
            print('---------')
    num = num + 1