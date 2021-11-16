# AUMENTO FUNCIONÁRIOS

cfg = 'SOMENTE PARA ADMINISTRADORES '
print(cfg)
print('='*len(cfg))
print()

au1 = float(input('Qual será a porcentagem de aumento até R$1.250?% '))
au2 = float(input('E acima desse valor?% '))

sau = 'BEM VINDO À UM PROGRAMA REALMENTE ÚTIL'
print(sau)
print('-'*len(sau))

sa1 = float(input('Me diga seu salário para que eu calcule seu aumento:R$ '))
print()
print('Calculando novo salário...')
print()

if sa1 <= 1250:
    print('Parabéns, seu novo salário é:R$ {:.2f}'.format((au1/100+1)*sa1))
else:
    print('Parabéns, seu novo salário é:R$ {:.2f}'.format((au2/100+1)*sa1))

print('É um prazer tê-lo em nossa empresa, aproveite o reajuste! ')
