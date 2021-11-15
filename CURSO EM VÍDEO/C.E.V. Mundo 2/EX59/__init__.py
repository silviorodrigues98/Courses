'''PROGRAMA QUE LÊ DOIS NÚMEROS E MOSTRA UM MENU NA TELA, DANDO A OPÇÃO DE SOMA,
MULTIPLICAÇÃO, MAIOR, NOVOS NUMEROS.'''

menu  = 4
while menu == 4:
    num1 = float(input('Digite o primeiro valor: '))
    num2 = float(input('Digite o segundo valor: '))
    menu = int(input(''' {:=^50} 
                
                    [1] SOMAR                        [3] MAIOR DELES
                    [2] MULTIPLICAR                  [4] NOVOS NÚMEROS
                                   
                                 [5] SAIR DO PROGRAMA
                                            
                                        '''.format('OPÇÕES')))
    maior  = num1
    soma = 0
    mult = 0

    if menu == 1:
        soma = (num1 + num2)
        print('A soma é {}'.format(soma))
    elif menu == 2:
        mult = num1 * num2
        print('MULT',mult)
    elif menu == 3:
        if num2 > num1:
            maior = num2
            print('MAIOR',maior)
        else:
            print('MAIOR', maior)
    if menu != 5:
        menu = int(input('OPÇOES 12345'))




