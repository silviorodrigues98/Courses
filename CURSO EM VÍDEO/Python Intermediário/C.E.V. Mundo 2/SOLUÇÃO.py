from datetime import date
ano = date.today().year
nasc = int(input('Qual o ano do seu nascimento: '))
idade = ano - nasc
print(' O atleta tem {} anos'.format(idade))
if idade<=9:
    print('Classificação infantil')
elif idade<=14:
    print('Infantil')
elif idade <=19:
    print('JUNIOR')
else:
    print('master')