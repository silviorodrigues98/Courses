""" FAZER DE OUTRA FORMA! """


numeros = list()
continuar = " "
while True:
    num = int(input("Digite um valor: -> "))
    numeros.append(num)
    print("Cadastrado com sucesso...")
    while continuar not in "SsNn":
        continuar = str(input("Continuar?[S/N] -> ")).upper().strip()[0]
    if continuar in "Nn":
        print("Até logo! ")
        break
    continuar = " "
pares = list()
impares = list()
for teste in numeros:
    if teste % 2 != 0:
        impares.append(teste)
    else:
        pares.append(teste)
print(f"Você digitou: {numeros}")
print(f"Deles, {pares} são pares, e {impares} são ímpares")

