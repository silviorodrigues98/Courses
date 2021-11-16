""" LISTAS DENTRO DE LISTAS. """


teste = list()
teste.append("Gustavo")
teste.append(40)
galera = []
teste[0] = "Silvio"
teste[1] = 22
galera.append(teste[:])
print(galera)

galera1 = [["JOAO", 19], ["ANA", 33], ["JOAQUIM", 13], ["MARIA", 45]]
print(galera1[2][1])
for p in galera1:
    print(f"{p[0]} tem {p[1]} anos de idade.")
galera2 = []
dado = []
for c in range(0, 5):
    dado.append(str(input("Nome > ")))
    dado.append(int(input("Idade")))
    galera2.append(dado[:])  # Isso serve para que o galera2 receba e guarde os dados, e que eles não sejam apagados.
    dado.clear()
print(galera2)
totmai = totmen = 0
for p in galera2:
    if p[1] >= 21:
        print(f" {p[0]} é maior de idade. ")
        totmai += 1
    else:
        print(f" {p[0]} é menor de idade. ")
        totmen += 1
print(f"Temos {totmai} maiores e {totmen} menores.")
