# CUSTO DA VIAGEM
con = 'SOMENTE PARA ADMNISTRADORES '
print(con)
print('-'*len(con))

pre1 = float(input('Qual o valor do Km até 200km?R$ '))
pre2 = float(input('E acima dos 200km?R$ '))

print()
sau = 'BEM VINDO AO {:=^27}'.format('VIAGEM SEM PRESSA')
print(sau)
print('-'*len(sau))
print()

dis = int(input('Qual a distência de sua viagem?Km '))

if dis <= 200:
    print('''O valor de sua viagem é R${:.2f}'''.format(dis*pre1))
else:
    print('O valor de sua viagem é R${:.2f}'.format(dis*pre2))
print()
print('Obrigado por usar nossos serviços.')
print('Tenha uma ótima viagem !!!')
print('-'*len(con))
