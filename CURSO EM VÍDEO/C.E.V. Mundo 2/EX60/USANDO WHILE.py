'''FIZ COM FOR, AGORA TO TENTANDO COM WHILE '''
from time import sleep
from emoji import emojize

num1 = int(input('Digite o número o qual você quer saber o fatorial: '))
num = num1
res = 1

while not num == 1:
    res *= num
    print('{}'.format(num), end='x')
    num -= 1
    if num == 1:
        print('''1
A fatorial de {}! é >> {}'''.format(num1, res))
