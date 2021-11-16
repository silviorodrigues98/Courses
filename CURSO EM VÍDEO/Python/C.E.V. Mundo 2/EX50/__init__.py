# LEITOR DE NUMEROS INTEIROS QUE OS SOMA SE FOREM PARES
from time import sleep
from emoji import emojize

a = 0
for b in range(0, 6):
    n = int(input(emojize('\n:imp:Digite um número inteiro: ', use_aliases=True)))
    if n % 2 == 0:
        a += n
print('''
Calculando...
'''), sleep(1)
print('A SOMA DOS NÚMEROS PARES É \033[1;30;42m{}\033[m'.format(a))
print('-'*40)