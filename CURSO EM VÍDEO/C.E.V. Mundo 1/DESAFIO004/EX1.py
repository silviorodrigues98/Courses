n1 = input("Digite qualquer coisa aqui, para que possa definir suas características: ")
print('Você digitou "{}", segue abaixo suas características: '.format(n1))

print('O tipo primitivo de "{}" é'.format(n1), type(n1))
print('Só tem espaços? {}'.format(n1.isspace()))
print('É um número? {}'.format(n1.isnumeric()))
print('É alfabético? {}'.format(n1.isalpha()))
print('É alphanumérico? {}'.format(n1.isalnum()))
print('Está em maiúculas? {}'.format(n1.isupper()))
print('Está em minúsculas? {}'.format(n1.islower()))
print('Está capitalizado? {}'.format(n1.istitle()))

# Hoje aprendi sobre .format; sobre isalnum/islower/entre outros
# Eles modoficam os objetos. Objetos, por sua vez, são os caracteres que recebem um input qualquer, e sempre geram string.
