'''LER SEXO DE PESSOA, ACEITANDO SOMENTE [M ou F]. CASO A RESPOSTA SEJA
DIFERENTE, PEDIR DIGITAÇÃO NOVAMENTE ATÉ QUE SEJA DIGITADO UM VALOR CORRETO'''
from time import sleep
from emoji import emojize
print('\033[1;3;4;30;46mBEM VINDO AO NOSSO SITE DE VENDAS!!!POR FAVOR, RESPONDA A PERGUNTA A SEGUIR PARAR CONTINUAR:\033[m')
print()
sexo = 'AAA'
while not sexo in 'MmFf':
    sexo = str(input('Qual seu sexo?[M/F]: ')).upper().strip()
    if sexo not in 'MmFf':
        print(emojize('\n:sunglasses:Opção não válida, por favor, tente novamente.:sunglasses: ', use_aliases=True))
    if sexo in 'Mm':
        conf = str(input('\nConfirma que seu sexo é Masculino?[S/N] ')).upper().strip()
        if conf not in 'Ss':
            print('\nPor favor, tente novamente: \n')
            sexo = 'ERRADO'
        else:
            print('\nPerfeito! Obrigado por responder nosso questionário!')
    if sexo in 'Ff':
        conf = str(input('\nConfirma que seu sexo é Feminino?[S/N] '))
        if conf not in 'Ss':
            print('\nPor favor, tente novamente. \n')
            sexo = 'ERRADO'
        else:
            print('\nPerfeito! Obrigado por responder nosso questionário ')
if sexo in 'Mm':
    print('{}Você agora está CADASTRADO em nosso sistema e pode utilizar nossos serviços.{} '.format('\033[1;3;4;30;42m', '\033[m'))
else:
    print('{}Você agora esta CADASTRADA em nosso sistema e pode utilizar nossos serviços.{} '.format('\033[1;3;4;30;41m', '\033[m'))

