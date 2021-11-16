# CALCULANDO O IMC:
from emoji import emojize
from time import sleep

print(emojize('SEJA BEM VINDO(a) AO PROGRAMA ":apple:MAIS SÁUDE EM SUA TELA:sweet_potato:"\nSIGA AS INSTRUÇÕES PARA SABER QUAL SUA SITUAÇÃO CORPÓREA.',use_aliases=True))

peso = float(input('\nPrimeiramente, me diga seu peso: Kg'))
altura = float(input('\nAgora me diga sua altura, em metros: m'))
imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é de {}{:.2f}{} e está muito BAIXO'.format('\033[1;30;45m', imc,'\033[1;30;44m'))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.2f} e está \033[1;30;44mideal para você'.format(imc))
elif 25<= imc < 30:
    print('Seu IMC é de {:.2f} e está \033[1;30;46mcom sobrepeso.'.format(imc))
elif 30<= imc <= 40:
    print('Seu IMC é de {:.2f} e está \033[1;30;47mcom obesidade .'.format(imc))
else:
    print(emojize('Seu IMC é de {:.2f} e você \033[1;30;41mvai morrer :smile:  ',use_aliases=True))

print('\n\033[mÉ um prazer poder cuidar de sua saúde!')