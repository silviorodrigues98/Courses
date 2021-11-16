# Ver se a palavra começa com 'SANTO'

print('Bem vindo ah foda-se')
print()
nome = str(input('Digite aqui o noma de sua cidade: '))
format = nome.strip().split()[0]
format1 = format.upper()
snt = 'SANTO' in format1
print(snt)
nome2 = str(input('Deixa eu testa um negócio aqui, rapidão: ')).strip()
nome3 = nome2.upper()
pesq = str(input('Diz ai o nome que quer achar: ')).strip()
pesq1 = pesq.upper()
snt1 = pesq1 in nome3
print(snt1)
# Meu teste deu certo, é possível encontrar palavras de outra lista, dentro da lista original.
