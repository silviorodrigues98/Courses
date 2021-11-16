# PROGRAMA QUE LÊ O NOME COMPLETO DE ALGUÉM E DEFINA ALGUMAS CARACTERÍSTICAS.

print('''Bem vindo à carrapinha, lemos seu nome e dizemos sua sorte!!! ')
Siga as instruções a seguir e boa sorte...VOCÊ VAI PRECISAR MWHAHAHAHAHA''')
print()

nome = str(input('Por favor, digite aqui seu nome completo: '))

print('''Primeiro...irei dizer todo seu nome em...letras MAIÚSCULAS! 
Sim...você se chama {}. '''.format(nome.strip().upper()))
print()

print('''Agora... veja, seu nome ficará minúsculo.
Afinal, você é um verme, não é, {} ?'''.format(nome.strip().lower(),))
print()

letras = nome.strip().split()
tama = int(len(letras))
total = tama-1
todo = int(len(nome))
fim = todo-total

print('Veja bem {}, posso ver que seu nome tem {} letras...'.format(nome , fim))
print()
print('''Estamos chegando lá...posso afirmar que seu primeiro nome
 é {} e tem {} letras'''.format(nome.strip().split()[0],len(nome.strip().split()[0])))
print()
print('''Pode confessar, você ficou surpreso nao é !?!
Aguarde!!! Pois haverão mais testes para você...MWAHAHAHAHAHAHA''')
