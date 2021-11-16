# COMPARADOR DE PESOS.

from time import sleep
from emoji import emojize

print('''{}OLÁ! SEU QUE VOCÊS ADORAM COMPETIR ENTRE SÍ,
E DESSA VEZ A COMPETIÇÃO SERÁ ENTRE O MAIOR E O MENOR PESO.
POR FAVOR, SIGAM AS INSTRUçÕES A SEGUIR PARA INICIARMOS A BRINCADEIRA!{}\n'''.format('\033[1;3;4;30;42m','\033[m'))
p1 = 0
while p1 in range(0,5):
    p1 = float(input('Por favor, digitem o peso de cada um, separadamente: '))
    if p1 > p1:
        print('deu')
