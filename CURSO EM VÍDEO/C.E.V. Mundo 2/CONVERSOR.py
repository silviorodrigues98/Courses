num = int(input('Numero inteiro: '))
tam = str(num).strip()
tam1 = tam.split()
tam2 = ''.join(tam1)
tam3 = len(tam2)
tam4 = len(tam2)
a = 0
b = 0
c = 0
for teste in range(1, 5):
    if tam[a] == 1:
        b += 2**tam3
    tam3 -= 1
print(b)
