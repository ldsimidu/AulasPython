#WHILE UTILIZANDO 'NOT'

num = input('Me da um numero ae paizao: ')
while not num.isnumeric():
    num = input('Me da um numero ae paizao: ')
#CONVERSÃO:
num = int(num)
print(num)