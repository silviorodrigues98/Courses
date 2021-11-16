from time import sleep


def maior(*num):
    cont = maior = 0
    print("-="*30)
    print(f"\nAnalisando os valores passados... ")
    for valor in num:
        print(f"{valor}", end="..."), sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"Foram informados {cont} numeros ao todo. ")
    print(F"O maior valor informado foi {maior}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
