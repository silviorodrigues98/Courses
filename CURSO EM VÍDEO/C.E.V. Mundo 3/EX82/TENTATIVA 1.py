"""CRIAR 3 LISTAS, COM TODOS, PARES E IMPARES."""


continuar = " "
numeros = list()
pares = list()
impares = list()
while True:
    num = int(input("Qual número você quer adicionar? ."))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    while continuar not in "SsNn":
        continuar = str(input("Deseja adicionar mais um número?[S/N] .")).strip().upper()[0]
    if continuar in "Nn":
        break
    continuar = " "
print(f"Você digitou: {numeros}")
print(f"Deles,{pares} são os pares")
print(f"e {impares} são os ímpares.")
