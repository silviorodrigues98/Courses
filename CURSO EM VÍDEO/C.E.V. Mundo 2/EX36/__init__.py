# APROVADOR DE EMPRÉSTIMO:

#PERGUTARÁ VALOR DA CASA, DO SALÁRIO E EM QUANTOS ANOS SERÁ PAGO

#CALCULAR O VALOR DA PRESTAÇÃO MENSAL. SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALÁRIO.
import math
from time import sleep
from math import ceil
# CASO EXCEDA, RECEBERÁ MENSAGEM DE 'CANCELADO'
from emoji import emojize

print(emojize('\033[1m\033[4;30;44m:thumbsup:BEM VINDO AO EXCHANGE CONSIGNADOS!:thumbsup:\033[m', use_aliases=True))
print()

nome = str(input('Para começarmos, me diga seu nome: '))

print()
print('Ótimo, creio que você tenha interesse fazer um empréstimo.\nDessa forma, peço que você informe os dados que serão requisitados a seguir.')
print()

casa = float(input('Qual o valor da casa que você pretente comprar?R$ \n'))
salario = float(input('Ótimo! E qual seu salário atual?R$ \n'))
anos = int(input('Por último, me diga em quantos anos a dívida será paga: \n\n'))

print('Otimo, estarei calculando o valor de sua prestação, e lhe informarei sua situação em instantes.')
print('\nCalculando...')
sleep(2)

prestacao = casa/(anos*12)
meses = anos*12


if prestacao > salario*0.3:
    print('Lamento lhe informar {}, mas seu empréstimo no valor de {:.0f} foi negado. '.format(nome, casa))
else:
    print('Parabéns {}, seu empréstmo no valor de {:.2f}foi aprovado, vá em uma de nossas agencias para finalizar o procedimento.'.format(nome, casa))
    print('Sua mensalidade será no valor de R${:.2f}, durante o prazo de {} meses.'.format(prestacao, meses))

print(emojize('\n\033[1m\033[4;30;46m:sunglasses:É um prazer atendê-lo(a) {}, estamos à disposição para quaisquer outras dúvidas.:sunglasses:\033[m '.format(nome), use_aliases=True))