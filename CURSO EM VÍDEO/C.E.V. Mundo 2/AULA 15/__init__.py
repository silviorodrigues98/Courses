''' INTERROMPENDO ESTRUTURAS WHILE '''

'''while True:
    if chão:
        passo
    if espaço:
        pula
    if moeda:
        pega
    if trofeu:
        pula
        break
pega'''

''' WHILE INFINITO CASO NÃO ACHAR O BREAK '''

'''cont = 1
while cont <= 10:
    print(cont, end='...')
    cont += 1
print('ACABOU ')'''

'''cont = 1
while True:
    print(cont,end='...')
    cont += 1
    if cont == 10:
        break
print('ACABOU ')'''

'''n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1'''

'''n = s = 0
while n != 999:#Isso se chama FLAG 999
    n = int(input('Digite um valor: '))
    s += n
print('A soma vale {}'.format(s))'''

"""n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f"A soma vale {s}")"""

nome = 'José'
idade = 33
print(f"O {nome} tem {idade} anos")
print('O {} tem {} anos'.format(nome, idade))
salario = 983.35
print(f"O {nome:=^20} tem {idade:<20} anos e ganha R${salario:.2f}") # Da pra formatar assim como o outro print.
