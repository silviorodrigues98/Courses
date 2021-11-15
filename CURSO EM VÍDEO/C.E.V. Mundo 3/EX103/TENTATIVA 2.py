"""
FICHA RECEBE DOIS PARÂMETROS:
NOME E SALDO DE GOLS.
CASO UM DELES FIQUE EM BRANCO, DEVE CONTINUAR FUNCIONANDO

"""


def ficha(nome="Desconhecido", gols=0):
    nome = str(input("Nome do jogador: .> "))
    gols = str(input(f"Quantidade de Gols marcado por {nome}: .> "))
    if not gols == "":
        gols = int(gols)
    return nome, gols


print(ficha())
