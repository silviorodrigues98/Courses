""" RECEBER VALORES ILIMITADOS DE NÚMEROS E OS COLCOAR EM UMA LISTA, CASO O NÚMERO JÁ EXISTA,
 ELE NÃO SERÁ ADICIONA.
 NO FINAL, EXIBIR TODOS OS VALORES ÚNICOS DIGITADOS PELO USUÁRIO """


valores = list()
continuar = " "
while True:
    num = int(input('Digite um valor > '))
    teste_logico = valores.count(num)
    if teste_logico == 0:
        print("Valor adicionado com sucesso...")
        valores.append(num)
    else:
        print("Valor repetido não adicionado.")
    while continuar not in "NnSs":
        continuar = str(input('Deseja adicionar outro número?[S/N] > ')).upper().strip()[0]
        if continuar not in "NnSs":
            print('Opção inválida! Tente novamente.')
    if continuar in "Nn":
        break
    continuar = " "
print(f"Você digitou os valores não repetidos, em ordem crescente: {sorted(valores)}")
