# COMPARADOR DE PESOS.

from time import sleep
from emoji import emojize

print('''{}OLÁ! SEU QUE VOCÊS ADORAM COMPETIR ENTRE SÍ,
E DESSA VEZ A COMPETIÇÃO SERÁ ENTRE O MAIOR E O MENOR PESO.
POR FAVOR, SIGAM AS INSTRUçÕES A SEGUIR PARA INICIARMOS A BRINCADEIRA!{}\n'''.format('\033[1;3;4;30;42m','\033[m'))


p1 = float(input('Por favor, digitem o peso de cada um, separadamente: '))
p2 = float(input('Peso 2: '))
p3 = float(input('Peso 3: '))
p4 = float(input('Peso 4: '))
p5 = float(input('Peso 5: '))

print('o maior peso lido foi: ',end= '')

if p1 > p2 and p1 > p3 and p1 > p4 and p1 > p5:
    print(1)
elif p2 > p1 and p2 > p3 and p2 > p4 and p2 > p5:
    print(p2)
elif p3 > p1 and p3 > p2 and p3 > p4 and p3 > p5:
    print(p3)
elif p4 > p1 and p4 > p2 and p4 > p3 and p4 > p5:
    print(p4)
elif p5 > p1 and p5 > p2 and p5 > p3 and p5 > p4:
    print(p5)
else:
    print('Os números maiores são repetidos')
print('o menor valor é : ', end='')
if p1 < p2 and p1 < p3 and p1 < p4 and p1 < p5:
    print(p1)
elif p2 < p1 and p2 < p3 and p2 < p4 and p2 < p5:
    print(p2)
elif p3 < p1 and p3 < p2 and p3 < p4 and p3 < p5:
    print(p3)
elif p4 < p1 and p4 < p2 and p4 < p3 and p4 < p5:
    print(p4)
elif p5 < p1 and p5 < p2 and p5 < p3 and p5 < p4:
    print(p5)
else:
    print('Os menores números são repetidos')