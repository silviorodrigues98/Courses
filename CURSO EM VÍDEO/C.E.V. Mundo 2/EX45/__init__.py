# JOGO DE PEDRA PAPEL OU TESOURA
from time import sleep
from emoji import emojize
from random import randint

pl1 = str(input('Escreva se quer pedra, papel ou tesoura')).strip().upper()
pc = randint(1, 3)

if pc == 1:
    print('Eu pensei em PEDRA')
elif pc == 2:
    print('Eu pensei em PAPEL')
else:
    print('Eu pensei em TESOURA')

if pl1 == 'PEDRA' and pc == 3 and pc !=1:
    print('OH NÃO, VOCE GANHOU')
elif pl1 == 'PEDRA' and pc == 1:
    print('Parece que empatamos...')

elif pl1 == 'PAPEL' and pc == 1 and pc != 2:
    print('VOCE VENCEU DESSA VEZ')
elif pl1 == 'PAPEL' and pc == 2:
    print('PARECE QUE ESTAMOS EMPATADOS')

elif pl1 == 'TESOURA' and pc == 2 and pc != 3:
    print('VOCE É MUITO BOM !')
elif pl1 == 3:
    print('ESTAMOS NO MESMO NÍVEL...')
else:
    print('Dessa vez você perdeu, mas quem sabe na próxima!')