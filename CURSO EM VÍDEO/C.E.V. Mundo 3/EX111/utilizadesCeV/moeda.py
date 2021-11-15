def aumentar(numero=0, porcentagem=10, formatacao=False):
    res = numero + numero * (porcentagem / 100)
    if formatacao:
        return moeda(res)
    else:
        return res


def diminuir(numero=0, porcentagem=13, formatacao=False):
    res = numero - numero * (porcentagem / 100)
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


def linhas(txt):
    print("-" * 50)
    print(f"{txt:^50}")
    print("-" * 50)


def resumo(numero, add=10, rmv=10):
    linhas("RESUMO DO VALOR")
    print(f"""
Preço analisado:           {moeda(numero):>20}
Dobro do preço:            {moeda(dobro(numero)):>20}
Metade do preço:           {moeda(metade(numero)):>20}
{add}% de aumento:         {moeda(aumentar(numero, add)):>23}
{rmv}% de redução:         {moeda(diminuir(numero, rmv)):>23}""")
    print("-" * 50)
