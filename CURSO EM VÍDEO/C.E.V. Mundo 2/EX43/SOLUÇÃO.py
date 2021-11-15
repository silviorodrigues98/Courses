peso = float(input('Qual seu peso: Kg'))
altu = float(input('Qual sua altura: m'))
imc = peso/(altu**2)
print('Seu imc é {:.1f}'.format(imc))
print('Sua situação é:', end='')
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obeso')
else:
    print('Mórbida')