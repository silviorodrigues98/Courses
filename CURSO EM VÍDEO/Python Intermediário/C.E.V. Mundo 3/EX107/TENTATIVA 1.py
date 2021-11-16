"""
PROGRAMA QUE UTILIZA UM MÓDULO PARA PODER FAZER AUMENTO,
DIVISÃO E OUTRAS COISAS.

"""
import moeda


num = float(input("Digite um preço >R$ "))
aumt = 10
redz = 13
print(f"O valor {num} aumentado em {aumt}% é {moeda.aumentar(num, aumt)}")
print(f"O dobro de {num} é {moeda.dobro(num)}")
print(f"Metade de {num} é {moeda.metade(num)}")
print(f"O número {num} reduzido em {redz} é igual a {moeda.diminuir(num, redz)}")
