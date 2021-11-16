# EXERCÍCIO DE POLÍNDROMO, DESCONSIDERANDO ESPAÇOS.
from time import sleep
from emoji import emojize

print('{}BEM VINDO AO POLIDROMÓFAGO!!!, SIGA A INSTRUÇÕES ABAIXO PARA COMEÇAR!!!{}'.format('\033[1;3;4;30;46m','\033[m'))

fra = str(input('Digite uma bela frase: '))
tam = len(fra.strip()) - len(fra.split()) + 1
fra.rfind(tam, [0])