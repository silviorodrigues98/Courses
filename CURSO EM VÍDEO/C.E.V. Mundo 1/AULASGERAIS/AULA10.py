# Condicionais simples, compostas e simplificadas.

# Método tem parênteses () no final.

# É primordial que se siga uma ordem contrológica e sequencial.

# Os comandos que estão "colados" do lado esquerdo, sempre acontece, já os que estão um pouco à direita, acontecerão em alguns casos.


num = int(input('Teste'))
if num == 10:
    print('ok')
else:
    print('Nao deu')

# Não se pode esquercer o "dois pontos" ':' depois do IF e do ELSE
sau = 'ME DIGA A IDADE DE SEU CARRO E DIREI SE ELE AINDA AGUENTA O TRANCO! '
print(sau)
print('-'*len(sau))

ida = int(input('E ai, qual a idade daquela coisa? '))

uai = 'Pois é, não é que seu carro ainda dá pro gasto? Por enquanto...KKK '
flw = 'KKKKKKK essa lata velha ainda funciona? '
blz = 'Aguardando processamento...(bricadeira é instantãneo)'

if ida <= 5:
    print(blz)
    print(uai)
    print('-'*len(uai))
else:
    print(blz)
    print(flw)
    print('-'*len(flw))

# Copiando Guanabara

tempo = int(input('Idade do carro: '))
if tempo >= 3:
    print('carro velho')
else:
    print('carro novo')

print('{:=^20}'.format('FIM'))

# Simplificação

print('carro novo' if tempo <=3 else 'carro velho')
print('{:$^20}'.format('FIM'))

n = str(input('Qual seu nome? ')).strip().upper()
if n == 'SILVIO':
    print('Que lindo nome!!!')
print('Bim dia {}'.format(n))

m = str(input('Qual seu nome. ')).upper().split()
if m == 'SILVIO':
    print('Que lindo nome!!!')
else:
    print('Nossa...que nome mais...CHATO')
print('Bom dia {}'.format(m))

n1 = float(input('Num 1'))
n2 = float(input('Num 2 '))
med = (n1*n2)/2
print('Sua média foi {:.1f}'.format(med))
if med >= 6:
    print('Parabéns, você está aprovado!')
else:
    print('Voce é um fracasso :)')

print('Horrível' if med<=6 else 'Delícia')

# Outro



