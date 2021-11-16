# PROGRAMA PARA NATÃO, QUE MOSTRA A CATEGORIA DO ATLETA.

from emoji import emojize
from time import sleep

print(emojize('BEM VINDO AO SISTEMA NACIONAL DE NATAÇÃO. SIGA AS INSTRUÇÕES PARA SER CADASTRADO EM NOSSO SISTEMA.'))

idade = int(input('\nPor favor, me diga sua IDADE: '))

if idade <= 9:
    print('\nVocê está classificado como \033[1;30;43mMIRIM\033[m')

elif idade <= 14:
    print('\nVocê está classificado como \033[1;30;42mINFANTIL\033[m')

elif idade <= 19:
    print('\nVocê está classificado como \033[1;30;41mJUNIOR\033[m')
elif idade <= 20:
    print('\nVocê está classificado como \033[1;30;44mSÊNIOR\033[m')
else:
    print('\nParabéns, você é um dos poucos \033[1;30;45mMASTER\033[m classificados.')

print('\nSeja bem vindo(a) à nossa confederação.')