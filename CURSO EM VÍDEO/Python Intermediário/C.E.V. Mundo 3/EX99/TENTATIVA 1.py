"""
PROGRAMA QUE TENHA FUNÇÃO MAIOR QUE RECEBA VÁRIOS PARÂMETROS, E DIZER QUAL DELES É O MAIOR.

"""
from time import sleep
from random import randint


def linhas(tam):
    print("~"*tam)


def maior():
    cont = int(input("Quantos valores quer randomizar? .> "))
    while True:
        valores = []
        linhas(40)
        print("Analidando os valores processados...")
        for aleatorios in range(cont, 0, -1):
            rand = randint(0, 10)
            valores.append(rand)
            print(rand, end="..."), sleep(1)
        print(f"Foram processados {len(valores)} valores ao todo. ")
        print(f"O maior deles é o {max(valores)}.")
        cont -= 1
        if cont == 0:
            break


maior()
