from datetime import date
totm = 0
totmn = 0
atual = date.today().year
for p in range(1, 8):
    nasc = int(input('Diga o ano de nascimento da {}ª pessoa: '.format(p)))
    idade = atual - nasc
    if idade >= 21:
        totm += 1
    else:
        totmn +=1
print('Ao todo tivemos {} pessoas maiores e {} menores'.format(totm, totmn))
