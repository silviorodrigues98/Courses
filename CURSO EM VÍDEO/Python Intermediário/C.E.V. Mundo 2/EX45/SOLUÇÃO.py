from time import sleep
from random import randint

p1 = int(input('''Opções:
1 -- PEDRA
2 -- PAPEL
3 -- TESOURA
Qual sua jogada? '''))
print('JO'), sleep(1)
print('KEN'), sleep(1)
print('PÔ'),

item = ('Pedra', 'Papel', 'Tesoura')
pc = int(randint(1, 3))

print('O computador escolheu {} '.format(item[pc-1]))
print('O jogador escolheu {}'.format(item[p1-1]))

if pc == 1:
    if p1 == 1:
        print('Empatamos')
    elif p1 == 2:
        print('Voce ganhou')
    elif p1 == 3:
        print('Eu venci')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if p1 == 2:
        print('Empatamos')
    elif p1 == 1:
        print('Eu venci')
    elif p1 == 3:
        print('Voce venceu')
    else:
        print('invalida')
elif pc == 3:
    if p1 == 3:
        print('Empatamos')
    elif p1 == 2:
        print('Eu venci')
    elif p1 == 1:
        print('Eu perdi')
    else:
        print('invalida')
else:
    print('UAAAAI')