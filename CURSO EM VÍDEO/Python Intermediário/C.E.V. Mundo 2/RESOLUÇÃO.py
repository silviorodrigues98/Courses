contador = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma  = soma + c
        contador += 1 # É a mesma coisa de soma = soma + c
print('A soma é de todos os {} é {}'.format(contador, soma))
