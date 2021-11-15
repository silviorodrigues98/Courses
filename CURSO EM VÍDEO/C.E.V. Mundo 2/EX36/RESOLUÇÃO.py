# EMPRÉSTIMO BANCÁRIO

#FAZER POR PARTES

casa = float(input('Valor da casa R$ '))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12)
minimo = salario*(30/100)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
print('Comparando tem que pagar {:.2f} e o mínimo é de  {:.2f}'.format(prestacao, minimo))
if prestacao <= minimo:
    print('Empréstimo concedido')
else:
    print('Empréstimo negado')