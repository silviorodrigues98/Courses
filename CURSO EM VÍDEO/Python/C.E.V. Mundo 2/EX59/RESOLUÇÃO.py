from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print("""[1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR DELES
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA""")
    opcao = int(input('Qual sua opção >>> '))
    if opcao == 1:
        soma = n1 = n2
        print('A soma entre {} e {} é {}'.format(n1, n2 , soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...'), sleep(2)
    else:
        print("Opção inválida, tente novamente. ")
    print("=-="*20)
print('Fim do programa! Volte sempre! ')
