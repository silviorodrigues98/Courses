""" CADA JOGADOR JOGA UM DADO, ENTRE 1 E 6, E OS RESULTADOS SÃO GUARDADOS EM UM DICIONÁRIO.
NO FINAL, COLOQUE O DICIONÁRIO EM ORDEM SABENDO QUE O VENCEDOR É O QUE TIROU MAIOR NÚMERO NO DADO."""
from random import randint
from time import sleep


jogadores = []
for cont, nomes in enumerate(range(0, 4)):
    pessoa = {"NOME": str(input(f"Nome do {cont+1}º jogador: ")).title().strip(),
              "DADO": randint(1, 6)}
    jogadores.append(pessoa)
resultados = []
print(jogadores)
for numeros in jogadores:
    resultados.append(numeros["DADO"])
resultados.sort(reverse=True)
print(resultados)
for cont, cada_numero in enumerate(resultados):
    contador = 0
    while not jogadores[contador]["DADO"] == cada_numero:
        contador += 1
    print(f"{cont + 1}º posição: {jogadores[contador]['NOME']}, com {jogadores[contador]['DADO']} pontos. "), sleep(1.5)
    del jogadores[contador]
 