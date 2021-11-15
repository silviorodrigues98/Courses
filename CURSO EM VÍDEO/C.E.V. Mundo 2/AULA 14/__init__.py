# ESTRUTURA WHILE
'''a = 0
while not a == 5:
    a += 1'''
'''print(a)'''

# while not maçã:
    # if chão:
        #passo
    # if vazio:
        #pula
    #if moeda:
        #pega
#pega

'''for c in range (1, 10):
    print(c)
print('fim')'''

'''c = 1'''

'''while c < 10:
    print(c)
    c += 1
print('Fim')'''

'''for c in range(1, 4):
    n = int(input('Digite um valor '))
print('Fim')'''
'''n = 0.1
while n != 0:
    n = float(input('Digite um valor: '))'''

'''r = 'S'
while r in 'Ss':
    n = int(input('Digite um valor '))
    r = str(input('Quer continuar[S/N]? '))
print('Fim ')'''
par = impar = 0

n = 1
while n !=  0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        if n % 2 != 0:
            impar += 1
print('Foram {} pares e {} impares'.format(par, impar))