def aumentar(preço=0, taxa=10, formato=False):
    res = preço + preço * (taxa / 100)
    return res if formato == False else(moeda(res))


def diminuir(preço=0, taxa=13, formato=False):
    res = preço - preço * (taxa / 100)
    return res if formato == False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0,moeda="R$"):
    return f"{moeda}{preço:>.2f}".replace(".", ",")


def linhas(txt):
    print("-" * 50)
    print(f"{txt:^50}")
    print("-" * 50)


def resumo(p=0, taxaaum=10, taxared=10):
    print("-"*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print(f"Preço analisado:               \t{moeda(p)}")
    print(f"Dobro do preço:\t\t{moeda(dobro(p))}")
    print(f"Metade do preço:\t{moeda(metade(p))}")
    print(f"{taxaaum}% de aumento:\t\t{moeda(aumentar(p, taxaaum))}")
    print(f"{taxared}% de redução:\t\t{moeda(diminuir(p, taxared))}")
    print("-" * 30)
