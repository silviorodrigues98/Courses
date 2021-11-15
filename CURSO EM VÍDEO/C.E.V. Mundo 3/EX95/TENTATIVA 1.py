""" APRIMORAR O DE JOGADOS DE FUTEBOL. 093"""


jogadores = []
jogador = {}
while True:
    todos_gols = []
    total_gols = 0
    jogador["NOME"] = str(input("Qual o nome do jogador? >: "))
    jogador["JOGOS"] = int(input(f"Quantos jogos {jogador['NOME']} jogou? >: "))
    for contador, gols in enumerate(range(0, jogador["JOGOS"])):
        gol = int(input(f"Quantos gols {jogador['NOME']} marcou? >: "))
        total_gols += gol
        todos_gols.append(gol)
    jogador["GOLS"] = todos_gols
    jogador["TOTAL"] = total_gols
    jogadores.append(jogador.copy())
    continuar = " "
    while continuar not in "NnSs":
        continuar = str(input("Deseja continuar?[S/N] >; ")).upper().strip()[0]
    if continuar in "Nn":
        break
print(f"{'cod':<5} {'nome':<10} {'gols'} {'total':>30}")
for cont, cada in enumerate(jogadores):
    print(f"{cont:<10} {cada['NOME']:<10} {cada['GOLS']} {cada['TOTAL']:>30}")
while True:
    mostrar = int(input("Mostrar dados de qual jogador? [999 cancela] >: "))
    if mostrar == 999:
        break
    if mostrar < len(jogadores):
        for partida, cada_gol in enumerate(jogadores[mostrar]["GOLS"]):
            print(f"No {partida+1}º jogo fez {cada_gol} gols.  ")
    else:
        print("Valor inválido! Tente novamente. ")
print("PROGRAMA FINALIZADO. VOLTE SEMPRE! ")
