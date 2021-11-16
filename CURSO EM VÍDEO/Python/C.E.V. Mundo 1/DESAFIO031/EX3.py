# CÓPIA DO GUANABARA.

from time import sleep

dis = float(input('Qual a distância da sua viagem?Km '))
print('Voce está prestes a começar uma viagem de {}Km'.format(dis))
print('Calculando roteiro...')
sleep(2)

per = 0.50
lon = 0.45

# IF simplificado

pre = dis * per if dis <=200 else dis * lon
print('O preço será de {:.2f}'.format(pre))
