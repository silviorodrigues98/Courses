jogador = dict()
partidas = list()
jogador["NOME"]= str(input("Nome do jogador: "))
tot = int(input(f"Quantas partidas {jogador['NOME']} jogou? "))
for c in range(0, tot):
    partidas.append(int(input(f"Quantos gols nas partida {c} ")))
jogador["GOLS"] = partidas[:]
jogador["TOTAL"] = sum(partidas)
print("-="*30)
print(jogador)
print("-="*30)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}. ")
print("-="*30)
print(f"O jogador {jogador['NOME']} jogou {len(jogador['GOLS'])} partidas")
for i, v in enumerate(jogador["GOLS"]):
    print(f"       => Na partida {i} fez {v} gols. ")
print(f"Foi um total de {jogador['TOTAL']} de gols. ")
