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
outrocontador = 0
for cont, cada_um in enumerate(jogadores):
    while not cada_um["DADO"] == resultados[contador]:
        contador += 1
    print(f"O {contador+1}º lugar foi {cada_um['NOME']}")
    contador = 0

