# PROGRAMA QUE LE IDADE, SEXO E NOME DA PESSOA
from time import sleep
from emoji import emojize

n = 0
i = 0
s = 0
cont = 0
hmv  = 0
menores = 0
cont2 = 1
hmvn = 'uai'

print('\033[1;3;4;30;47mBEM VINDO AO PROGRAMA DE FÉRIAS, POR FAVOR, NOS INFORME SEUS DADOS A SEGUIR!\033[m\n')

for z in range(1, 5):
    nome = str(input(emojize('Nome da {}º pessoa::hatching_chick: '.format(z), use_aliases=True)).strip().upper())
    idade = int(input(emojize('Idade da {}º pessoa::two_women_holding_hands:  '.format(z), use_aliases=True)))
    sexo = str(input(emojize('''Selecione o sexo da {}º pessoa::light_rail:
    Masculino - Digite M
    Feminino - Digite F
    '''.format(z), use_aliases=True)).strip().upper())

    i += idade
    cont += 1
    if sexo == 'M' and z == 1:
        hmv = idade
        hmvn = nome
    elif sexo == 'M' and z !=1:
        if idade > hmv:
            hmv = idade
            cont2 += 1
            hmvn = nome
    if sexo == 'F' and idade < 20:
        menores += 1
media = i / cont
print('\n{:=^40}'.format('Calculando...'))
sleep(1.5)
print('\nA {}MÉDIA{} de idade do grupo é de {:.1f}'.format('\033[1;3;4;30;44m', '\033[m', media))
print('\nO {}homem mais velho{} tem {} anos. Seu nome é: {}'.format('\033[1;3;4;30;44m','\033[m',hmv, hmvn))
print('\n{} mulheres tem {}menos de 20 anos.{}'.format(menores, '\033[1;3;4;30;45m','\033[m'))


