"""
PROGRAMA QUE TENHA FUNÇÃO NOTAS QUE RECEBE VÁRIAS NOTAS.
RETORNA UM DICIONÁRIO COM:
QTDE DE NOTAS; MAIOR E MENOR; ENTRE OUTRAS.
USAR DOCSTRING

"""


def notas(*pontos, sit=False):
    """
    -> Recebe várias notas e retorna algumas informações sobre elas.
    :param pontos:recebe várias notas, float ou inteiras.
    :param sit:padrão False. Caso receba comando True, retorna a situação do aluno
    :return:retorna as infomações processadas.
    """
    cadastro = {"MEDIA": sum(pontos) / len(pontos), "QUANTIDADE": len(pontos),
                "MAIOR": max(pontos), "MENOR": min(pontos)}
    if cadastro["MEDIA"] >= 7:
        situacao = "BOA"
    elif cadastro["MEDIA"] >= 4:
        situacao = "RAZOÁVEL"
    elif cadastro["MEDIA"] < 4:
        situacao = "RUIM"
    if sit:
        cadastro["SITUAÇÃO"] = situacao
    return cadastro


resp = notas(10, 10, 7)
print(resp)
help(notas)
