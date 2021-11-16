""" PROGRAMA QUE LE NOME E PESO DE VÁRIAS PESSOAS, GUARDANDO TUDO EM UMA LISTA.
MOSTRAR QUANTIDADE DE PESSOAS CADASTRADAS.
MOSTRAR PESSOAS MAIS PESADAS
MOSTRAR PESSOAS MAIS LEVES. """

geral = []
continuar = " "
while True:
    nome = str(input("Nome > "))
    peso = float(input("Peso > "))
    geral.append(nome)
    geral.append(peso)
    while continuar not in "NnSs":
        continuar = str(input("Continuar?[S/N] > ")).upper().strip()[0]
    if continuar in "Nn":
        break
    continuar = " "
pesos = []
nomeg = []
nomem = []
for peso in range(1, len(geral), 2):
    pesos.append(geral[peso])
for pm in range(1, len(geral), 2):
    if geral[pm] == max(pesos):
        nomeg.append(geral[pm-1])
    elif geral[pm] == min(pesos):
        nomem.append(geral[pm-1])
print(f"Foram cadastradas {len(geral) / 2:.0f} pessoas. ")
print(f"O maior peso foi de {max(pesos):.1f}Kg, referente à: {nomeg}")
print(f"O menor peso foi de {min(pesos):.1f}Kg, referente à: {nomem}")
