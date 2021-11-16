'''PROGRAMA QUE MELHORA O JOGO 028 ONDE O COMPUTADOR VAI PENSAR DE UM NÚMERO ENTRE 0 E 10 E QUE AGORA VAI TENTAR ADIVINHAR ATÉ ACERTAR'''
from time import sleep
from emoji import emojize
from random import randint

print('{}{:^150}{}'.format('\033[1;3;4;30;43m', '''OLÁ, MORTAL! TENHO UM DESAFIO PARA VOCÊ,MAS DUVIDO QUE VOCÊ SEJA CAPAZ DE COMPRI-LO.\033[m
\033[1;3;4;30;41mI'M GONNA THING ABOUT A NUMBER...CAN YOU GUESS WHAT WAS THAT NUMBER ?''','\033[m'))

pcr = randint(0, 10)
plr = 11
tentativas = 0

while plr != pcr:
    plr = int(input(emojize('\n:sunglasses: Em qual número eu pensei? ',use_aliases=True)))
    print('Vejamos...'), sleep(0.25)
    tentativas += 1
    if plr  == pcr:
        print('\nParabéns, você acertou', end=' ')
    else:
        print('\nVocê errou!!! Chute mais uma vez.')
print('após {} tentativas! '.format(tentativas))