print('Este programa terá a participação do Sirvão')
c1 = float(input('Digite aqui o valor que você tem sua carteira: '))
d1 = float(input('Cotação do dólar hoje: '))
r1 = c1/d1
print('Fazendo a conversão, você ficará com US${:.2f} '.format(r1))

print('Agora sim é o ÚLTIMO!\nA proposta é medir a área de uma parede,\ne calcular as latas de tintas necessárias para pinta-la')
alt = float(input('Digite aqui a altura da parede que você quer pintar: '))
lar = float(input('Digite aqui a largura desta mesma parede: '))
are = lar*alt


print('A área de sua parede é {:.2f}'.format(are))
lat = float(input('Me diga, considerando o tamanho da lata de tinta,\nquanto você acredita que ela pinta, em m2?'))
print('Ótimo! Então você necessitara aproximadamente de {} latas de tinta para pintar toda a parede.'.format(are/lat))
