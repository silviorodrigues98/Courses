''' REFAZENDO O EXERCÍCIO 51, AGORA COM WHILE AO INVÉS DE FOR'''

from emoji import emojize
from time import sleep
print('\33[1;3;4;30;42mSEJA BEM VINDO AO ANALISADOR DE P.A! SIGA AS INSTRUÇÕES A SEGUIR:\33[m')
primeiro1 = int(input('Drigite o primeiro número da PA: '))
razao = int(input('Digite a razão desta mesma PA: '))
print('{:=^40}'.format('Calculando...')),sleep(1)
termo =  1
primeiro = primeiro1
progressao = 0
while termo != 11:
    primeiro  += razao
    if termo == 1:
        print('\033[1;3;4;30;43m{}\033[m'.format(primeiro1),end=' >> ')
    termo += 1
    if termo != 11:
        print(emojize(':sunglasses: {}'.format(primeiro),use_aliases=True),end=' >> ')
    if termo == 11:
        print('\033[1;3;4;30;42m{}\033[m'.format(primeiro))