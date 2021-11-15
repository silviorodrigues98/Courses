from math import floor
import math
print('REMOVER OS NÚMEROS APÓS A VÍRGULA!!!')
print()
print('*'*20)
v1 = float(input('Digite aqui um número qualquer: '))
v2 = float(input('Agora digite um número para multiplica-lo'))
m1 = v1*v2
r1 = math.floor(m1)
print('O número sem vírgula é igual a : {}'.format(r1))
