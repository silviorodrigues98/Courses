from EX108 import moeda


p = float(input("Digite um preço >R$ "))
aumt = 10
redz = 13
print(f"O valor {moeda.moeda(p)} aumentado em {aumt}% é {moeda.moeda(moeda.aumentar(p, aumt))}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O número {moeda.moeda(p)} reduzido em {redz}% é igual a {moeda.moeda(moeda.diminuir(p, redz))}")
