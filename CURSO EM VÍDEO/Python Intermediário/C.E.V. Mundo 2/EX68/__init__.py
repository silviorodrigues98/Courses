""" CRIAR UM JOGO DE PAR OU ÍMPAR COM O PC, CONTANDO AS VEZES QUE ELE GANHOU. ELE SÓ PARA QUANDO VOCÊ PERDER. """
from random import randint
from time import sleep
from emoji import emojize
from playsound import playsound
cores = ['\033[1;3;4;31;42m', '\033[m']
print(f"""{cores[0]}OLÁ, SOU SEU COMPUTADOR.
O QUE ACHA DE JOGARMOS PAR OU ÍMPAR?
DUVIDO QUE POSSA ME VENCER\n{cores[1]}""")
soma_par = 0
vitorias_jogador = 0
while True:
    valor_computador = randint(0, 10)
    valor_jogador = int(input(emojize('Qual seu valor?:smile: ', use_aliases=True)))
    jogada_jogador = str(input(emojize('Qual sua jogada?:imp:[P]ar ou [I]mpar > ', use_aliases=True))).strip()[0]
    print('Vejamos....'), sleep(1)
    soma_par = (valor_computador + valor_jogador) % 2
    if jogada_jogador in 'Pp' and soma_par == 0:
        print('VOCÊ VENCEU! ')
        vitorias_jogador += 1
    elif jogada_jogador in 'ÍíIi' and soma_par == 0:
        print('VOCÊ VENCEU! ')
        vitorias_jogador += 1
    else:
        print('HAHAHA, EU VENCI! ')
        break
print(f"""VOCÊ TEVE {vitorias_jogador} VITÓRIAS CONSECUTIVAS.
O QUE ACHA DE JOGARMOS OUTRA VEZ? """)
playsound('C:/door.mp3')
