a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor : '))

menor = a
if b < a and b < a:
    menor = b
if c < b and c < a:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O maior número é {} e o menor é {}'.format(maior, menor))