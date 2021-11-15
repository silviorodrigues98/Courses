# TRIâNGULO, PODE OU NÃO SE FORMAR?

# PEGUEI NA NET

print(' BEM VINDO AO TRIANGULADOR TRIANGULAR DE 3 LADOS ! ')
print()

l1 = float(input('Me diga o primeiro lado:(m) '))
l2 = float(input('Agora, do segundo:(m)'))
l3 = float(input('E por último, o terceirO:(m) '))

"if 1"

if l1 < l2 +l3:
    v1 = 1
else:
    v1 = 0
if l2 < l1 +l3:
    v2 = 1
else:
    v2 = 0
if l3 < l2 + l1:
    v3 = 1
else:
    v3 = 0
if v1 + v2 + v3 == 3:
    print('Ótimo! Com essas medidas é sim possível fazer um triÂngulo!!!')
else:
    print('Infelizmente é impossível criar um triângulo com essas medidas.')
