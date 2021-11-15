# CÓPIA GUANABARA!!!
from datetime import date

ano = int(input('Qual ano você quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year# Este IF usa o ano atual do PC caso eu digite '0'
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:# Não igual usa EXCLAMAÇÃO antes do IGUAL, assim : !=
    print('O ano {} e´BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))
