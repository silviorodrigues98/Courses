# FORMAS DE PAGAMENTO:

from time import sleep
from emoji import emojize

print(emojize('BEM VINDO À NOSSA LOJA, SINTA-SE AVONTADA PARA OBSERVAR NOSSOS PRODUTOS.:imp:', use_aliases=True))

vista = float(input('''
Que bom que já escolheu um produto!
Agora que já o fez, informe seu valor: R$'''))
print()
modo = int(input('''Selecione o modo de pagamento:
1 -- À VISTA, COM DINHEIRO OU CHEQUE(10% de desconto).
2 -- À VISTA, NO CARTÃO DE CRÉDITO.(5% de desconto). 
3 -- 2x NO CARTÃO.
4 -- 3x OU MAIS NO CARTÃO(contém juros).
'''))
print()

if modo == 1:
    print('O valor de seu produto será \033[1;30;42m{:.2f}'.format(vista*0.9))
elif modo == 2:
    print('O valor de seu produto será \033[1;30;43m{:.2f}'.format(vista*0.95))
elif modo == 3:
    print('O valor de seu produto será em duas vezes de \033[1;30;46m{:.2f}'.format(vista/2))
elif modo == 4:
    par = int(input('Em quantas parcelas você quer dividir o preço? '))
    print('O valor do produto à vista será \033[1;30;42m{:.2f}, com parcelas de {:.2f}'.format(vista*1.2,(vista*1.2)/par))

print(emojize('\nAgradeçemos a preferência:thumbsup:', use_aliases=True))
