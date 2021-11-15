from EX109 import moeda


p = float(input("Digite um preço >R$ "))
aumt = 10
redz = 13
print(f"O valor {moeda.moeda(p)} aumentado em {aumt}% é {moeda.aumentar(p, aumt, True)}")
print(f"O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}")
print(f"Metade de {moeda.moeda(p)} é {moeda.metade(p, True)}")
print(f"O número {moeda.moeda(p)} reduzido em {redz}% é igual a {moeda.diminuir(p, redz, True)}")
