def aumentar(numero=0, porcentagem=10, formatacao=False):
    res = numero + numero * (porcentagem / 100)
    if formatacao:
        return moeda(res)
    else:
        return res


def diminuir(numero=0, porcentagem=13, formatacao=False):
    res = numero + numero * (porcentagem / 100)
    if formatacao:
        return moeda(res)
    else:
        return res


def dobro(numero, formatacao=False):
    res = numero * 2
    if formatacao:
        return moeda(res)
    else:
        return res


def metade(numero, formatacao=False):
    res = numero / 2
    if formatacao:
        return moeda(res)
    else:
        return res


def moeda(numero):
    res = f"R${numero:.2f}"
    return res
