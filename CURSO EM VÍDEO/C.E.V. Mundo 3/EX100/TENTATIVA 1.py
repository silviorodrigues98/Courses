"""
PROGRAMA QUE SORTEIA 5 VALORES E SOMA OS PARES USANDO FUNÇÕES
"""
from random import randint
from time import sleep


def somapar(lista):
    somapares = 0
    num_pares = []
    for cada_um in lista:
        if cada_um % 2 == 0:
            somapares += cada_um
            num_pares.append(cada_um)
    print(f"A soma de {num_pares} é {somapares}")


def sorteia():
    cont = int(input("Quantos valores você deseja sortar? >. "))
    print(f"Sorteando os {cont} valores: ")
    lista = []
    for contador, sorteio in enumerate(range(0, cont)):
        lista.append(randint(0, 20))
        print(lista[contador], end="; "), sleep(0.2)
    print(" PRONTO! ")
    somapar(lista)


sorteia()
