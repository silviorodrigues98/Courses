import moedaRES


p = float(input("Digite um preço >R$ "))
print(f"A metade do preço é {moedaRES.moeda(moedaRES.metade(p))}")
print(f"O dobro de {moedaRES.moeda(p)} é {moedaRES.moeda(moedaRES.dobro(p))}")
print(f"Aumentando em 10%, temos {moedaRES.moeda(moedaRES.aumentar(p, 10))}")
