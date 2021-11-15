""" FAZER TUPLA RECEBER 5 NÚMEROS ALEATÓRIOS. """
from random import randint

nr1 = randint(0, 100)
nr2 = randint(0, 100)
nr3 = randint(0, 100)
nr4 = randint(0, 100)
nr5 = randint(0, 100)
numeros_random = nr1, nr2, nr3, nr4, nr5
print(f"""Os numeros sorteados foram:{numeros_random}
Entre eles, o {max(numeros_random)} foi o maior.
Já o menor foi o {min(numeros_random)}.""")
