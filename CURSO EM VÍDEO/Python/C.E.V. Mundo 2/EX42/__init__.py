# VOLTANDO NO EXERCÍCIO DE TRIÂNGULOS.
# AGORA UTILIZANDO OS IF'S PARA SABER SUA CLASSIFICAÇÃO.

from emoji import emojize
from time import sleep

print(emojize('''Olá, somos amantes dos triângulos...
Alguns dizem até que somos :alien:ILLUMINATI:alien:
 Bem, isso você nunca saberá...''', use_aliases=True))

l1 = int(input('''
Brincadeiras à parte...agora me diga a primeira medida da reta: m'''))
l2 = int(input('\nAgora, nos diga quantos metros tem o segundo lado: m'))
l3 = int(input('\nPerfeito, agora basta NOS dizer qual a medida do terceiro: m'))

print('Calculando...'), sleep(1)

if l1 < l2+l3 and l2 < l3+l1 and l3 < l2+l1:
    t1 = bool(True)
else:
    t1 = bool(False)
if t1 == True and l1 == l2 == l3:
    print('Este triângulo é \033[1;30;42mEQUILÁTERO')
elif t1 ==True and l1==l2!=l3 or l1==l3!=l2:
    print('Este triângulo é \033[1;30;45mISÓCELES')
elif t1 ==True and l1!=l2!=l3:
    print('Este triângulo é \033[1;30;46mESCALENO')
else:
    print('Com estas medidas não é possível formar \033[1;30;47mNenhum triângulo.')
print('\nEspero ter sido útil')
