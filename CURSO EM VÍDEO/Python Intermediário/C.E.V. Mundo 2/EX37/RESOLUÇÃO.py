num = int(input('Digite um número inteiro'))
print('''Escolha uma das bases para conversão:
1 BINÁRIO
2 OCTAL
3 HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} Convertido para binário é igual {}'.format(num, bin(num)[2:]))
elif opcao ==2:
    print('{} convertido para octal é igual {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O numero {} convertido para hexadecimal é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')