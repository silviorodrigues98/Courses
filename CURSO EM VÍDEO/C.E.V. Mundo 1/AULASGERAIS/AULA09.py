# AULA SOBRE FORMATAÇÃO E MANIPULAÇÃO DE TEXTO
print('Bem vindo !!! Hoje vamos MANIPULAR textos.')

frase = '    O Estado é um LIXO, compre Bitcoins!!!       '
print(frase[9])
print(frase[:9])
print(frase[9:])
print(frase[::2])
print(frase[12::3])
print(frase.count('o, 5, 8'))
print(frase.count('i'))
print(frase[:5:2])
print(frase[9:20:4])
print(frase.find('Estado'))
string = '       Vamos começar também a investir em Fundos Imoboliários         !'
print(string.find('Fundos'))
print(string.find('Piru'), frase.find('Meu saco'))
# O valor -1 quer dizer que não existe tal palavra na frase que eu pesquisei.

print('Estado' in frase)
print('Cálculo' in string)

# Eles retornam True or False pois ou existe a palavra, ou não.
# Contudo, a função IN não diz a posição da palavra, somente se existe ou não.

print(frase.replace('Bitcoins','Etherium'))
print(string.replace('Fundos ', 'Ações'),('Imobiliários','Estrangeiras'))
print(string.upper())
# Fica em maiúsculas
print(string.lower())
# Fica minúsculo
print(frase.capitalize())
print(frase.title())
# São parecidos mas diferentes
print(string.strip())
# remove espaços inuteis antes e depois da frase,
print(string.lstrip())
print(string.rstrip())
# removem da esquerda ou direita.
print(frase.split())
# Divide a frase em 'setores' baseado nas palavras
print('-'.join(frase))
n1 = int('100')
print(n1*3)
print('''Não tinha medo tal João do Santo Cristo, era o que todos diziam
quando ele se perdeu, deixou pra trás todo o marasmo da fazenda só pra
sentir no seu sangue o ódio que Jesus lhe deu.''')
# Usa-se 3 aspas """ no começo e no final para printar grandes textos.
print(string.count('t'))
print(frase.upper().count('o'))
print(len(frase))
# Len é a função que mostra quantos caracteres existem na frase.
print(len(frase.strip().split()))
# O strip então irá remover os espaços inuteis e o split divide a frase por palavras, e não por letras.
print(string.replace('Imoboliários','Logísticos'))
print(string.replace('Fundos Imoboliários','Ações').strip().split())
print(frase[0])
print(string)
#O replace não muda a base da string, ele somente muda o print atual.
print(string.find('Fundos'))
bct = string.strip().split()
print(bct)
print('Fundos' in string)
print('Fundos' in bct)
print(bct[0])
