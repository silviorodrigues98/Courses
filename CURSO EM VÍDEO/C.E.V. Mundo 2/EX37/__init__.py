# PROGRAMA QUE LÊ UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO.

# VOU UTILIZAR AS PRÓPIAS FUNÇÕES DO PYTHON PARA FAZER A CONVERSÃO DE BASES DECIMAIS.
import math
from time import sleep
from emoji import emojize
print(emojize('\033[1m\033[4;30;42mBem vindo ao seu conversor universal de unidades.:sunglasses:\033[m', use_aliases=True))

num = int(input('\nPrimeiro, diga seu número: '))
tipo = int(input('\nAgora, escolha entre: \n1 para Binário.\n2 para Octal.\n3 para Hexadecimal.\n'))

if tipo == 1:
    print('\nA conversão binária do número {} é igual a: \033[3;30;45m{}\033[m'.format(num, bin(num)))
elif tipo == 2:
    print('\nA conversão octal do número {} é igual a: \033[3;30;44m{}\033[m'.format(num, oct(num)))
else:
    print('\nA conversão hexadecimal do número {} é igual a: \033[3;30;43m{}\033[m'.format(num, hex(num)))

print(emojize('Foi um prazer trabalhar com você! :thumbsup:', use_aliases=True))
