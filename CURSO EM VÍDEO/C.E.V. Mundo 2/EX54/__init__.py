# CONTATOR DE MAIORIDADE
from time import sleep
from emoji import emojize
from datetime import date

print('\033[1;3;4;30;44mBEM VINDOS AO PARQUE TOPATUDO!!!\nDIGITEM SEUS ANOS DE NASCIMENTO PARA QUE POSSAM PROSSEGUIR!!!\033[m\n')

ano = date.today().year
maior = 0
menor = 0

for c in range(0,7):
    nasc = int(input('Ano de nascimento: '))
    if (ano - nasc) < 21:
        menor += 1
    else:
        maior += 1
print('\n{:=^50}'.format('Calculando...')), sleep(1.5)
print(emojize('''\n:smile:{} pessoas já alcançaram a maioridade e poderão utilizar nossos brinquedos.
{} poderão utilizar somente os brinquedos infantis pois ainda não são maiores de idade.:smile:'''.format(maior, menor), use_aliases=True))
