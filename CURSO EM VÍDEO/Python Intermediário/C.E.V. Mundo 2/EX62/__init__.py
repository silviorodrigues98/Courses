'''MODIFICAR O 61, ADICIONANDO MAIS INTERAÇÃO '''


bb = ['\033[1;3;4;30;44m', '''SEJA MUITO BEM VINDO AO CONTADOR DE P.A
POR FAVOR, SIGA AS INSTRUÇÕES ABAIXO PARA PROSSEGUIR: ''', '\033[m']
print('{}{}\n{}'.format(bb[0],bb[1],bb[2]))
primeirof = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
primeiro = primeirof
termo = 1
quantos = ''
termo1 = 1
while not termo == 11:
    primeiro += razao
    print('{}'.format(primeiro),end=' -> ')
    termo += 1
pergunta = str(input('Você deseja adicionar mais termos?[S/N] ')).upper().split()
if 'S' in pergunta:
    quantos = int(input('Quandos números deseja adicionar? '))
    while not termo1 == quantos+1:
        primeiro += razao
        termo1 += 1
        print('{}'.format(primeiro),end=' >> ')
