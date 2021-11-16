# PARES NO INTERVALO DE 1-50
from time import sleep
from emoji import emojize
print('Qual o período que você quer contar? ')
ini = int(input('\nINÍCIO: '))
fin = int(input('FINAL: '))
print()
for c in range(ini, fin+2):
    if (c % 2) == 0:
        print('\033[1;30;45m{}\033[mé PAR'.format(c))
print(emojize('\nFIM DA CONTAGEM:smile:',use_aliases=True))
