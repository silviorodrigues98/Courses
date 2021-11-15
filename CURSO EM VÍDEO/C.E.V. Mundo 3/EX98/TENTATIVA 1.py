"""
PROGRAMA QUE TENHA FUNÇÃO CONTADOR QUE RECEBA SEMPRE 3 PARAMETROS
INÍCIO, FIM E PASSO.
ELE DEVE CONTAR DE 1 À 10, DE 1 EM 1.
DE 10 ATÉ 0, DE 2 EM 2
E UMA CONTAGEM PERSONALIZADA.

"""
from math import ceil
from time import sleep


def linhas(msg):
    print("~" * (len(msg)),
          msg,
          "~" * (len(msg)))


def simples(msg):
    print("-=" * (ceil(len(msg) * 1.5)))


def contador():
    for cont, vezes in enumerate(range(0, 3)):
        inicio = 1
        fim = 10
        passo = 1
        if cont == 1:
            inicio = 10
            fim = 0
            passo = 2
        if cont == 2:
            inicio = int(input("Início >. "))
            fim = int(input("Fim >. "))
            passo = int(input("Passo >. "))
        if passo == 0:
            passo = 1
        copias = inicio, fim, passo
        if inicio > fim and passo > 0 or inicio < fim and passo < 0:
            passo *= -1
        if passo > 0:
            fim += 1
        else:
            fim -= 1
        msg = f"Contagem de {copias[0]} até {copias[1]} de {abs(copias[2])} em {abs(copias[2])}."
        linhas(msg)
        for contagem in range(inicio, fim, passo):
            print(contagem, end=" >> "), sleep(0.5)
        print("FIM! ")
        simples(msg)


contador()
