import moedaRES


p = float(input("Digite um preço >R$ "))
print(f"A metade do preço é {moedaRES.metade(p, True)}")
print(f"O dobro de {moedaRES.moeda(p)} é {moedaRES.dobro(p, True)}")
print(f"Aumentando em 10%, temos {moedaRES.aumentar(p, 10, True)}")
print(f"Reduzindo 13%, temos {moedaRES.diminuir(p, 13, True)}")
