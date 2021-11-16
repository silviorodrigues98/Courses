''' PROGRAMA QUE LÊ VÁRIOS NÚMEROS E SÓ PARE QUANDO O USUÁRIO DIGITAR 999
NO FINAL, MOSTRE SUA SOMA E QUANTOS NÚMEROS FORAM DIGITADOS '''
from time import sleep
from emoji import emojize
import playsound
num = 0
cont = 1
soma = 0
bb = ['\033[1;3;4;30;41m','\033[m']
print('{}BEM VINDO(A) À SUA CALCULADORA SUPER-FÁCIL: Adicione os números para começar >>{}'.format(bb[0], bb[1]))
while num != 999:
    num = int(input(emojize('\nDigite seu {}º número::sunglasses: '.format(cont), use_aliases=True)))
    if num != 999:
        cont += 1
        soma += num
cont -= 1
print('\n{}VOCÊ DIGITOU {} NÚMEROS E A SOMA ENTRE ELES É: {}{}'.format(bb[0], cont, soma, bb[1]))

playsound.playsound('C:/Users/Silvio/PycharmProjects/C.E.V Mundo 2/01.mp3')
