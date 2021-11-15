from math import floor
import math
print('PREVIEW DE DESAFIOS"')
re = float(input('Digite aqui um número real: '))
print(floor(re))

print(math.trunc(re))
#Quadrado da hipotenusa é igual a soma dos quadrados dos catetos

ca = float(input('Adjacente'))
co = float(input('Oposto'))
hi = pow(ca, 2)+pow(co, 2)
print(hi)
