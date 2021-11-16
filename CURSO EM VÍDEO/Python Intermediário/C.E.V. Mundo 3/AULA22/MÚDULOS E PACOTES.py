#  from mods1 import fatorial  # Múdulo que eu criei
from uteis import numeros


num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}.")
print(f"O triplo de {num} é {numeros.triplo(num)}.")

# Quando os módulos não são suficientes, utilizam-se então os PACOTES(BIBLIOTECAS)
