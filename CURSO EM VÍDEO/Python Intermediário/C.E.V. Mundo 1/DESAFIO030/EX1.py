import math
# KRL EU SOU UM GÊNIO
# SISTEMA QUE DIZ SE O NÚMERO É IMPAR OU PAR

print('BEM VINDO AO...SISTEMA QUE DIZ SE É PAR OU NÃO!!!(Muito Complexo)')
print()
num = int(input('Primeiro, me diga o número, é claro né: '))
print('''Aguardando processamento...''')

#Contas

par = num % 2

#Condição

if par == 0:
    print('Simmm! Seu número {} é par'.format(num))
else:
    print('''
Não...INFELIZMENTE seu número não é par, 
portanto você não pode participar de nosso grupo,
pois ele é feito para números pares.
LAMENTO MUITO SUA PERDA :c''')
