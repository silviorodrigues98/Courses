from random import randint
from time import sleep
from emoji import emojize

print('\033[1;34;43mOlá Mundo!')

print('\033[4;35;40mTESTE 1')
print('\033[44;41mTESTE 2')
print('\033[7;32;47mTESTE 3')
print()
print('\033[30;30mBRANCO30')
print('\033[31;41mVERMELHO31')
print('\033[32;42mVERDE32')
print('\033[33;43mAMARELO33')
print('\033[34;44mAZUL')
print('\033[35;45mROXO')
print('\033[36;46mSKY')
print('\033[37;47mGRAY')
print()
print('\033[30;41mGUANABARÁ')
print('\033[4;33;44mGUANABARA')
print('\033[1;35;43mGUANABARA')
print('\033[30;42mGUANABARA')
print('\033[mGUANABARA')
print('\033[7;30mGUANABARA')

print('\033[1;45mParabéns, voce foi \033[1;31;42mVENCEDOR\033[m !!!')

n1 = randint(0, 3)
t1 = int(input('Diga um número, duvido ele ser o mesmo que pensei!\033[1;m '))
print('\033[1;30;44mANALISANDO...\033[m')
sleep(2)

print('\033[mHAHAHAHAHAHAHAHA VOCÊ FOI \033[1;30;41mDERROTADO!!!\033[m ' if t1 != n1 else '\033[mESSA NÃO, VOCÊ FOI \033[1;30;42mVENCEDOR!!!\033[m',emojize(':sunglasses:',use_aliases=True))
a = 3
b = 5

print('Os valores são \033[1;30;47m{} e \033[1;46m{}\033[m '.format(a, b))

#MELHOR JEITO USA MENOS LETRAS

print('Olá muito prazer em te conhecer {}{}{}'.format('\033[m', 'Silvio', '\033[m'))

cores = {'limpa':'\033[m', 'azul':'\033[1;43m',
         'vermelho':'\033[1;42m'}
# ISTO É UM DICIONÁRIO, QUE ESTAREI ESTUDANDO POSTERIORMENTE.

print('Agora vamos usar as cores já formatadas{}VERMELHO{} E {}AZUL{}'.format(cores['vermelho'], cores['limpa'], cores['azul'], cores['limpa']))