def notas(*n, sit=False):
    """
    -> Analisar notas e situações de vários alunos
    :param n: Uma ou mais notas dos alunos
    :param sit: valor opcional indicando se deve ou não adicionar "situação"
    :return: retorna uma bibliotéca com as dados.
    """
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n) / len(n)
    if sit:
        if r["media"] > 7:
            r["situação"] = "BOA"
        elif r["media"] >= 5:
            r["situação"] = "RAZOÁVEL"
        elif r["media"] < 5:
            r["situação"] = "RUIM"
    return r


#  PROGRAMA PRINCIPAL:


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)
