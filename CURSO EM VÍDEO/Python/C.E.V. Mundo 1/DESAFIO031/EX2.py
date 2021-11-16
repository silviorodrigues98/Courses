from time import sleep

dis = float(input('Qual a distância da sua viagem?Km '))
print('Voce está prestes a começar uma viagem de {}Km'.format(dis))
print('Calculando roteiro...')
sleep(2)

per = 0.50
lon = 0.45

if dis <= 200:
    print('O preço é R${}'.format(dis*per))
else:
    print('O preço é R${}'.format(dis*lon))
print('Tenha uma ótima viagem!!! ')
