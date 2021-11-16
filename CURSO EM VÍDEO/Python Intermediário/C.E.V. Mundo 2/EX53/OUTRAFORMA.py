fra = str(input('Digite uma bela frase; ')).strip().upper()
separada = fra.split()
junto = ''.join(separada)
tam = len(junto)
inverso = junto[::-1]
if inverso == junto:
    print('É palíndromo!!!')
else:
    print('A frase não é um palíndromo!!!')
print('O inverso de {} é {}'.format(junto, inverso))