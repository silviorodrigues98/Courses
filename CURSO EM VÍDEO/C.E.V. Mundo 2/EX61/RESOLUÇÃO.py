print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
print('-='*10)
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ->'.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
