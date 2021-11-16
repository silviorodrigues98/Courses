# COPIANDO GUANABARA!!!
from time import sleep
print('ANALISADOR DE TRIÂNGULOS')

l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
print('ANALISANDO...')
sleep(2)

if l1 < l2 + l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Sim, eles formam triângulos.')
else:
    print('Não é possível se formar um triângulo.')