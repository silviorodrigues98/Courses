# BELIEVER ! PAAAAAAAIN
# AGORA VAI DARRRRRRR
from math import ceil

bv = 'BEM VINDO AO SISTEMA DE CONVERSÃO DE UNIDADES!'
print(bv)
con1 = int(len(bv))
print('-'*con1)
print()

num = str(input('Basta digitar um número, que eu farei o resto: '))
print()

re = 'SEUS DADOS SÃO:'
print(re)
con2 = int(len(re))
print('v'*con2)
print()

num1 = num.strip()
und = ((float(len(num1))-1).ceil())
dez = (float(len(num1))-2).ceil()
cen = (float(len(num1))-3).ceil()
mil = (float(len(num1))-4).ceil()
print(num1[und] ,num1[dez], num1[cen], num1[mil])


