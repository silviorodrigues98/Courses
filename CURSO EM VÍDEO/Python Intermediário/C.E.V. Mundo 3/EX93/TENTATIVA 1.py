""" APROVEITAMENTO DE UM JOGADOR DE FUTEBOL
LER QUANTAS PERTIDAS, E QUANTIDADE DE GOLS EM CADA UMA.
MOSTRAR DICIONÁRIO INCLUINDO GOLS FEITOS DURANTE O CAMPEONATO. """

aproveitamento = {"nome": str(input("Nome do jogador >: "))}
aproveitamento["qtde_jogos"] = int(input(f"Quantos jogos {aproveitamento['nome']} jogou? >: "))
todos_gols = []
total_gols = 0
for contador, perguntas in enumerate(range(0, aproveitamento["qtde_jogos"])):
    qtde_gols = int(input(f"Quantos gols {aproveitamento['nome']} marcou na {contador+1}ª partida? >: "))
    todos_gols.append(qtde_gols)
    total_gols += qtde_gols
aproveitamento["todos_gols"] = todos_gols
aproveitamento["total_gols"] = total_gols
print("-="*30)
for keys, values in aproveitamento.items():
    print(f"O campo {keys} tem o valor {values}")
print("-="*30)
print(f"O jogador {aproveitamento['nome']} jogou {aproveitamento['qtde_jogos']}. ")
for cont, gols in enumerate(aproveitamento["todos_gols"]):
    print(f"No jogo {cont+1}, fez {gols} gols. ")
print(f"Foi um total de {aproveitamento['total_gols']}")
