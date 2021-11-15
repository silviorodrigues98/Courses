import random
sau = 'VAMOS JOGAR UM JOGO?!? DUVIDO VOCÊ ADIVINHAR O NÚMERO QUE EU ESTOU PENSANDO'
print(sau)
print('-'*len(sau))

ran = random.randint(0, 5)
var = int(input('Digite aqui um número de 0 a 5: '))

if var == ran:
    print('O que? IMPOSSÍVEL!!! Vamos jogar outra vez.')
else:
    print('MwAHAHAHAHAa, eu sabia que você era um perdedor.')
print('Eu pensei no número {}...'.format(ran))

fim = 'Pressione CTRL+SHIFT+F10 para jogar novamente.'
print('-'*len(fim))
print(fim)


