import moedaRES


p = float(input("Digite um preço >R$ "))
print(f"A metade do preço é {moedaRES.metade(p)}")
print(f"O dobro de {p} é {moedaRES.dobro(p)}")
print(f"Aumentando em 10%, temos {moedaRES.aumentar(p, 10)}")
