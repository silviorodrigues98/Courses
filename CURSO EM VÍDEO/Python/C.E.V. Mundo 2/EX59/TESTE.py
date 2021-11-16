'''PROGRAMA QUE LÊ DOIS NÚMEROS E MOSTRA UM MENU NA TELA, DANDO A OPÇÃO DE SOMA,
MULTIPLICAÇÃO, MAIOR, NOVOS NUMEROS.'''
from time import sleep
from emoji import emojize


print('{}{:^200}{}'.format('\033[1;3;4;30;45m','''SEJA MUITO BEM VINDO À SUA CALCULADORA SUPERFÁCIL.
POR FAVOR, SIGA AS INSTRUÇÕES ABAIXO PARA SEU MELHOR APROVEITAMENTO.''',''))
print('\033[m')

loop = 0
menu = 0
while menu != 5:
    num1 = float(input(emojize(':imp: Digite o primeiro valor: ',use_aliases=True)))
    num2 = float(input(emojize(':imp: Digite o segundo valor: ',use_aliases=True)))
    menu = int(input(''' {:=^50} 

    [1] SOMAR                        [3] MAIOR DELES
    [2] MULTIPLICAR                  [4] NOVOS NÚMEROS

                [5] SAIR DO PROGRAMA

                                        '''.format('OPÇÕES')))
    print('Analisando...'),sleep(1)
    maior = num1
    soma = 0
    mult = 0
    loop  += 1

    if menu == 1:
        soma = (num1 + num2)
        print('A soma entre {} e {} resulta em {:.1f}'.format(num1, num2, soma))
    elif menu == 2:
        mult = num1 * num2
        print('O resultado da multiplicação entre {} e {} resulta em {:.1f}'.format(num1, num2, mult))
    elif menu == 3:
        if num2 > num1:
            maior = num2
            print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
        else:
            print('O maior número entre {} e {} é {}'.format(num1, num2, maior))
print('\n\033[1;3;4;30;44mÉ UM PRAZER PODER AJUDAR,VOCE FEZ {} OPERAÇÕES DESSA VEZ. VOLTE LOGO!\033[m'.format(loop-1))





