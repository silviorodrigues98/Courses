# LIGHT THAT NEVER COMES
# LER NOME E DIZER PRIMEIRO E ULTIMO
sau = 'Bem vindo(a)!, iremos te cadastrar em nosso sistema. '
print(sau)
tra = int(len(sau))
print('-'*tra)
nome = str(input('Por favor, digite seu completo para que possamos prosseguir: '))
print()
split = nome.strip().split()
pri = split[0]
ult = len(split)
ult1 = int(ult)-1
ultf = split[ult1]
print('Voce confirma que seu nome começa com {} e termina com {} ?'.format(pri, ultf))
print()
fim = 'Parabéns {}, seu cadastro foi um sucesso! '
ter =  int(len(fim))
print('^'*ter)

