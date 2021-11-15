def aumentar(preço=0, taxa=10):
    res = preço + preço * (taxa / 100)
    return res


def diminuir(preço=0, taxa=13):
    res = preço + preço * (taxa / 100)
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def metade(preço=0):
    res = preço / 2
    return res


def moeda(preço=0, moeda = "R$"):
    return f"{moeda}{preço:>8.2f}".replace(".", ",")
