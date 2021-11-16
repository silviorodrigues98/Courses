# PROGRAMA QUE LE DOIS NÚMEROS INTEIROS E OS COMPARA, MOSTRANDO O MAIOR E O MENOR VALOR, OU SE OS DOIS SÃO IGUAIS.
from emoji import emojize
from time import sleep
import math

print(emojize('Olá!!! Me diga dois números, e os os compararei para você.:sunglasses:', use_aliases=True))

num1 = int(input('Primeiro valor: '))
num2 = int(input('\nSegundo valor: '))

print('\nVerificando...\n')
sleep(1)
if num1 > num2:
    print('O primeiro valor, de {}, é o \033[1;30;47mmaior\033[m entre eles.'.format(num1))
elif num2 > num1:
    print('O segundo valor, de {}, é o \033[1;30;46mmaior\033[m entre eles.'.format(num2))
else:
    print('Não existe valor maior, \033[1;30;41mambos\033[m são iguais ')
print(emojize('\nObrigado por usar nosso serviço, até logo ! :thumbsup:',use_aliases=True))

