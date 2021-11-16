# DESCOBRIDOR DE NÚMEROS PRIMOS !
import math
from time import sleep
from emoji import emojize
print('{} SEJAM BEM VINDOS AOS A{:=^9}MORAMENTOS HEHE{}'.format('\033[1;3;4;30;42m','PRIMO', '\033[m'))

num = int(input('\nDigite um número para saber se é ou não primo: '))
div = 2

print(emojize(':sunglasses:{:=^60}:sunglasses:'.format('\nLoading, might take  some time...\n'), use_aliases=True))
sleep(1.5)
for primo in range(0, num):
    if num % div != 0 and num // div > div:
        div += 1
if num % div == 0 and num // div >= div:
    print('Este número não é primo')
elif num % div != 0 and num // div <= div:
    print('Este número é primo')
else:
    print('Este número é primo')




