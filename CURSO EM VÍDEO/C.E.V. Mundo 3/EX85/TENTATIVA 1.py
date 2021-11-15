""" DIGITAR SETE VALORES, E CRIAR UMA LISTA SEPARA COM DUAS LISTAS DE PARES E DE ÍMPARES. """


numeros = [[], []]
for ordem, numer in enumerate(range(0, 7)):
    num = int(input(f"Digite o {ordem+1}º valor > "))
    if num % 2 == 0:
        numeros[1].append(num)
    else:
        numeros[0].append(num)
print(f"Os pares forem: {sorted(numeros[1])}")
print(f"Os ímpares foram: {sorted(numeros[0])}")
