# EXERCÍCIO DE POLÍNDROMO, DESCONSIDERANDO ESPAÇOS.
from time import sleep
from emoji import emojize
import math

print('{}BEM VINDO AO PALIDROMÓFAGO!!!, SIGA A INSTRUÇÕES ABAIXO PARA COMEÇAR!!!{}'.format('\033[1;3;4;30;46m','\033[m'))

frase = str(input('Diga sua bela frase, por obséquio: ')).upper().strip()
print()
print('{:=^40}'.format('Calculando...'))
sleep(1.5)
separada = frase.split()
junta = ''.join(separada)
a = 0
b = 0
c = 0
tam = int(len(junta) - 1 - b)
tam1 = len(junta)-1

for d in range(1, tam1):
    if str(junta[a]) == str(junta[tam]):
        a += 1
        tam -= 1
        c += 1
if c+1 == tam1:
    print(emojize('Esta palavra é um políndromo!!! :smile: ', use_aliases=True))
else:
    print(emojize('Esta palavra não é um políndromo!!! :disappointed: ', use_aliases=True))





