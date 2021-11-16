from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('''Seu sexo é masculino ou feminino?
Digite 'M' para masculino.
Digite 'F' para feminino.
Sexo: ''')).upper().strip()
idade = atual-nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
s = False
if sexo == 'M':
    s = True
elif idade == 18 and s == True:
    print('Você tem que se alistar IMEDIATAMENTE! ')
elif idade < 18 and s == True:
    print('Você deveria se alisstar em {} anos'.format(18-idade))
    print('Seu alistamento será em  {}'.format((18-idade)+atual))
elif idade > 18 and s == True:
    print('Você já deveria ter se alistado a {} anos.'.format(idade-18))
    print('Seu alistamente deveria ter acontedio em {}.'.format(atual-(idade-18)))
else:
    print('Em nossa democracia, mulheres nao precisam se alistar, parabens :)')



