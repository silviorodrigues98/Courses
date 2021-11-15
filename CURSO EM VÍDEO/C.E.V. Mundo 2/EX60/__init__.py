'''FATORIAL DE UM NÚMERO SEM UTILIZAR A FUNÇÃO MATH
Fazer com FOR e com WHILE'''

num = int(input('Digite um número: '))
fatoracao = 0
passo = 0
resultado = 0
primeiro = 0
for fatorial in range(num-1, 0, -1):
    if fatorial == num-1:
        primeiro = num * fatorial
    else:
        primeiro *= fatorial
if fatorial == 1:
    print('Resultado {}'.format(primeiro))