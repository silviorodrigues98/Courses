''' PROGRAMA QUE LÊ VÁRIOS NÚMEROS INTEIROS E DIZ:
MÉDIA, MAIOR E MENOR. E OFERECE A OPÇÃO DE CONTINUAR. '''
from time import sleep
from emoji import emojize
from playsound import playsound
num = 0
opcao = 'S'
total = 0
maior = 0
menor = 0
cont = 0
bb = ['\033[1;3;4;30;42m', '\033[m']
print('{}BEM VINDO À SUA CALCULADORA AINDA MAIS FÁCIL !!! NOVAMENTE, SIGA AS INSTRUÇÕES PARA CONTINUAR >>{}'.format(bb[0], bb[1]))
while 'S' in opcao:
    num = int(input(emojize('\nDigite um número inteiro::smile: ', use_aliases=True)))
    opcao = str(input('Quer continuar?[S/N] ')).upper().strip()
    total += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    if cont != 1:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
media = total / cont
print('''{:^30}'''.format('Calculando...')), sleep(1)
print('''\n{}VOCÊ DIGITOU {} NÚMEROS, E O TOTAL ENTRE ELES É {}.
JA A MÉDIA ENTRE ELES É {:.1f}...
ALÉM DISSO, POSSO AFIRMAR QUE O MAIOR É {} E O MENOR É {}\n{}'''.format(bb[0], cont, total, media, maior, menor, bb[1]))
playsound('C:/Users/Silvio/PycharmProjects/C.E.V Mundo 2/01.mp3')