""" CADA JOGADOR JOGA UM DADO, ENTRE 1 E 6, E OS RESULTADOS SÃO GUARDADOS EM UM DICIONÁRIO.
NO FINAL, COLOQUE O DICIONÁRIO EM ORDEM SABENDO QUE O VENCEDOR É O QUE TIROU MAIOR NÚMERO NO DADO."""
from random import randint
from time import sleep


jogadores = []
for cont, nomes in enumerate(range(0, 4)):
    pessoa = {"NOME": str(input(f"Nome do {cont+1}º jogador: ")),
              "DADO": randint(1, 6)}
    jogadores.append(pessoa.copy())
    pessoa.clear()
