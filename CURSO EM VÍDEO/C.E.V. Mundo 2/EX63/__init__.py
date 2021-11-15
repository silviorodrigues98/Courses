''' ESCREVER A SEQUÊNCIA FIBONACCI DE UM NÚMERO '''
from time import sleep
from emoji import emojize
bb =['\033[1;3;4;30;41m','\033[m','\033[1;3;4;30;46m']
print('{}{}{}'.format(bb[0], 'SEJA BEM VINDO AO FIBONANDO! SIGA AS INSTRUÇÕES A SEGUIR:', bb[1]))
no = int(input('\nQuantos elementos Fibonacci você quer calcular? '))
print('\n{:^40}'.format('Calculando...')), sleep(1)
n1 = no
cont = 0
fiba = 0
fibt = 1
fibj = 0
teste = ''
while cont < no:
    if cont < no-1:
        print(emojize(' {} :imp: '.format(fiba),use_aliases=True), end=' ')
    else:
        print(bb[2],'{}'.format(fiba),bb[1])
    cont += 1
    fibj = fiba + fibt
    fiba = fibt
    fibt = fibj
print('\n{}{}{}'.format(bb[0], 'OBRIGADO POR USAR NOSSOS SERVIÇOS, ATÉ LOGO! ', bb[1]))




