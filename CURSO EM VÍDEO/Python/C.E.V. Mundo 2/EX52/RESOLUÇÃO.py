tot = 0
num = int(input('Número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;3;4;34m', end=' ')
        tot  += 1
    else:
        print('\033[1;3;4;33m', end= ' ')
    print('{}'.format(c), end=' -> ')

print('\033[mO número {} foi divisível{} vezes'.format(num, tot))
if tot == 2:
    print('Por isso, ele É PRIMO')
else:
    print('E por isso, ele NÃO É PRIMO')