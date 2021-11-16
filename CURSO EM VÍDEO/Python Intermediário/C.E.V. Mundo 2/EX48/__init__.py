# SOMA DE TODOS OS NÚMEROS  NO INTERVALO
from time import sleep
from emoji import emojize
s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c
        print(emojize(':imp:', use_aliases=True), c)
print('A SOMA ENTRE ELES É: {}{:.2f}{}'.format('\033[1;30;46m',s ,'\033[m'))
