l1 = float(input('Lado 1: '))
l2  = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))
if l1 < l2+l3 and l2<  l1+l3 and l3< l2+l1:

    print('O triângulo formado é ',end = '')

    if l1 == l2 == l3:
        print('Equilátero')
    if l1 != l2 != l3 != l1:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Não é possível criar um triângulo com essa medidas')
