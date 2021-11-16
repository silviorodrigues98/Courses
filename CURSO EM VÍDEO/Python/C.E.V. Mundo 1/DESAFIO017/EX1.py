from math import sqrt

co = float(input('Cateto oposto: ° '))
ca = float(input('Cateto adjacente: ° '))
h1 = (co**2)+(ca**2)
hp = sqrt(h1)
print('O valor da hipotenusa é igual a: {:.02f}°'.format(hp))