# PROGRAMA QUE MOSTRA A CONTAGEM REGRESSIVA PARA OS FOGOS ARTIFÍCIOS COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES:
from time import sleep
from emoji import emojize
boas = ('{}{:=^100}{}'.format('\033[1;30;44m', 'SEJA BEM VINDO(A)! VAMOS COMEÇAR A CONTAGEM?', '\033[m'))
print(boas)
print('''
Começando...'''), sleep(1)
for c in range(10, 0, -1):
    print(emojize(':fire:', use_aliases=True), c), sleep(1)
print('''
ÓTIMO, OS FOGOS!!!''')
