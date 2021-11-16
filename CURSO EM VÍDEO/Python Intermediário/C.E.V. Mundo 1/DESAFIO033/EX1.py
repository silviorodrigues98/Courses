#ACHAR NUMERO MENOR E MAIOR ENTRE 3

print('Já me cansei de fazer programas tão úteis! ')
print()
print('Vou lhe pedir para digitar 3 números, se seguida, lhe direi qual o maior e qual o menor entre eles.')
print()

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceito número '))

if n1 > n2 and n1 > n3:
    print('O maior é {:.2f}'.format(n1))
if n1<n2>n3:
    print('O maior é {:.2f}'.format(n2))
if n1<n3>n2:
    print('O maior é {:.2f}'.format(n3))
if n2>n1<n3:
    print('O menor é {:.2f}'.format(n1))
if n1>n2<n3:
    print('O menor é {:.2f}'.format(n2))
if n1>n3<n2:
    print('O menor é {:.2f}'.format(n3))
