time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador["NOME"]= str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['NOME']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f"Quantos gols nas partida {c} ")))
    jogador["GOLS"] = partidas[:]
    jogador["TOTAL"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar° [S/N] ")).upper().strip()[0]
        if resp in "SsNn":
            break
        print("ERRO! Responda apenas S ou N .")
    if resp == 'N':
        break
print("-="*30)
print(f"cod ", end="")
for i in jogador.keys():
    print(f"{i:<15}", end="")
print()
print("-="*30)
for k, v in enumerate(time):
    print(f"{ k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print("-="*30)
while True:
    busca = int(input("Mostrar dados de qual jogador? [999 para parar] "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existee jogador com código {busca}")
    else:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['NOME']}")
        for i, g in enumerate(time[busca]["GOLS"]):
            print(f"      No jogo {i+1} fez {g} gols.")
    print("-="*30)
print("<< VOLTE SEMPRE >>")
