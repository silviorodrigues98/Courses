def aumentar(preço=0, porcentagem=10):
    res = preço + preço * (porcentagem / 100)
    return res


def diminuir(preço=0, porcentagem=13):
    res = preço + preço * (porcentagem / 100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res
