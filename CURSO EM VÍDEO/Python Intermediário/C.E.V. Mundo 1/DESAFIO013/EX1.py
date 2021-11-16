print('AUMENTO NO SALÁRIO DO FUNCIONÁRIO!')
print()
print('*'*20)
print()
print('Olá, bem vindo ao ajuste de salários automático! Siga as instruções abaixo para atualiza-lo:')
print()
sa = float(input('Qual seu salário atual? R$ '))
au = float(input('Certo, agora me diga qual a porcentagem do seu aumento: % '))
no = sa*au/100
fi = sa+no
print('Parabéns!!! Seu salário foi atualizado.\nA partir de hoje, você receberá R$ {:=^20.2f}\nSeu reajuste foi de R$ {:.2f}'.format(fi, no))
print()
print('*'*20)
