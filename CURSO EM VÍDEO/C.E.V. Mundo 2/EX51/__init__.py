# LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRESSÃO ARITIMÉTICA. MOSTRE OS 10 PRIMEIROS TERMOS DA PROGRESSÃO
from time import sleep
from emoji import emojize
import math

print('{}BEM VINDO AO SEU PROGRAMA DE CONTABILIZAÇÃO!!!{}'.format('\033[1;4;3;30;45m','\033[m'))

num = float(input('\nPor favor, digite o primeiro termo da progressão: '))
raz = int(input('\nAgora, digite a razão dessa progressão arítmética: '))

print('\n{:^40}\n'.format('Calculando...')), sleep(1.5)

ter = 1

for ar in range(0, 10):

    ter += 1
    pa = num + (ter- 1) * raz
    print(emojize(':fire:'), pa)

print('\nO valor do Décimo termo é \033[1;3;30;44m{:.0f}\033[m'.format(pa))





