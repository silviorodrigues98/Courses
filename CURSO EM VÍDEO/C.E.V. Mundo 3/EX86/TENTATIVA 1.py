""" CRIAR UMA MATRIZ 3X3 QUE ME PERMITA DIGITAR VALORES DENTRO DELA. """

matriz = [[], [], []]
for contador, valores in enumerate(range(0, 3)):
    for valor in range(0, 3):
        matriz[contador].insert(contador, int(input(f" Posição {contador, valor} >: ")))
print("-="*30)
for matrizes in range(0, 3):
    for tabela in range(0, 3):
        print(f"[ {matriz[matrizes][tabela]} ]", end="")
    print()
