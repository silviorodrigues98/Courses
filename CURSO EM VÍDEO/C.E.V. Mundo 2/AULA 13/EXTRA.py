num = int(input('Diga um número: '))
print('0', end='')
for bin in range(0,num):
    if num // 2 != 0:
        num = num // 2
        print(num%2,end='')

