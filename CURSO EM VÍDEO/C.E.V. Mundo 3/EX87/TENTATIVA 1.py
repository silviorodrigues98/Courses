""" MELHORAR MEU PROGRAMA ANTERIOR CALCULANDO AGUMAS COISAS."""


matriz = [[], [], []]
for cont, listas in enumerate(matriz):
    for contador in range(0, 3):
        matriz[cont].append(int(input(f"Posição {cont, contador} >: ")))
somatot = somater = maiorseg = 0
print("-="*30)
for cont, valores in enumerate(matriz):
    for teste in range(0, 3):
        print(f"[  {valores[teste]:^5}  ]", end="")
        if valores[teste] % 2 == 0:
            somatot += valores[teste]
        if teste == 2:
            somater += valores[teste]
        if cont == 1 and valores[teste] > maiorseg:
            maiorseg = valores[teste]
    print()
print("-="*30, f"""
A soma dos valores pares é {somatot}.
Já a soma dos valores da terceira coluna é: {somater}.
Finalmente, o valor da segunda linha é: {maiorseg}.""")
