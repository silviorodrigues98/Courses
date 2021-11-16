""" CADA JOGADOR JOGA UM DADO, ENTRE 1 E 6, E OS RESULTADOS SÃO GUARDADOS EM UM DICIONÁRIO.
NO FINAL, COLOQUE O DICIONÁRIO EM ORDEM SABENDO QUE O VENCEDOR É O QUE TIROU MAIOR NÚMERO NO DADO."""
from random import randint


jogadores = []
for cont, nomes in enumerate(range(0, 4)):
    pessoa = {"NOME": str(input(f"Nome do {cont+1}º jogador: ")),
              "DADO": randint(1, 6)}
    jogadores.append(pessoa)
resultados = []
print(jogadores)
for numeros in jogadores:
    resultados.append(numeros["DADO"])
resultados.sort(reverse=True)
print(resultados)
contador = 0
contador2 = 0
for teste in range(0, 4):
    while not jogadores[contador]["DADO"] == resultados[contador2]:
        contador +=1
    print(f"O jogadador {jogadores[contador]['NOME']} é o {contador2+1}º lugar.")
    contador2 += 1
    contador = 0
