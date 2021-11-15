pro = float(input('Preço do produto: R$'))
meto = int(input('''Escolhe o metodo de pagamento:
1 -- A vista
2 -- A vista cartao
3 -- 2x Cartao
4 -- 3x ou mais no cartao'''))
print('O preço final ', end='')
if meto == 1:
    print('é {:.2f} '.format(pro*0.90))
elif meto == 2:
    print('é {:.2f}'.format(pro*0.95))
elif meto == 3:
    print('é {:.2f}, em duas parcelas de {:.2f}'.format(pro, pro/2))
elif meto == 4:
    par = int(input('Quantas parcelas: '))
    print('é {:.2f}, em {} parcelas de {:.2f}'.format(pro*1.2, par, pro*1.2/par ))
else:
    print('''não está disponível...
A OPÇÃO DE PAGAMENTO É INVÁLIDA, TENTE NOVAMENTE.''')
