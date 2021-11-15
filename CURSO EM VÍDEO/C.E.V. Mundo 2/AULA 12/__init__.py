# ESTRUTURAS DE CONTROLE

# CONDIÇÕES ANINHADAS

# carro.siga()
# carro.pare()

# se carro.esquerda()

###if algo acontecer:
#    print('algo')
#elif algo2:
#    print('algo 2')
#elif algo3:
# #  print('algo3')###

nome = str(input('Qual é seu nome? '))
if nome == 'Silvio':
    print('Que nome mais lindo !!! ')
elif nome == 'Jose' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comumzinho ')
elif nome in 'Daniele Castro Dani':# A função IN facilita a criação de viriáveis, pois tudo que estiver entre as aspas sera considerado na regra
    print('Estou triste')
else:
    print('Que nome feio kkkkk')

print('Tenha um bom dia {}!'.format(nome))