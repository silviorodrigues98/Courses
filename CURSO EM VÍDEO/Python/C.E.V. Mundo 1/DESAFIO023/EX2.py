#Teste 2, este eu consigo fazer, mas nao fica perfeito pois só funciona com números de 4 dígitos.

print('Bem vindo ao transmissor de unidades!!! Siga as instruções para saber características de seu número.')

print()
num = str(input('Primeiramente, digite aqui o número que deseja separar, que seja de 1000 à 9999: '))
print()

und = num[3]
dez = num[2]
cen = num[1]
mil = num[0]

print('''Unidade: {:=^20}
Dezena = {:>20}
Centena = {:<10}
Milhar = {:.2}'''.format(und, dez, cen, mil))
print()
print('Feito!!! SÓ QUE DE UM JEITO MUITO RUIM:)')
