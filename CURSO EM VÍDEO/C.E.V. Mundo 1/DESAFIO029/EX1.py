# MULTA FDP

print('{:=^10}CONFIGURAÇÃO PARA ADMINISTADORES {:=^10}'.format('=', '='))
lim = int(input('Qual a velocidade permitida na via?Km/h '))
pre = float(input('E qual o valor da multa por Km excedido?R$ '))
print()
sau = 'BEM VINDO AO SISTEMA DE MULTAS DO DETRAN MG, POR FAVOR, SEIGA AS INSTRUÇÕES A SEGUIR.'
print('-'*len(sau))

print(sau)
print('-'*len(sau))
print()
vel = int(input('Qual foi a sua velocidade registrada?Km/h '))

print('Você foi MULTADO' if vel > lim else 'Você nao levou multa...AINDA :)')
print()
exc = vel-lim
if exc > 0:
    print('O valor de sua multa é: R${:.2f}'.format(exc*pre))

