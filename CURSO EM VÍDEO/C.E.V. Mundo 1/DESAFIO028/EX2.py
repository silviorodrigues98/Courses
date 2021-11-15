# COPIANDO GUANABARA !
from random import randint
import time # Esse métido funciona para criar um efeito de carregamento...


print('=/='*20)
print('Vou pensar em um número entre 0 e 5,. Tenta adivinhar...')
print('CARREGANDO...')
time.sleep(3)
print('=/='*20)

num = int(input('Em que número eu pensei? '))
ran = randint(0, 5)
print('LOADING...')
time.sleep(3)

if num == ran:
    print('Parabéns, você conseguiu me vencer ')
else:
    print('Eu venci.Meu número era {} e não {}.'.format(ran, num))
