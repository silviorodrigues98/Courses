"""
PROGRAMA QUE SORTEIA 5 VALORES E SOMA OS PARES USANDO FUNÇÕES
"""
from random import randint


def sorteia():
    cont = int(input("Quantos valores você deseja sortar? >. "))
    print(f"Sorteando os {cont} valores: ")
    for contador, sorteio in enumerate(range(0, cont)):
        lista.append(randint(0, 20))
        print(lista[contador], end="; ")
    print(" PRONTO! ")
    return lista

sorteia()
lista
def somapar(lista):
    soma = 0
    print(f"A soma dos valores {lista} é:")
    for valores in lista:
        if valores % 2 == 0:
            soma += valores

