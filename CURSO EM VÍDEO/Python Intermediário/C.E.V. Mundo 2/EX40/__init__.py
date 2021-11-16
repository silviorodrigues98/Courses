# MÉDIAS DOS ALUNOS.
import math
from emoji import emojize
from time import sleep

print(emojize('BEM VINDO AO SISTEMA ANGLO DE ENSINO\nSIGA AS INSTRUÇÕES PARA CALCULAR A MÉDIA DAS NOTAS DE UM ALUNO: :smile:'))

n1 = float(input('\nNOTA 1: '))
n2 = float(input('\nNOTA 2: '))
media = (n1+n2)/2

if media < 5:
    print('\033[1;30;41mREPROVADO\033[m')
elif  5<media<6.9 :
    print('\033[1;30;42mRECUPERAÇÃO\033[m')
else:
    print('\033[1;30;43mAPROVADO\033[m')
print('Tenha um bom dia!')