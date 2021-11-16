# REFAZER DESAFIO 009 USANDO LAÇO FOR
from time import sleep
from emoji import emojize
num = int(input('Me diga um número, e direi sua tabuada: '))
a = 0
print('\nCalculando...\n'), sleep(2)
for v in range(0, 10):
    print('\033[1;30;43m{} x {} = {}\033[m'.format(num, a, num*a))
    a += 1
    print('-'*10)
print(emojize('\nFoi um prazer poder ajudar :smile:', use_aliases=True))