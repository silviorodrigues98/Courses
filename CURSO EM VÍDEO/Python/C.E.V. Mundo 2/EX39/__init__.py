# PROGRAMA QUE LÊ A IDADE DE UM JOVEM, E INFORME, DE ACORDO COM SUA IDADE:
# SE VAI SE ALISTAR AINDA; SE É HORA DE SE ALISTAR; OU SE JÁ PASSOU DO PRAZO.
from datetime import datetime
from emoji import emojize
from time import sleep

print(emojize('''BEM VINDO AO SISTEMA DE ESCRAVIDÃO OBRIGATÓRIO
TAMBÉM CONHECIDO COMO "ALISTAMENTO MILITAR" :imp:''', use_aliases=True))

nasc = int(input(emojize('\nVOCÊ \033[1;30;43mDEVE\033[m DIZER SEU ANO DE NASCIMENTO, OU ENTÃO MORRERÁ :rage: :\n',use_aliases=True)))
ano = str(datetime.now()).split('-')[0]
idade = int(ano)-nasc

if idade < 18:
    print('Fique tranquilo, em breve você será nossa \033[3;30;45mprostitutinha\033[m')
    print(emojize('Faltam somente \033[1;30;46m{} MESES\033[m para que possamos comer seu cúzinho :yum: '.format((18-idade)*12), use_aliases=True))
elif idade > 18:
    print(emojize('O QUE?! VOCÊ OUSA SE ATRASAR PERANTE A NÓS??? INSOLENTE, PAGARÁ COM SUA LIBERDADE.:punch:',use_aliases=True))
    print('VOCE DEVERIA TER SE APRESENTADO \033[1;30;45m{} MESES\033[m ATRÁS'.format((idade-18)*12))
else:
    print('HAHAHAHAHA, vai ser um prazer te-lo à nossa disposição... para fazer \033[1;30;45mTUDO...\033[m ')

print(emojize('\nÉ um prazer podermos colaborar com sua segurança :cow:',use_aliases=True))
