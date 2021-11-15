"""
FICHA RECEBE DOIS PARÂMETROS:
NOME E SALDO DE GOLS.
CASO UM DELES FIQUE EM BRANCO, DEVE CONTINUAR FUNCIONANDO

"""


def ficha():
    nome = str(input("Nome do jogador: .> ")).strip().capitalize()
    if nome == "":
        nome = "Desconhecido"
    gols = str(input(f"Quantidade de Gols marcado por {nome}: .> "))
    if gols in "":
        gols = 0
    else:
        gols = int(gols)
    return f"O jogador {nome} fez {gols} gols."


print(ficha())
